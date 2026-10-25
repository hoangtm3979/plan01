# Research notebooks / Bốn notebook nghiên cứu

Đây là bản đóng gói công khai từ các notebook Colab đã thực thi của KLTN v2.1. Các phép
tính đặc trưng, tập tham số mô hình và 13 tình huống RQ2 được giữ lại. Phần thiết lập
đường dẫn, cài thư viện tùy chọn và mặc định cho một lượt tái lập được điều chỉnh.

| Thứ tự | Notebook | Công việc |
| --- | --- | --- |
| 00 | [Data feasibility](00_DATA_FEASIBILITY_v2_1.ipynb) | Kiểm tra LendingClub, DGraphFin và thiết lập phiên chạy |
| 01 | [Credit outputs](01_CREDIT_OUTPUTS_v2_1.ipynb) | Chia theo tháng, chọn mô hình bằng validation và sinh đầu ra tín dụng |
| 02 | [RQ1 DGraphFin](02_RQ1_DGRAPHFIN_v2_1.ipynb) | Đặc trưng đồ thị, đối chứng LightGBM, đóng băng lựa chọn trước test, đánh giá cuối |
| 03 | [RQ2 context routing](03_RQ2_SHARED_CONTEXT_ROUTING_v2_1.ipynb) | Kiểm tra nguồn dự đoán, ánh xạ, tuân thủ toàn bộ, 13 tình huống và tính xác định |

## Environment and paths

The captured original RQ1 environment was Python 3.13.15, NumPy 2.1.3, LightGBM 4.6.0,
PyTorch 2.11.0+cu128 and PyG 2.8.0.post1. It is recorded in [PROVENANCE.json](../PROVENANCE.json).
The optional [requirements](requirements.txt) follow the original notebook dependency
ranges; they are not a lock of the entire historical environment. Full retraining with
those dependencies has not been repeated as part of publishing this package.

Use a new reproduction workspace. On a local machine, set these environment variables
before opening the notebooks:

```bash
export KLTN_WORKSPACE=/absolute/path/to/kltn_reproduction
export KLTN_CONFIG_POINTER=/absolute/path/to/KLTN_REPRODUCTION_CONFIG_POINTER.json
python -m pip install -r requirements.txt
```

On Colab, the default reproduction directory is
`/content/drive/MyDrive/KLTN_REPRODUCTION_25410008`. The default pointer is
`/content/drive/MyDrive/KLTN_REPRODUCTION_CONFIG_POINTER.json`. The original Drive
experiment directory is not used as the default. Put the two datasets in the paths
described in [DATA.md](../DATA.md) before running all cells.

## Run order

1. Run notebook 00 with `FINAL_MODE=False`, `FINAL_TEST_AUTHORISED=False` and
   `TECHNICAL_RERUN_OVERRIDE=False`. Continue after the data checks pass.
2. Run 01. It fits source models using training/validation data, freezes the choice and
   evaluates the LendingClub holdout.
3. Run 02 in development mode. It selects the two RQ1 models using validation data and
   writes `rq1_freeze_manifest.json` without evaluating the final test labels.
4. Inspect that freeze before the final evaluation. Keep the features, candidate grid,
   seeds and model files fixed. Set the two final flags in 00 to `True`, rerun 00 to
   update its config, then run 02 once in final mode.
5. Run 03 after the required upstream manifests exist. Its last cell writes the final
   experiment lock after checking the available artifacts.

If a final run stops after recording test access, keep its record and use a separately
documented technical rerun; do not silently treat it as a fresh untouched test set.
The original 10,000-resample paired bootstrap and seed-stability runs can take substantial
time. Graph construction and the LightGBM matrices require more RAM than the public demos.

## Packaging and interpretation

Historical Colab outputs and account metadata are omitted from these four notebooks.
Their original file hashes and the public versions are recorded in `PROVENANCE.json`.
The two small [public notebooks](../notebooks/) have fresh execution outputs.

Notebook 00 retains the original exploratory CSV/compression checks, with paths made
configurable. The scientific computations are retained so the package can be compared
with the report; a portable setup and passing syntax checks do not establish a newly
completed full-data training run.
