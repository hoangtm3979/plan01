"""Verify saved thesis predictions and recompute metrics and context conformance.

Supply a local protocol_v2_1 directory. Input Parquet data are not distributed
with this public repository. This replays saved outputs, without model fitting.
"""
from pathlib import Path
import argparse
import hashlib
import json
import time
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score, brier_score_loss
from shared_risk_context import context
from shared_risk_context.evaluation import score_metrics
from shared_risk_context.examples import run_controlled_checks

ROOT = Path(__file__).resolve().parent
HASHES = json.loads((ROOT/'evidence/historical/source_hashes.json').read_text())


def read_verified(root, relative):
    path = root/relative
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != HASHES['files'][relative]:
        raise ValueError(f'Original evidence hash mismatch: {relative}')
    return path, actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifacts', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('outputs/saved_output_replay.json'))
    args = parser.parse_args()
    started = time.monotonic()
    sources = {
        'credit': 'credit/credit_predictions_for_context.parquet',
        'fraud_node_only': 'rq1/dgraphfin_node_only_predictions_for_context.parquet',
        'fraud_node_plus_graph': 'rq1/dgraphfin_node_plus_graph_predictions_for_context.parquet',
    }
    expected_bulk = json.loads((ROOT/'evidence/historical/rq2_bulk_conformance.json').read_text())
    records, metrics, bulk, verified = {}, {}, {}, {}
    for key, relative in sources.items():
        path, sha = read_verified(args.artifacts, relative)
        verified[relative] = sha
        context.SOURCE_REGISTRY[key]['artifact_sha256'] = sha
        frame = pd.read_parquet(path)
        records[key] = frame.iloc[0].to_dict()
        if not frame['source_record_reference'].is_unique:
            raise ValueError(f'Duplicate prediction identifiers: {key}')
        label_rel = ('credit/credit_evaluation_labels.parquet' if key == 'credit'
                     else 'rq1/dgraphfin_evaluation_labels.parquet')
        label_path, label_sha = read_verified(args.artifacts, label_rel)
        verified[label_rel] = label_sha
        labels = pd.read_parquet(label_path)
        if not labels['source_record_reference'].is_unique:
            raise ValueError('Duplicate label identifiers')
        joined = frame.merge(labels, on='source_record_reference', validate='one_to_one', how='left')
        if len(joined) != len(labels) or joined['y_true'].isna().any():
            raise ValueError('Prediction/label populations do not match')
        y, scores = joined['y_true'].to_numpy(), joined['score_value'].to_numpy()
        if not np.isin(y, [0, 1]).all() or not np.isfinite(scores).all():
            raise ValueError('Invalid evaluation values')
        if key == 'credit':
            actual = {'average_precision': float(average_precision_score(y, scores)),
                      'roc_auc': float(roc_auc_score(y, scores)),
                      'brier_score': float(brier_score_loss(y, scores))}
            expected = json.loads((ROOT/'evidence/historical/credit_metrics.json').read_text())
        else:
            actual = score_metrics(y, scores, joined['source_record_reference'].to_numpy(dtype='int64'))
            table = pd.read_csv(ROOT/'evidence/historical/rq1_primary_metrics.csv')
            variant = 'node_only' if key == 'fraud_node_only' else 'node_plus_graph'
            expected = table.set_index('variant').loc[variant].to_dict()
        for name, value in actual.items():
            if not np.isclose(value, expected[name], rtol=0, atol=1e-12):
                raise AssertionError(f'Metric mismatch: {key}.{name}: {value} != {expected[name]}')
        metrics[key] = {'rows': len(joined), 'positives': int(y.sum()), **actual}
        preservation = {field: 0 for field in context.SOURCE_REQUIRED}
        statuses = {'ACCEPTED': 0, 'HELD': 0, 'REJECTED': 0}
        for record in frame.to_dict('records'):
            adapted = context.adapt_record(record, key)
            statuses[context.validate_context(adapted, key)['status']] += 1
            for field in preservation:
                preservation[field] += int(adapted[field] == record[field])
        assert len(frame) == expected_bulk[key]['source_rows']
        assert statuses['ACCEPTED'] == len(frame) and all(v == len(frame) for v in preservation.values())
        bulk[key] = {'rows': len(frame), 'status_counts': statuses,
                     'preservation_rates': {k: v/len(frame) for k, v in sorted(preservation.items())}}
        print(f'{key}: {len(frame):,} predictions; metrics and context field preservation PASS', flush=True)
    bootstrap_path, bootstrap_sha = read_verified(args.artifacts, 'rq1/rq1_paired_bootstrap_10000.npy')
    verified['rq1/rq1_paired_bootstrap_10000.npy'] = bootstrap_sha
    deltas = np.load(bootstrap_path, allow_pickle=False)
    expected_ci = json.loads((ROOT/'evidence/historical/rq1_summary.json').read_text())['delta_ap_ci_95']
    np.testing.assert_allclose(np.percentile(deltas, [2.5, 97.5]), expected_ci, rtol=0, atol=1e-12)
    assert len(deltas) == 10000
    checks = run_controlled_checks(records)
    assert checks['controlled_cases_passed'] == 13 and checks['unique_output_hashes'] == 1
    assert checks['order_invariant'] and checks['joint_score'] is None
    result = {
        'status': 'PASS', 'scope': 'saved-output replay; no model retraining',
        'verified_input_sha256': verified, 'metrics': metrics, 'rq2_bulk_replay': bulk,
        'controlled_checks': checks,
        'bootstrap': {'scope': 'verified existing resamples and recomputed quantiles; not regenerated resamples',
                      'count': len(deltas), 'delta_ap_ci_95': np.percentile(deltas, [2.5, 97.5]).tolist()},
        'duration_seconds': round(time.monotonic()-started, 3),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Saved-output replay PASS: {args.output}')


if __name__ == '__main__':
    main()
