# AI Learning Labs — Google Colab Journey / Nhật ký thực hành AI

[English](#english) · [Tiếng Việt](#tiếng-việt) · [Lab inventory](#verified-sample-inventory--danh-mục-đã-đối-chiếu)

> **Purpose:** show the progression from mathematical/Python foundations to classical ML, deep learning, NLP and applied decision systems. This is **not** a list of production-grade or wholly original projects. Course handouts, tutorials and copied starter notebooks are treated as practice materials.

## English

On **2026-10-25** a read-only inventory of the connected `lapnhan81` Colab folder returned **85 notebook-type entries** (70 named and 15 untitled); the `hoangaegi89` Colab folder returned **18 notebook-type entries** (14 named and 4 untitled). These are **file counts, not unique completed assignments**: some are copied versions or shared across accounts, and folders can contain non-notebook files.

**Structural source inspection is now complete for 101/101 native Colab notebooks and two non-native `.ipynb` files**. Among native files, 52 show execution counters on all code cells, 21 on some cells, 28 none, and 22 have at least one saved error. See [Source audit & release queue](REVIEW_QUEUE.md). This section publishes seven safety-reviewed examples; a historical run counter is not a fresh reproducibility test.

## Tiếng Việt

Tôi giữ lại cả bài tập nhỏ để thể hiện **quá trình học, thử, gặp lỗi, sửa và nâng độ khó**, bên cạnh các project lớn.

Hai thư mục Colab có **85 + 18 mục dạng notebook**, bao gồm bản sao và Untitled, **không phải 103 đồ án độc lập**. Đã đọc cấu trúc mã/đầu ra của **101 notebook Colab gốc và 2 file notebook lưu dạng khác**. Trong 101 bản Colab: 52 bản có dấu chạy ở mọi cell code, 21 chạy một phần, 28 chưa chạy, 22 có ít nhất một output lỗi lưu lại. [Bảng kiểm tra đầy đủ](REVIEW_QUEUE.md) phân biệt nguồn đã đọc và bản chạy tái lập (chưa đạt).

### Learning progression / Tiến trình theo chủ đề

1. **Math & Python:** vectors, dot products, PCA projection, NumPy, Python exercises.
2. **Classical ML:** linear/logistic regression, K-means, decision trees, multi-class classification, Random Forest, XGBoost.
3. **Deep Learning:** TensorFlow basics, MNIST, fully connected neural networks, ANN lab.
4. **NLP:** Vietnamese tokenization (VnCoreNLP), PhoBERT introduction, co-occurrence and transformer experiments.
5. **Applied AI/Decision Systems:** e-commerce purchase-intent prediction + expected-value decisions; credit scoring; SNJ RAG; financial-regime research.
6. **Software engineering & MLOps (next):** clean data contracts, tests, reproducible environments, Docker, monitored cloud API.

## Verified sample inventory / Danh mục đã đối chiếu

| Date | Exercise / Bài tập | Skills | Observed state / Trạng thái quan sát | Public artifact |
| --- | --- | --- | --- | --- |
| 2025-04 | Linear Regression | train/test, MAE/MSE/R² | **Incomplete:** 1/6 code cells executed; stored `FileNotFoundError` for local CSV | Not uploaded / Chưa đưa source |
| 2025-05 | Nonlinear clustering comparison | K-Means vs Spectral vs GMM, circles/moons | 1/4 saved code cells executed; not replayed | [Notebook](notebooks/nonlinear-clustering-comparison.ipynb) |
| 2025-06 | Python interactive input & CSV tuples | loops, input, file upload, parsing | 2/2 saved code cells executed; interactive steps | [Notebook](notebooks/python-input-and-csv-tuples.ipynb) |
| 2025-07 | K-means with Python | clustering, distances | **Incomplete:** 1/9 code cells executed; stored `NameError` | Not uploaded |
| 2025-08 | PCA Mathematics | vectors, dot product, projection | 2/2 code cells show historical execution; outputs removed in public copy | [Notebook](notebooks/pca-dot-product.ipynb) |
| 2025-08 | MNIST Fully Connected Neural Network | TensorFlow FCN, train/test, save/load | 9/9 saved code cells executed, not independently rerun | [Notebook](notebooks/mnist-fully-connected-network.ipynb) |
| 2025-08 | Vietnamese sentiment (UIT-VSFC) | custom Naive Bayes + Logistic OVR | 0/8 saved executions; unavailable private ZIP; [review](notes/uit-vsfc-sentiment.md) | Withheld source |
| 2025-08 | Handwritten MNIST (copy) | FCN, MNIST | 0/9 code cells executed in inspected copy; source provenance needs review | Not uploaded |
| 2025-12 | Logistic Regression practice | scaling, log loss, classification | 13/13 code cells show historical execution; course tutorial attribution (Skills Network) | Not republished due to third-party material |
| 2025-12 | Multi-class Classification | class encodings, One-vs-One | 17/17 code cells show historical execution; assignment text partly tutorial-derived | Not uploaded |
| 2025-12 | Random Forest vs XGBoost | boosted trees, regression metrics | 14/14 code cells show historical execution; not replayed | Not uploaded |
| 2026-04 | NumPy Lab 01 | arrays, vectorized computation | 175/175 code cells show historical execution; 291-cell educational notebook | Not uploaded; source/provenance review |
| 2026-04 | Toy regression & classification | linear regression, logistic, synthetic training data | 18/18 saved code cells executed; not independently rerun | [Notebook](notebooks/regression-classification-toy-lab.ipynb) |
| 2026-04 | Medical image segmentation with U-Net | paired ultrasound/masks, Dice/BinaryIoU | 15/15 saved code cells executed; [privacy/source review](notes/busi-unet.md) | Withheld source and data |
| 2026-04 | Decision Tree (copy) | supervised trees | 0/10 code cells executed in inspected copy | Not uploaded |
| 2026-04 | VnCoreNLP (copy) | Vietnamese NLP tools | 2/2 code cells show historical execution | Not uploaded; origin review |
| 2026-04 | PhoBERT (copy) | Transformer embeddings | 0/6 code cells executed in inspected copy | Not uploaded; origin review |
| 2026-04 | E-commerce Intent + EV | purchase propensity, decision optimization | 17/17 code cells show historical execution; no stored errors noted | [Notebook](notebooks/ecommerce-intent-expected-value.ipynb) |
| 2026-05 | TensorFlow/MNIST Intro | neural networks, training/evaluation | 13/13 code cells show historical execution; output removed | [Notebook](notebooks/tensorflow-mnist-intro.ipynb) |
| 2026-05 | ANN Lab 4.1 | TensorFlow, tabular preprocessing | 29/29 code cells show historical execution; not replayed | Not uploaded |
| 2026-06 | Big Data mode test | market regimes, historical HMM/XGBoost | Source inspected: full-sample HMM fit and price `.bfill()` before split; [REVISED case](../projects/regimelens.md) | Not uploaded: leakage risk/version mismatch |
| 2026-06 | SNJ RAG evolution | dense → strict filter → hybrid retrieval | Multiple versioned notebooks found; separate [case study](../projects/snj-hybrid-rag.md) | Source under IP/data review |

*Note / Lưu ý:* `n/n executed` reflects saved Colab execution counters, **not fresh passing tests**. A notebook can have executed cells and still contain incorrect assumptions, dependency problems, outdated data or hidden errors. All uploaded notebooks were cleaned of historical outputs and Colab metadata; public files therefore open with no stored outputs.

## Why keep failed or incomplete exercises? / Vì sao giữ bài chưa hoàn thiện?

A genuine learning portfolio can show the failure-to-fix path. **Audit summary and source release gates:** [REVIEW_QUEUE.md](REVIEW_QUEUE.md). Examples identified:

- **Linear Regression:** the notebook references a CSV that is absent from its expected Colab path. Fix by recording data provenance, using a stable public dataset, and keeping evaluation code reproducible.
- **K-means:** a historical `NameError` calls for defining and checking execution order/dependencies.
- **Copied tutorials:** explicitly credit teaching material and distinguish personal modifications; do not claim an imported notebook as original work.

**Release policy / Nguyên tắc công khai:** Never bulk-upload private Drive folders. For each lab: identify origin/license → inspect code/data/secrets → reproduce in clean environment → write a small README → publish only the permitted, sanitized artifact.

## Bilingual mini-lab template / Mẫu ghi chú cho từng bài

1. **Context / Bối cảnh:** What concept was I learning? Học khái niệm gì?
2. **Problem / Bài toán:** What should the code solve?
3. **Input → Output:** What exact data and result?
4. **Method / Phương pháp:** Why this algorithm?
5. **Constraints / Ràng buộc:** Data, CPU/GPU, runtime, license.
6. **Result / Kết quả:** Executed, error, not run, or independently reproduced?
7. **Failure & fix / Lỗi và cách sửa:** What changed and why?
8. **Next experiment:** One thing to test next.
9. **Attribution / Nguồn:** Original, adapted from teaching material, or group work?

## Next promotion gates / Khi nào thành project mạnh?

A lab is promoted to a standalone project **only if** its code runs from a fresh clone, its dataset and license are identified, a meaningful baseline and evaluation protocol exist, and the owner can defend design decisions in Vietnamese and English.

_Inventory date: 2026-10-25. No private Colab links, source customer data or proprietary AEGI notebooks are exposed here._
