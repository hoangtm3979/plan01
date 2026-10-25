# Wine Quality Classification / Phân loại chất lượng rượu vang

**Evidence:** UIT Machine Learning group report on Drive, `Báo Cáo WINE_QUALITY.docx`. Executable notebook and experiment log still need to be matched to the report.

## English

**Context:** Structured chemical measurements can be used to explore interpretable versus nonlinear supervised-learning methods.

**Problem:** Convert the UCI Wine Quality score to a binary label (quality >= 6 versus <= 5) and compare classification models.

**Input:** UCI red and white wine datasets; approximately 6,497 records combined and 11 physicochemical features per sample (as reported).

**Output:** binary prediction, confusion matrices, Accuracy/Precision/Recall/F1/ROC-AUC and feature importance visualizations.

**Approach:** exploratory data analysis (missingness, class distribution, feature correlation/outliers), scaling for appropriate models, train/test comparisons, Logistic Regression and Decision Tree baselines versus LightGBM/XGBoost.

**Report-stated observations:** boosted tree models are reported as better performing than simple baselines in tested settings; the report names LightGBM at a 0.2 test split as a strong combined-dataset configuration. Exact scores are not quoted because they have not been independently recovered and rerun from machine-readable outputs.

**Constraints:** class imbalance, duplicate observations, metric selection, threshold effects and leakage caused by preprocessing before splitting. The original report's model-selection method needs testing on held-out data.

**Next:** recover notebook, pin UCI dataset version/license, create train-only preprocessing pipeline, compare fixed folds/metrics, run simple hyperparameter tuning with a separate validation set and record seeds.

**Team attribution:** this is group coursework; precise individual responsibilities should be documented before interviewing.

## Tiếng Việt

- **Bối cảnh:** phân tích dữ liệu hóa lý của rượu vang để so sánh các thuật toán phân loại.
- **Bài toán:** chuyển nhãn quality thành hai lớp: chất lượng cao (>= 6), thấp (<= 5).
- **Input:** bộ UCI Wine Quality đỏ/trắng; báo cáo dùng khoảng 6.497 mẫu và 11 biến.
- **Output:** nhãn dự đoán, confusion matrix, F1/ROC-AUC và độ quan trọng đặc trưng.
- **Phương pháp:** EDA, chuẩn hóa, nhiều tỉ lệ train/test; Logistic Regression, Decision Tree, LightGBM, XGBoost.
- **Kết quả:** báo cáo nêu LightGBM là cấu hình tốt trong thử nghiệm. Chưa khẳng định một trị số cụ thể vì notebook/log chưa được chạy lại trong vòng rà soát này.
- **Ràng buộc:** tránh leakage khi scale, lựa chọn ngưỡng, kiểm soát class imbalance và tập test độc lập.
- **Bước tiếp:** tái chạy notebook, đưa kết quả ra bảng CSV, định nghĩa baseline và quy trình tối ưu siêu tham số có thể tái lập.

**Interview focus / Phỏng vấn:** cross-validation, StandardScaler placement, ROC-AUC vs F1, tree ensembles, bias/variance and ablations.
