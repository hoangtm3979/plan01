# RegimeLens — Financial Market Regimes / Nghiên cứu trạng thái thị trường tài chính

> **Điểm nổi bật:** Tôi nghiên cứu trạng thái thị trường bằng HMM và so sánh dự đoán ngày kế tiếp với đối chứng giữ nguyên trạng thái hiện tại.

[Tiếng Việt](#tiếng-việt) · [English](#english) · [Notebook](notebooks/01_chronological_hmm_filtering.ipynb)

## Tiếng Việt

### Bài toán

Trong đồ án nhóm môn **Big Data tại UIT**, nhóm nghiên cứu cách biểu diễn trạng thái thị trường từ dữ liệu giá, khối lượng và biến động. Tôi trình bày tại đây bản thực nghiệm ba trạng thái, với notebook, mã xử lý và kết quả có thể chạy lại.

- **Input:** dữ liệu cổ phiếu S&P 500 trong snapshot của nhóm và chỉ số VIX.
- **Output:** xác suất trạng thái HMM, nhãn trạng thái và dự đoán trạng thái ngày kế tiếp.
- **Phương pháp:** tạo đặc trưng theo thời gian, HMM, Logistic Regression, Random Forest và XGBoost.

### Cách triển khai

Từ **2.087.863 dòng cổ phiếu**, pipeline tạo **6.374 ngày thị trường**. Tôi chia dữ liệu theo thời gian **70% train / 15% validation / 15% test**. Scaler và HMM chỉ học trên tập train; forward filtering tính trạng thái từ những quan sát đã xuất hiện đến ngày đang xét.

Các cặp dự đoán **t → t+1** được giữ trong từng giai đoạn. Mô hình được chọn bằng macro F1 trên validation và so sánh với **persistence**: dùng trạng thái hôm nay làm dự đoán cho ngày mai.

### Kết quả thực nghiệm

| Mô hình | Validation macro F1 | Test macro F1 |
| --- | ---: | ---: |
| Persistence | 0.933908 | 0.930728 |
| Logistic Regression | 0.932080 | 0.929316 |
| **Random Forest — chọn bằng validation** | **0.941223** | **0.943915** |
| XGBoost | 0.935525 | 0.927891 |

Random Forest đạt test macro F1 **0,943915**, so với **0,930728** của persistence. Đây là kết quả dự đoán **nhãn ẩn do HMM tạo ra**, trên một cách chia dữ liệu; chỉ số này đo khả năng dự đoán trạng thái của mô hình. Đánh giá chiến lược giao dịch là một bài toán riêng.

### Bài học và hướng phát triển

Tôi tập trung vào thứ tự thời gian, cách hình thành nhãn và lựa chọn đối chứng. Hướng phát triển tiếp theo là đánh giá qua nhiều cửa sổ walk-forward, kiểm tra độ ổn định của trạng thái và mô phỏng chiến lược có phí giao dịch, trượt giá.

## English

> **In one sentence:** I study next-day HMM-state prediction and compare machine-learning models with a persistence baseline.

This **UIT Big Data team project** explores market-state modeling from price, volume and volatility data. The experiment shared here uses **three HMM states** and **6,374 market days**, aggregated from **2,087,863 stock records** in the team's data snapshot.

I use a chronological **70/15/15 split**, fit the scaler and HMM on training data, and apply forward filtering. Each next-day target stays within its train, validation or test period. Validation macro F1 selects the predictor before test evaluation.

**Random Forest reaches test macro F1 0.943915**, compared with **0.930728** for persistence. These results measure prediction of the fitted HMM's latent labels in one chronological split. My next steps are multi-window evaluation, state stability analysis and a separate trading simulation with transaction costs.

## Mã và cách chạy / Code and reproduction

[**Notebook có output**](notebooks/01_chronological_hmm_filtering.ipynb) · [Pipeline](chronological_experiment.py) · [Kết quả JSON](evidence/chronological_experiment.json) · [Phương pháp, dữ liệu và phiên bản](AUDIT.md) · [Tư liệu môn học](research/README.md)

```bash
cd projects/regimelens-market-regimes
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
REGIMELENS_DATA_DIR=/path/to/original/data python run_notebooks.py --in-place
```

Đặt hai file `SP500_Historical_Data.csv` và `VIXCLS.csv` trong thư mục dữ liệu. Khi thiếu CSV, notebook chạy ví dụ giả lập để kiểm tra luồng xử lý; kết quả ví dụ được ghi riêng với kết quả trên dữ liệu thị trường.

---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
