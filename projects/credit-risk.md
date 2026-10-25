# Credit Risk Modeling / Mô hình hóa rủi ro tín dụng

**Evidence / Bằng chứng:** [Executed notebook + code](https://github.com/hoangtm3979/credit) · [Starter/template project](https://github.com/hoangtm3979/danhgiatindungcanhan)

## English case study

**Context and decision:** An evaluator needs a repeatable way to estimate adverse loan outcome risk and compare model families while respecting decision-time information boundaries.

**Problem:** Binary tabular classification of a historical loan outcome, with an interpretable Logistic Regression baseline and a nonlinear LightGBM challenger.

**Input:** historical CSV tables (development 2014–2018; time-held-out 2019–2020), loan and applicant fields, outcome labels. The data are external to GitHub and their redistribution rights/lineage have not been verified.

**Output:** predicted adverse-outcome probability, illustrative score and suggestions, evaluation/plots, exported transformers/models and a single-record inference function. The score is an academic illustration, **not** a credit bureau/CIC score.

**Constraints:** target leakage; post-origination fields; imbalanced outcomes; training/serving consistency; historical as-of dates; calibration; fairness; model drift; no personally identifying customer data published.

**Approach:** inspect and clean columns, engineer credit-style ratios/history features, remove known leakage columns, process categoricals, train Logistic Regression and LightGBM, compare ROC-AUC and KS, then serialize artifacts for inference.

**Recorded result:** The publicly committed Colab notebook contains outputs for **2,029,952 training** and **664,824 holdout** records; reported ROC-AUC is **0.930624 (Logistic)** and **0.935931 (LightGBM)**. These are notebook outputs, **not an independent replay**.

**Critical reflection:** Current implementation should not be advertised as leakage-free: a denylist does not establish feature timing; missing values are imputed independently in separate tables; some history length uses today's date rather than each loan's decision date. A high score may therefore overstate real decision-time reliability.

**Next acceptance gates:** data lineage and licensing; point-in-time availability matrix; train-only fitted transformers; frozen temporal folds; reproducible benchmark run; calibrated probabilities and subgroup analysis; minimal API/Docker test.

**What to explain in interview:** Why ROC-AUC is insufficient for credit use, how future information contaminates a score, what happens to precision/recall under class imbalance, how thresholds differ from business policy, and the difference between a notebook and deployed MLOps.

## Hồ sơ tiếng Việt

- **Bối cảnh:** hỗ trợ đánh giá rủi ro khoản vay từ dữ liệu cấu trúc, trong đó người sử dụng cần kết quả có thể giải thích và kiểm chứng theo thời gian.
- **Bài toán:** phân loại nhị phân rủi ro; Logistic Regression baseline so với LightGBM.
- **Input:** dữ liệu khoản vay theo hai giai đoạn lịch sử; đặc trưng khoản vay/khách hàng và nhãn đầu ra. Chưa đưa CSV gốc lên GitHub.
- **Output:** xác suất sự kiện bất lợi, điểm và gợi ý minh họa, metric, mô hình được lưu và hàm inference.
- **Ràng buộc:** chống target leakage, giữ đúng “thời điểm ra quyết định”, lệch phân bố train/test, mất cân bằng lớp, calibration và tính công bằng.
- **Kết quả:** notebook có log AUC **0,930624 / 0,935931** trên 2.029.952 dòng train và 664.824 dòng holdout. **Chưa được tái lập và kiểm toán dữ liệu độc lập.**
- **Quyết định kỹ thuật quan trọng:** thử model tuyến tính trước, tree-based sau; không xem model phức tạp là mặc nhiên tốt hơn trong vận hành.
- **Tồn đọng cần làm thật:** audit toàn bộ biến, sửa imputation trên holdout, dùng thời điểm lịch sử thay cho ngày hiện tại, tái chạy pipeline từ môi trường sạch và xuất báo cáo đánh giá chính thức.
- **Giới hạn:** chưa vận hành ngân hàng, chưa được xác thực như mô hình ra quyết định tín dụng.

**Contribution note / Ghi chú đóng góp:** Repository contains an executed notebook. Exact team/individual contribution and access rights for the source dataset must be checked before broader redistribution.
