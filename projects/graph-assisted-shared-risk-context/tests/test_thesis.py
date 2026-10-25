import csv
import hashlib
import json
from pathlib import Path
import unittest
import numpy as np
from shared_risk_context import context
from shared_risk_context.evaluation import score_metrics
from shared_risk_context.examples import example_records, graph_fixture, original_cases, run_controlled_checks
from shared_risk_context.graph_features import build_graph_features

ROOT = Path(__file__).resolve().parents[1]


class GraphFeatureTests(unittest.TestCase):
    def test_directed_neighbors_match_hand_calculation(self):
        x, edges, types = graph_fixture()
        actual = build_graph_features(x, edges, types)
        np.testing.assert_allclose(actual[:, 4:], [[4, 8], [1, 2], [7, 14], [5, 10], [0, 0]])
        np.testing.assert_allclose(actual[:, 0], np.log1p([1, 1, 2, 1, 0]))
        np.testing.assert_allclose(actual[:, 1], np.log1p([2, 1, 1, 1, 0]))
        np.testing.assert_allclose(actual[:, 2], [0.5, 1, 1, 1, 0])
        np.testing.assert_allclose(actual[:, 3], np.log1p([2, 1, 1, 1, 0]))

    def test_reversing_edges_changes_the_neighborhood(self):
        x, edges, types = graph_fixture()
        outgoing = build_graph_features(x, edges, types)
        incoming = build_graph_features(x, edges[::-1], types)
        np.testing.assert_allclose(incoming[0, 4:], [3, 6])
        self.assertFalse(np.array_equal(outgoing[0, 4:], incoming[0, 4:]))

    def test_empty_graph_has_zero_graph_features(self):
        x = np.ones((3, 2), dtype='float32')
        actual = build_graph_features(x, np.empty((2, 0), dtype='int64'), np.array([], dtype='int64'))
        np.testing.assert_array_equal(actual, np.zeros((3, 6)))

    def test_top_budget_ties_use_numeric_id(self):
        metrics = score_metrics(np.array([1, 0, 0]), np.array([0.5, 0.5, 0.1]), np.array([20, 10, 30]))
        self.assertEqual(metrics['top_1_percent_n'], 1)
        self.assertEqual(metrics['top_1_percent_positive'], 0)


class ContextTests(unittest.TestCase):
    def test_contract_and_policy_match_original_hashes(self):
        contract = json.loads((ROOT/'evidence/historical/shared_risk_context_contract_v2_1.json').read_text())
        policy = json.loads((ROOT/'evidence/historical/routing_policy_v2_1.json').read_text())
        self.assertEqual(context.CONTRACT_SHA256, contract['contract_sha256'])
        self.assertEqual(context.ROUTING_POLICY_SHA256, policy['policy_sha256'])

    def test_original_13_expected_statuses_match_historical_table(self):
        with (ROOT/'evidence/historical/rq2_controlled_cases.csv').open() as stream:
            expected = {r['case_id']: r for r in csv.DictReader(stream)}
        cases = original_cases()
        self.assertEqual(len(cases), 13)
        for case in cases:
            with self.subTest(case=case['case_id']):
                actual = context.validate_context(case['context'], case['source_key'], case['reference_available'])
                self.assertEqual(actual['status'], expected[case['case_id']]['expected_status'])
                self.assertEqual(actual['route'], expected[case['case_id']]['expected_route'])
                self.assertEqual(actual['reasons'], json.loads(expected[case['case_id']]['reasons']))

    def test_adapter_preserves_all_declared_source_fields(self):
        for key, record in example_records().items():
            adapted = context.adapt_record(record, key)
            for field in context.SOURCE_REQUIRED:
                self.assertEqual(adapted[field], record[field])

    def test_nonfinite_scores_rejected(self):
        record = example_records()['credit']
        for value in [float('nan'), float('inf'), -0.1]:
            adapted = context.adapt_record({**record, 'score_value': value}, 'credit')
            self.assertEqual(context.validate_context(adapted, 'credit')['status'], 'REJECTED')

    def test_repeated_and_reordered_contexts_do_not_create_linkage_or_joint_score(self):
        results = run_controlled_checks()
        self.assertEqual(results['controlled_cases_passed'], 13)
        self.assertEqual(results['determinism_repetitions'], 100)
        self.assertEqual(results['unique_output_hashes'], 1)
        self.assertTrue(results['order_invariant'])
        self.assertEqual(results['entity_linkage_status'], 'synthetic_not_observed')
        self.assertIsNone(results['joint_score'])


class EvidenceTests(unittest.TestCase):
    def test_published_aggregates_match_original_bytes(self):
        hashes = json.loads((ROOT/'evidence/historical/source_hashes.json').read_text())
        for name, expected in hashes['published_aggregate_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/'evidence/historical'/name).read_bytes()).hexdigest(), expected, name)


if __name__ == '__main__':
    unittest.main()
