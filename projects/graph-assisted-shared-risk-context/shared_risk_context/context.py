"""Academic Shared Risk Context v2.1 adapter, validator and routing functions.

Extracted from the executed thesis RQ2 notebook. These functions check the
declared academic contract. They are not a general-purpose evidence verifier.
Default registry hashes identify synthetic examples; real replay replaces them
with the verified upstream prediction-file hashes.
"""
import hashlib
import json
import numpy as np

def canonical_hash(obj) -> str:
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'), default=str).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()

CONTEXT_VERSION = 'shared_risk_context_v2.1'
CREDIT_ADAPTER_VERSION = 'credit_adapter_v2.1'
FRAUD_ADAPTER_VERSION = 'fraud_graph_adapter_v2.1'
ROUTING_POLICY_VERSION = 'routing_policy_v2.1'

SOURCE_REGISTRY = {
    'credit': {
        
        'artifact_sha256': hashlib.sha256(b'demo-credit-source').hexdigest(),
        'entity_scope': 'lendingclub_loan_record',
        'risk_domain': 'credit',
        'score_semantics': 'lightgbm_default_class_score',
        'source_dataset': 'lendingclub_granting_models_v0.1',
        'model_versions': {'credit_lightgbm_v2.1'},
        'assessment_time_status': 'source_observed_month',
        'adapter_version': CREDIT_ADAPTER_VERSION,
        'route': 'CREDIT_REVIEW',
    },
    'fraud_node_only': {
        
        'artifact_sha256': hashlib.sha256(b'demo-node-source').hexdigest(),
        'entity_scope': 'dgraphfin_user_node',
        'risk_domain': 'fraud_graph',
        'score_semantics': 'dgraphfin_anomaly_class_score',
        'source_dataset': 'dgraphfin_original',
        'model_versions': {'dgraphfin_lightgbm_node_only_v2.1'},
        'assessment_time_status': 'not_available_in_source',
        'adapter_version': FRAUD_ADAPTER_VERSION,
        'route': 'FRAUD_GRAPH_REVIEW',
    },
    'fraud_node_plus_graph': {
        
        'artifact_sha256': hashlib.sha256(b'demo-graph-source').hexdigest(),
        'entity_scope': 'dgraphfin_user_node',
        'risk_domain': 'fraud_graph',
        'score_semantics': 'dgraphfin_anomaly_class_score',
        'source_dataset': 'dgraphfin_original',
        'model_versions': {'dgraphfin_lightgbm_node_plus_graph_v2.1'},
        'assessment_time_status': 'not_available_in_source',
        'adapter_version': FRAUD_ADAPTER_VERSION,
        'route': 'FRAUD_GRAPH_REVIEW',
    },
}

SOURCE_REQUIRED = {
    'source_record_reference', 'entity_scope', 'risk_domain', 'score_value',
    'score_semantics', 'model_version', 'source_dataset',
    'assessment_time', 'assessment_time_status'
}
CONTEXT_REQUIRED = SOURCE_REQUIRED | {
    'context_version', 'adapter_version', 'source_artifact_sha256',
    'trace_id', 'quality_flags'
}

CONTRACT = {
    'context_version': CONTEXT_VERSION,
    'score_range': [0.0, 1.0],
    'joint_score_allowed': False,
    'real_customer_linkage_claim_allowed': False,
    'routing_scope': 'offline_recommendation_only',
    'required_fields': sorted(CONTEXT_REQUIRED),
    'optional_fields': ['reason_signals', 'risk_band', 'risk_band_policy'],
}
CONTRACT_SHA256 = canonical_hash(CONTRACT)
ROUTING_POLICY = {
    'policy_version': ROUTING_POLICY_VERSION,
    'single_context_routes': {'credit': 'CREDIT_REVIEW', 'fraud_graph': 'FRAUD_GRAPH_REVIEW'},
    'held_route': 'DATA_REVIEW',
    'rejected_route': 'NONE',
    'controlled_multi_context_route': 'MULTI_CONTEXT_REVIEW',
    'decision_authority': 'NONE_RECOMMENDATION_ONLY',
}
ROUTING_POLICY_SHA256 = canonical_hash(ROUTING_POLICY)


def adapt_record(record: dict, source_key: str) -> dict:
    spec = SOURCE_REGISTRY[source_key]
    # Không tự điền giá trị source bắt buộc. Thiếu source field vẫn được mang sang None để validator fail-closed.
    source_ref = record.get('source_record_reference')
    trace_material = {
        'context_version': CONTEXT_VERSION,
        'adapter_version': spec['adapter_version'],
        'source_artifact_sha256': spec['artifact_sha256'],
        'source_record_reference': source_ref,
        'model_version': record.get('model_version'),
    }
    trace_id = 'CTX-' + canonical_hash(trace_material)[:24].upper()
    flags = ['RETROSPECTIVE_OFFLINE']
    if source_key == 'credit':
        flags += ['ISSUE_MONTH_GRANULARITY', 'NOT_BANK_PD']
    else:
        flags += ['DGRAPHFIN_ANOMALY_LABEL', 'ASSESSMENT_TIME_NOT_AVAILABLE']

    return {
        'source_record_reference': None if source_ref is None else str(source_ref),
        'entity_scope': record.get('entity_scope'),
        'risk_domain': record.get('risk_domain'),
        'score_value': record.get('score_value'),
        'score_semantics': record.get('score_semantics'),
        'model_version': record.get('model_version'),
        'source_dataset': record.get('source_dataset'),
        'assessment_time': record.get('assessment_time'),
        'assessment_time_status': record.get('assessment_time_status'),
        'context_version': CONTEXT_VERSION,
        'adapter_version': spec['adapter_version'],
        'source_artifact_sha256': spec['artifact_sha256'],
        'trace_id': trace_id,
        'quality_flags': flags,
    }

