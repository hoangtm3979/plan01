# Project Sources & Technical Notes / Nguồn tư liệu và ghi chú kỹ thuật

*Cập nhật 25/10/2026 · Updated 25 October 2026*

Tôi ghi lại nguồn tài liệu đã xem và phần sẽ tiếp tục thực hành để khi cần có thể **giải thích cách làm, tái lập thí nghiệm và phát triển dự án**. Trang giới thiệu chính nằm tại [README](README.md); đây là ghi chú chuyên sâu.

| Dự án / Case | Nguồn tôi đã đối chiếu / Materials | Điều đã thể hiện / What I can discuss | Hướng tiếp tục / Next technical work |
| --- | --- | --- | --- |
| **Credit Risk** | [Personal Colab notebook](https://github.com/hoangtm3979/credit) có mã và kết quả lưu | 2,03 triệu train, ~0,665 triệu holdout, Logistic/LightGBM và ROC-AUC | Kiểm tra dữ liệu theo thời điểm, `fit` preprocessing trên train, tái chạy benchmark |
| **Credit AI Thinking Starter** | [Personal study repo](https://github.com/hoangtm3979/danhgiatindungcanhan), tài liệu khung ML | Cách phân rã bài toán ML và xây lộ trình triển khai | Hoàn thiện các mô-đun huấn luyện/suy luận từng được lên kế hoạch |
| **Graph-Assisted Shared Risk Context — KLTN** | Báo cáo KLTN cá nhân bản cập nhật 23/10/2026, phụ lục kiểm thử và tài liệu rà soát hướng cạnh | RQ1: DGraphFin, node-only so với node+graph LightGBM (AP 0,025033 → 0,032505; Top-1% 62 → 55). RQ2: chuẩn hóa và định tuyến ngữ cảnh, 13 kịch bản kiểm soát | Ablation hướng cạnh, kiểm tra tied scores tại Top-K, đánh giá theo các review capacity khác nhau |
| **SNJ Hybrid RAG** | Báo cáo học phần UIT | 376 sản phẩm/22 cột; intent, lọc danh mục, hybrid retrieval | Bổ sung tập query độc lập, đối chứng WooCommerce và test API read-only |
| **Intelligent Commerce Chatbot** | [Hybrid RAG coursework](projects/snj-hybrid-rag.md), bối cảnh triển khai SNJ và yêu cầu beta nội bộ đã xác định | Đặc tả bài toán tư vấn nhiều lượt, input/output, kiến trúc retrieval + rules + memory + tool orchestration | Chạy bộ tình huống đa lượt, xác nhận catalog, test WooCommerce read-only, đo chất lượng và latency |
| **RegimeLens** | Báo cáo nhóm Big Data và notebook lịch sử `BIGDATA_mode_test_.ipynb` | Thiết kế HMM/XGBoost, số đo trong báo cáo và bài học về look-ahead | Xác định phiên bản code tương ứng, refit HMM theo thời gian, đánh giá chi phí giao dịch |
| **Traffic-Law QA** | Hai báo cáo môn học UIT | Kiến trúc truy hồi văn bản + phân tích ảnh biển báo | Đối chiếu notebook, bộ luật theo phiên bản, đánh giá query và API |
| **PAR** | [Personal demo repository](https://github.com/hoangtm3979/aegi-par-demo) | Luồng giao diện, quản lý trạng thái bất đồng bộ, kiểm thử kịch bản | Kiểm thử luồng người dùng, triển khai và đánh giá UX |
| **Wine Quality** | Báo cáo nhóm Machine Learning UIT | EDA và so sánh mô hình phân loại UCI | Chạy lại với cross-validation và bảng metrics cố định |
| **Face Attendance (IoT/CV)** | Báo cáo cuối kỳ nhóm năm người, ghi tên Hoàng và vai trò xử lý ảnh | MVP PC/LAN, camera, YOLO/ArcFace/FastAPI/SQLite, ghi nhận điểm danh | Test đa khuôn mặt, FAR/FRR, spoofing, latency và thiết bị edge |
| **Business cases** | Kinh nghiệm và tài liệu giao dịch người dùng lưu riêng | Tranh chấp phí SaaS, B2B Philippines, hoạt động Amazon/eBay/Ads | Gom dữ liệu định lượng, che thông tin đối tác, phân tích KPI/chi phí |

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

## Những điểm tôi đã điều chỉnh sau khi đối chiếu nguồn

- **REVISED — KLTN (23/10/2026):** Đánh giá RQ1 phải phản ánh cả hai mặt: AP và ROC-AUC tăng khi bổ sung graph features, nhưng kết quả Top-1% trong lần chạy seed 42 giảm từ 62 xuống 55 trường hợp dương tính. Phân tích sau thí nghiệm xác định đặc trưng láng giềng đang dùng hướng cạnh đi ra và có nhiều tied scores cần kiểm tra thêm.
- **ONGOING — Intelligent Commerce Chatbot (25/10/2026):** Đây là nhánh phát triển tiếp từ SNJ Hybrid RAG, mới có đặc tả phạm vi và kế hoạch beta nội bộ được đối chiếu ở giai đoạn này. Thông số riêng của chatbot đa lượt sẽ cập nhật sau các lượt chạy thực tế.

- **REVISED — IoT/CV (25/10/2026):** Có hai báo cáo nhận diện khuôn mặt thuộc hai nhóm khác nhau. Báo cáo khớp với tôi là **đồ án nhóm Nam Sài Gòn** về YOLO/ArcFace, FastAPI, SQLite, MVP chạy PC/LAN. Báo cáo MobileNetV2/Pi 5 của một nhóm khác không được dùng để mô tả kết quả của tôi.
- **REVISED — RegimeLens (25/10/2026):** Mã Colab lịch sử có `bfill` và bước scaler/HMM được huấn luyện trên cả chuỗi trước phép chia thời gian; phương án đó cần sửa để đánh giá walk-forward. Các chỉ số F1/Sharpe nêu tại [case](projects/regimelens.md) thuộc báo cáo môn học, còn mối liên hệ với phiên bản notebook vẫn đang đối chiếu.
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

