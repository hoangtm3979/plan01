"""Directed graph features extracted from thesis RQ1 v2.1.

The feature formula is unchanged. Adjacency rows are sources, so A @ x
aggregates outgoing neighbors. Duplicate edges become binary adjacency.
"""
import numpy as np
import scipy.sparse as sp

def build_graph_features(x: np.ndarray, edge_index: np.ndarray, edge_type: np.ndarray) -> np.ndarray:
    n_nodes = x.shape[0]
    src, dst = edge_index
    adjacency = sp.csr_matrix((np.ones(len(src), dtype='float32'), (src, dst)), shape=(n_nodes, n_nodes))
    adjacency.sum_duplicates(); adjacency.data[:] = 1.0

    out_degree = np.asarray(adjacency.sum(axis=1)).ravel().astype('float32')
    in_degree = np.asarray(adjacency.sum(axis=0)).ravel().astype('float32')
    reciprocal_degree = np.asarray(adjacency.multiply(adjacency.T).getnnz(axis=1)).ravel().astype('float32')
    reciprocal_ratio = reciprocal_degree / np.maximum(out_degree, 1.0)

    type_base = int(edge_type.max()) + 1 if len(edge_type) else 1
    unique_source_type = np.unique(src.astype('int64') * type_base + edge_type.astype('int64'))
    unique_sources = unique_source_type // type_base
    relation_diversity = np.bincount(unique_sources, minlength=n_nodes).astype('float32')

    neighbor_sum = adjacency @ x
    neighbor_mean = neighbor_sum / np.maximum(out_degree[:, None], 1.0)
    result = np.column_stack([
        np.log1p(in_degree), np.log1p(out_degree), reciprocal_ratio,
        np.log1p(relation_diversity), neighbor_mean,
    ]).astype('float32')
    return result
