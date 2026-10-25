# Breast Ultrasound U-Net Segmentation — Educational Lab Review
# Phân đoạn ảnh siêu âm bằng U-Net — Rà soát bài thực hành

**Evidence:** `LAB6_21540008.ipynb`, retrieved from the owner's Colab folder. 15 code cells carried historical execution counters; the saved notebook required a private `Dataset_BUSI.zip` under a mounted Google Drive folder. This page reports **coursework observations, not a clinically evaluated medical AI tool**.

## English

- **Context:** learn pixel-level image segmentation and the roles of a binary ground-truth mask, encoder–decoder network and overlap metric.
- **Input:** paired breast-ultrasound images and masks after preprocessing/resizing.
- **Output:** predicted segmentation mask, training/validation loss curves, BinaryIoU and representative images for inspection.
- **Method seen in code:** combine image/mask pairs → train/validation/test splitting → custom U-Net blocks → Adam training with Dice-style loss and BinaryIoU tracking → threshold predictions at 0.5.
- **Constraints:** private ZIP and trained `.keras` model not available publicly, data source/license and patient-image sharing permissions require review, performance heavily depends on patient-level splits and mask alignment.
- **Observed status:** educational code with historical executions; **not independently rerun**. No numeric sensitivity/specificity, patient-level generalization or clinical effect is asserted.
- **Required improvements:** verify no same-patient leakage across splits; fix seeds and versions; publish only rights-cleared examples; evaluate Dice + IoU with confidence intervals; assess mask annotation uncertainty and external validation.

## Tiếng Việt

- **Bài toán:** biến ảnh siêu âm đầu vào thành mặt nạ nhị phân vùng quan tâm.
- **Pipeline:** ảnh + mask → tiền xử lý → U-Net → xác suất pixel → ngưỡng → mask → IoU/Dice.
- **Giới hạn:** dữ liệu BUSI đang ở đường dẫn Drive riêng; kết quả trong notebook không tương đương hiệu năng lâm sàng. Cần xét nguồn ảnh, quyền dùng, chia tập theo bệnh nhân, mask chuẩn và tái lập.
- **Tình trạng:** bài học có mã và dấu vết từng chạy, chưa benchmark lại.

**Privacy:** no patient images, private ZIP, original masks, model weights or clinical recommendations were released.
