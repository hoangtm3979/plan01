# Data sources / Nguồn dữ liệu

## Online Shoppers Purchasing Intention

- Creators: C. Sakar and Y. Kastro (2018).
- Official dataset: https://doi.org/10.24432/C5F88Q (UCI dataset 468).
- Official archive: https://archive.ics.uci.edu/static/public/468/online+shoppers+purchasing+intention+dataset.zip
- File: `online_shoppers_intention.csv`, 1,072,063 bytes, 12,330 rows × 18 columns.
- CSV SHA-256: `b3055ee355f59134d851d32641183cb4a8b45def7124d2f50442a042f358e0d9`.
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- The notebook downloads and checks the original CSV, then caches it under `labs/data/`.
  Set `SHOPPERS_CSV` to an existing copy for offline execution. A missing file or checksum
  mismatch raises an error; there is no synthetic-data substitution.

Tôi dùng dữ liệu công khai nguyên bản, chuẩn hóa nhãn, bỏ `PageValues` khỏi X và xem mã
OS/browser/region/traffic là danh mục. UCI mô tả `PageValues` gắn với giá trị giao dịch;
metadata hiện có chưa chứng minh đặc trưng sẵn có tại thời điểm can thiệp. Những đặc trưng
tổng hợp phiên khác cũng cần snapshot theo thời điểm trước khi dùng cho quyết định trực tiếp.

The session data contain no randomized promotion log or precise intervention-time snapshots.
The EV calculation is an assumed scenario, not an estimate of treatment effect or realized profit.

## MNIST

- Original source and attribution: [MNIST handwritten digit database](https://yann.lecun.com/exdb/mnist/),
  Yann LeCun, Corinna Cortes and Christopher J. C. Burges.
- Loader: [Keras MNIST](https://keras.io/api/datasets/mnist/).
- Keras archive: https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
- File SHA-256: `731c5ac602752760c8e48fbffcf8c3b850d9dc2a2aedcf2cc48468fc17b673d1`.
- Official split: 60,000 training images and 10,000 test images. Both notebooks split the
  training portion into 54,000 train / 6,000 validation, stratified with seed 42.
- All images are used; neither run uses a smoke-test subset. The data and generated model
  weights are downloaded/created locally rather than committed.

## Generated examples / Ví dụ tạo mẫu

Python & CSV uses inline sample text. PCA uses explicit vectors. Regression/classification
uses constructed examples and seeded random numbers. Clustering uses scikit-learn
`make_circles` / `make_moons`. These datasets illustrate programming or algorithm behavior;
they do not describe customer, employee or operational outcomes.
