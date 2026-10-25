# Traffic-Law QA — Source & Evaluation Audit

## Recovered materials

`Question_Traffic.ipynb` has 105 cells, including 46 code cells, multiple retrieval/generation redefinitions, placeholder answers, fixed confidence placeholders and saved errors. SBERT/FAISS retrieval, OCR and attempted PhoBERT generation appear in the history; this is not a single clean implementation of every method listed in the report. The historical source is syntax-checked, not fully rerun.

The recovered release README describes a two-document corpus and labeled train questions with image references. The new script indexes only `(law_id, article_id)` plus article text and asks only the `question` field; it excludes choices, answers and image content from queries/index fitting. TF-IDF and BM25 parameters were fixed before this replay; no labels were used to train them.

## Corpus alignment

The raw JSON has 399 records. K.1 and K.2 each occur three times for related subsections. All their text is concatenated under the source parent key used by labels, yielding 395 unique law/article keys. No subsection text is discarded. A total of 40/530 questions have at least one relevance key absent from this snapshot. They remain in the evaluation denominator; missing keys are not guessed or repaired from the scores.

| Input | SHA-256 |
| --- | --- |
| vlsp2025_law.json | `e499512ff55703c8489ada1e72a4e7d66042f54bdefe947ab110032a80c4cac0` |
| vlsp_2025_train.json | `49d28bcef00906ebf3da4331306d08158150da237d0106ddb28fa9b6a1bf9d03` |

## Metric interpretation

Precision@1 = relevant first result. Recall@5 = distinct relevant article hits / all supplied relevant article keys. MRR@10 = reciprocal rank of the first hit within ten results, else zero. Duplicated retrieved IDs are counted once; law/article pairs keep article 1 in different laws separate. No-match does not force a top result.

All 530 labeled train questions refer to images. Ignoring the image removes task information. Thus the new low text-only results cannot be compared directly with the report's 0.72/0.88 retrieval and ~92% sign recognition. They identify missing engineering/evaluation work rather than replace that report with an equivalent benchmark.

## Next bounded experiment

Resolve corpus/label version alignment; define image groups before splitting to avoid near-duplicate leakage; freeze a development protocol; compare lexical/dense/reranked retrieval with and without image-derived tokens on the same query set; evaluate generator grounding separately. Raw corpus/questions/images are not redistributed. No current legal advice or law-validity claim is made by this academic replay.
