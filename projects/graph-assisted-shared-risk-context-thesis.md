# Graph-Assisted Shared Risk Context — Khóa luận tốt nghiệp AI / AI Undergraduate Thesis

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

### Bối cảnh và bài toán

Trong đánh giá rủi ro tài chính, tín hiệu đến từ nhiều mô hình khác nhau. Tôi muốn giải quyết hai câu hỏi riêng: **liệu đặc trưng quan hệ trong dữ liệu đồ thị giúp phát hiện bất thường tốt hơn thuộc tính đơn lẻ?** Và **làm sao sử dụng các đầu ra rủi ro khác miền trong một quy trình hỗ trợ xem xét, mà vẫn giữ rõ ý nghĩa và nguồn gốc từng kết quả?**

Đây là **khóa luận tốt nghiệp cá nhân** tại Trường Đại học Công nghệ Thông tin, ĐHQG-HCM. Tôi xây dựng nguyên mẫu nghiên cứu ngoại tuyến, thực hiện thí nghiệm và phân tích kết quả dưới sự hướng dẫn của **ThS. Phạm Thế Sơn**.

### Input, output và ràng buộc

| Nhánh | Input | Output |
| --- | --- | --- |
| **RQ1 — Graph features** | Thuộc tính nút, liên kết có hướng và nhãn phân lớp của **DGraphFin** | Điểm xếp hạng bất thường từ hai cấu hình LightGBM, bảng AP/ROC-AUC, kết quả Top-K và so sánh thống kê |
| **RQ2 — Shared Risk Context** | Đầu ra độc lập của mô hình rủi ro tín dụng trên **LendingClub** và mô hình phát hiện bất thường trên DGraphFin | Các đối tượng ngữ cảnh có kiểu dữ liệu/nguồn gốc rõ ràng, kết quả kiểm tra hợp đồng, định tuyến theo chính sách và dấu vết thực thi |

Tôi giữ các ranh giới thiết kế sau:

- DGraphFin gồm **3.700.550 nút và 4.300.999 cạnh có hướng**; phải phân biệt quan hệ trong dữ liệu với giao dịch tài chính. Trong bộ dữ liệu này, cạnh biểu diễn quan hệ người liên hệ khẩn cấp, không phải chuyển tiền.
- LendingClub và DGraphFin là **hai bộ dữ liệu độc lập**, không có khóa định danh chung để ghép khách hàng. Shared Risk Context tiếp nhận đầu ra **sau dự đoán**, không tạo điểm tín dụng–gian lận kết hợp.
- Với dữ liệu lệch lớp mạnh, tôi chọn **Average Precision (AP)** làm thước đo chính, đồng thời xem xét năng lực tại nhóm ưu tiên rà soát **Top-1%**.
- Các mô hình, cách tách dữ liệu, phiên bản ngữ cảnh và tiêu chí kiểm thử được xác định để có thể đối chiếu kết quả.

### Cách tôi thực hiện

**RQ1.** Tôi tạo một đối chứng LightGBM chỉ dùng thuộc tính nút và một cấu hình bổ sung đặc trưng cấu trúc/láng giềng trên đồ thị, cùng tập kiểm thử và cùng thiết lập đánh giá. Tôi so sánh AP, ROC-AUC, độ ổn định theo seed, bootstrap ghép cặp và hiệu quả tại ngưỡng Top-K.

**RQ2.** Tôi định nghĩa hợp đồng **Shared Risk Context v2.1** để giữ lại miền rủi ro, ý nghĩa điểm số, phạm vi thực thể, phiên bản mô hình và tham chiếu nguồn. Sau đó tôi xây nguyên mẫu **kiểm tra → chuẩn hóa → định tuyến theo chính sách → lưu dấu vết**, sử dụng các trường hợp kiểm thử kiểm soát.

### Kết quả từ báo cáo KLTN cập nhật 23/10/2026

Trên **183.840** nút kiểm thử DGraphFin:

| Chỉ số | Node-only LightGBM | Node + Graph LightGBM |
| --- | ---: | ---: |
| Average Precision | 0,025033 | **0,032505** |
| ROC-AUC | 0,712745 | **0,768485** |
| True positives ở Top-1% | **62** | 55 |

Chênh lệch AP là **+0,007473**, với khoảng tin cậy bootstrap ghép cặp 95% **[+0,006049; +0,008813]** qua 10.000 lần lấy mẫu. Điều đáng chú ý là **AP và ROC-AUC cải thiện nhưng số trường hợp dương tính trong Top-1% lại giảm**. Vì thế tôi tách rõ đánh giá khả năng xếp hạng tổng thể khỏi mục tiêu xử lý theo công suất rà soát hữu hạn.

