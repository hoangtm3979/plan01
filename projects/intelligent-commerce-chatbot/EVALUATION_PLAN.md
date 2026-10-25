# Intelligent Commerce Chatbot — Evaluation Plan

**Status: NOT_RUN.** The [12 cases](evaluation_cases.json) define acceptance behavior for future implementation; they are not passed tests or user-study evidence.

Before beta evaluation, version the catalog, resolve duplicate product IDs in the predecessor source, define a session-state schema and label an independent query set. Keep product selection grounded in catalog data; missing price/stock/certificates remain unknown until verified.

| Area | Measurement | Required evidence |
| --- | --- | --- |
| Retrieval | Recall@K, MRR with product-level judgments | Frozen relevant product IDs per query |
| Constraints | Mandatory category/size/budget violation rate | Expected conditions and returned records |
| Conversation | Budget/category update and reference-resolution success | Full synthetic multi-turn transcripts |
| No-match | Correct abstention/clarification | Unanswerable and contradictory cases |
| Tools | Wrong-item/unauthorized-state-change rate | Read-only and confirmed-action logs |
| Runtime | p50/p95 latency, per-turn cost | Versioned environment and measured runs |

Use fictional shopper information for software tests. Keep catalog freshness and transaction-side confirmation explicit. Image retrieval and checkout/tool actions require their own implemented artifacts before they can be marked tested.
