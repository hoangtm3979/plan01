# Colab Inventory & Next Experiments / Kiểm kê và hướng phát triển bài Colab

*Rà soát ngày 25/10/2026 · Review on 25 October 2026*

Tôi đã kiểm tra các notebook lưu trên hai tài khoản Drive cũ để hệ thống lại quá trình học. Danh mục gồm cả bài môn học, bản copy, bài nháp, thử nghiệm có lỗi và các hướng phát triển sau này.

## Kết quả kiểm kê / Inventory

| Hạng mục / Item | Số lượng / Count |
| --- | ---: |
| Mục tìm thấy trong hai thư mục / All folder entries | **94 + 19 = 113** |
| Mục có dạng notebook / Notebook-like entries | **103** |
| Notebook Colab chuẩn được đọc cấu trúc JSON / Native Colab structures inspected | **101/101** |
| Notebook lưu dưới MIME khác / Other notebook formats | **2** |
| Bản Colab có execution counters ở tất cả code cells / All cells historically executed | **52** |
| Bản Colab có một phần code cells từng chạy / Partially executed | **21** |
| Bản Colab chưa có execution counter / Without saved execution counters | **28** |
| Bản Colab có ít nhất một output lỗi lưu lại / With saved error output | **22** |

Những số đếm này giúp tôi **quản lý nguồn bài tập**, không phải số lượng đồ án độc lập. Các nhóm kết quả chạy và lỗi có thể giao nhau; bản copy được xem riêng khi cần.

## Cập nhật bảy bài đã chọn / Selected notebook update

**SUPERSEDED — 25/10/2026:** bảy bài mẫu đã chạy đầy đủ **7/7 notebook, 49/49 code cell**.
Hai bài MNIST đã huấn luyện/đánh giá trên đủ dữ liệu chính thức; bài e-commerce đã chạy
trên CSV UCI gốc. Xem [báo cáo và hướng dẫn tái lập](EXECUTION_REPORT.md).

Bảng 103 mục ở trên là kết quả kiểm kê nguồn trước đó. Lượt chạy mới này xác nhận bảy
notebook công khai; phần phân loại, gộp bản trùng và tái lập các bài còn lại vẫn tiếp tục.

## Phân nhóm bài tập / Learning topics

| Nhóm | Kết quả rà soát và hướng tiếp tục |
| --- | --- |
| **Python** | File, vòng lặp, input, cấu trúc dữ liệu. Làm lại ví dụ thiếu CSV thành bài chạy không phụ thuộc máy cá nhân |
| **Toán và ML nền tảng** | Vector, PCA, regression, K-Means, Spectral/GMM. So sánh thuật toán và trực quan hóa lỗi |
| **ML cổ điển** | Logistic, Decision Tree, ensemble, multiclass. Đóng gói preprocess và cross-validation |
| **Deep Learning** | TensorFlow/MNIST, FCN và ANN. Chạy lại với dependency và seed cố định |
| **Vietnamese NLP** | Tokenization, UIT-VSFC, VnCoreNLP, PhoBERT. Đánh giá trên tập chia đúng và dẫn nguồn tutorial |
| **Image segmentation** | U-Net và BUSI. Thử nghiệm Dice/IoU với dữ liệu được phép sử dụng và chia tập phù hợp |
| **Applied AI** | E-commerce expected value, SNJ RAG, credit risk và RegimeLens. Gắn mô hình với input/output nghiệp vụ |
| **AEGI R&D** | Phần nghiên cứu đang phát triển trong hệ thống riêng, được trình bày ở mức bài toán và kiến trúc |

Bảy notebook đã chọn nằm ở [AI Learning Labs](README.md). Những bài còn lại sẽ được bổ sung khi tôi hoàn thiện dữ liệu mẫu, môi trường chạy và phần giải thích.

## Một vài lỗi học được nhiều điều

- **CSV thiếu:** bài Linear Regression cũ phụ thuộc đường dẫn dữ liệu không còn sẵn. Hướng sửa là quản lý data provenance và ví dụ có thể tải/cung cấp hợp lệ.
- **Chạy cell sai thứ tự:** bài K-Means từng có `NameError`, nhắc tôi kiểm tra luồng khai báo biến và phụ thuộc.
- **Look-ahead trong chuỗi thời gian:** bản RegimeLens lịch sử `fit` HMM cả chuỗi và có `.bfill()`. Tôi sẽ thực hành cách đánh giá theo từng mốc thời gian.
- **Nội dung tutorial:** ghi rõ tài liệu tham khảo và điểm chỉnh sửa của mình khi chuyển thành bài học công khai.

## Các bước tôi sẽ thực hiện / Reproduction steps

1. Chọn bài và làm rõ đầu vào, đầu ra, nguồn dữ liệu.
2. Chốt môi trường, phiên bản thư viện, seed và cách chạy.
3. Chạy notebook từ đầu, lưu metric và ví dụ lỗi.
4. So sánh baseline và kiểm tra train/test split, đặc biệt với dữ liệu theo thời gian.
5. Viết phần giải thích song ngữ và chia sẻ dữ liệu/mã phù hợp.

[**Xem nhật ký học tập**](README.md) · [**Xem ghi chú dự án**](../EVIDENCE_REGISTER.md)

