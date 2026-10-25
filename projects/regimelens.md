# RegimeLens — Financial Market Regime Research / Nghiên cứu chế độ thị trường tài chính

**Evidence / Bằng chứng:** UIT Big Data team report, `BaoCao_Bigdata.pdf`. Code, dataset snapshots and dashboard deployment are **not verified in this public portfolio**.

## English case study

**Context:** Market behavior varies across trend and volatility regimes. A portfolio analyst may want to understand the current state and systematically test a risk-allocation rule.

**Problem:** Forecast a next-period market regime using information available up to the decision time and evaluate whether a regime-dependent hypothetical allocation changes simulated risk.

**Input:** historical S&P 500/market data, technical factors, volatility indicators and macro variables. The report analyzes a 2021–2026 research window.

**Output:** one of five modeled regimes (Bull, Bear, High Volatility, Recovery, Sideways), evaluation metrics, interpretability artifacts, a Streamlit-style research dashboard and simulated backtest.

**Approach:** data collection/merge → feature engineering → rolling/expanding HMM labeling → time-based training/validation/testing → Logistic Regression and Random Forest baselines vs XGBoost → confusion matrix, SHAP and a rule-based backtest.

**Report-stated results** (not independently replayed): XGBoost **Macro F1 0.563**, **Bear Recall 0.591**, **High-Volatility Recall 0.548**; a regime-switching backtest reports **Sharpe ~0.90** versus **~0.48** for buy-and-hold. These values must not be marketed as live investment performance or reliable alpha.

**Constraints and risks:** severe temporal leakage risk (especially regime labels and rolling transforms), label instability as the HMM is refitted, relatively short test window/class imbalance, point-in-time availability of revised macro series, unrealistic transaction-cost assumptions, and overfitting through repeated backtests.

**Critical reflection:** Even expanding-window HMM is not a blanket proof against look-ahead bias. The entire labeling, scaling, joining and strategy-evaluation pipeline must be checked at each timestamp; walk-forward replay and costs are essential.

**Next validation:** rebuild data provenance; frozen seeds/snapshots; walk-forward with no future data; purged/embargoed testing where appropriate; fees/slippage/turnover; regime confusion by period; model and random-strategy baselines.

**Collaboration:** This is a **UIT group project**. This page describes the group's reported system; the author's exact individual code contribution remains to be documented with commits or team confirmation.

## Hồ sơ tiếng Việt

- **Bối cảnh:** trạng thái thị trường thay đổi giữa tăng, giảm, biến động mạnh, phục hồi và đi ngang.
- **Bài toán:** dự báo regime tại bước thời gian tiếp theo và kiểm thử nguyên tắc phân bổ tài sản mô phỏng.
- **Input:** dữ liệu giá/khối lượng, VIX, chỉ báo kỹ thuật, dữ liệu vĩ mô; cần xác định thời điểm mỗi biến thật sự khả dụng.
- **Output:** nhãn chế độ thị trường, metric phân loại, SHAP, dashboard và backtest.
- **Mô hình:** HMM tạo nhãn theo cửa sổ mở rộng; Logistic/Random Forest làm baseline; XGBoost làm candidate.
- **Số liệu trong báo cáo:** Macro F1 **0,563**, Bear Recall **59,1%**, High-Volatility Recall **54,8%**; Sharpe backtest **~0,90 so với ~0,48**. **Đó là báo cáo môn học, chưa tái lập độc lập.**
- **Ràng buộc:** look-ahead bias, nhãn HMM thay đổi theo lần train, dữ liệu vĩ mô công bố trễ, số lượng mẫu hiếm, backtest thiếu phí/trượt giá.
- **Bước tiếp:** kiểm toán time-series pipeline, tái lập kết quả, walk-forward theo nhiều giai đoạn, báo cáo turnover và sensitivity.

**Scope:** educational financial research only; no investment advice and no deployed trading system claim.
