# Portfolio Review / Rà soát đồ án — 25/10/2026

Tôi đã chuẩn hóa 10 thư mục dự án và chín trang dẫn từ tên case cũ. Sáu notebook nguồn được đưa vào research với tên mô tả nội dung và ghi nguồn; tám bài archive được sửa tên/tiêu đề và phân nhóm, giữ nguyên mã/output.

| Kiểm tra mới / Current check | Kết quả / Result | Phạm vi / Scope |
| --- | --- | --- |
| Notebook thực thi | **4/4, 24/24 code cells** | Wine 8; SNJ 7; RegimeLens 5; Traffic-Law 4 |
| Notebook nguồn | **6/6 schema/syntax PASS** | 111 historical code cells, no new end-to-end run |
| Unit tests | **20/20 PASS** | SNJ 12, Traffic-Law 5, HMM filtering 3 |
| Python source | **12 files syntax PASS** | Modules, tests and notebook runners |
| Wine input guard | **PASS** | Official fingerprints accepted; modified file rejected |
| Internal Markdown links | **288 checked, 0 broken** | Includes old case entry pages and renamed archive references |
| Publication scan | **PASS** | No detected embedded credential patterns in new project artifacts |

Wine is a grouped-holdout reproduction on all 6,497 UCI rows. RegimeLens is a new frozen-HMM latent-state experiment on 6,374 days from the original CSV snapshot. Traffic-Law is a text-only development replay of 530 labeled train questions. SNJ checks use 12 fictional products and audit the original catalog; dense retrieval was not rerun.

**Phần còn mở / Open work:** Credit v3.1 needs its label/preprocessing protocol resolved and original-data retraining; SNJ has five duplicate product IDs and no fresh dense evaluation; Traffic needs corpus/label alignment and image/reranker/generator evaluation; IoT full source/camera/hardware remains unreviewed; the multi-turn commerce chatbot has no separate runnable artifact verified. PAR deployment acceptance is historical release evidence, not a new live endpoint check.

[Detailed JSON and fingerprints](validation/review-2026-10-25.json) · [Project index](README.md) · [File map](FILE_MAP.md)
