# Multi-Camera Face Attendance (IoT / Computer Vision)
# Điểm danh công nhân qua camera bằng nhận diện khuôn mặt

> **Điểm nổi bật:** Đồ án nhóm về quy trình điểm danh từ camera đến nhận diện khuôn mặt, kiểm tra sự kiện và lưu lịch sử trong mạng LAN.

[Tiếng Việt](#tiếng-việt) · [English](#english)

> **REPORT_GROUNDED:** đúng báo cáo nhóm Nam Sài Gòn; bộ mã đầy đủ/camera/hardware chưa được kiểm tra độc lập. [System design](SYSTEM_DESIGN.md).

## Tiếng Việt

### Bối cảnh và bài toán
Đây là **đồ án nhóm năm người tại UIT** về điểm danh công nhân bằng camera. Ở môi trường có nhiều cổng và nhiều ca làm, việc nhập tay hoặc dùng thẻ có thể làm phát sinh chờ đợi, ghi trùng và khó tổng hợp dữ liệu.

Nhóm xây dựng một **MVP trên máy tính trong mạng LAN**: nhận hình từ webcam hoặc IP camera/RTSP, phát hiện và đối chiếu khuôn mặt, lưu sự kiện điểm danh và hiển thị báo cáo.

| Thành phần | Thiết kế trong báo cáo nhóm |
| --- | --- |
| **Input** | Frame webcam/RTSP, ảnh đăng ký, mã công nhân, thông tin camera |
| **Output** | Danh tính được so khớp hoặc trạng thái unknown/spoof, thời gian/camera, log và CSV/XLSX |
| **Phát hiện khuôn mặt** | YOLO, phương án dự phòng OpenCV Haar |
| **Nhận diện** | InsightFace/ArcFace embedding, cosine similarity với gallery, LBP dự phòng |
| **Kiểm tra sự kiện** | Mô hình anti-spoof qua ONNX khi có sẵn; xử lý ghi trùng, mặc định 20 giây trong báo cáo |
| **Backend** | Python, OpenCV, FastAPI, ONNX Runtime, SQLite, dashboard trình duyệt |

### Phần việc và lựa chọn kỹ thuật
**Theo phân công trong báo cáo nhóm, tôi phụ trách xử lý ảnh, phát hiện/nhận diện khuôn mặt, nghiên cứu yêu cầu nhiều khuôn mặt và giảm nhận nhầm.**

Luồng chính: nhận frame → phát hiện mặt → tạo embedding/đối chiếu → kiểm tra điều kiện sự kiện → lưu SQLite → thống kê. Tôi đặc biệt quan tâm đến ngưỡng cosine, trường hợp người chưa đăng ký, chất lượng ảnh và cách phản ứng khi thiếu mô hình dự phòng.

Một khác biệt quan trọng trong thiết kế hiện tại: **nhiều camera đầu vào không đồng nghĩa nhận diện đồng thời nhiều người**. Đường nhận diện chính mô tả trong báo cáo chọn **khuôn mặt lớn nhất** trên ảnh. Xử lý từng khuôn mặt khi khung hình đông người là hướng tiếp tục.

### Kết quả và bước tiếp
Báo cáo môn học mô tả MVP chạy trong môi trường PC/LAN với các chức năng quản lý công nhân/camera, đăng ký ảnh, webcam/RTSP, ghi nhận sự kiện và xuất báo cáo.

Tôi muốn đào sâu tiếp phần **FAR/FRR, người lạ, chống giả mạo, reconnect camera, latency/FPS và kiểm soát dữ liệu khuôn mặt**. Raspberry Pi hoặc thiết bị edge chuyên dụng là giai đoạn benchmark sau MVP.

**Tài liệu:** báo cáo cuối kỳ nhóm Nam Sài Gòn, UIT, 2026. Các ảnh khuôn mặt và dữ liệu nhân sự được giữ trong bộ tài liệu học tập riêng.

## English

> **In one sentence:** A team project mapping camera input, face matching and event logging into a local-network attendance workflow.

### Context and goal
This was a **five-member UIT team project** exploring a camera-based worker attendance workflow. The team built a **local PC/LAN MVP** that ingests webcam and IP-camera frames, recognizes enrolled workers and stores timestamped attendance events.

- **Input:** camera frames/RTSP, enrollment portraits, worker and camera identifiers.
- **Output:** matched identity or unknown/spoof event, attendance records, dashboard and CSV/XLSX export.
- **Stack:** Python, OpenCV, YOLO/Haar, InsightFace ArcFace with cosine similarity, optional ONNX anti-spoofing, FastAPI and SQLite.
- **Constraints:** lighting and pose, false matches, duplicate events, camera stability and biometric privacy.

### My role and engineering lessons
The group report assigns me to **image processing, face detection/recognition, multi-face requirements and error reduction**. The main reported recognition path selects the **largest detected face**; expanding it to each detected person is a follow-up engineering task.

The local attendance workflow and reporting were demonstrated in the coursework setting. I would next test false acceptance/rejection, unseen identities, spoof attempts, multiple people per frame, camera reconnects and per-stage latency, then benchmark on actual edge hardware.

*UIT team coursework, 2026.*


## Tư liệu và mức hoàn thiện / Materials and publication scope

Đã đọc lại báo cáo cuối kỳ **nhóm Nam Sài Gòn**, có tên và phân công của Hoàng. [Thiết kế hệ thống và API](SYSTEM_DESIGN.md) nối từng thành phần tới luồng điểm danh, gồm fallback và giới hạn nhiều khuôn mặt.

Mã đầy đủ đang nằm trong `Code_NhanDienKhuonMat.zip` (555.414.721 bytes), lớn hơn giới hạn tải 256 MiB của kết nối đọc file hiện tại. Đợt này **chưa đọc/kiểm thử độc lập toàn bộ ZIP**, chưa công bố notebook YOLO của nhóm khác thay cho mã đội mình. Dữ liệu khuôn mặt, gallery và database nhân sự không được đưa vào Git.

**English:** the case and architecture are grounded in the correct team report. Full source extraction, camera runtime, face matching, spoofing and hardware benchmarks remain unverified in this publication. The 80–95% figure in slides is a target range, not a measured accuracy.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
