# Colab source audit & release queue / Nhật ký kiểm tra Colab

**Inventory date / Ngày kiểm tra: 2026-10-25.** Read-only inspection of the `lapnhan81` and `hoangaegi89` Colab folders; no private source code or raw Drive account links are mirrored here.

## Inventory findings / Kết quả thống kê

| Scope | Source checked | Interpretation |
| --- | ---: | --- |
| Folder items listed / Mục trong thư mục | 94 + 19 = **113** | Mixed folders, data and notebook files |
| Notebook-looking items / Mục dạng notebook | **103** | 101 native Colab notebooks plus 2 `.ipynb` files stored with other MIME types |
| Native notebook JSONs parsed / File Colab đọc được JSON | **101/101** | Metadata + code/output structure scanned, not independently executed |
| All code cells have historical execution counters | **52** | Does **not** prove correctness or reproduce in a fresh runtime |
| Some, not all, code cells historically executed | **21** | Partial/inconsistent notebook runs |
| No code cells with execution counter | **28** | Includes blank/Untitled documents |
| At least one saved error output / Có lưu lỗi | **22** | Includes runtime/import/path errors, some despite other executed cells |

**Do not add the 52/21/28 categories to the two non-native notebooks.** The non-native `BIGDATA_mode_test_.ipynb` and `02410008-Truong Minh Hoang.ipynb` were examined separately. Entries include duplicate/copy versions and private R&D notebooks; these are **file counts, not independent projects**.

## Audit outcomes / Kết luận phân loại

| Topic | Evidence observed | Portfolio treatment |
| --- | --- | --- |
| Python fundamentals | Interactive input, file upload, arrays, basic algorithms; some missing local files | One cleaned source example; keep failed cases as honest learning history |
| Math, PCA and clustering | Saved vector/PCA calculations; nonlinear clustering comparisons, some cells unexecuted | Cleaned examples with reproducibility caveats |
| Classical ML | Regression, classification, tree ensembles, many course/copy notebooks | One cleaned toy lab and project-level case studies; **no course handout mass copy** |
| Deep Learning | TensorFlow MNIST and FCN with historical saved executions | Cleaned notebooks only, no model weights/outputs |
| Vietnamese NLP | Tokenizer exercises have duplicated versions and auto-grading fragments; sentiment notebook references unavailable `UIT-VSFC.zip` | Educational summary; no grader templates or dataset redistribution |
| Medical image segmentation | Educational U-Net notebook references `Dataset_BUSI.zip` on private Drive | Educational [source review](notes/busi-unet.md); no patient images or model export |
| Applied e-commerce AI | Purchase-intent/expected-value notebook | Curated synthetic/education case; no business KPI claim |
| Finance/Big Data | Historical notebook code and group report **do not yet establish source/result parity** | [REVISED warning](../projects/regimelens.md); no leakage-safe claim |
| SNJ RAG | Multiple Colab versions with private product data | [Project case](../projects/snj-hybrid-rag.md); source pending IP/data review |
| AEGI research and thesis | Many internal versioned notebooks, group projects and source dependencies | **Not copied to personal public repository** |

Exact source inspection found duplicate content clusters, including unnamed empty notebooks, multiple versions of a tokenizer exercise and two identical credit-scoring notebook copies. Some notebooks have similar titles but non-identical cells; deduplication by filename alone would misstate the learning record.

### Specific problems worth discussing in interviews

1. **Missing dependencies:** course CSV paths, pretrained weights, Drive mounts, ZIP inputs and version-specific packages must be documented or replaced by legal public fixtures.
2. **Runtime errors:** at least 22 native Colab notebooks contain saved error outputs. An executed cell count alone is inadequate evidence.
3. **Classification leakage:** training/validation must be split before fitting data-dependent transforms; the RegimeLens historical notebook needs a point-in-time HMM relabeling protocol.
4. **Privacy and ownership:** biometric datasets, customer data, team-author attribution, private advertising bills, unpublished AEGI code and PCT materials are excluded.

## Publication levels / Mức công bố

- **L0 — Catalogued:** title/topic recognized; no runnable public source.
- **L1 — Sanitized learning source:** notebook/code scanned and outputs stripped; *not independently replayed*.
- **L2 — Reproduced lab:** clean environment, pinned data/dependencies, working command and expected result.
- **L3 — Portfolio project:** complete bilingual case study, independent benchmark, owner contribution and demo/reliability claims supported.

Current uploaded Colab examples are **L1**. Even the ones with historical execution counters have not passed L2. The strong academic projects remain at report/prototype evidence levels, not production proof.

## Reproduction gates / Checklist tái lập

- [ ] Verify data rights, provenance and contributor attribution.
- [ ] Use a public/open or permission-cleared dataset; supply version/checksum.
- [ ] Lock packages, seed and hardware assumptions; remove Google Drive absolute paths.
- [ ] Re-execute every cell in order in a clean environment.
- [ ] Check target leakage, CV folds, temporal availability and objective/metric fit.
- [ ] Document baseline, negative tests and limitations in EN + VI.
- [ ] Scan for secrets, keys, personal data, bank/vendor details and research IP.
- [ ] Record outcome: PASS, ERROR, NOT_RUN, or WITHHELD; do not silently erase failed cases from history.

_This file is an audit index and public release boundary. It is not a claim that all archived Colab experiments are independently correct or should be publicly distributed._
