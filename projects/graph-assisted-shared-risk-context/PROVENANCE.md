# Source and version notes / Ghi nguồn và phiên bản

**Author / Người thực hiện:** Trương Minh Hoàng, MSSV 25410008.  
**Academic scope:** Graph-Assisted Shared Risk Context, individual AI undergraduate thesis.

## Materials read for this publication

- Final academic report `25410008_Truong_Minh_Hoang_KLTN.docx`, updated 23 October 2026.
  Its bytes match the updated `BAO_CAO_KLTN_25410008_Truong_Minh_Hoang_2110.docx` copy.
- Four executed personal Colab notebooks for protocol v2.1, including the patched final
  RQ1 access block and final evidence-lock cell in RQ2.
- Original final evidence lock v2.1 and 31 selected artifacts checked against its inventory,
  including prediction/label files, summaries, models and saved bootstrap samples.
- Official dataset descriptions linked in [DATA.md](DATA.md).

Hashes and the original recorded runtime are in [PROVENANCE.json](PROVENANCE.json).
No claim is made that every historical draft or post-thesis ablation has been reproduced.

## Public implementation

The graph-feature formula, score metric, context adapter, validator, canonical output and
controlled multi-context route are extracted from the executed academic notebook code.
The 13 expected scenario statuses/routes match the historical scenario table. The public
contract and routing-policy semantic hashes match the original aggregate files.

Changes for publication:

- Extract reusable functions into `shared_risk_context/`.
- Add five-node and `DEMO-*` synthetic fixtures so a reader can inspect behavior quickly.
- Add a CLI, tests, two explanatory notebooks and a saved-output replay tool.
- Keep the four full research notebooks, clear historical outputs/account metadata, make
  workspace/pointer paths configurable, and default to a new reproduction workspace.
- Default final-evaluation flags to development mode. Preserve the scientific feature
  formulas, model candidate grids, seed lists, bootstrap procedure and validation routes.

The validator is the v2.1 research implementation, not an expanded production interface.
It assumes the declared source registry and JSON-like inputs used in the thesis. Its
JSON hashing procedure is the study's Python serialization convention; no cross-language
canonicalization or general assurance certification is implied.

## Evidence interpretation

`evidence/historical/` stores original aggregate bytes. `evidence/current/` stores new
verification results and notebook outputs. The replay reads original prediction files
to check metrics and field preservation; it does not refit LightGBM. The saved bootstrap
array is hash-verified and its quantiles recalculated, rather than resampled again.

**STILL VALID:** original AP/ROC-AUC/Top‑1% results, their interpretation limits, and the
separation of LendingClub and DGraphFin populations. The main post-hoc next steps remain
directional feature ablation and tie-sensitivity analysis.

**REVISED:** the portfolio previously offered only a case-study page for this thesis.
It now includes academic source code, research notebooks, runnable examples and an
evidence replay. This changes publication coverage, not the historical experiment results.
