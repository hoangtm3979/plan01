# PAR Decision-Support Demo / Giao diện hỗ trợ quyết định PAR

[Tiếng Việt](#tiếng-việt) · [English](#english) · [Personal source repository](https://github.com/hoangtm3979/aegi-par-demo)

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

### Problem
I developed a **bounded decision-support UI prototype** for users navigating uncertain or potentially risky digital situations. Its three example journeys cover prevention/verification and recovery.

- **Input:** synthetic scenario selections, example user entries and optional image upload.
- **Output:** guided steps, visible request status, errors, cancellation/confirmation and reset.
- **Engineering work:** asynchronous UI state, stale-response handling, upload flow and interaction consistency.
- **Constraints:** network failures, privacy, repeated submissions and accessible feedback.

The repository describes a **40/40 PAR and 40/40 baseline** test on the example set. My focus is the usability and reliability of the workflow; user-outcome evaluation would be a separate step. Next I would strengthen security, mobile/accessibility review and reproducible demos.

*Public UI case from my personal repository.*
