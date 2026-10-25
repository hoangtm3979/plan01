# U-Net Breast Ultrasound Segmentation — Learning Lab
# Bài thực hành phân đoạn ảnh siêu âm bằng U-Net

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

Trong bài thực hành Deep Learning này, tôi tìm hiểu cách mạng **U-Net phân đoạn vùng quan tâm trên ảnh siêu âm**. Thay vì dự đoán một nhãn cho cả ảnh, mô hình tạo kết quả ở cấp độ pixel.

- **Input:** các cặp ảnh siêu âm và mặt nạ vùng quan tâm (mask).
- **Output:** mask dự đoán, biểu đồ loss và phép đo mức trùng khớp như BinaryIoU/Dice.
- **Phương pháp trong notebook:** chuẩn bị ảnh/mask → chia dữ liệu → U-Net encoder/decoder → Adam và Dice-style loss → threshold mask.
- **Ràng buộc:** căn chỉnh ảnh–mask, nguồn ảnh, chia tập theo bệnh nhân, dữ liệu ít và tài nguyên huấn luyện.

Notebook gốc có lịch sử chạy các cell; dữ liệu BUSI được tham chiếu từ Drive riêng. Tôi muốn chạy lại với cách chia tập rõ ràng, báo cáo Dice/IoU theo ảnh và phân tích những vùng mô hình phân đoạn chưa tốt.

## English

This educational lab helped me understand **pixel-level medical image segmentation** using U-Net.

- **Input:** paired ultrasound images and annotation masks.
- **Output:** predicted masks, training curves and overlap metrics.
- **Method:** custom U-Net blocks, Adam optimization, Dice-style loss, BinaryIoU and thresholded predictions.
- **Focus:** patient-level splitting, image/mask alignment, data provenance, reproducibility and error inspection.

My next step is a clean experimental run using a properly sourced dataset and a consistent evaluation protocol.
