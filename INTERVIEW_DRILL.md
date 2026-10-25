# Project Defense & Interview Drill / Câu hỏi đào sâu phỏng vấn

Use this as a self-assessment sheet. Answer each prompt first in **Vietnamese (2–3 minutes)** and then in **English (2–3 minutes)**. Do not memorize conclusions you cannot derive from the source or reproduce.

## 1. Credit Risk / Tín dụng

1. **EN:** At what timestamp is a feature available? **VI:** Đặc trưng này biết được tại thời điểm nào? Explain as-of joins and why `credit_history_length` cannot use today's date for an old decision.
2. **EN:** Why can ROC-AUC be 0.936 yet the project fail in production? **VI:** Vì sao AUC cao vẫn chưa đủ? Discuss leakage, calibration, drift, label semantics, representativeness and human policies.
3. **EN:** Show how train-only preprocessing works. **VI:** Minh họa `fit` trên train và `transform` trên test; identify the separate imputation risk in current code.
4. **EN:** Define default or adverse event and observation window precisely. **VI:** Phân biệt overdue, charged-off, default và thời điểm đo.
5. **EN:** How would you deploy and roll back this model? **VI:** Hãy thiết kế API, versioned artifacts, monitoring và rollback.

## 2. SNJ Hybrid RAG

1. **EN:** Why not just use a large language model? **VI:** Vì sao phải retrieval/filtering thay vì hỏi LLM trực tiếp?
2. Compare dense retrieval, TF-IDF/BM25 and metadata-filter/rule scoring on “ruby stones for earrings” versus “ruby earrings.”
3. **EN:** Why is 100% on curated queries insufficient? **VI:** Tại sao 100% trên vài truy vấn chọn không chứng minh tổng quát? Design blind held-out evaluation and negative tests.
4. Discuss hallucination, grounding, no-match, price/stock freshness, latency and cost.
5. Draw a private beta architecture: WooCommerce read-only catalog → retrieval service → evaluator → assistant UI; separate real checkout authorization.

## 3. Big Data — RegimeLens

1. Explain HMM hidden states, emissions, label switching, rolling versus expanding windows.
2. Distinguish predicting regime `t+1` from retrospectively labeling regime `t` using future information.
3. Discuss timestamped macro data, publication lags, revision vintages, missing market days and point-in-time joins.
4. Why does a backtest without fees, slippage and multiple walk-forward periods overstate expected performance?
5. Defend macro F1 and Bear Recall for imbalanced multiclass classification.

## 3A. Critical Big Data code audit / Kiểm toán mã RegimeLens

1. **EN:** In the inspected notebook, where are `StandardScaler.fit_transform` and `GaussianHMM.fit` called relative to the chronological 70/15/15 split? **VI:** Vì sao huấn luyện HMM toàn chuỗi có thể làm nhãn ngày trước phụ thuộc dữ liệu ngày sau?
2. What happens if stock prices are filled using `.bfill()`? How can that affect historical features and model selection?
3. What exact version/commit produced the final report's Macro F1 and Sharpe numbers? What evidence would establish parity?

## 4. Multi-Camera Edge Face Attendance / Nhận diện khuôn mặt IoT

1. Explain why **multi-camera** support does not imply **multi-face** recognition; the reported main path selected the largest detected face.
2. Compare YOLO→ArcFace→cosine matching with Haar/LBP fallbacks. How is degraded quality surfaced to the operator?
3. Why is slide target **80–95%** not a measured accuracy? Design a consented test suite for FAR, FRR, spoofing, low light and unseen identities.
4. Demonstrate race-safe attendance deduplication, reconnect/backpressure handling, face-data retention, authorization and deletion.
5. Separate local LAN MVP evidence from Raspberry Pi 5 latency/FPS/quantization claims.

## 5. NLP / CV Traffic QA

1. Why BM25 and Cross-Encoder? Which stage dominates latency and how would you measure it?
2. Explain RGB vs HSV, Canny/contours, OCR, and failure cases under low light or occlusion.
3. What must happen if the retrieved legal provision is outdated, ambiguous or absent?
4. Verify the Cloud Run revision and metrics independently. How do source dates, Docker image digests and structured logs connect?
5. Explain Precision@1 vs Recall@K and how to generate a difficult held-out query set.

## 5. PAR / Human Decision Support

1. Show async state transitions, reset behavior, stale-response handling and upload cancellation.
2. Explain why a 40/40 match with baseline proves compatibility at most, not fraud reduction.
3. What data leave the browser during image upload? Who decides, who stores evidence, and what user disclosures are needed?
4. Discuss accessibility, mobile UI, auditability, fail-safe error states and incidents.
5. Draw a boundary between public user experience and proprietary core/service implementation.

## 6. Wine Quality / Classical ML

1. Explain class label >=6, imbalance and whether accuracy is meaningful.
2. Why use Logistic Regression baseline before LightGBM/XGBoost?
3. Explain feature scaling for linear models vs trees, hyperparameters, overfitting and regularization.
4. Which preprocessing belongs inside cross-validation? How would you avoid validation leakage?
5. Propose ablation, test-set freeze and experiment-tracking table.

## 7. Commercial / Kinh doanh

1. **Vendor dispute:** distinguish authorization, refund promise, settlement and business learning — which document supports which assertion?
2. **B2B Philippines:** why did an interested buyer not convert? Discuss landed cost, competitor pricing, margins, MOQ and what you would change.
3. **Ads:** distinguish billed amount from actual spend, revenue, attributable conversions, incrementality and ROAS/ACOS.
4. **eBay:** compare marketplace purchase versus off-platform direct sourcing, payment protection and authenticity risk.
5. **Portfolio ownership:** describe decisions you made personally versus actions by teams, suppliers or platforms.

## 8. MLOps / AWS & GCP deployment exercise

For **one** project (recommended: sanitized SNJ read-only retrieval or a UCI Wine demo):

- Containerize an API with pinned dependencies and a deterministic smoke test.
- Test locally first: malformed input, unknown categories, timeout, empty result and model version mismatch.
- Deploy behind authentication with least-privilege service account, spending limits, request logs, health/readiness checks and no secrets in Git.
- Record model/data version, latency p50/p95, RAM, cold-start behavior, error rate and per-request cost.
- Produce a runbook: deploy → verify → monitor → rollback → delete nonessential infrastructure.

**Do not claim AWS/GCP production experience solely because you have cloud accounts.** Demonstrate an actual controlled deployment and include its measured cost and logs.

## Interview answer template / Khung trả lời

1. **Problem / Bài toán:** What decision was uncertain?
2. **Contract / I/O:** What data enter, what exact output leaves?
3. **Constraints / Ràng buộc:** What cannot be violated?
4. **Baseline / Đối chứng:** What simple method was tried?
5. **Engineering / Triển khai:** Why that architecture or parameter choice?
6. **Evidence / Bằng chứng:** How was it measured and reproduced?
7. **Failure / Giới hạn:** Which counterexample breaks it?
8. **Next step / Bước tiếp:** What single test would reduce uncertainty most?

_Practice routine: one project per week; one live code reading, one failure demonstration, one bilingual mock interview, one short screen recording._
