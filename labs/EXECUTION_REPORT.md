# Notebook execution / Kết quả chạy notebook

Ngày 25/10/2026, tôi chạy lại **7/7 notebook, 49/49 code cell** từ đầu. Mỗi bài dùng
một IPython kernel mới trong một tiến trình Python riêng. Output, biểu đồ và metric
trong các notebook là kết quả của lượt chạy này.

All seven notebooks executed successfully, including the complete public MNIST and
Online Shoppers datasets. The result means that the cells and embedded checks passed;
it does not establish production readiness or business impact.

## Results / Kết quả

| Notebook | Code cells | Result |
| --- | ---: | --- |
| [Python input & CSV](notebooks/python-input-and-csv-tuples.ipynb) | 3/3 PASS | Uppercase example, quoted CSV/BOM, sorting and invalid-value rejection |
| [PCA & dot product](notebooks/pca-dot-product.ipynb) | 2/2 PASS | Unit-vector projection 3.5355339059; approximate direction 3.535 |
| [Regression & classification](notebooks/regression-classification-toy-lab.ipynb) | 18/18 PASS | Housing R² 0.991486; revenue R² 0.975898; three toy classification examples run |
| [Nonlinear clustering](notebooks/nonlinear-clustering-comparison.ipynb) | 4/4 PASS | Moons ARI: K-Means 0.239339, GMM 0.497933, Spectral 1.000000 |
| [TensorFlow MNIST intro](notebooks/tensorflow-mnist-intro.ipynb) | 6/6 PASS | Test accuracy **97.14%**, loss 0.094808; 5 epochs |
| [MNIST fully connected](notebooks/mnist-fully-connected-network.ipynb) | 8/8 PASS | Test accuracy **97.72%**, loss 0.080735; 10 epochs; reload max absolute probability difference **0.0** |
| [E-commerce intent & EV](notebooks/ecommerce-intent-expected-value.ipynb) | 8/8 PASS | Random Forest; test ROC-AUC **0.757777**, AP **0.355999**, log loss **0.371005**, Brier **0.115860** |

MNIST uses 54,000 training / 6,000 validation / 10,000 test images in each notebook,
with seed 42 and batch size 128. The two architectures and epoch counts were fixed
before the test results were inspected. The FCN reload check compares all 10,000
test probability vectors at `atol=1e-7, rtol=1e-6`.

E-commerce uses 12,330 rows split 7,398 / 2,466 / 2,466. Validation log loss selects
the model before the test scores are evaluated. The training-prior baseline has test
ROC-AUC 0.5, AP 0.154907, log loss 0.431127 and Brier 0.130911.

## What changed / Những điểm tôi đã sửa

- **Python:** kiểm tra số hữu hạn, header sau dòng trống, UTF-8 BOM và dấu phẩy trong tên có quote.
- **PCA:** phân biệt hướng xấp xỉ với vector đơn vị; làm rõ ví dụ phép chiếu và bước trừ trung bình của PCA.
- **Regression/classification:** giữ năm ví dụ học tập, ghi metric vào kết quả tổng hợp và kiểm tra đầu ra hữu hạn.
- **Clustering:** cố định `n_init`, sửa tên dữ liệu hai vầng trăng, ghi ARI cho cả ba thuật toán.
- **MNIST:** chuẩn hóa float32; tách validation từ train; seed và CPU settings; chạy đủ dữ liệu;
  dùng dataset batching, lưu `.keras` và kiểm tra dự đoán sau tải lại.
- **E-commerce:** thay nguồn OpenML không chạy được bằng archive UCI có cache/checksum; kiểm tra schema;
  coi mã danh mục là categorical; bỏ PageValues; fit preprocessing riêng trên train; thêm prior baseline;
  bỏ class weighting và chọn theo validation log loss; bổ sung calibration và độ nhạy giả định EV.

## Interpreting the EV calculation / Cách đọc kết quả EV

Trong kịch bản gốc, EV trung bình của rule là 7.234902; EV của policy chọn giá trị lớn nhất
là 8.079576, chênh 0.844675 đơn vị tiền giả định trên mỗi phiên. Policy này được chọn bằng
chính công thức dùng để chấm, nên điểm cao hơn là tính chất của phép tối ưu.

Khi giữ policy cố định nhưng đặt uplift thật trong kịch bản bằng 0, EV của policy giảm còn
7.657694, thấp hơn no-action 7.922870. Ví dụ này cho thấy quyết định phụ thuộc vào giả định.
Dữ liệu không có randomized treatment logs; xác suất lịch sử cũng chưa được xác nhận là
xác suất khi không can thiệp. **Chưa có kết luận về causal uplift hoặc lợi nhuận thực tế.**

The offline data lack intervention-time snapshots. PageValues is excluded conservatively,
but the availability of other session aggregates still needs to be established before an
in-session deployment. Random-split metrics do not measure future-time performance.

## Reproduce / Chạy lại

Tested: Linux CPU, CPython 3.12.14, TensorFlow CPU 2.21.0, Keras 3.15.1. Exact direct
dependency versions are in [requirements](requirements.txt) and
[TensorFlow requirements](requirements-tensorflow.txt). Installation should be done in a
separate Python 3.12 environment; full transitive dependency locking has not been added.

From the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r labs/requirements-tensorflow.txt
python labs/run_notebooks.py
```

The default command writes fresh outputs to `labs/executed/` and a report to
`labs/validation/latest.json`. To reproduce the published execution files:

```bash
python labs/run_notebooks.py --in-place --report labs/validation/execution-results.json
```

Run one notebook by its stem, for example:

```bash
python labs/run_notebooks.py ecommerce-intent-expected-value
```

The runner uses `ipykernel.inprocess` inside a separate OS process for each notebook.
This avoids local sockets, which were unavailable in the execution environment, while
executing the actual IPython cells and collecting their standard notebook outputs.
The default worker timeout is 600 seconds per notebook. A failed run returns a nonzero
exit code and saves its notebook under `labs/executed/`; it does not replace the source
notebook with failed outputs. TensorFlow was run on CPU; no GPU run was performed.

The original image/CSV downloads require network access on the first run. Cached copies
support later offline runs. See [data provenance and checksums](DATA_SOURCES.md).

## Evidence and status / Bằng chứng và trạng thái

- [Machine-readable execution results](validation/execution-results.json): environment, timestamps,
  cell counts, model metrics, notebook source fingerprints and executed-file SHA-256 hashes.
- [Executed notebooks](notebooks/): actual text/table/plot outputs from the successful run.
- **SUPERSEDED:** trạng thái “4/7 đã chạy, 2 syntax-only, 1 chờ dữ liệu” được thay bằng **7/7 đã chạy**.
  Hai lượt chạy đầy đủ trên môi trường này cho cùng metric; thời gian chạy và byte của output
  có thể thay đổi. Điều này chưa chứng minh tính tái lập giữa mọi phần cứng/phiên bản thư viện.
- **STILL VALID:** các bài toy và EV có giới hạn dữ liệu/giả định đã ghi trong từng notebook.
- **Scope:** đợt này hoàn thiện bảy bài hiện có. Danh mục 103 mục Colab cũ vẫn là công việc
  kiểm kê và lựa chọn tiếp theo; các dự án lớn có trạng thái riêng trong case study.