def validate_context(context: dict, source_key: str, reference_available: bool = True) -> dict:
    spec = SOURCE_REGISTRY[source_key]
    missing = sorted(
        field for field in CONTEXT_REQUIRED
        if field not in context or (context[field] is None and field != 'assessment_time') or context[field] == ''
    )
    if missing:
        return {'status': 'REJECTED', 'route': 'NONE', 'reasons': [f'MISSING:{field}' for field in missing]}
    if not reference_available:
        return {'status': 'HELD', 'route': 'DATA_REVIEW', 'reasons': ['REFERENCE_UNAVAILABLE']}
    if 'joint_score' in context or 'joint_credit_fraud_score' in context:
        return {'status': 'REJECTED', 'route': 'NONE', 'reasons': ['UNAUTHORISED_JOINT_SCORE']}

    reasons = []
    try:
        score = float(context['score_value'])
    except (TypeError, ValueError):
        return {'status': 'REJECTED', 'route': 'NONE', 'reasons': ['SCORE_NOT_NUMERIC']}
    if not np.isfinite(score) or not 0.0 <= score <= 1.0:
        reasons.append('SCORE_OUT_OF_RANGE')
    if context['context_version'] != CONTEXT_VERSION:
        reasons.append('UNSUPPORTED_CONTEXT_VERSION')
    if context['entity_scope'] != spec['entity_scope']:
        reasons.append('ENTITY_SCOPE_MISMATCH')
    if context['risk_domain'] != spec['risk_domain']:
        reasons.append('DOMAIN_MISMATCH')
    if context['score_semantics'] != spec['score_semantics']:
        reasons.append('SCORE_SEMANTICS_MISMATCH')
    if context['model_version'] not in spec['model_versions']:
        reasons.append('MODEL_VERSION_UNREGISTERED')
    if context['source_dataset'] != spec['source_dataset']:
        reasons.append('SOURCE_DATASET_MISMATCH')
    if context['source_artifact_sha256'] != spec['artifact_sha256']:
        reasons.append('PROVENANCE_HASH_MISMATCH')
    if context['adapter_version'] != spec['adapter_version']:
        reasons.append('ADAPTER_VERSION_MISMATCH')
    if context['assessment_time_status'] != spec['assessment_time_status']:
        reasons.append('ASSESSMENT_TIME_STATUS_MISMATCH')
    if source_key == 'credit' and (context['assessment_time'] is None or context['assessment_time'] == ''):
        reasons.append('ASSESSMENT_TIME_REQUIRED')
    if source_key != 'credit' and context['assessment_time_status'] == 'not_available_in_source' and context['assessment_time'] not in [None, '']:
        reasons.append('ASSESSMENT_TIME_UNDECLARED_VALUE')

    if reasons:
        return {'status': 'REJECTED', 'route': 'NONE', 'reasons': reasons}
    return {'status': 'ACCEPTED', 'route': spec['route'], 'reasons': []}

def canonical_output(context: dict, validation: dict) -> dict:
    return {
        'trace_id': context['trace_id'],
        'status': validation['status'],
        'route': validation['route'],
        'reasons': sorted(validation['reasons']),
        'context_sha256': canonical_hash(context),
        'context_version': context['context_version'],
        'adapter_version': context['adapter_version'],
        'source_artifact_sha256': context['source_artifact_sha256'],
        'contract_sha256': CONTRACT_SHA256,
        'routing_policy_version': ROUTING_POLICY_VERSION,
        'routing_policy_sha256': ROUTING_POLICY_SHA256,
    }

def route_controlled_multi_context(context_specs):
    outputs = []
    for context, source_key in context_specs:
        val = validate_context(context, source_key)
        outputs.append(canonical_output(context, val))
    if any(o['status'] == 'REJECTED' for o in outputs):
        route = 'DATA_REVIEW'
    elif any(o['status'] == 'HELD' for o in outputs):
        route = 'DATA_REVIEW'
    else:
        domains = {c['risk_domain'] for c, _ in context_specs}
        route = 'MULTI_CONTEXT_REVIEW' if {'credit', 'fraud_graph'}.issubset(domains) else outputs[0]['route']
    result = {
        'case_reference_type': 'controlled_synthetic_scenario',
        'entity_linkage_status': 'synthetic_not_observed',
        'recommended_route': route,
        'input_trace_ids': sorted(o['trace_id'] for o in outputs),
        'joint_score': None,
        'routing_policy_version': ROUTING_POLICY_VERSION,
        'routing_policy_sha256': ROUTING_POLICY_SHA256,
    }
    result['output_sha256'] = canonical_hash(result)
    return result
