"""Text-only retrieval replay on a versioned VLSP corpus. No legal answer generation."""
from pathlib import Path
import hashlib, json, re, unicodedata
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def normalize(text):
    text=unicodedata.normalize('NFC',str(text).lower())
    return re.sub(r'\s+',' ',text).strip()


def article_key(law_id,article_id): return str(law_id).strip()+'::'+str(article_id).strip()


def load_articles(path):
    raw=Path(path).read_bytes(); laws=json.loads(raw)
    records=[]
    for law in laws:
        for article in law['articles']:
            records.append({'id':article_key(law['id'],article['id']),
              'text':str(article.get('title',''))+'\n'+str(article.get('text',''))})
    # The supplied corpus repeats K.1/K.2 for their subsections. Preserve all text
    # under the exact parent identifier used by the relevance labels.
    combined={}
    for record in records:combined.setdefault(record['id'],[]).append(record['text'])
    articles=[{'id':key,'text':'\n\n'.join(parts)} for key,parts in combined.items()]
    return articles,hashlib.sha256(raw).hexdigest()


class TextRetriever:
    def __init__(self,articles):
        self.ids=np.array([r['id'] for r in articles]);texts=[r['text'] for r in articles]
        if len(set(self.ids))!=len(self.ids):raise ValueError('Article identifiers must be unique')
        self.tfidf_vectorizer=TfidfVectorizer(preprocessor=normalize,lowercase=False,ngram_range=(1,2))
        self.tfidf=self.tfidf_vectorizer.fit_transform(texts)
        self.count_vectorizer=CountVectorizer(preprocessor=normalize,lowercase=False)
        counts=self.count_vectorizer.fit_transform(texts).tocsr()
        length=np.asarray(counts.sum(axis=1)).ravel();avg=float(length.mean())
        df=np.asarray((counts>0).sum(axis=0)).ravel();n=len(articles)
        self.idf=np.log1p((n-df+.5)/(df+.5))
        self.bm25=counts.astype(float)
        rows=np.repeat(np.arange(n),np.diff(counts.indptr))
        frequency=self.bm25.data.copy()
        norm=1.5*(1-.75+.75*length/max(avg,1))
        self.bm25.data=frequency*2.5/(frequency+norm[rows])
        self.bm25=self.bm25.multiply(self.idf).tocsr()

    def retrieve(self,query,method='bm25',k=10):
        if method=='bm25':
            terms=self.count_vectorizer.transform([query]);terms.data[:]=1
            scores=(self.bm25@terms.T).toarray().ravel()
        elif method=='tfidf':scores=(self.tfidf@self.tfidf_vectorizer.transform([query]).T).toarray().ravel()
        else:raise ValueError('Unknown method')
        order=np.lexsort((self.ids,-scores))
        return [str(self.ids[i]) for i in order[:k] if scores[i]>0]


def ranking_metrics(retrieved,relevant):
    relevant=set(relevant)
    if not relevant:raise ValueError('A labeled case needs at least one relevant article')
    unique=list(dict.fromkeys(retrieved))
    rr=next((1/(i+1) for i,key in enumerate(unique[:10]) if key in relevant),0.)
    return {'precision_at_1':float(bool(unique) and unique[0] in relevant),
        'recall_at_5':len(set(unique[:5])&relevant)/len(relevant),'mrr_at_10':rr}


def evaluate(articles,questions):
    engine=TextRetriever(articles);known=set(engine.ids);results={};reference_issues=0;labeled=[]
    for q in questions:
        relevant={article_key(r['law_id'],r['article_id']) for r in q.get('relevant_articles',[])}
        if not relevant:continue
        reference_issues+=int(not relevant.issubset(known));labeled.append((q,relevant))
    if not labeled:raise ValueError('No labeled retrieval cases')
    for method in ['tfidf','bm25']:
        rows=[ranking_metrics(engine.retrieve(q['question'],method),rel) for q,rel in labeled]
        results[method]={key:float(np.mean([r[key] for r in rows])) for key in rows[0]}
    return {'scope':'DEV_REPLAY_TEXT_ONLY','articles':len(articles),'questions':len(questions),
      'labeled_questions':len(labeled),'questions_with_unknown_article_reference':reference_issues,
      'queries_with_image_reference':sum(bool(q.get('image_id')) for q,_ in labeled),
      'uses_question_text_only':True,'uses_choices':False,'uses_images':False,
      'fits_to_question_labels':False,'generation':'NOT_RUN','cross_encoder':'NOT_RUN',
      'bm25_parameters':{'k1':1.5,'b':.75},'metrics':results}


def run_files(law_path,question_path):
    articles,law_hash=load_articles(law_path);raw=Path(question_path).read_bytes();questions=json.loads(raw)
    result=evaluate(articles,questions)
    result['source_sha256']={'law_json':law_hash,'question_json':hashlib.sha256(raw).hexdigest()}
    result['duplicate_article_id_policy']='concatenate source subsections under the labeled (law_id, article_id) key'
    return result


def sample_data():
    # Deliberately fictional catalog, not legal text or rules.
    articles=[{'id':'DEMO::1','text':'Tài liệu minh họa màu đỏ hình tròn.'},
      {'id':'DEMO::2','text':'Tài liệu minh họa màu xanh hình vuông.'},
      {'id':'DEMO::3','text':'Tài liệu minh họa màu vàng hình tam giác.'}]
    questions=[{'id':f'DEMO-{i}','question':q,'relevant_articles':[{'law_id':'DEMO','article_id':str(i)}]}
      for i,q in [(1,'màu đỏ hình tròn'),(2,'màu xanh hình vuông'),(3,'màu vàng tam giác')]]
    return articles,questions


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--law-json',required=True);p.add_argument('--questions-json',required=True);p.add_argument('--output',default='evidence/text_retrieval_replay.json');args=p.parse_args()
    result=run_files(args.law_json,args.questions_json);out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print(json.dumps(result,indent=2,ensure_ascii=False))
