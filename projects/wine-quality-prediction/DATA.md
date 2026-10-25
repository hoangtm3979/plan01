# Wine Quality — Data & Protocol

Source: [UCI Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality), DOI [10.24432/C56S3T](https://doi.org/10.24432/C56S3T). Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). License: CC BY 4.0. The original semicolon-separated red/white CSVs are downloaded from the official UCI archive.

| File | Rows | SHA-256 |
| --- | ---: | --- |
| winequality-red.csv | 1,599 | `4a402cf041b025d4566d954c3b9ba8635a3a8a01e039005d97d6a710278cf05e` |
| winequality-white.csv | 4,898 | `76c3f809815c17c07212622f776311faeb31e87610d52c26d87d6e361b169836` |

Binary target: quality ≥6. Regression target: original quality score. Features: the 11 physicochemical measurements. Wine type is used for EDA, not input.

Identical 11-feature vectors share one group even if their observed targets differ. The first fold of shuffled StratifiedGroupKFold(5, seed=42) is the holdout; the remaining rows are development data. Three grouped folds inside development choose a fixed classifier by macro F1. Regression uses GroupKFold(3) and RMSE on the same development/holdout groups. No threshold or hyperparameter tuning follows inspection of holdout metrics.

All original rows remain. There are 5,318 distinct feature vectors and zero shared groups across train/holdout or inner classification folds. This controls measured duplicates; no winery/batch identifiers are available to establish broader sample independence.
