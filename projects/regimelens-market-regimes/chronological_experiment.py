"""Fresh train-frozen HMM experiment. Latent-state prediction, not investment validation."""
from pathlib import Path
import hashlib
import numpy as np
import pandas as pd
from scipy.special import logsumexp
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score,recall_score,confusion_matrix
from hmmlearn.hmm import GaussianHMM

SEED=42
FEATURES=['market_return','market_volatility_20','advance_ratio','above_ma50','above_ma200','avg_volume_change','vix_close']


def build_market(data_dir):
    data_dir=Path(data_dir)
    names=['SP500_Historical_Data.csv','VIXCLS.csv']
    hashes={n:hashlib.sha256((data_dir/n).read_bytes()).hexdigest() for n in names}
    d=pd.read_csv(data_dir/names[0],usecols=['Ticker','Date','Adj Close','Volume'])
    d=d.rename(columns={'Ticker':'ticker','Date':'date','Adj Close':'price','Volume':'volume'})
    d.date=pd.to_datetime(d.date,errors='coerce')
    for c in ['price','volume']:d[c]=pd.to_numeric(d[c],errors='coerce')
    input_rows=len(d);d=d.dropna(subset=['ticker','date']).drop_duplicates(['ticker','date'],keep='first').sort_values(['ticker','date'])
    # Missing/invalid prices are dropped. No backfill or cross-ticker fill.
    d=d[d.price.gt(0)&d.volume.ge(0)].copy()
    group=d.groupby('ticker',sort=False)
    d['ret']=group.price.pct_change(fill_method=None)
    d['ma50']=group.price.transform(lambda x:x.rolling(50,min_periods=50).mean())
    d['ma200']=group.price.transform(lambda x:x.rolling(200,min_periods=200).mean())
    d['above50']=(d.price>d.ma50).where(d.ma50.notna()).astype(float)
    d['above200']=(d.price>d.ma200).where(d.ma200.notna()).astype(float)
    previous_volume=group.volume.shift(1).replace(0,np.nan)
    d['volume_change']=(d.volume/previous_volume-1).replace([np.inf,-np.inf],np.nan)
    d['advance']=(d.ret>0).where(d.ret.notna()).astype(float)
    m=d.groupby('date',sort=True).agg(market_return=('ret','mean'),advance_ratio=('advance','mean'),
       above_ma50=('above50','mean'),above_ma200=('above200','mean'),avg_volume_change=('volume_change','mean'),ticker_count=('ticker','nunique')).reset_index()
    m['market_volatility_20']=m.market_return.rolling(20,min_periods=20).std()
    v=pd.read_csv(data_dir/names[1]);v=v.rename(columns={'observation_date':'date','VIXCLS':'vix_close'})
    v.date=pd.to_datetime(v.date,errors='coerce');v.vix_close=pd.to_numeric(v.vix_close,errors='coerce')
    v=v.dropna(subset=['date','vix_close']).drop_duplicates('date').sort_values('date')
    m=pd.merge_asof(m.sort_values('date'),v[['date','vix_close']],on='date',direction='backward')
    m=m.replace([np.inf,-np.inf],np.nan).dropna(subset=FEATURES).reset_index(drop=True)
    assert m.date.is_monotonic_increasing and m.date.is_unique
    return m,{'source_sha256':hashes,'source_stock_rows':input_rows,'usable_market_days':len(m),
              'universe':'tickers supplied in source export; historical membership not reconstructed'}


def causal_filter(model,X):
    """Forward filtering only: p(z_t | x_1..x_t), with the fitted model held fixed."""
    X=np.asarray(X,dtype=float)
    cov=np.asarray(model.covars_)
    variance=np.diagonal(cov,axis1=1,axis2=2) if cov.ndim==3 else cov
    variance=np.maximum(variance,1e-10)
    emission=-.5*(np.log(2*np.pi*variance).sum(axis=1)[None,:]+((X[:,None,:]-model.means_[None,:,:])**2/variance[None,:,:]).sum(axis=2))
    log_start=np.log(np.maximum(model.startprob_,1e-300));log_trans=np.log(np.maximum(model.transmat_,1e-300))
    result=[];alpha=None
    for t in range(len(X)):
        alpha=(log_start if alpha is None else logsumexp(alpha[:,None]+log_trans,axis=0))+emission[t]
        alpha-=logsumexp(alpha);result.append(np.exp(alpha))
    return np.asarray(result)


