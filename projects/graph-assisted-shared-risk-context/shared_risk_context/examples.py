"""Small public fixtures for demonstrating the original controlled scenarios."""
from copy import deepcopy
import numpy as np
from .context import (SOURCE_REGISTRY, canonical_hash, adapt_record, validate_context,
                      canonical_output, route_controlled_multi_context)

def example_records():
    records = {}
    for i, (key, spec) in enumerate(SOURCE_REGISTRY.items()):
        records[key] = {
            'source_record_reference': f'DEMO-{key.upper()}',
            'entity_scope': spec['entity_scope'], 'risk_domain': spec['risk_domain'],
            'score_value': [0.18, 0.41, 0.43][i],
            'score_semantics': spec['score_semantics'],
            'model_version': sorted(spec['model_versions'])[0],
            'source_dataset': spec['source_dataset'],
            'assessment_time': '2018-01' if key == 'credit' else None,
            'assessment_time_status': spec['assessment_time_status'],
        }
    return records

def original_cases(records=None):
    records = example_records() if records is None else records
    valid_credit = adapt_record(records['credit'], 'credit')
    valid_node = adapt_record(records['fraud_node_only'], 'fraud_node_only')
    valid_graph = adapt_record(records['fraud_node_plus_graph'], 'fraud_node_plus_graph')
    cases = []
    def add_case(case_id, context, source_key, expected_status, expected_route, reference_available=True):
        cases.append({
            'case_id': case_id, 'context': context, 'source_key': source_key,
            'reference_available': reference_available,
            'expected_status': expected_status, 'expected_route': expected_route,
        })

    add_case('C01_VALID_CREDIT', deepcopy(valid_credit), 'credit', 'ACCEPTED', 'CREDIT_REVIEW')
    add_case('C02_VALID_FRAUD_NODE', deepcopy(valid_node), 'fraud_node_only', 'ACCEPTED', 'FRAUD_GRAPH_REVIEW')
    add_case('C03_VALID_FRAUD_GRAPH', deepcopy(valid_graph), 'fraud_node_plus_graph', 'ACCEPTED', 'FRAUD_GRAPH_REVIEW')
    c = deepcopy(valid_credit); c.pop('score_semantics'); add_case('C04_MISSING_MANDATORY', c, 'credit', 'REJECTED', 'NONE')
    c = deepcopy(valid_graph); c['score_semantics'] = 'generic_fraud_probability'; add_case('C05_WRONG_SEMANTICS', c, 'fraud_node_plus_graph', 'REJECTED', 'NONE')
    c = deepcopy(valid_credit); c['model_version'] = 'unknown_model'; add_case('C06_UNSUPPORTED_MODEL', c, 'credit', 'REJECTED', 'NONE')
    c = deepcopy(valid_credit); c['score_value'] = 1.01; add_case('C07_SCORE_RANGE', c, 'credit', 'REJECTED', 'NONE')
    c = deepcopy(valid_node); c['source_artifact_sha256'] = '0'*64; add_case('C08_BAD_PROVENANCE', c, 'fraud_node_only', 'REJECTED', 'NONE')
    add_case('C09_REFERENCE_UNAVAILABLE', deepcopy(valid_credit), 'credit', 'HELD', 'DATA_REVIEW', reference_available=False)
    c = deepcopy(valid_credit); c['joint_credit_fraud_score'] = 0.5; add_case('C10_JOINT_SCORE_FORBIDDEN', c, 'credit', 'REJECTED', 'NONE')
    c = deepcopy(valid_credit); c['risk_domain'] = 'fraud_graph'; add_case('C11_DOMAIN_MISMATCH', c, 'credit', 'REJECTED', 'NONE')
    c = deepcopy(valid_graph); c['entity_scope'] = 'customer'; add_case('C12_ENTITY_SCOPE_ELEVATION', c, 'fraud_node_plus_graph', 'REJECTED', 'NONE')
    c = deepcopy(valid_graph); c['context_version'] = 'unsupported_v999'; add_case('C13_UNSUPPORTED_CONTEXT_VERSION', c, 'fraud_node_plus_graph', 'REJECTED', 'NONE')

    return cases

def run_controlled_checks(records=None):
    records = example_records() if records is None else records
    rows = []
    for case in original_cases(records):
        actual = validate_context(case['context'], case['source_key'], case['reference_available'])
        rows.append({'case_id': case['case_id'], 'expected_status': case['expected_status'],
                     'expected_route': case['expected_route'], **actual,
                     'pass': actual['status'] == case['expected_status'] and actual['route'] == case['expected_route']})
    contexts = [(adapt_record(records[k], k), k) for k in SOURCE_REGISTRY]
    multi_input = [contexts[0], contexts[2]]
    forward = route_controlled_multi_context(multi_input)
    reverse = route_controlled_multi_context(list(reversed(multi_input)))
    hashes = []
    for _ in range(100):
        batch = sorted([canonical_output(c, validate_context(c, k)) for c, k in contexts], key=lambda x: x['trace_id'])
        batch.append(route_controlled_multi_context(multi_input))
        hashes.append(canonical_hash(batch))
    return {'controlled_cases': rows, 'controlled_cases_passed': sum(r['pass'] for r in rows),
            'controlled_case_count': len(rows), 'determinism_repetitions': len(hashes),
            'unique_output_hashes': len(set(hashes)),
            'multi_context_route': forward['recommended_route'],
            'order_invariant': forward['output_sha256'] == reverse['output_sha256'],
            'entity_linkage_status': forward['entity_linkage_status'], 'joint_score': forward['joint_score']}

def graph_fixture():
    x = np.array([[1,2],[3,6],[5,10],[7,14],[9,18]], dtype='float32')
    edges = np.array([[0,0,0,1,2,3],[1,2,1,0,3,2]], dtype='int64')
    types = np.array([0,1,0,0,2,2], dtype='int64')
    return x, edges, types
