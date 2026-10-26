# Technical Interview Practice / Trình bày dự án và phỏng vấn

Tôi dùng bộ câu hỏi này để **giải thích dự án bằng tiếng Việt và tiếng Anh**, mỗi ngôn ngữ khoảng 2–3 phút. Mục tiêu là hiểu và diễn giải được dữ liệu, thuật toán, lựa chọn kỹ thuật, kết quả và hướng cải tiến.

## 1. Credit Risk / Tín dụng

1. **EN:** At what timestamp is a feature available? **VI:** Đặc trưng này biết được tại thời điểm nào? Explain as-of joins and why `credit_history_length` cannot use today's date for an old decision.
2. **EN:** What does ROC-AUC 0.936 tell me, and what does it miss? **VI:** AUC 0,936 phản ánh điều gì và còn thiếu điều gì? Thảo luận leakage, calibration, drift, định nghĩa nhãn và chính sách nghiệp vụ.
3. **EN:** Show how train-only preprocessing works. **VI:** Minh họa `fit` trên train và `transform` trên test; identify the separate imputation risk in the archived v3.1 source.
4. **EN:** Define default or adverse event and observation window precisely. **VI:** Phân biệt overdue, charged-off, default và thời điểm đo.
5. **EN:** How would I deploy and roll back this model? **VI:** Hãy thiết kế API, versioned artifacts, monitoring và rollback.

## 1A. Graph-Assisted Shared Risk Context — KLTN

1. **EN:** Why use Average Precision as the primary metric for DGraphFin? **VI:** Vì sao AP phù hợp dữ liệu lệch lớp hơn accuracy, và khác gì ROC-AUC?
2. **EN:** Why did graph features improve AP while reducing Top-1% true positives from 62 to 55? **VI:** Phân tích rank distribution, threshold, tied scores và review capacity.
3. Explain `A @ x` on a directed graph: outgoing versus incoming neighbors, adjacency convention, possible information leakage and a fair ablation.
4. **EN:** Why normalize LendingClub and DGraphFin outputs into separate contexts instead of combining their scores? **VI:** Phân biệt model score, đối tượng thực thể, dữ liệu và chính sách định tuyến.
5. Reproduce the 13 controlled routing scenarios, the 100 repeated hashes and the field-preservation checks; identify what each verifies.

## 2. SNJ Hybrid RAG

1. **EN:** Why not just use a large language model? **VI:** Vì sao phải retrieval/filtering thay vì hỏi LLM trực tiếp?
2. Compare dense retrieval, TF-IDF/BM25 and metadata-filter/rule scoring on “ruby stones for earrings” versus “ruby earrings.”
3. **EN:** Why is 100% on curated queries insufficient? **VI:** Tại sao 100% trên vài truy vấn chọn không chứng minh tổng quát? Design blind held-out evaluation and negative tests.
4. Discuss hallucination, grounding, no-match, price/stock freshness, latency and cost.
5. Draw a private beta architecture: WooCommerce read-only catalog → retrieval service → evaluator → assistant UI; separate real checkout authorization.

## 2A. Intelligent Commerce Chatbot / Context-Aware Sales Decision Intelligence

1. Compare the earlier **SNJ Hybrid RAG** coursework with the new multi-turn commerce assistant: what decision and system states were added?
2. **EN:** How does the assistant distinguish loose ruby stones from finished ruby jewelry and enforce budget/size constraints? **VI:** Thiết kế ontology, hard filters, ranking và lời giải thích.
3. Design a memory and reference-resolution test for “sản phẩm thứ hai,” after the user changes budget mid-conversation.
4. Explain how text, optional image attributes, retrieval, catalog truth, LLM responses and user-confirmed tool calls should interact.
5. Define held-out evaluation for category correctness, Recall@K, violated constraints, no-match handling, p95 latency and per-turn cost before beta expansion.

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

1. Why BM25 and Cross-Encoder? Which stage dominates latency and how would I measure it?
2. Explain RGB vs HSV, Canny/contours, OCR, and failure cases under low light or occlusion.
3. What must happen if the retrieved legal provision is outdated, ambiguous or absent?
4. Design a deployment record linking corpus version, image digest, runtime revision and logs; distinguish a proposed deployment from a verified one.
5. Explain Precision@1 vs Recall@K and how to generate a difficult held-out query set.

## 5. PAR / Human Decision Support

