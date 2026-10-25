# PAR Decision-Support Demo / Bản mẫu hỗ trợ quyết định PAR

**Public source:** [Personal repository — aegi-par-demo](https://github.com/hoangtm3979/aegi-par-demo)

## English

**Context:** A time-sensitive digital action can expose a person to fraud or uncertainty. A bounded prototype can illustrate how users receive warnings, verification prompts, and recovery guidance.

**Problem:** Present understandable decision-support steps for three example scenarios and preserve a consistent, reversible UI state during interruptions.

**Input:** user-selected synthetic scenario, voluntary example entries and optionally an uploaded image in the prototype workflow.

**Output:** guided prevention/verification/recovery steps; visible status, loading/error handling and reset behavior.

**Scenarios shown in the existing public repository:** PREVENT_VERIFY, VERIFY_LIGHT and RECOVER.

**Engineering focus:** separate the presentation layer from a pre-existing backend; protect UI state against stale async responses; disable conflicting submissions during uploads; make reset and deletion confirmations explicit.

**Recorded evidence:** The repository's README describes local tests, including a **40/40 vs 40/40** PAR/baseline comparison on a bounded set. This **does not demonstrate superior fraud prevention, real customer outcomes or production readiness**.

**Constraints:** user privacy, consent for image transfer, false certainty, network outages, clear human responsibility, and preservation of non-public backend/IP.

**Trade-offs:** a guided workflow is understandable but only covers pre-defined cases; the tool must not pretend to connect to banks, police or telecom providers.

**Next verification:** source-level public disclosure review, isolated tests, Docker image reproducibility, deployment revision verification, accessibility/mobile review, security test and human evaluation.

## Tiếng Việt

- **Bối cảnh:** người dùng cần hỗ trợ nhận biết rủi ro và lựa chọn bước tiếp theo khi gặp tình huống không chắc chắn.
- **Bài toán:** thiết kế một luồng hỗ trợ quyết định rõ ràng cho ba ca minh họa, xử lý tốt trạng thái bất đồng bộ và lỗi mạng.
- **Input:** lựa chọn tình huống, dữ liệu ví dụ, ảnh (nếu sử dụng tính năng upload).
- **Output:** hướng dẫn phòng ngừa/xác minh/khôi phục; hiển thị trạng thái, xác nhận và reset.
- **Đồ án thể hiện:** logic giao diện, xử lý stale response, ngăn thao tác lặp khi upload, hoàn nguyên trạng thái và giới hạn tuyên bố năng lực.
- **Bằng chứng:** test nội bộ theo README, PAR và baseline cùng **40/40** — không phải bằng chứng PAR tốt hơn đối chứng.
- **Ràng buộc:** quyền riêng tư, người dùng là chủ thể quyết định, không tạo ảo tưởng đã tích hợp ngân hàng/cơ quan công quyền.
- **Giới hạn:** cần xác nhận trạng thái deploy hiện hành; không tự suy luận đã được production acceptance.

**IP boundary:** No Core/Shield proprietary verifier implementation, patent claims, keys or private backend bundles are reproduced in this portfolio.
