# Credit Risk Modeling / Mô hình hóa rủi ro tín dụng

> **Điểm nổi bật:** So sánh Logistic Regression và LightGBM để ước lượng rủi ro khoản vay, đồng thời rà soát dữ liệu có thể biết tại thời điểm xét vay.

[Tiếng Việt](#tiếng-việt) · [English](#english) · [Notebook](https://github.com/hoangtm3979/credit)

> **SOURCE_REVIEW:** 13 code cells syntax PASS; AUC là output lịch sử, chưa huấn luyện lại. [Audit](AUDIT.md).

## Tiếng Việt

### Bối cảnh và bài toán
Tôi thực hành xây dựng một hệ thống **ước lượng xác suất rủi ro của khoản vay** từ dữ liệu lịch sử. Tôi chọn Logistic Regression làm mô hình đối chứng dễ giải thích và LightGBM để nghiên cứu quan hệ phi tuyến.

- **Input:** bảng dữ liệu khoản vay và đặc trưng khách hàng, nhãn kết quả lịch sử; giai đoạn phát triển 2014–2018 và holdout 2019–2020.
- **Output:** xác suất sự kiện bất lợi, điểm số minh họa, bảng chỉ số đánh giá, các mô hình/transformer lưu để suy luận.
- **Ràng buộc:** dữ liệu mất cân bằng, xử lý nhất quán giữa train/test, biến chỉ xuất hiện sau khi cho vay, biến động theo thời gian và khả năng diễn giải xác suất.

### Cách tôi triển khai
1. Khảo sát phân bố dữ liệu, giá trị thiếu và đặc trưng liên quan đến khoản vay.
2. Xây các biến tỷ lệ và lịch sử tín dụng; mã hóa dữ liệu phân loại.
3. Huấn luyện Logistic Regression, sau đó thử LightGBM và so sánh trên tập holdout.
4. Xuất artifact và hàm suy luận cho một hồ sơ đầu vào.

### Kết quả và điều tôi học được
Notebook lưu kết quả trên **2.029.952 bản ghi train** và **664.824 bản ghi holdout**, với **ROC-AUC 0,930624 (Logistic)** và **0,935931 (LightGBM)**. Tôi quan tâm không chỉ chỉ số cao mà còn việc kết quả có đúng trong điều kiện ra quyết định hay không.

Khi đọc lại pipeline, tôi xác định các điểm cần cải tiến: đảm bảo mọi feature có trước thời điểm xét vay, chỉ `fit` bước điền thiếu trên tập train và tính thời gian lịch sử theo mốc của từng hồ sơ. Đây là phần tôi sẽ sửa trước khi benchmark lại, bổ sung calibration và phân tích theo nhóm.

## English

> **In one sentence:** Compare Logistic Regression and LightGBM for loan-risk estimation while reviewing which features are available at decision time.

### Problem and data
I explored **loan risk probability estimation** on structured historical records, comparing an interpretable Logistic Regression baseline with LightGBM.

- **Input:** loan/applicant features and historical outcome labels, with a later time-based holdout.
- **Output:** risk probabilities, illustrative scores, evaluation plots and serialized inference components.
- **Constraints:** class imbalance, temporal feature availability, leakage, calibration and consistent preprocessing.

### My approach
I explored data quality and distributions, engineered lending-related features, prepared categorical variables, trained the two models and compared ROC-AUC and KS. I also packaged a single-record inference path.

### Results and next steps
The saved notebook records **2,029,952 training** and **664,824 holdout** rows, and ROC-AUC values of **0.930624** and **0.935931**. My current focus is a point-in-time feature audit, train-fitted imputation, a clean rerun and calibration. This project taught me how easily a strong offline score can depend on assumptions about when information becomes available.

**Code:** [Personal Credit Risk notebook](https://github.com/hoangtm3979/credit).


## Mã và trạng thái hiện tại / Code and current status

**SOURCE_REVIEW — 25/10/2026:** đã đưa [notebook v3.1 có tên rõ nội dung](research/credit-risk-logistic-lightgbm-v3.1.ipynb) vào thư mục này và sửa token thừa gây lỗi cú pháp trong `to_float_percent`. **13 code cells đạt kiểm tra cú pháp**; chưa huấn luyện lại trên hai CSV gốc. Các AUC 0,930624/0,935931 ở trên là output lịch sử, chưa xác nhận bằng một lần chạy mới.

- [Kiểm tra pipeline và những điểm còn mở](AUDIT.md).
- [Nguồn, thay đổi khi xuất bản](PROVENANCE.json) · [Hướng dẫn nguồn lịch sử](research/README.md).
- [Repo nguồn cá nhân trước đây](https://github.com/hoangtm3979/credit) được giữ làm dấu mốc học tập.
- [Credit source trong KLTN](../graph-assisted-shared-risk-context/research/01_CREDIT_OUTPUTS_v2_1.ipynb) là **một thí nghiệm khác** với nhãn/feature/split riêng; không dùng chỉ số của nó thay cho v3.1.

The syntax fix makes the historical source inspectable. It does not resolve the label horizon, point-in-time feature availability or holdout-fitted imputation. See the audit before reusing the training/inference code.


### Bộ khung học tập trước đó / Earlier learning scaffold

[Credit Scoring — AI Thinking Starter Pack](https://github.com/hoangtm3979/danhgiatindungcanhan) ghi lại bước phân rã bài toán, cấu hình, giao diện Streamlit và đề cương báo cáo. Đây là bộ khung học tập; README nguồn vẫn ghi train/inference là phần dự kiến hoàn thiện. Tôi giữ liên kết này để nối quá trình từ thiết kế ban đầu tới notebook thực nghiệm v3.1.

The starter pack records the planning stage and is kept as learning history; it is not counted as another validated credit model.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