Ở RQ2, nguyên mẫu đã ánh xạ **195.420** đầu ra tín dụng và hai tập **183.840** đầu ra bất thường sang các ngữ cảnh tương ứng; các trường được kiểm tra bảo toàn **100%**. **13** kịch bản định tuyến cho kết quả dự kiến; **100** lần chạy lặp tạo cùng giá trị băm đầu ra trong phạm vi kiểm thử.

### Phát hiện kỹ thuật và hướng đào sâu

Khi rà soát sau thí nghiệm, tôi xác định phép tổng hợp láng giềng trong mã dùng `A @ x`, tương ứng với **láng giềng theo cạnh đi ra** của đồ thị có hướng. Tôi cũng phát hiện **rất nhiều trường hợp đồng điểm gần ngưỡng Top-1%**, khiến kết quả xếp hàng ưu tiên nhạy với cơ chế xử lý ties. Đây là cơ sở cho bước ablation tiếp theo: kiểm tra đặc trưng cạnh đi vào/đi ra, quy tắc phá hòa điểm và hiệu quả theo nhiều mức công suất K.

Bài học lớn nhất của tôi là: **một mô hình có AP tốt hơn chưa chắc tốt hơn ở điểm ra quyết định mà nghiệp vụ thực sự sử dụng**. Ở tầng hệ thống, ngữ nghĩa và nguồn gốc của đầu ra quan trọng không kém con số điểm số.

*Dự án cá nhân · KLTN ngành Trí tuệ nhân tạo · Báo cáo và mã nghiên cứu lưu trong hồ sơ học thuật cá nhân.*

## English

### Context and problem

This undergraduate thesis explores two connected but distinct questions: **Do graph-derived features improve anomaly ranking compared with node attributes alone?** And **how can independent credit-risk and anomaly-model outputs be brought into a shared decision-support workflow while preserving each output's meaning and provenance?**

I developed an **offline research prototype** and conducted the experiments as my individual AI thesis at the University of Information Technology, VNU-HCM, supervised by **MSc Phạm Thế Sơn**.

### Input, output and constraints

| Research question | Input | Output |
| --- | --- | --- |
| **RQ1 — Graph features** | DGraphFin node attributes, directed edges and labels | LightGBM ranking scores; AP, ROC-AUC, Top-K and statistical comparisons |
| **RQ2 — Shared Risk Context** | Independent LendingClub credit-model outputs and DGraphFin anomaly outputs | Typed, traceable risk-context objects, contract checks and deterministic policy-routing results |

The DGraphFin graph contains **3,700,550 nodes and 4,300,999 directed edges**. Its edges encode emergency-contact relationships, rather than payment transactions. LendingClub and DGraphFin have **no verified common identities**, so I keep their predictions separate and normalize their meanings after inference instead of joining records or calculating a fused credit–fraud score.

### Approach

For **RQ1**, I compared a node-only LightGBM baseline against a node-plus-graph-feature variant under the same evaluation setup. I examined AP, ROC-AUC, seed stability, paired bootstrap estimates and the operational Top-1% review slice.

For **RQ2**, I designed **Shared Risk Context v2.1** with explicit risk domains, score meanings, entity scope, model versions, data provenance and trace references. I implemented an offline workflow to validate, map and route those contexts according to declared policies.

### Results and lessons

On the **183,840-node** DGraphFin test set, AP rose from **0.025033 to 0.032505**, and ROC-AUC from **0.712745 to 0.768485**. Paired bootstrap yielded a ΔAP of **+0.007473** (95% interval **[+0.006049, +0.008813]**, 10,000 draws). Yet the Top-1% slice captured **62 positives with the node-only model versus 55 with graph features**. This trade-off shaped how I discuss model quality versus operational ranking.

The RQ2 prototype mapped **195,420** credit outputs and **two sets of 183,840** anomaly outputs with **100% preservation of the contract fields checked**. All **13** controlled routing scenarios matched their expected results; **100** repeated executions produced the same output hash under the tested conditions.

A post-experiment review also identified that `A @ x` aggregated **outgoing neighbors** and that a large tied-score group affected Top-1% ordering. I would next test direction-aware feature ablations and explicit tie-handling rules.

**What I learned:** aggregate discrimination and performance at a fixed review budget can point in different directions. Reliable decision-support design also requires unambiguous output semantics and provenance, not just model scores.

*Individual undergraduate thesis · Artificial Intelligence · Academic report revised 23 October 2026.*
