# Multi-Camera Face Recognition Attendance — Edge AI Coursework
# Hệ thống điểm danh công nhân đa camera bằng nhận diện khuôn mặt

> **Evidence / Bằng chứng:** 2026 UIT course group report `Final Bao cao do an nhom Nam Sai Gon.docx` in the owner's private Drive, with **Trương Minh Hoàng (25410008)** named in the five-member team. This page is an anonymized technical case, **not** a public copy of camera footage, staff biometrics, source ZIP, or project report.

## English — Engineering case study

**Context.** Construction sites have multiple entry points and shift changes. Manual attendance or transferable access cards can cause queues, fragmented audit trails and proxy attendance.

**Problem.** Build a research-stage, LAN-oriented attendance workflow able to ingest camera frames, identify a registered worker if possible, detect unknown/spoof conditions and record time-stamped events without repeated records.

| Contract | Research-stage design / implementation described in the team report |
| --- | --- |
| **Input** | Browser webcam frames, IP camera/RTSP stream, enrollment portraits, worker identifiers, camera settings |
| **Output** | Recognition result/unknown/spoof event, worker/camera/time, attendance log, dashboard summaries, CSV/XLSX |
| **Detection** | YOLO face detector when its model is present; OpenCV Haar fallback |
| **Recognition** | InsightFace/ArcFace embeddings + cosine similarity against registered face gallery; LBP fallback |
| **Safety checks** | Anti-spoofing model via ONNX when available or a weaker heuristic fallback; event deduplication (report default 20 seconds) |
| **Engineering** | Python, OpenCV, ONNX Runtime, FastAPI, SQLite, browser dashboard, local/LAN service |
| **Target environment** | Local PC/laptop service with LAN cameras; Raspberry Pi/edge quantization discussed as future deployment |

**Pipeline.** Camera/webcam → extract frame → detect face → recognize registered identity → anti-spoof/deduplicate → attendance database → dashboard and reports.

**Architectural constraints and trade-offs.**
- Edge-first aspirations do not mean a Raspberry Pi deployment was proven; the report describes an **MVP on a local PC/laptop**, with physical edge deployment an extension.
- A pretrained ArcFace model is distinct from training a facial-recognition model from scratch. The team described embedding-gallery enrollment and threshold matching.
- The report says the **main image-recognition path selects the largest face** for embedding. Multi-camera input support does **not** establish full multi-face attendance for every person in a crowded frame.
- Model-dependent and heuristic fallback modes are **not performance-equivalent**; the fallback must be explicitly signaled in tests, especially for anti-spoofing.
- Biometric enrollment and snapshots require informed permission, restricted retention/access, encryption/security controls and practical withdrawal/deletion procedures.

**Report-described outcome.** Employee and camera management, portrait enrollment, webcam/RTSP input, face-recognition workflow, spoof/unknown event logging, deduplication, SQLite event history and CSV/XLSX reporting were described as tested in the course environment. **This review did not rerun the original ZIP or independently validate hardware/device tests.**

**Not a measured claim.** A slide's **80–95%** recognition range was identified by the report itself as an *expectation/target*, **not a validated benchmark**. No verified field-site deployment, FAR/FRR by condition, latency/FPS on Pi 5 or longitudinal operational impact is available here.

**My contribution.** The group report assigns Hoàng to image processing, face detection/recognition, multi-face requirements and threshold/error-reduction work. This is a **documented responsibility**, not an unverified claim of sole code authorship. Commit-level attribution remains pending.

**Next experiments.**
1. Verify the exact source revision against the final group report, then separate ONNX/ArcFace vs fallback test modes.
2. Run end-to-end tests with consenting test faces, unseen identities and spoof materials; report false-accept/false-reject and unknown rates.
3. Handle *every* detected face crop independently in crowded frames, and test camera reconnection, clock/timezone and duplicate-event semantics.
4. Benchmark each stage on the stated hardware; verify encrypted biometric storage, access controls and deletion.
5. Produce a reproducible, non-biometric synthetic demo before any public code release.

## Tiếng Việt — Hồ sơ kỹ thuật

**Bối cảnh:** công trường có nhiều cổng/camera, điểm danh theo ca cần tránh nhập tay, trùng lặp và khó truy vết.

**Bài toán:** nhận frame từ webcam hoặc camera IP/RTSP; phát hiện mặt, đối chiếu người đã đăng ký, đánh dấu unknown/spoof, lưu sự kiện và xuất báo cáo.

**Input → Output:** frame/ảnh đăng ký/mã công nhân/camera → danh tính được nhận dạng (nếu đủ điều kiện), trạng thái ngoại lệ, timestamp, lịch sử SQLite và báo cáo.

**Thiết kế:** YOLO → ArcFace/InsightFace → so khớp cosine với gallery → kiểm tra liveness/anti-spoof → chống ghi trùng → FastAPI + SQLite + dashboard. Khi thiếu mô hình có thể dùng Haar/LBP/heuristic, nhưng **không được coi các chế độ fallback có độ chính xác ngang nhau**.

**Đóng góp cá nhân theo báo cáo nhóm:** Hoàng phụ trách xử lý ảnh, phát hiện/nhận diện, yêu cầu nhiều khuôn mặt và giảm nhận nhầm. Cần đối chiếu commit/source cụ thể trước khi nhận phần lập trình độc lập.

**Kết quả:** báo cáo mô tả MVP hoạt động trong mạng LAN với webcam/camera IP, quản lý công nhân, đăng ký ảnh, logs và xuất CSV/XLSX. **Chưa xác minh lại mã nguồn hoặc triển khai công trường.**

**Giới hạn quan trọng:**
- Mới xử lý **mặt lớn nhất** trên đường nhận diện chính; multi-camera khác với multi-face đầy đủ.
- Raspberry Pi 5, quantization, chạy dài ngày và kiểm chứng hiện trường vẫn là bước tiếp.
- **80–95%** trong slide là mức kỳ vọng, không phải accuracy đã benchmark.
- Không công bố ảnh khuôn mặt, embedding, địa chỉ RTSP, dữ liệu chấm công hoặc nguồn có thông tin sinh trắc.

**Bài học kỹ thuật:** hệ thống CV không dừng ở lựa chọn model; còn phải kiểm soát camera, ngưỡng nhận dạng, trường hợp unknown, fallback, trùng sự kiện và quyền riêng tư.

_Reviewed 2026-10-25. Academic team project; no field-production performance claim._
