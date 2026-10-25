"""Thesis ranking metrics; ties are ordered by ascending numeric entity ID."""
import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score

def score_metrics(y_true: np.ndarray, score: np.ndarray, entity_ids: np.ndarray) -> dict:
    top_n = max(1, int(np.ceil(0.01 * len(score))))
    order = np.lexsort((entity_ids.astype('int64'), -score))[:top_n]
    return {
        'average_precision': float(average_precision_score(y_true, score)),
        'roc_auc': float(roc_auc_score(y_true, score)),
        'top_1_percent_n': int(top_n),
        'top_1_percent_positive': int(y_true[order].sum()),
    }
