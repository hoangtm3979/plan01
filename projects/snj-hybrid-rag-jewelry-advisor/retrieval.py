"""Catalog retrieval with explicit constraints. No generation API or commerce side effects."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from domain import (
    normalize_vi, parse_query, contains_any_phrase, extract_query_sizes,
    STONE_SYNONYMS, COLOR_TERMS,
)

MODEL_NAME='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'


def minmax(values):
    values=np.asarray(values,dtype=float)
    return np.zeros_like(values) if len(values)==0 or np.isclose(np.ptp(values),0) else (values-values.min())/np.ptp(values)


def row_text(row):
    return ' '.join(str(row.get(c,'')) for c in ['name','stone_names','color','category'] if pd.notna(row.get(c,'')))


def has_size(row,size):
    value=pd.to_numeric(row.get('size_value'),errors='coerce')
    unit=normalize_vi(row.get('size_unit','mm'))
    if pd.notna(value) and unit in ['mm','ly'] and np.isclose(float(value),size): return True
    return any(np.isclose(x,size) for x in extract_query_sizes(row.get('name','')))


def has_certificate(row):
    value=' '.join(str(row.get(c,'')) for c in ['certificate','certificate_code'] if pd.notna(row.get(c,'')))
    value=normalize_vi(value).strip()
    if not value or value in ['none','nan','khong','no','false','0']:return False
    if contains_any_phrase(value,['không kiểm định','không có','chưa kiểm định']):return False
    return contains_any_phrase(value,['PNJ','SJC','GIA','kiểm định','chứng nhận','yes','true'])


def matches(row,profile):
    """Unknown prices never satisfy an upper budget; mandatory attributes are not relaxed."""
    from domain import PRODUCT_INTENT_RULES
    intent=profile['product_intent']
    if intent and row['category'] not in PRODUCT_INTENT_RULES[intent]['categories']:return False
    if profile['max_price'] is not None:
        price=pd.to_numeric(row.get('price'),errors='coerce')
        if pd.isna(price) or price<=0 or price>profile['max_price']:return False
    if profile['certificate_required'] and not has_certificate(row):return False
    if profile['sizes'] and not any(has_size(row,s) for s in profile['sizes']):return False
    text=row_text(row)
    attributes=[]
    if profile['stones']:attributes.append(any(contains_any_phrase(text,STONE_SYNONYMS[s]+[s]) for s in profile['stones']))
    if profile['colors']:attributes.append(any(contains_any_phrase(text,COLOR_TERMS[c]) for c in profile['colors']))
    if attributes and not (any(attributes) if profile.get('attribute_or') else all(attributes)):return False
    if profile['genders']:
        gender=normalize_vi(row.get('gender_fit',''))
        allowed=set(profile['genders'])|{'unisex','all','both'}
        if gender not in allowed:return False
    return True


class CatalogRetriever:
    def __init__(self,catalog,model_dir=None,model_revision=None):
        self.df=catalog.copy().reset_index(drop=True)
        required=['product_id','name','category','price','search_text']
        if any(c not in self.df for c in required):raise ValueError('Missing catalog columns: '+', '.join(c for c in required if c not in self.df))
        if self.df.product_id.isna().any() or self.df.product_id.astype(str).duplicated().any():raise ValueError('product_id must be unique and present')
        self.df['price']=pd.to_numeric(self.df.price,errors='coerce')
        texts=self.df.search_text.fillna('').astype(str).tolist()
        self.vectorizer=TfidfVectorizer(preprocessor=normalize_vi,lowercase=False,ngram_range=(1,3),max_df=1.0)
        self.tfidf=self.vectorizer.fit_transform(texts)
        self.model=None;self.embeddings=None;self.mode='lexical_rules'
        if model_dir is not None:
            from sentence_transformers import SentenceTransformer
            self.model=SentenceTransformer(str(model_dir),device='cpu',revision=model_revision,trust_remote_code=False)
            self.embeddings=self.model.encode(texts,normalize_embeddings=True,batch_size=32,show_progress_bar=False)
            self.mode='dense_lexical_rules'

    def retrieve(self,query,top_k=5):
        if not isinstance(query,str) or not query.strip():return self.df.iloc[:0].assign(final_score=pd.Series(dtype=float))
        if not isinstance(top_k,int) or top_k<1:raise ValueError('top_k must be a positive integer')
        profile=parse_query(query)
        profile['attribute_or']=contains_any_phrase(query,['hoặc','or'])
        mask=self.df.apply(lambda r:matches(r,profile),axis=1)
        candidates=self.df.loc[mask].copy();idx=candidates.index.to_numpy()
        if not len(candidates):return candidates.assign(final_score=pd.Series(dtype=float))
        keyword=(self.tfidf[idx]@self.vectorizer.transform([query]).T).toarray().ravel()
        # No arbitrary default product when a general lexical query has no catalog overlap.
        if self.model is None and not np.any(keyword>0):return candidates.iloc[:0].assign(final_score=pd.Series(dtype=float))
        dense=np.zeros(len(candidates))
        if self.model is not None:
            dense=self.embeddings[idx]@self.model.encode([query],normalize_embeddings=True,show_progress_bar=False)[0]
        # Constraints are enforced above; rule score expresses matched requested fields.
        requested=sum(bool(profile[k]) for k in ['product_intent','stones','colors','genders','sizes','certificate_required'])
        rule=np.full(len(candidates),min(1.,.2+.15*requested))
        candidates['dense_score']=dense;candidates['keyword_score']=keyword;candidates['rule_score']=rule
        candidates['final_score']=(.40*minmax(dense)+.25*minmax(keyword)+.30*rule) if self.model is not None else (.65*minmax(keyword)+.30*rule)
        candidates['retrieval_mode']=self.mode
        candidates['_tie']=candidates.product_id.astype(str)
        return candidates.sort_values(['final_score','_tie'],ascending=[False,True],kind='stable').head(top_k).drop(columns='_tie')


def format_answer(rows):
    if rows.empty:return 'Chưa có sản phẩm thỏa đủ điều kiện trong catalog. Hãy bổ sung hoặc điều chỉnh yêu cầu.'
    lines=[]
    for _,row in rows.iterrows():
        price=row.get('price')
        value=f'{price:,.0f} VND' if pd.notna(price) and price>0 else 'giá cần xác minh'
        lines.append(f"{row['product_id']} — {row['name']} — {value}")
    return '\n'.join(lines)+'\nThông tin lấy từ bản catalog đã nạp; giá và tồn kho thực tế cần được kiểm tra tại nguồn.'
