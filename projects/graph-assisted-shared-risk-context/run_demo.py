"""Run the small public graph/context examples; no data downloads or model APIs."""
from pathlib import Path
import argparse
import json
import numpy as np
from shared_risk_context.graph_features import build_graph_features
from shared_risk_context.examples import graph_fixture, run_controlled_checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('outputs/demo_results.json'))
    args = parser.parse_args()
    x, edges, types = graph_fixture()
    features = build_graph_features(x, edges, types)
    expected_mean = np.array([[4, 8], [1, 2], [7, 14], [5, 10], [0, 0]], dtype='float32')
    np.testing.assert_allclose(features[:, 4:], expected_mean)
    contexts = run_controlled_checks()
    assert contexts['controlled_cases_passed'] == contexts['controlled_case_count'] == 13
    assert contexts['unique_output_hashes'] == 1 and contexts['order_invariant']
    assert contexts['multi_context_route'] == 'MULTI_CONTEXT_REVIEW'
    assert contexts['joint_score'] is None
    results = {'scope': 'synthetic public examples; no dataset benchmark rerun',
               'graph_fixture': {'nodes': 5, 'edges_including_duplicate': 6,
                                 'feature_shape': list(features.shape), 'outgoing_mean_check': 'PASS'},
               'rq2': contexts, 'status': 'PASS'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f"PASS: graph directions, 13/13 routing cases, 100 repeats, one output hash. {args.output}")


if __name__ == '__main__':
    main()
