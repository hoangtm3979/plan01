# Wine Quality Classification / Phân loại chất lượng rượu vang

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

### Bối cảnh và bài toán
Trong **đồ án nhóm môn Machine Learning tại UIT**, nhóm dùng dữ liệu hóa lý của rượu vang để thực hành các bước **khám phá dữ liệu, xây mô hình đối chứng và so sánh thuật toán phân loại**.

- **Input:** bộ UCI Wine Quality gồm vang đỏ/trắng; báo cáo sử dụng khoảng **6.497 mẫu và 11 đặc trưng hóa lý**.
- **Output:** hai lớp chất lượng (`quality >= 6` và `quality <= 5`), nhãn dự đoán, confusion matrix, Accuracy/Precision/Recall/F1/ROC-AUC và biểu đồ đặc trưng.
- **Ràng buộc:** phân bố hai lớp, bản ghi trùng, chia tập train/test, chuẩn hóa chỉ dựa trên train và tránh chọn mô hình theo test.

### Phương pháp và kết quả
Nhóm thực hiện EDA để kiểm tra đặc trưng, tương quan, ngoại lệ và phân bố nhãn; sau đó so sánh **Logistic Regression, Decision Tree, LightGBM và XGBoost** ở nhiều cấu hình dữ liệu.

Báo cáo nhóm ghi nhận **LightGBM là một trong những cấu hình cho kết quả tốt** ở thiết lập kết hợp dữ liệu với tỷ lệ test 20%. Tôi muốn đối chiếu lại notebook để lập bảng metric và chạy một quy trình cross-validation cố định.

**Điều tôi học được:** model mạnh chỉ có ý nghĩa khi so sánh với baseline và kiểm soát cùng cách chia dữ liệu, tiền xử lý, metric và seed.

## English

### Problem and workflow
In a UIT Machine Learning team assignment, we explored **binary wine-quality classification** using the UCI red/white wine data.

- **Input:** approximately **6,497 samples** and **11 physicochemical features** in the report.
- **Output:** class label (`quality >= 6` vs `<= 5`), confusion matrix, classification metrics and feature analysis.
- **Approach:** EDA, data preparation and comparison of Logistic Regression, Decision Tree, LightGBM and XGBoost.
- **Constraints:** class balance, duplicates, validation design and preprocessing leakage.

The group report highlights **LightGBM** as a strong tested configuration. My next step is to reconnect the experimental notebook, build a fixed cross-validation pipeline and report a reproducible metric table for each baseline.

*UIT Machine Learning group coursework.*
