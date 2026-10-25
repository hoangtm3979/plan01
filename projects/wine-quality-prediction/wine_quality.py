"""Wine coursework reproduction with grouped duplicates and train-only model selection."""
from pathlib import Path
import hashlib
import io
import zipfile
import urllib.request

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import StratifiedGroupKFold, GroupKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score,
    confusion_matrix, root_mean_squared_error, mean_absolute_error, r2_score,
)

DATA_URL = 'https://archive.ics.uci.edu/static/public/186/wine+quality.zip'
SEED = 42
DATA_SHA256={'winequality-red.csv':'4a402cf041b025d4566d954c3b9ba8635a3a8a01e039005d97d6a710278cf05e',
             'winequality-white.csv':'76c3f809815c17c07212622f776311faeb31e87610d52c26d87d6e361b169836'}


def load_wine(data_dir='data/local'):
    """Cache exact official red and white CSVs; never silently fabricate data."""
    data_dir=Path(data_dir); data_dir.mkdir(parents=True,exist_ok=True)
    names=['winequality-red.csv','winequality-white.csv']
    if not all((data_dir/name).exists() for name in names):
        with urllib.request.urlopen(DATA_URL,timeout=60) as response:
            archive=zipfile.ZipFile(io.BytesIO(response.read()))
        for name in names: (data_dir/name).write_bytes(archive.read(name))
    frames=[]; fingerprints={}
    for name in names:
        raw=(data_dir/name).read_bytes(); fingerprints[name]=hashlib.sha256(raw).hexdigest()
        if fingerprints[name]!=DATA_SHA256[name]:raise ValueError('Unexpected data fingerprint: '+name)
        frame=pd.read_csv(io.BytesIO(raw),sep=';');frame['wine_type']='red' if 'red' in name else 'white';frames.append(frame)
    data=pd.concat(frames,ignore_index=True)
    features=[c for c in data.columns if c not in ['quality','wine_type']]
    if len(data)!=6497 or len(features)!=11 or data[features+['quality']].isna().any().any():
        raise ValueError('Official Wine Quality schema/count check failed; inspect the input files.')
    return data,features,fingerprints


def grouped_split(data,features):
    """Identical feature vectors stay together, even when observed labels differ."""
    groups=pd.util.hash_pandas_object(data[features],index=False).to_numpy()
    y=(data['quality']>=6).astype(int)
    splitter=StratifiedGroupKFold(n_splits=5,shuffle=True,random_state=SEED)
    train,test=next(splitter.split(data[features],y,groups))
    assert not set(groups[train]) & set(groups[test])
    return train,test,groups


def classification_models():
    from lightgbm import LGBMClassifier
    from xgboost import XGBClassifier
    return {
        'Logistic Regression':make_pipeline(SimpleImputer(strategy='median'),StandardScaler(),LogisticRegression(max_iter=2000,random_state=SEED)),
        'Decision Tree':make_pipeline(SimpleImputer(strategy='median'),DecisionTreeClassifier(max_depth=6,min_samples_leaf=5,random_state=SEED)),
        'LightGBM':make_pipeline(SimpleImputer(strategy='median'),LGBMClassifier(n_estimators=200,learning_rate=.05,num_leaves=15,max_depth=6,random_state=SEED,n_jobs=1,verbosity=-1,deterministic=True,force_col_wise=True)),
        'XGBoost':make_pipeline(SimpleImputer(strategy='median'),XGBClassifier(n_estimators=200,learning_rate=.05,max_depth=4,subsample=1,colsample_bytree=1,eval_metric='logloss',random_state=SEED,n_jobs=1,tree_method='hist')),
    }


def run_classification(data,features,train,test,groups):
    X=data[features];y=(data.quality>=6).astype(int)
    cv=StratifiedGroupKFold(n_splits=3,shuffle=True,random_state=SEED)
    folds=list(cv.split(X.iloc[train],y.iloc[train],groups[train]))
    for a,b in folds: assert not set(groups[train][a])&set(groups[train][b])
    cv_rows=[];fitted={}
    for name,model in classification_models().items():
        scores=cross_val_score(model,X.iloc[train],y.iloc[train],cv=folds,scoring='f1_macro',n_jobs=1,error_score='raise')
        cv_rows.append({'model':name,'cv_macro_f1_mean':float(scores.mean()),'cv_macro_f1_std':float(scores.std()),'fold_scores':[float(x) for x in scores]})
    cv_table=pd.DataFrame(cv_rows).sort_values(['cv_macro_f1_mean','model'],ascending=[False,True])
    winner=cv_table.iloc[0]['model']
    # The winner is frozen above, before accessing any held-out metrics.
    rows=[]
    for name,model in classification_models().items():
        model.fit(X.iloc[train],y.iloc[train]);p=model.predict_proba(X.iloc[test])[:,1];pred=(p>=.5).astype(int)
        fitted[name]=model
        rows.append({'model':name,'accuracy':float(accuracy_score(y.iloc[test],pred)),'precision':float(precision_score(y.iloc[test],pred,zero_division=0)),
                     'recall':float(recall_score(y.iloc[test],pred,zero_division=0)),'f1':float(f1_score(y.iloc[test],pred,zero_division=0)),
                     'macro_f1':float(f1_score(y.iloc[test],pred,average='macro',zero_division=0)),'roc_auc':float(roc_auc_score(y.iloc[test],p)),
                     'confusion_matrix':confusion_matrix(y.iloc[test],pred,labels=[0,1]).tolist()})
    return cv_table,pd.DataFrame(rows),winner,fitted


def run_regression(data,features,train,test,groups):
    X=data[features];y=data.quality
    models={
       'Ridge':make_pipeline(SimpleImputer(strategy='median'),StandardScaler(),Ridge(alpha=1.0)),
       'Random Forest':make_pipeline(SimpleImputer(strategy='median'),RandomForestRegressor(n_estimators=150,min_samples_leaf=2,random_state=SEED,n_jobs=1)),
    }
    folds=list(GroupKFold(n_splits=3).split(X.iloc[train],y.iloc[train],groups[train]))
    cv=[]
    for name,model in models.items():
        scores=-cross_val_score(model,X.iloc[train],y.iloc[train],cv=folds,scoring='neg_root_mean_squared_error',n_jobs=1,error_score='raise')
        cv.append({'model':name,'cv_rmse_mean':float(scores.mean()),'cv_rmse_std':float(scores.std())})
    winner=min(cv,key=lambda r:(r['cv_rmse_mean'],r['model']))['model']
    rows=[];predictions={}
    for name,model in models.items():
        model.fit(X.iloc[train],y.iloc[train]);p=model.predict(X.iloc[test]);predictions[name]=p
        rows.append({'model':name,'rmse':float(root_mean_squared_error(y.iloc[test],p)), 'mae':float(mean_absolute_error(y.iloc[test],p)), 'r2':float(r2_score(y.iloc[test],p))})
    return pd.DataFrame(cv),pd.DataFrame(rows),winner,predictions
