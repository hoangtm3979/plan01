# Project Index / Danh mục đồ án

**Trương Minh Hoàng · 25410008 · Updated 26 October 2026**

Tôi gom mỗi đồ án vào một thư mục có tên phản ánh nội dung. Bắt đầu bằng README để hiểu bài toán, phần việc, kết quả và cách chạy; sau đó theo liên kết sang mã, notebook hoặc bằng chứng. Những bài nhóm, bản nháp và các lỗi học được vẫn có nguồn riêng.

Each project has one descriptive folder and a bilingual entry page. The table distinguishes published artifacts from the scope actually checked. A case study, a syntax check, a synthetic smoke test and an original-data experiment establish different things.

| Dự án / Project | Điểm nổi bật / One-line highlight | Kiểm tra và phần còn mở / Validation scope |
| --- | --- | --- |
| [**Graph-Assisted Shared Risk Context — KLTN**](graph-assisted-shared-risk-context/README.md) | Nghiên cứu tác động của đặc trưng đồ thị lên phát hiện mẫu rủi ro hiếm và chuẩn hóa đầu ra tín dụng, bất thường để hỗ trợ rà soát. | 2 demo notebooks, 10 tests; 563.100 saved outputs replayed |
| [**Credit Risk Modeling**](credit-risk-modeling/README.md) | So sánh Logistic Regression và LightGBM để ước lượng rủi ro khoản vay, đồng thời rà soát dữ liệu có thể biết tại thời điểm xét vay. | 13 cells syntax PASS; original-data training NOT_RUN |
| [**SNJ Hybrid RAG Jewelry Advisor**](snj-hybrid-rag-jewelry-advisor/README.md) | Hiểu yêu cầu mua trang sức bằng tiếng Việt để lọc đúng loại hàng và tìm sản phẩm phù hợp trong catalog. | 1 notebook; 12 tests; original catalog needs ID review; dense NOT_RUN |
| [**Intelligent Commerce Chatbot**](intelligent-commerce-chatbot/README.md) | Thiết kế trợ lý bán hàng nhiều lượt, ghi nhớ nhu cầu và kiểm tra dữ liệu sản phẩm trước khi đưa ra gợi ý. | 12 proposed cases NOT_RUN; no separate runtime verified |
| [**RegimeLens — Market Regimes**](regimelens-market-regimes/README.md) | Khám phá trạng thái thị trường bằng HMM, rồi kiểm tra dự đoán ngày kế tiếp với đối chứng giữ nguyên trạng thái hôm nay. | 1 notebook on original CSVs; 3 tests; no backtest |
| [**Multimodal Traffic-Law QA**](traffic-law-multimodal-qa/README.md) | Khám phá cách tra cứu luật giao thông bằng tiếng Việt và hướng kết hợp ảnh biển báo, bắt đầu từ đối chứng truy hồi văn bản. | 1 notebook, 530 train questions; 5 tests; image/generation NOT_RUN |
| [**PAR Decision-Support UI**](par-decision-support/README.md) | Bản mẫu giao diện hướng dẫn người dùng phòng ngừa, xác minh hoặc khôi phục khi gặp tình huống rủi ro số. | Historical UI 1.1 acceptance; no fresh endpoint/effectiveness run |
| [**Wine Quality — Classification & Regression**](wine-quality-prediction/README.md) | Dự đoán chất lượng rượu vang từ chỉ số hóa lý, so sánh phân loại và hồi quy với cách chia dữ liệu kiểm soát mẫu trùng. | 1 notebook on 6.497 UCI rows; classification and regression |
| [**Multi-Camera Face Attendance**](multi-camera-face-attendance/README.md) | Đồ án nhóm về quy trình điểm danh từ camera đến nhận diện khuôn mặt, kiểm tra sự kiện và lưu lịch sử trong mạng LAN. | Correct team report; full ZIP/runtime not independently reviewed |
| [**Business Problem Solving**](business-problem-solving/README.md) | Các tình huống thực tế về tranh chấp phí SaaS, tìm khách hàng B2B và vận hành marketplace, tập trung vào quyết định và bài học kinh doanh. | Stated business outcomes; private source records retained |

## Chọn cách đọc / Suggested reading

- **Bắt đầu / Overview:** đọc README trong thư mục dự án.
- **Xem mã / Code:** `notebooks/` là bài thực hành mới có output; `research/` là nguồn lịch sử có ghi giới hạn.
- **Kiểm tra kết quả / Evidence:** `evidence/*.json`, `validation/latest.json`, `AUDIT.md` hoặc release records của repo nguồn.
- **Tìm tên cũ / Old filenames:** [File map](FILE_MAP.md) và [machine-readable map](file-map.json). Các đường dẫn case `.md` cũ vẫn là trang dẫn tới vị trí mới.
- **Bài nhỏ / Learning history:** [35 archive notebooks](../labs/archive/README.md) và [7 verified labs](../labs/README.md) được giữ riêng, không tính thành đồ án lớn.

Không phải mọi đồ án đã có một benchmark tái lập hoàn chỉnh. Credit cần lượt chạy dữ liệu gốc sau khi chốt lại protocol; SNJ cần xử lý ID và chạy dense; chatbot mới là design record; IoT cần đọc bộ mã và kiểm tra camera. Các phần này được ghi ở ngay trang dự án để người xem đánh giá đúng mức.

[**Portfolio home**](../README.md) · [**Evidence register**](../EVIDENCE_REGISTER.md) · [**Latest validation JSON**](validation/review-2026-10-25.json) · [**Interview practice**](../INTERVIEW_DRILL.md)