1. Show async state transitions, reset behavior, stale-response handling and upload cancellation.
2. Explain what the 40/40 PAR and baseline exercise measures, and design a separate user study for decision quality.
3. What data leave the browser during image upload? Who decides, who stores evidence, and what user disclosures are needed?
4. Discuss accessibility, mobile UI, auditability, fail-safe error states and incidents.
5. Draw a boundary between public user experience and proprietary core/service implementation.

## 6. Wine Quality / Classical ML

1. Explain class label >=6, imbalance and whether accuracy is meaningful.
2. Why use Logistic Regression baseline before LightGBM/XGBoost?
3. Explain feature scaling for linear models vs trees, hyperparameters, overfitting and regularization.
4. Which preprocessing belongs inside cross-validation? How would I avoid validation leakage?
5. Propose ablation, test-set freeze and experiment-tracking table.

## 7. Commercial / Kinh doanh

1. **Vendor dispute:** distinguish authorization, refund promise, settlement and business learning — which document supports which assertion?
2. **B2B Philippines:** why did an interested buyer not convert? Discuss landed cost, competitor pricing, margins, MOQ and what I would change.
3. **Ads:** distinguish billed amount from actual spend, revenue, attributable conversions, incrementality and ROAS/ACOS.
4. **eBay:** compare marketplace purchase versus off-platform direct sourcing, payment protection and authenticity risk.
5. **Portfolio ownership:** describe decisions I made personally versus actions by teams, suppliers or platforms.

## 8. MLOps / AWS & GCP deployment exercise

I use **one** project for this exercise: sanitized SNJ read-only retrieval or a UCI Wine demo.

- Containerize an API with pinned dependencies and a deterministic smoke test.
- Test locally first: malformed input, unknown categories, timeout, empty result and model version mismatch.
- Deploy behind authentication with least-privilege service account, spending limits, request logs, health/readiness checks and no secrets in Git.
- Record model/data version, latency p50/p95, RAM, cold-start behavior, error rate and per-request cost.
- Produce a runbook: deploy → verify → monitor → rollback → delete nonessential infrastructure.

**Mục tiêu thực hành:** hoàn thành một bản triển khai có thể trình diễn, kèm log, chi phí, kết quả kiểm thử và hướng rollback.

## Interview answer template / Khung trả lời

1. **Problem / Bài toán:** What decision was uncertain?
2. **Contract / I/O:** What data enter, what exact output leaves?
3. **Constraints / Ràng buộc:** What cannot be violated?
4. **Baseline / Đối chứng:** What simple method was tried?
5. **Engineering / Triển khai:** Why that architecture or parameter choice?
6. **Evidence / Kết quả:** Đã đo như thế nào? Làm sao chạy lại?
7. **Lessons / Bài học:** Trường hợp nào làm mô hình hoặc quy trình sai, và tôi sẽ cải tiến ra sao?
8. **Next step / Bước tiếp:** What single test would reduce uncertainty most?

_Practice routine: one project per week; one live code reading, one failure demonstration, one bilingual mock interview, one short screen recording._


## Questions grounded in the latest runs / Câu hỏi từ lần chạy mới

1. **Wine:** vì sao XGBoost nhỉnh hơn trên test mà vẫn giữ LightGBM đã chọn bằng CV? Giải thích 5.318 nhóm feature, 0 nhóm giao nhau, và regression RMSE 0,707821.
2. **RegimeLens:** vì sao macro F1 ~0,944 chưa chứng minh hiểu trạng thái kinh tế hoặc sinh lời? So sánh với persistence ~0,931; phân biệt filtering và smoothing/Viterbi, 3-state source với 5-state report.
3. **Traffic-Law QA:** vì sao 530 câu có ảnh nhưng baseline text-only thấp? Xử lý 40 relevance keys không có trong corpus và tránh chia các câu dùng chung ảnh sang hai tập.
4. **SNJ:** xử lý 5 product_id trùng thế nào trước khi lookup giá/tồn kho? Giải thích vì sao missing price không đạt budget, 8ly khác 8ly5, và lexical smoke PASS chưa là dense benchmark.
5. **PAR / IoT / Chatbot:** chỉ rõ artifact nào chứng minh UI deployment lịch sử, phần nào chỉ có báo cáo nhóm, phần nào mới là thiết kế.

[Open the project index and evidence](projects/README.md).
