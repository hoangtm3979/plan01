# Project Index / Danh mục đồ án

**Trương Minh Hoàng · 25410008 · Updated 25 October 2026**

Tôi gom mỗi đồ án vào một thư mục có tên phản ánh nội dung. Bắt đầu bằng README để hiểu bài toán, phần việc, kết quả và cách chạy; sau đó theo liên kết sang mã, notebook hoặc bằng chứng. Những bài nhóm, bản nháp và các lỗi học được vẫn có nguồn riêng.

Each project has one descriptive folder and a bilingual entry page. The table distinguishes published artifacts from the scope actually checked. A case study, a syntax check, a synthetic smoke test and an original-data experiment establish different things.

| Dự án / Project | Nội dung hiện có / Coverage | Kiểm tra và phần còn mở / Validation scope |
| --- | --- | --- |
| [**Graph-Assisted Shared Risk Context — KLTN**](graph-assisted-shared-risk-context/README.md) | Mã + research + replay | 2 demo notebooks, 10 tests; 563.100 saved outputs replayed |
| [**Credit Risk Modeling**](credit-risk-modeling/README.md) | Nguồn v3.1 + audit | 13 cells syntax PASS; original-data training NOT_RUN |
| [**SNJ Hybrid RAG Jewelry Advisor**](snj-hybrid-rag-jewelry-advisor/README.md) | Nguồn + module + ví dụ | 1 notebook; 12 tests; original catalog needs ID review; dense NOT_RUN |
| [**Intelligent Commerce Chatbot**](intelligent-commerce-chatbot/README.md) | Thiết kế + evaluation plan | 12 proposed cases NOT_RUN; no separate runtime verified |
| [**RegimeLens — Market Regimes**](regimelens-market-regimes/README.md) | Nguồn + chronological experiment | 1 notebook on original CSVs; 3 tests; no backtest |
| [**Multimodal Traffic-Law QA**](traffic-law-multimodal-qa/README.md) | Nguồn + text-only replay | 1 notebook, 530 train questions; 5 tests; image/generation NOT_RUN |
| [**PAR Decision-Support UI**](par-decision-support/README.md) | Case + code links + release records | Historical UI 1.1 acceptance; no fresh endpoint/effectiveness run |
| [**Wine Quality — Classification & Regression**](wine-quality-prediction/README.md) | Nguồn + full reproduction | 1 notebook on 6.497 UCI rows; classification and regression |
| [**Multi-Camera Face Attendance**](multi-camera-face-attendance/README.md) | Case + report-grounded design | Correct team report; full ZIP/runtime not independently reviewed |
| [**Business Problem Solving**](business-problem-solving/README.md) | Narrative case studies | Stated business outcomes; private source records retained |

## Chọn cách đọc / Suggested reading

- **Bắt đầu / Overview:** đọc README trong thư mục dự án.
- **Xem mã / Code:** `notebooks/` là bài thực hành mới có output; `research/` là nguồn lịch sử có ghi giới hạn.
- **Kiểm tra kết quả / Evidence:** `evidence/*.json`, `validation/latest.json`, `AUDIT.md` hoặc release records của repo nguồn.
- **Tìm tên cũ / Old filenames:** [File map](FILE_MAP.md) và [machine-readable map](file-map.json). Các đường dẫn case `.md` cũ vẫn là trang dẫn tới vị trí mới.
- **Bài nhỏ / Learning history:** [35 archive notebooks](../labs/archive/README.md) và [7 verified labs](../labs/README.md) được giữ riêng, không tính thành đồ án lớn.

Không phải mọi đồ án đã có một benchmark tái lập hoàn chỉnh. Credit cần lượt chạy dữ liệu gốc sau khi chốt lại protocol; SNJ cần xử lý ID và chạy dense; chatbot mới là design record; IoT cần đọc bộ mã và kiểm tra camera. Các phần này được ghi ở ngay trang dự án để người xem đánh giá đúng mức.

[**Portfolio home**](../README.md) · [**Evidence register**](../EVIDENCE_REGISTER.md) · [**Latest validation JSON**](validation/review-2026-10-25.json) · [**Interview practice**](../INTERVIEW_DRILL.md)
