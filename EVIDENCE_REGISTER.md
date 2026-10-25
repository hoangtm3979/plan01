# Project Sources & Technical Notes / Nguồn tư liệu và ghi chú kỹ thuật

*Cập nhật 25/10/2026 · Updated 25 October 2026*

Tôi ghi lại nguồn tài liệu đã xem và phần sẽ tiếp tục thực hành để khi cần có thể **giải thích cách làm, tái lập thí nghiệm và phát triển dự án**. Trang giới thiệu chính nằm tại [README](README.md); đây là ghi chú chuyên sâu.

| Dự án / Case | Nguồn và mã hiện có / Sources | Đã kiểm tra / Checked scope | Còn mở / Open work |
| --- | --- | --- | --- |
| [KLTN](projects/graph-assisted-shared-risk-context/README.md) | 4 research notebooks, 2 demo notebooks, original frozen evidence | 10 tests; metrics replay and 563.100 output preservation | New full training, directed-edge/tie ablations |
| [Credit Risk](projects/credit-risk-modeling/README.md) | Public v3.1 source and source audit | 13 code cells syntax PASS; syntax defect fixed | Label horizon, train-only preprocessing, original-data retraining |
| [SNJ Hybrid RAG](projects/snj-hybrid-rag-jewelry-advisor/README.md) | Recovered source, parser/retrieval module, fictional sample catalog | 1 notebook; 12 tests; original catalog audited 376×22 / 371 IDs | Resolve 5 duplicate IDs; dense and held-out retrieval evaluation |
| [Commerce Chatbot](projects/intelligent-commerce-chatbot/README.md) | Multi-turn design and 12 structured proposed cases | DESIGN_RECORD; implementation not independently verified | Separate runnable artifact; all 12 cases NOT_RUN |
| [RegimeLens](projects/regimelens-market-regimes/README.md) | Recovered notebook/CSV snapshot; new chronological experiment | 6.374 days; train-frozen HMM, causal filtering; 3 tests | Survivorship/release-vintage audit, multiple windows, costs/backtest |
| [Traffic-Law QA](projects/traffic-law-multimodal-qa/README.md) | 105-cell exploration; corpus/train snapshot; TF-IDF/BM25 replay | 395 article keys, 530 text-only train queries; 5 tests | 40 source-reference mismatches, images, reranker and generation |
| [PAR](projects/par-decision-support/README.md) | Public personal code and release/acceptance records | Historical 25/09 UI 1.1 deployment acceptance reviewed | Fresh runtime/user-effectiveness study not performed |
| [Wine Quality](projects/wine-quality-prediction/README.md) | 2 recovered source notebooks; new grouped-holdout notebook | 6.497 rows; 4 classifiers, 2 regressors, train-only CV | External/batch validation beyond supplied columns |
| [Face Attendance](projects/multi-camera-face-attendance/README.md) | Correct Nam Sài Gòn report and report-grounded API/design | Hoàng role and PC/LAN scope verified from report | Full 555 MB source ZIP/runtime/hardware not reviewed |
| [Business cases](projects/business-problem-solving/README.md) | Narrative summaries; private source records retained | Results remain within stated case scope | Public quantitative KPI/settlement reconciliation not added |
| [Credit AI Thinking Starter](https://github.com/hoangtm3979/danhgiatindungcanhan) | Personal learning scaffold: problem decomposition, Streamlit/configuration and report outlines | Source README reviewed; planning record, not an additional model benchmark | Complete training/inference and sample-data pipeline in a separate implementation step |


## Notebook thực hành đã chạy lại / Re-executed learning notebooks

Ngày 25/10/2026: **7/7 notebook, 49/49 code cell PASS**. Các file công khai có output mới,
nguồn dữ liệu, dependency và lệnh chạy. [Báo cáo](labs/EXECUTION_REPORT.md) ·
[Kết quả JSON và fingerprint](labs/validation/execution-results.json).

- MNIST intro: test accuracy **97,14%**, 5 epochs; MNIST FCN: **97,72%**, 10 epochs.
  Cả hai dùng 54.000 train / 6.000 validation / 10.000 test. FCN save/reload giữ nguyên dự đoán.
- E-commerce: **12.330 phiên UCI**; Random Forest được chọn bằng validation log loss;
  test ROC-AUC **0,757777**, AP **0,355999**, Brier **0,115860**. Phần EV dùng giả định,
  chưa có kết luận về tác động khuyến mãi hoặc lợi nhuận thực tế.
- **SUPERSEDED:** trạng thái 4/7 đã chạy, 2 syntax-only và 1 chờ dữ liệu được thay bởi
  kết quả chạy đầy đủ trên. Phạm vi xác nhận là bảy bài, không phải toàn bộ kho 103 mục.

## KLTN — kiểm tra mã và bằng chứng công khai

**REVISED — 25/10/2026:** KLTN đã có [thư mục mã riêng](projects/graph-assisted-shared-risk-context/), hai notebook minh họa đã chạy, bốn notebook nghiên cứu, kiểm thử và công cụ replay. Đã đối chiếu 31 tệp với inventory của evidence lock, tính lại metrics từ dự đoán gốc và kiểm tra bảo toàn trường trên đủ 563.100 đầu ra RQ2. Kết quả AP/ROC-AUC/Top‑1% giữ nguyên; chưa huấn luyện lại toàn bộ mô hình. [Báo cáo kiểm tra](projects/graph-assisted-shared-risk-context/RESULTS.md).


## Rà soát các đồ án khác / Other-project review — 25/10/2026

**REVISED:** đã bổ sung sáu notebook nguồn có tên theo nội dung và bốn notebook mới có output. Wine là lượt tái chạy classification/regression có grouped holdout; RegimeLens là thí nghiệm ba trạng thái với HMM fit trên train; Traffic-Law QA là text-only development replay; SNJ là kiểm tra ràng buộc trên catalog giả lập và audit catalog riêng. Phạm vi bốn lượt chạy khác nhau, không cộng chúng thành bốn benchmark tương đương.

**REVISED — SNJ:** catalog 376×22 có 371 product_id khác nhau, 5 ID lặp cần làm rõ. 100%/MRR 1.00 chỉ là số cũ trên 9 query nội bộ; chưa có fresh dense rerun.

**REVISED — RegimeLens:** source riêng tìm lại dùng 3 trạng thái và dữ liệu 2000–2026, khác case 5-state/report. Kết quả mới RF macro F1 0.943915 so với persistence 0.930728 chỉ áp dụng cho frozen latent-state labels; không tái xác nhận Sharpe.

**REVISED — Traffic-Law QA:** 530 train questions đều tham chiếu ảnh. Replay mới không dùng ảnh; TF-IDF P@1 0.107547, BM25 0.060377, 40 câu có relevance key không có trong corpus. Không đối chiếu trực tiếp với 0.72/0.88/92% trong báo cáo.

**REVISED — PAR:** release records có nghiệm thu triển khai UI 1.1 ngày 25/09; README cũ ghi triển khai là việc tiếp theo. Đây là đối chiếu hồ sơ release, không phải lượt kiểm tra endpoint mới.

**STILL VALID:** chatbot đa lượt chưa có artifact thực thi riêng được xác nhận; IoT chưa kiểm thử toàn bộ ZIP/camera; dữ liệu riêng và mã nghiên cứu nội bộ không được đưa vào public.

## Những điểm tôi đã điều chỉnh sau khi đối chiếu nguồn

- **REVISED — KLTN (23/10/2026):** Đánh giá RQ1 phải phản ánh cả hai mặt: AP và ROC-AUC tăng khi bổ sung graph features, nhưng kết quả Top-1% trong lần chạy seed 42 giảm từ 62 xuống 55 trường hợp dương tính. Phân tích sau thí nghiệm xác định đặc trưng láng giềng đang dùng hướng cạnh đi ra và có nhiều tied scores cần kiểm tra thêm.
- **ONGOING — Intelligent Commerce Chatbot (25/10/2026):** Đây là nhánh phát triển tiếp từ SNJ Hybrid RAG, mới có đặc tả phạm vi và kế hoạch beta nội bộ được đối chiếu ở giai đoạn này. Thông số riêng của chatbot đa lượt sẽ cập nhật sau các lượt chạy thực tế.

- **REVISED — IoT/CV (25/10/2026):** Có hai báo cáo nhận diện khuôn mặt thuộc hai nhóm khác nhau. Báo cáo khớp với tôi là **đồ án nhóm Nam Sài Gòn** về YOLO/ArcFace, FastAPI, SQLite, MVP chạy PC/LAN. Báo cáo MobileNetV2/Pi 5 của một nhóm khác không được dùng để mô tả kết quả của tôi.
- **REVISED — RegimeLens (25/10/2026):** Mã Colab lịch sử có `bfill` và bước scaler/HMM được huấn luyện trên cả chuỗi trước phép chia thời gian; phương án đó cần sửa để đánh giá walk-forward. Các chỉ số F1/Sharpe nêu tại [case](projects/regimelens-market-regimes/README.md) thuộc báo cáo môn học, còn mối liên hệ với phiên bản notebook vẫn đang đối chiếu.
- **STILL VALID — dữ liệu và IP:** Mã nghiên cứu nội bộ, dữ liệu sinh trắc, hồ sơ giao dịch và thông tin đối tác được giữ trong nguồn phù hợp, không đưa nguyên bản vào portfolio công khai.

## Cách tôi phân biệt các mức kết quả

| Mức | Ví dụ |
| --- | --- |
| **Bài thực hành / Lab** | Mã môn học, tutorial được tham khảo, notebook thử nghiệm |
| **Kết quả lưu trong notebook** | Output của một lần chạy lịch sử |
| **Kết quả trong báo cáo nhóm** | Số liệu nhóm tổng hợp cho đồ án môn học |
| **Bài chạy tái lập** | Dữ liệu, môi trường và hướng dẫn để chạy lại từ đầu |
| **Bản demo** | Luồng phần mềm có thể dùng thử trong phạm vi xác định |
| **Vận hành thực tế** | Triển khai có người dùng, theo dõi và số đo hoạt động |

## Checklist khi nâng một bài lên bản demo

- [ ] Xác định nguồn dữ liệu, quyền sử dụng và phân công của nhóm.
- [ ] Ghi phiên bản data/model, seed, thư viện và cấu hình.
- [ ] Chạy lại từ môi trường sạch, lưu bảng đối chiếu baseline.
- [ ] Kiểm tra leakage, đúng thời điểm dữ liệu và nhóm tình huống lỗi.
- [ ] Tạo ví dụ dữ liệu mẫu dễ chia sẻ; tách tài khoản, khóa và thông tin riêng tư.
- [ ] Hoàn thiện hướng dẫn chạy và demo song ngữ.

[**Quay về danh mục dự án**](README.md)

