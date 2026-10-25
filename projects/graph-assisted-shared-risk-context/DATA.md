# Data / Dữ liệu

## DGraphFin

- Official project and loader: [DGraphFin baseline](https://github.com/DGraphXinye/DGraphFin_baseline),
  [PyG DGraphFin documentation](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.DGraphFin.html).
- Dataset reference: 3,700,550 nodes, 4,300,999 directed edges, 17 node features.
- Edges represent an emergency-contact relationship. They are not payment transactions.
- Obtain `DGraphFin.zip` through the dataset's official download instructions and place it at
  `<KLTN_WORKSPACE>/data/DGraphFin/raw/DGraphFin.zip`.
- The thesis keeps original masks and evaluates only binary-labeled records. Its declared
  transductive setting permits unlabeled graph topology and node features; it is not a
  prospective, time-sliced deployment evaluation.

Graph features are log in/out degree, reciprocity ratio, outgoing relation-type diversity
and the mean of outgoing neighbors' node features. Duplicate edges become binary adjacency;
isolated nodes get zero neighbor means. No labels are passed to the graph-feature function.

## LendingClub granting-model dataset

- Source: [Zenodo record 11295916, version 0.1](https://doi.org/10.5281/zenodo.11295916),
  Ariza-Garzón, Sanz-Guerrero, Arroyo Gallardo and Lending Club.
- The source defines its target from resolved loan outcomes. Read its data dictionary and
  terms before reuse; a source-model score is not automatically a calibrated bank PD.
- Put the actual CSV at `<KLTN_WORKSPACE>/data/LendingClub/LC_loans_granting_model_dataset.csv`.
  Check whether a downloaded file is compressed before treating it as CSV.
- The thesis separates chronological month groups: train through April 2016,
  validation through February 2017, holdout March 2017–December 2018. Exact row counts
  and the nine selected features are in `evidence/historical/credit_split_summary.csv`
  and `credit_feature_manifest.json`.

The datasets describe different populations and entity types. This project does not
join LendingClub loan IDs to DGraphFin node IDs.

## Public examples and saved-output replay

The small five-node graph and `DEMO-*` records are synthetic examples defined in
`shared_risk_context/examples.py`. Their scores are hand-specified fixtures, not outputs
from a newly trained model. They only demonstrate feature and routing behavior.

`evidence/historical/` contains selected aggregate files from the thesis. Their bytes are
checked against `source_hashes.json`. The replay tool requires original prediction/label
Parquet files and the saved bootstrap array under a local `protocol_v2_1` directory.
It does not download them, retrain a model or regenerate bootstrap resamples.