def state_metrics(y,pred):
    return {'accuracy':float(accuracy_score(y,pred)), 'macro_f1':float(f1_score(y,pred,labels=[0,1,2],average='macro',zero_division=0)),
       'recall_by_state':recall_score(y,pred,labels=[0,1,2],average=None,zero_division=0).tolist(),
       'confusion_matrix':confusion_matrix(y,pred,labels=[0,1,2]).tolist()}


def run_experiment(market):
    from xgboost import XGBClassifier
    n=len(market);train_boundary=int(n*.70);val_boundary=int(n*.85)
    raw=market[FEATURES].to_numpy()
    scaler=StandardScaler().fit(raw[:train_boundary]);scaled=scaler.transform(raw)
    hmm=GaussianHMM(n_components=3,covariance_type='diag',n_iter=200,tol=1e-3,random_state=SEED).fit(scaled[:train_boundary])
    proba=causal_filter(hmm,scaled);states=proba.argmax(axis=1)
    # A label at t+1 must stay inside its own train/validation/test period.
    train=np.arange(0,train_boundary-1);val=np.arange(train_boundary,val_boundary-1);test=np.arange(val_boundary,n-1)
    X=np.column_stack([raw,proba]);y=states[1:]
    assert market.date.iloc[train[-1]+1]<market.date.iloc[val[0]]
    assert market.date.iloc[val[-1]+1]<market.date.iloc[test[0]]
    models={
      'Logistic Regression':make_pipeline(StandardScaler(),LogisticRegression(max_iter=3000,random_state=SEED)),
      'Random Forest':RandomForestClassifier(n_estimators=200,min_samples_leaf=5,random_state=SEED,n_jobs=1),
      'XGBoost':XGBClassifier(n_estimators=200,max_depth=3,learning_rate=.05,eval_metric='mlogloss',random_state=SEED,n_jobs=1,tree_method='hist'),
    }
    fitted={};val_rows=[{'model':'Persistence',**state_metrics(y[val],states[val])}]
    for name,model in models.items():
        model.fit(X[train],y[train]);fitted[name]=model
        val_rows.append({'model':name,**state_metrics(y[val],model.predict(X[val]))})
    winner=sorted(val_rows,key=lambda x:(-x['macro_f1'],x['model']))[0]['model']
    # No refit on validation: HMM/state definitions remain frozen throughout this experiment.
    test_rows=[{'model':'Persistence',**state_metrics(y[test],states[test])}]
    for name,model in fitted.items():test_rows.append({'model':name,**state_metrics(y[test],model.predict(X[test]))})
    prefix=min(train_boundary+50,n)
    changed=scaled.copy();changed[prefix:]+=100
    invariant=np.allclose(causal_filter(hmm,changed)[:prefix],proba[:prefix],atol=1e-12,rtol=0)
    assert invariant
    result={'status':'PASS','scope':'NEW_CHRONOLOGICAL_LATENT_STATE_EXPERIMENT','seed':SEED,'states':3,
      'hmm_fit_days':train_boundary,'hmm_converged_flag':bool(hmm.monitor_.converged),
      'train_pairs':len(train),'validation_pairs':len(val),'test_pairs':len(test),
      'periods':{key:{'first_feature_date':str(market.date.iloc[ix[0]].date()),'last_target_date':str(market.date.iloc[ix[-1]+1].date())}
        for key,ix in [('train',train),('validation',val),('test',test)]},
      'selected_using_validation':winner,'validation_metrics':val_rows,'test_metrics':test_rows,
      'causal_filter_future_perturbation_test':bool(invariant),'state_labels':'frozen HMM latent states, not observed economic ground truth',
      'backtest':'NOT_RUN','transaction_cost_evaluation':'NOT_RUN'}
    return result,proba,states,test,y
