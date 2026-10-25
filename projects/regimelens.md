# RegimeLens — Financial Market Regime Research / Nghiên cứu chế độ thị trường tài chính

**Evidence / Bằng chứng:** UIT Big Data group report `BaoCao_Bigdata.pdf` plus an inspected historical Colab file named `BIGDATA_mode_test_.ipynb`. The **version link between the notebook and the reported final model/backtest is unverified**, and deployment is not independently reproduced.

> **REVISED — 2026-10-25 / ĐÍNH CHÍNH:** An inspected notebook fits `StandardScaler` and `GaussianHMM` to the **full regime series before a subsequent 70/15/15 chronological split**; an earlier stock-level preparation step also uses backward fill (`.bfill()`). Thus **that notebook version is not a leakage-safe walk-forward experiment**. The course report describes a rolling/expanding HMM methodology, but the inspected code does not establish that it was implemented in this file. Previous wording implying the inspected implementation was rolling is superseded; report-stated metrics remain only report evidence.

## English case study

**Context:** Market behavior varies across trend and volatility regimes. A portfolio analyst may want to understand the current state and systematically test a risk-allocation rule.

**Problem:** Forecast a next-period market regime using information available up to the decision time and evaluate whether a regime-dependent hypothetical allocation changes simulated risk.

**Input:** historical S&P 500/market data, technical factors, volatility indicators and macro variables. The report analyzes a 2021–2026 research window.

**Output:** one of five modeled regimes (Bull, Bear, High Volatility, Recovery, Sideways), evaluation metrics, interpretability artifacts, a Streamlit-style research dashboard and simulated backtest.

**Report-described approach:** data collection/merge → feature engineering → rolling/expanding HMM labeling → time-based training/validation/testing → Logistic Regression and Random Forest baselines vs XGBoost → confusion matrix, SHAP and a rule-based backtest. **Inspected notebook differs** at the HMM-label stage; source/report parity is not established.

**Report-stated results** (not independently replayed): XGBoost **Macro F1 0.563**, **Bear Recall 0.591**, **High-Volatility Recall 0.548**; a regime-switching backtest reports **Sharpe ~0.90** versus **~0.48** for buy-and-hold. These values must not be marketed as live investment performance or reliable alpha.

**Constraints and risks:** severe temporal leakage risk (especially regime labels and rolling transforms), label instability as the HMM is refitted, relatively short test window/class imbalance, point-in-time availability of revised macro series, unrealistic transaction-cost assumptions, and overfitting through repeated backtests.

**Critical reflection:** This is a concrete leakage warning, not a theoretical possibility for the inspected notebook: its scaler/HMM see later observations before chronological model evaluation, and stock-price backward-filling can put future information into earlier rows. The measured F1 must be rerun after fixing these steps. The report may refer to a different version; identifying its actual source commit is prerequisite to attributing results.

**Next validation:** rebuild data provenance; frozen seeds/snapshots; walk-forward with no future data; purged/embargoed testing where appropriate; fees/slippage/turnover; regime confusion by period; model and random-strategy baselines.

**Collaboration:** This is a **UIT group project**. This page describes the group's reported system; the author's exact individual code contribution remains to be documented with commits or team confirmation.

## Hồ sơ tiếng Việt

- **Bối cảnh:** trạng thái thị trường thay đổi giữa tăng, giảm, biến động mạnh, phục hồi và đi ngang.
- **Bài toán:** dự báo regime tại bước thời gian tiếp theo và kiểm thử nguyên tắc phân bổ tài sản mô phỏng.
- **Input:** dữ liệu giá/khối lượng, VIX, chỉ báo kỹ thuật, dữ liệu vĩ mô; cần xác định thời điểm mỗi biến thật sự khả dụng.
- **Output:** nhãn chế độ thị trường, metric phân loại, SHAP, dashboard và backtest.
- **Mô hình theo báo cáo:** HMM tạo nhãn mở rộng; Logistic/Random Forest làm baseline; XGBoost làm candidate. **Trong notebook được xem**, HMM học toàn bộ chuỗi trước khi chia 70/15/15, khác với mô tả walk-forward.
- **Số liệu trong báo cáo:** Macro F1 **0,563**, Bear Recall **59,1%**, High-Volatility Recall **54,8%**; Sharpe backtest **~0,90 so với ~0,48**. **Đó là báo cáo môn học, chưa tái lập độc lập.**
- **Ràng buộc và phát hiện mới:** notebook có `.bfill()` trên giá từng mã, `StandardScaler.fit_transform(X_hmm)` và `hmm_model.fit(X_hmm_scaled)` toàn chuỗi trước khi chia tập; đây là nguy cơ nhìn trước **đã thấy trong mã**, không chỉ rủi ro giả định. Cần đối chiếu phiên bản và huấn luyện lại theo từng thời điểm; chưa có kiểm chứng phí/trượt giá.
- **Bước tiếp:** kiểm toán time-series pipeline, tái lập kết quả, walk-forward theo nhiều giai đoạn, báo cáo turnover và sensitivity.

**Scope:** educational financial research only; no investment advice and no deployed trading system claim.
