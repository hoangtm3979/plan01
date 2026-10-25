# Public Portfolio Evidence Register / Sổ đối chiếu bằng chứng

**Review date / Ngày rà soát:** 2026-10-25

This register distinguishes files that have actually been inspected from evidence that is still missing. A course report is **not** the same as an independently reproducible benchmark. A GitHub repository is **not** the same as a live service.

| Case | Source checked / Nguồn đã xem | Claim allowed / Có thể nói | Missing evidence / Còn thiếu |
| --- | --- | --- | --- |
| Credit Risk | Public `credit` notebook with stored code and execution outputs | A Colab run recorded 2.03m training / 0.665m holdout rows; ROC-AUC values stored | Dataset rights/lineage, clean replay, temporal leakage & imputation audit, fresh environment |
| Credit AI Thinking Starter | Public `danhgiatindungcanhan` root file listing + report outline | Educational scaffold and planning of ML pipeline | Missing `src/train.py`/`src/infer.py` referred to in former README; real trained pipeline |
| SNJ RAG | Owner's UIT PDF course report | Coursework describes 376 items/22 fields, hybrid retrieval, curated evaluation | Sanitized code/dataset, independent held-out queries, WooCommerce baseline, service logs |
| RegimeLens | UIT Big Data team report | Team report states HMM/XGBoost/backtest experiment | Code, point-in-time replay, revised macro-data as-of check, transaction costs, individual contributions |
| Traffic QA | Two UIT NLP/Python team reports | Team designed text and sign-image retrieval system | Source, non-template experiment log, current law corpus, validated GCP deployment |
| PAR | Public `aegi-par-demo` README/source listing | Local UI workflow and scoped synthetic/benchmark narrative | Current deployment verification, third-party test, real-world outcome evidence |
| Wine Quality | UIT ML team DOCX | Team compared standard ML models on UCI Wine Quality | Full notebook, metrics and reproducible run, contribution breakdown |
| IoT/CV Face | User description | Owner reports a face-detection coursework project | Matching source, report, exact model, dataset consent and evaluation |
| Commercial | User-supplied business history; records remain private | Describe negotiation/refund/sourcing as anonymized case studies | Verify ownership and settlement; redact supplier/buyer/client names; KPI/revenue mapping |

## Evidence classification / Phân loại

- **E0 — Narrative only / Chỉ lời kể:** user description, no inspected artifact.
- **E1 — Report / Báo cáo:** a document describes inputs, methods or results.
- **E2 — Executed artifact / Artifact có output:** source with saved execution result, still subject to audit.
- **E3 — Reproduced / Tái lập độc lập:** pinned data/dependencies, fresh repeat and acceptance checks.
- **E4 — Operational / Vận hành:** controlled deployment, logs, monitoring, security and outcome evidence.
- **E5 — External outcome / Kết quả thực tế:** independent customer/user/business evidence.

**The current portfolio makes no E4/E5 claim for these academic or synthetic AI projects.**

## Immediate public-repository exposure check / Kiểm tra phơi lộ hiện hữu

The **already-public** `hoangtm3979/aegi-par-demo` repository contains a file named `AEGI_PAR_P3_APP_BUNDLE.zip` (~80 KB) in addition to source/documentation. Its exact binary contents were **not audited** in this review. The owner should inspect its archive manifest and contents against current IP/security authority **before promoting the link more widely**. Do not infer the archive is safe merely because it was previously committed.

AEGI Shield's internal public-claim guard is a **release-candidate control**, not blanket permission to republish Shield/Core implementation, private evidence, or patent-sensitive details in a personal portfolio. Consequently, the portfolio uses high-level references only.

## Before publishing original files / Trước khi upload tài liệu gốc

- [ ] Verify that all code, data and model weights can legally be redistributed.
- [ ] Obtain agreement for identifying team member contributions.
- [ ] Remove personal identifiers, order/customer details, bank and vendor emails, receipts and private addresses.
- [ ] Scan notebooks and datasets for API keys, Colab mount references and embedded secrets.
- [ ] Strip proprietary AEGI/patent-sensitive details and unpublished internals.
- [ ] Record dataset version, training seed, environment, model parameters and expected metric tolerances.
- [ ] Run source from a clean clone without unpublished Drive dependencies.
- [ ] Verify cloud demo isolation and avoid ongoing charges.

## Không công bố / Do not publish raw

AEGI private Core/Shield/Ops source or PCT specification; personal eBay/Meta/Google advertising receipts; Helium10 support thread; Philippines B2B spreadsheet; customers' identities; credentials; private SNJ catalog exports; photos/face datasets without appropriate permission.

_Goal: evidence that can withstand technical questions, not merely a polished project description._
