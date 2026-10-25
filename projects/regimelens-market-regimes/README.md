# RegimeLens — Financial Market Regimes / Nghiên cứu trạng thái thị trường tài chính

> **Điểm nổi bật:** Khám phá trạng thái thị trường bằng HMM, rồi kiểm tra dự đoán ngày kế tiếp với đối chứng giữ nguyên trạng thái hôm nay.

[Tiếng Việt](#tiếng-việt) · [English](#english)

> **FRESH_EXPERIMENT:** HMM 3 trạng thái chỉ fit train, đánh giá latent-state prediction; chưa đánh giá lợi nhuận. [Audit](AUDIT.md).

## Tiếng Việt

### Bối cảnh và bài toán
Đây là **đồ án nhóm môn Big Data tại UIT**. Nhóm nghiên cứu việc phân loại trạng thái thị trường—tăng, giảm, biến động mạnh, hồi phục hoặc đi ngang—để hỗ trợ phân tích rủi ro và kiểm thử quy tắc phân bổ tài sản mô phỏng.

- **Input:** dữ liệu giá/khối lượng, chỉ báo kỹ thuật, VIX và biến vĩ mô trong giai đoạn nghiên cứu 2021–2026.
- **Output:** nhãn một trong năm trạng thái, mô hình dự báo, chỉ số phân loại, SHAP, dashboard nghiên cứu và backtest.
- **Ràng buộc:** thứ tự thời gian, ngày công bố dữ liệu vĩ mô, cách tạo nhãn HMM, biến động giữa các giai đoạn, chi phí giao dịch và trượt giá.

### Thiết kế trong đồ án
Theo báo cáo nhóm, bài toán gồm: tích hợp dữ liệu → tạo đặc trưng → gán trạng thái bằng HMM → so sánh Logistic Regression/Random Forest với XGBoost → đánh giá phân loại → mô phỏng chiến lược theo regime.

Báo cáo ghi **Macro F1 = 0,563**, **Bear Recall = 0,591**, **High-Volatility Recall = 0,548** với XGBoost; Sharpe của backtest regime khoảng **0,90** so với **0,48** của buy-and-hold. Đây là kết quả của báo cáo nhóm.

### Điều tôi rút ra khi xem lại mã
**REVISED — 25/10/2026:** Khi đối chiếu một bản Colab lịch sử, tôi thấy `StandardScaler` và HMM được `fit` trên toàn chuỗi trước khi chia dữ liệu theo thời gian; bước xử lý giá còn có `.bfill()`. Điều này có thể đưa thông tin tương lai vào quan sát quá khứ và khác quy trình rolling/expanding mô tả trong báo cáo. Tôi giữ riêng **số liệu trong báo cáo** và **hành vi của notebook được kiểm tra**, vì chưa xác định được đây có phải cùng phiên bản chạy benchmark cuối hay không.

Đợt cập nhật bên dưới bổ sung mã nguồn, CSV snapshot đã đối chiếu và một phép thử HMM cố định trên train. Multi-window walk-forward, phí/trượt giá và phân tích độ nhạy vẫn là phần tiếp theo. Đây cũng là bài học của tôi về sự khác nhau giữa một backtest hấp dẫn và một thử nghiệm chuỗi thời gian đáng tin cậy.

## English

> **In one sentence:** Study next-day HMM-state prediction and compare machine-learning models with a simple persistence baseline.

### Research question
In this UIT Big Data group project, we explored whether financial **market regimes** could be modeled and used to test a hypothetical risk-allocation strategy.

- **Input:** price, volume, technical/volatility and macroeconomic features.
- **Output:** five-regime labels, predictive models, evaluation, interpretability views and a simulated backtest.
- **Methods described in the group report:** HMM regime labeling, Logistic Regression and Random Forest baselines, XGBoost, SHAP and a regime-based allocation rule.

The report records **Macro F1 0.563**, **Bear Recall 0.591**, **High-Volatility Recall 0.548**, and simulated Sharpe figures of about **0.90 vs 0.48**.

### Code review and next iteration
**REVISED (25 Oct 2026):** An inspected historical notebook fits its scaler/HMM on the full sequence and backfills price data before the chronological split. That implementation differs from the report's rolling/expanding design and raises look-ahead concerns. I am treating the report metrics and inspected notebook as **different evidence until their versions are matched**.

I would rebuild this experiment with point-in-time features, walk-forward fitting and transaction-cost sensitivity. The main learning is that a time-series model is only as credible as its information boundaries.

*UIT team project. Results are from the course report; the historical notebook is under version and evaluation review.*


## Thí nghiệm mới và đối chiếu phiên bản / Fresh experiment and version review

[**Notebook có output**](notebooks/01_chronological_hmm_filtering.ipynb) · [Mã thử nghiệm](chronological_experiment.py) · [Bằng chứng](evidence/chronological_experiment.json) · [Audit và dữ liệu](AUDIT.md)

Đã lấy được `mode_test_.ipynb` và ba CSV từ `Data.rar` của nhóm. Mã này dùng **3 trạng thái**, dữ liệu khoảng **2000–2026**, khác cấu hình 5 trạng thái/2021–2026 được mô tả trong case từ báo cáo. Những chỉ số cũ 0,563/0,90/0,48 được giữ ở mức **HISTORICAL_REPORT**, không xem là kết quả tái lập của mã mới.

Thí nghiệm mới dùng 2.087.863 dòng cổ phiếu để tạo **6.374 ngày thị trường**. Scaler/HMM chỉ fit 4.461 ngày train. Forward filtering không nhìn các quan sát tương lai; cặp t→t+1 không vượt biên train/validation/test. Không dùng backfill. 3/3 kiểm thử filtering đạt.

| Model | Validation macro F1 | Test macro F1 |
| --- | ---: | ---: |
| Persistence | 0.933908 | 0.930728 |
| Logistic Regression | 0.932080 | 0.929316 |
| **Random Forest — chọn bằng validation** | **0.941223** | **0.943915** |
| XGBoost | 0.935525 | 0.927891 |

Đây là **dự đoán trạng thái ẩn của một HMM đã cố định**, chưa phải độ đúng của trạng thái kinh tế độc lập hoặc lợi nhuận giao dịch. Chỉ một split/seed; universe lịch sử và thời điểm khả dụng của giá điều chỉnh/VIX chưa được xác minh đầy đủ. Backtest/chi phí/slippage chưa chạy.

```bash
cd projects/regimelens-market-regimes
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
REGIMELENS_DATA_DIR=/path/to/original/data python run_notebooks.py --in-place
```

Thiếu CSV, notebook chạy một **synthetic smoke test** và ghi scope tương ứng; không dùng số của ví dụ đó làm kết quả S&P 500. Cần hai file `SP500_Historical_Data.csv`, `VIXCLS.csv`; `SP500.csv` chỉ được dùng bởi notebook lịch sử.

**English:** the fresh chronological experiment freezes the three-state HMM on training data and compares next-day latent-state prediction with persistence. The saved five-state report metrics and trading claims have not been reproduced. The [historical source](research/regimelens-hmm-xgboost-historical.ipynb) remains available for the code review.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
