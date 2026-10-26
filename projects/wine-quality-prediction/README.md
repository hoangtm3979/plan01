# Wine Quality — Classification & Regression / Phân loại và hồi quy chất lượng rượu vang

> **Điểm nổi bật:** Dự đoán chất lượng rượu vang từ chỉ số hóa lý, so sánh phân loại và hồi quy với cách chia dữ liệu kiểm soát mẫu trùng.

[Tiếng Việt](#tiếng-việt) · [English](#english)

> **REPRODUCTION_PASS:** 8/8 code cells, đủ 6.497 mẫu UCI; có classification, regression và grouped holdout. [Kết quả](evidence/reproduction.json).

## Tiếng Việt

### Bối cảnh và bài toán
Trong **đồ án nhóm môn Machine Learning tại UIT**, nhóm dùng dữ liệu hóa lý của rượu vang để thực hành các bước **khám phá dữ liệu, xây mô hình đối chứng và so sánh thuật toán phân loại**.

- **Input:** bộ UCI Wine Quality gồm vang đỏ/trắng; báo cáo sử dụng khoảng **6.497 mẫu và 11 đặc trưng hóa lý**.
- **Output:** hai lớp chất lượng (`quality >= 6` và `quality <= 5`), nhãn dự đoán, confusion matrix, Accuracy/Precision/Recall/F1/ROC-AUC và biểu đồ đặc trưng.
- **Ràng buộc:** phân bố hai lớp, bản ghi trùng, chia tập train/test, chuẩn hóa chỉ dựa trên train và tránh chọn mô hình theo test.

### Phương pháp và kết quả
Nhóm thực hiện EDA để kiểm tra đặc trưng, tương quan, ngoại lệ và phân bố nhãn; sau đó so sánh **Logistic Regression, Decision Tree, LightGBM và XGBoost** ở nhiều cấu hình dữ liệu.

Báo cáo nhóm ghi nhận **LightGBM là một trong những cấu hình cho kết quả tốt** ở thiết lập kết hợp dữ liệu với tỷ lệ test 20%. Bản tái chạy có cách chia nhóm trùng và cross-validation cố định nằm ở phần dưới.

**Điều tôi học được:** model mạnh chỉ có ý nghĩa khi so sánh với baseline và kiểm soát cùng cách chia dữ liệu, tiền xử lý, metric và seed.

## English

> **In one sentence:** I predict wine quality from physicochemical measurements, comparing classification and regression with duplicate-aware evaluation.

### Problem and workflow
In a UIT Machine Learning team assignment, we explored **binary wine-quality classification** using the UCI red/white wine data.

- **Input:** approximately **6,497 samples** and **11 physicochemical features** in the report.
- **Output:** class label (`quality >= 6` vs `<= 5`), confusion matrix, classification metrics and feature analysis.
- **Approach:** EDA, data preparation and comparison of Logistic Regression, Decision Tree, LightGBM and XGBoost.
- **Constraints:** class balance, duplicates, validation design and preprocessing leakage.

The group report highlights **LightGBM** as a strong tested configuration. The new reproduction below supplies the notebook, a fixed cross-validation protocol and a separate holdout table.

*UIT Machine Learning group coursework.*


**Nhóm môn học / Coursework team:** Lê Văn Quang, Phạm Vũ Hải, Trương Minh Hoàng, Nguyễn Hoàng Liêm, Trương Thanh Phong.

## Tái chạy ngày 25/10/2026 / Fresh reproduction

[**Notebook có output và biểu đồ**](notebooks/01_wine_quality_classification_and_regression.ipynb) · [Mã pipeline](wine_quality.py) · [Kết quả JSON](evidence/reproduction.json) · [Nguồn dữ liệu](DATA.md)

6.497 dòng, 11 feature hóa lý, **5.318 nhóm vector đặc trưng khác nhau**. Holdout có 1.299 dòng, train có 5.198 dòng; số nhóm giao nhau bằng 0. Chuẩn hóa và điền thiếu nằm trong pipeline của mỗi fold. Không dùng cột `quality`, nhãn nhị phân hoặc loại vang trong X.

| Phân loại / Classification | Train CV macro F1 | Holdout ROC-AUC | Holdout macro F1 |
| --- | ---: | ---: | ---: |
| Logistic Regression | 0.711069 | 0.777860 | 0.697219 |
| Decision Tree | 0.704248 | 0.764311 | 0.697442 |
| **LightGBM — chọn bằng CV / CV-selected** | **0.750612** | **0.800852** | **0.718118** |
| XGBoost | 0.741751 | 0.801696 | 0.718821 |

XGBoost nhỉnh hơn trên holdout trong lần chạy này; lựa chọn vẫn là LightGBM vì đã khóa theo CV trước khi xem test.

| Hồi quy / Regression | Train CV RMSE | Holdout RMSE | Holdout MAE | Holdout R² |
| --- | ---: | ---: | ---: | ---: |
| Ridge | 0.732695 | 0.754475 | 0.587681 | 0.268010 |
| **Random Forest — chọn bằng CV** | **0.686276** | **0.707821** | **0.539239** | **0.355739** |

```bash
cd projects/wine-quality-prediction
python -m pip install -r requirements.txt
python run_notebooks.py --in-place
```

CSV UCI được tải và kiểm tra SHA-256 tự động, hoặc đặt `WINE_DATA_DIR` đến bản cache. [Hai notebook lịch sử](research/README.md) giữ lại quá trình học; bản pipeline nháp cũ thiếu `y_pred_reg`, còn bài nhóm từng chọn cấu hình theo test F1. Bản mới bổ sung huấn luyện/predict hồi quy và chỉ chọn model trong train CV.

**English:** all eight code cells ran successfully on the official red/white data. These scores use a new duplicate-aware protocol; they do not replace the historical group scores as though the splits were identical. Winery/batch independence cannot be established from the available columns.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
