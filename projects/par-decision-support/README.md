# PAR Decision-Support Demo / Giao diện hỗ trợ quyết định PAR

> **Điểm nổi bật:** Bản mẫu giao diện hướng dẫn người dùng phòng ngừa, xác minh hoặc khôi phục khi gặp tình huống rủi ro số.

[Tiếng Việt](#tiếng-việt) · [English](#english) · [Personal source repository](https://github.com/hoangtm3979/aegi-par-demo)

> **RELEASE_EVIDENCE_REVIEW:** đã đối chiếu mã cá nhân và nghiệm thu UI 1.1 ngày 25/09/2026; chưa kiểm tra endpoint mới. [Runbook](RUNBOOK.md).

## Tiếng Việt

### Bối cảnh và bài toán
Khi gặp một tình huống số có khả năng rủi ro, người dùng cần **hiểu tình huống và biết bước tiếp theo**. Tôi nghiên cứu cách tổ chức một luồng tương tác ngắn, rõ ràng, có thể quay lại khi thao tác gián đoạn.

Bản mẫu PAR diễn giải ba nhóm tình huống: **PREVENT_VERIFY**, **VERIFY_LIGHT** và **RECOVER**.

- **Input:** kịch bản giả lập được chọn, thông tin minh họa và ảnh tải lên nếu dùng chức năng tương ứng.
- **Output:** các bước phòng ngừa, xác minh hoặc khôi phục; trạng thái đang xử lý, kết quả, lỗi và reset.
- **Ràng buộc:** kết nối bất ổn, gửi yêu cầu lặp, phản hồi bất đồng bộ về muộn, thao tác tải ảnh và quyền riêng tư.

### Cách tôi tiếp cận
Tôi tập trung tách **luồng người dùng** khỏi dịch vụ phía sau, xử lý các phản hồi cũ (stale response), khóa thao tác xung đột khi upload và làm rõ nút hủy/đặt lại trạng thái.

README của repository có mô tả bài kiểm **40/40 cho PAR và 40/40 cho đối chứng** trên tập tình huống giới hạn. Tôi xem đó là kiểm tra hành vi luồng xử lý; bước đánh giá tác động với người dùng thực tế cần một thiết kế nghiên cứu khác.

### Bài học và bước tiếp
Một công cụ hỗ trợ quyết định phải làm rõ người dùng đang ở bước nào, dữ liệu được xử lý ra sao và nên hành động thế nào khi thiếu thông tin. Tôi muốn tiếp tục kiểm tra usability trên di động, khả năng truy cập, lỗi mạng, bảo mật upload và tái lập môi trường thử nghiệm.

[**Xem mã và tài liệu PAR tại GitHub cá nhân**](https://github.com/hoangtm3979/aegi-par-demo)

## English

> **In one sentence:** I prototype guided prevention, verification and recovery journeys for users facing uncertain digital-risk situations.

### Problem
I developed a **bounded decision-support UI prototype** for users navigating uncertain or potentially risky digital situations. Its three example journeys cover prevention/verification and recovery.

- **Input:** synthetic scenario selections, example user entries and optional image upload.
- **Output:** guided steps, visible request status, errors, cancellation/confirmation and reset.
- **Engineering work:** asynchronous UI state, stale-response handling, upload flow and interaction consistency.
- **Constraints:** network failures, privacy, repeated submissions and accessible feedback.

The repository describes a **40/40 PAR and 40/40 baseline** test on the example set. My focus is the usability and reliability of the workflow; user-outcome evaluation would be a separate step. Next I would strengthen security, mobile/accessibility review and reproducible demos.

*Public UI case from my personal repository.*


## Đối chiếu release / Release evidence review

**REVISED — 25/10/2026:** README nguồn vẫn mô tả phần triển khai là công việc tiếp theo, nhưng [`UI_RELEASE.json`](https://github.com/hoangtm3979/aegi-par-demo/blob/main/UI_RELEASE.json) và [biên bản nghiệm thu](https://github.com/hoangtm3979/aegi-par-demo/blob/main/PRODUCTION_ACCEPTANCE_UI_1.1.md) ghi nhận UI 1.1 / core rc4 đã được nghiệm thu triển khai **25/09/2026**: readiness/health/assets và 3/3 luồng, evidence 3/3, dọn 3/3 demo cases. Đây là bằng chứng triển khai lịch sử; không phải một lần kiểm tra endpoint mới trong đợt portfolio này.

[Code cá nhân](https://github.com/hoangtm3979/aegi-par-demo) · [Các tệp UI](https://github.com/hoangtm3979/aegi-par-demo/tree/main/submission_overlay) · [Hướng dẫn đọc và kiểm tra](RUNBOOK.md)

Bộ 40/40 PAR và 40/40 baseline là internal source-grounded offline evaluation có development exposure, không có ưu thế action-level giữa hai cấu hình và chưa có gold độc lập. Lần rà soát này không công bố thêm mã lõi nội bộ hoặc thay đổi backend.

**English:** public release records establish a historical UI 1.1 production acceptance, while the README is older in its deployment wording. The portfolio now links directly to the release evidence and separates runtime/UI acceptance from effectiveness and user-outcome evaluation.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
