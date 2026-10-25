# RegimeLens — Financial Market Regimes / Nghiên cứu trạng thái thị trường tài chính

[Tiếng Việt](#tiếng-việt) · [English](#english)

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

Bước tiếp theo: dựng lại lịch sử dữ liệu và phiên bản nguồn, thử walk-forward đúng thời điểm, so sánh baseline, thêm phí/trượt giá và phân tích độ nhạy theo giai đoạn. Đây cũng là bài học của tôi về sự khác nhau giữa một backtest hấp dẫn và một thử nghiệm chuỗi thời gian đáng tin cậy.

## English

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
