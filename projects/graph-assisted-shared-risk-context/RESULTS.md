# Results and verification / Kết quả và kiểm tra

## Original thesis experiment

The report updated 23 October 2026 and the final v2.1 evidence lock agree on these
results. The selected aggregate files in [historical evidence](evidence/historical/)
are byte-for-byte copies checked against that lock's inventory.

| DGraphFin test metric | Node-only | Node + graph |
| --- | ---: | ---: |
| Test nodes | 183,840 | 183,840 |
| Positive labels | 2,326 | 2,326 |
| Average Precision | 0.025032560758073565 | 0.03250543778360551 |
| ROC-AUC | 0.7127446394300898 | 0.7684845987448782 |
| Top‑1% review slots | 1,839 | 1,839 |
| True positives in Top‑1% | 62 | 55 |

ΔAP = 0.007472877025531947. The saved 10,000 paired node-bootstrap resamples give a
95% interval of [0.006048999421841472, 0.008812994249018382]. Node resampling does not
remove dependence between connected graph nodes; this remains a statistical limitation.
AP and Top‑1% support different conclusions about the same two rankings.

The independent credit source has 195,420 holdout rows, AP 0.3286191945,
ROC-AUC 0.6624414216 and Brier score 0.1638282058. These scores belong to another
dataset and target and are not directly comparable to DGraphFin performance.

## Current checks — 25 October 2026

| Check | Result | What was actually executed |
| --- | --- | --- |
| Retrieved historical artifact hashes | 31/31 match | Original lock inventory compared with selected downloaded files |
| Saved-output metric replay | PASS | Recomputed AP/ROC-AUC/Top‑1% and credit Brier from original prediction/label files; tolerance 1e-12 |
| Full RQ2 source-field replay | PASS | 195,420 credit + 183,840 node-only + 183,840 node+graph rows; nine declared source fields preserved |
| Controlled routing | 13/13 PASS | All original expected statuses, routes and reasons checked against the historical scenario table |
| Repeated controlled outputs | PASS | 100 repetitions, one output hash; independent context order invariant |
| Unit tests | 10/10 PASS | Hand-calculated graph features, edge reversal, isolated nodes, ties, context semantics and aggregate integrity |
| Extracted scientific functions | 7/7 AST matches | Public functions compared with executed notebook source |
| Public explanatory notebooks | 2/2 PASS, 9/9 code cells | Fresh IPython process per notebook, actual outputs retained |
| Full research notebook syntax | 4/4 PASS | All code cells parsed; dataset-backed model fitting not rerun |
| Full LightGBM training | NOT_RUN in this publication | Original fitted models and saved predictions remain the experiment source |

Machine-readable records:

- [Saved-output replay](evidence/current/saved_output_replay.json)
- [Synthetic public demo](evidence/current/demo_results.json)
- [Unit, source-parity and syntax checks](evidence/current/verification.json)
- [Notebook execution](evidence/current/notebook_execution.json)

The replay verifies the saved bootstrap array and recalculates its quantiles. It does
not perform a new 10,000-resample run. Fresh synthetic examples and historical results
are labeled separately in the public notebooks.

## Reproduce the checks

From this project directory:

```bash
python -m pip install -r requirements.txt
python run_demo.py --output outputs/demo_results.json
python -m unittest discover -s tests -v
python run_notebooks.py --in-place --report outputs/notebook_execution.json
```

For the score-level replay, add the replay requirements and provide the original local
`protocol_v2_1` artifacts as described in [README](README.md#chạy-nhanh--quick-start).
For a new model-training experiment, follow the [research notebooks](research/README.md).

The current demo/replay environment uses CPython 3.12.14, NumPy 2.3.5, SciPy 1.17.0,
pandas 2.2.3, scikit-learn 1.8.0 and PyArrow 26.0.0. This is distinct from the captured
historical training environment in `PROVENANCE.json`.

## Interpretation

**STILL VALID:** graph-derived features improved AP/ROC-AUC in the reported setup while
Top‑1% positives fell from 62 to 55. Neither a shared score nor a real customer join is
part of the thesis design. The system checks establish conformance to its declared
academic contract; they do not measure real banking decision quality.

**REVISED — publication coverage:** the portfolio now contains source code and executable
demonstrations in addition to the original case study. Saved experimental outputs have
been independently recomputed; the historic benchmark is not relabeled as new training.
