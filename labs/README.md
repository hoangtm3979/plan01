# AI Learning Labs / Nhật ký thực hành AI trên Google Colab

[Tiếng Việt](#tiếng-việt) · [English](#english) · [Notebooks](#notebooks--bài-thực-hành)

## Tiếng Việt

Tôi giữ lại các bài thực hành nhỏ bên cạnh đồ án chính vì chúng cho thấy quá trình học: **nắm khái niệm → tự viết code → thử dữ liệu → gặp lỗi → kiểm tra và cải tiến**.

Các chủ đề đi từ Python/NumPy và đại số tuyến tính đến phân loại, phân cụm, mạng nơ-ron, NLP và bài toán ứng dụng. Một số notebook xuất phát từ bài tập môn học hoặc tutorial; tôi dùng chúng để luyện cách đọc, chỉnh sửa và giải thích code.

Tôi đã rà lại hai thư mục Colab cũ trên Drive, với **103 mục dạng notebook** (bao gồm bản sao và bản nháp). Sau khi xem cấu trúc mã, tôi chọn **7 bài mẫu** để giới thiệu trước. Các bài còn lại được gom theo nhóm chủ đề và lưu [ghi chú nguồn](REVIEW_QUEUE.md), giúp tôi biết bài nào cần chạy lại hoặc tiếp tục học sâu.

### Các mảng đã học và thực hành

1. **Python và toán nền tảng:** biến, vòng lặp, CSV, vector, dot product, NumPy, PCA.
2. **Machine Learning:** Linear/Logistic Regression, cây quyết định, Random Forest, XGBoost, K-Means, GMM và đánh giá mô hình.
3. **Deep Learning:** TensorFlow, MNIST, fully connected network, cấu trúc U-Net.
4. **NLP tiếng Việt:** tiền xử lý, tách từ, BoW, Naive Bayes, Logistic OVR, VnCoreNLP và PhoBERT.
5. **Applied AI:** dự đoán ý định mua hàng và expected value, credit risk, Hybrid RAG và phân tích trạng thái thị trường.

## English

I keep smaller exercises alongside full projects to show **how I learn, experiment, debug and improve**. My Colab work spans Python and mathematical fundamentals, classical machine learning, deep learning, Vietnamese NLP and applied decision modeling.

I reviewed **103 notebook-like archived entries** across two Drive folders, including drafts and copies, and selected **seven representative notebooks** for this public learning journal. The [source review notes](REVIEW_QUEUE.md) track additional labs and topics for future clean reruns.

## Notebooks / Bài thực hành

| Notebook | Tôi luyện tập gì / What I practiced | File |
| --- | --- | --- |
| **Python input & CSV tuples** | Đọc dữ liệu, điều kiện, vòng lặp, xử lý tương tác | [Open](notebooks/python-input-and-csv-tuples.ipynb) |
| **PCA & dot product** | Vector, phép chiếu, nền tảng giảm chiều | [Open](notebooks/pca-dot-product.ipynb) |
| **Regression & classification toy lab** | Hồi quy và phân loại với dữ liệu tạo mẫu | [Open](notebooks/regression-classification-toy-lab.ipynb) |
| **Nonlinear clustering** | So sánh K-Means, Spectral, GMM trên hình dạng cụm | [Open](notebooks/nonlinear-clustering-comparison.ipynb) |
| **TensorFlow / MNIST intro** | TensorFlow, train/test và đánh giá mạng nơ-ron | [Open](notebooks/tensorflow-mnist-intro.ipynb) |
| **MNIST fully connected network** | Cấu trúc FCN, huấn luyện, lưu/tải mô hình | [Open](notebooks/mnist-fully-connected-network.ipynb) |
| **E-commerce intent & expected value** | Kết hợp dự đoán xác suất và quyết định kinh doanh | [Open](notebooks/ecommerce-intent-expected-value.ipynb) |

### Kết quả chạy 25/10/2026 / Execution results

Tôi đã chạy lại **7/7 notebook, 49/49 code cell** từ đầu trong các kernel riêng.
Các file hiện có output và biểu đồ mới, kèm [báo cáo chi tiết](EXECUTION_REPORT.md)
và [kết quả JSON](validation/execution-results.json).

| Bài / Notebook | Code cells | Kết quả / Result |
| --- | ---: | --- |
| Python input & CSV | **3/3 PASS** | Parser, uppercase, CSV có quote/BOM và kiểm tra dữ liệu lỗi |
| PCA & dot product | **2/2 PASS** | Phép chiếu theo vector đơn vị: **3,535534** |
| Regression & classification toy | **18/18 PASS** | Chạy đủ năm ví dụ hồi quy/phân loại trên dữ liệu tạo mẫu |
| Nonlinear clustering | **4/4 PASS** | ARI: K-Means **0,2393**, GMM **0,4979**, Spectral **1,0000** |
| TensorFlow/MNIST intro | **6/6 PASS** | Test accuracy **97,14%**, 5 epochs |
| MNIST FCN | **8/8 PASS** | Test accuracy **97,72%**, 10 epochs; tải lại mô hình giữ nguyên xác suất dự đoán |
| E-commerce intent & EV | **8/8 PASS** | **12.330 phiên UCI**; Random Forest test AUC **0,7578**, AP **0,3560** |

**SUPERSEDED:** bảng cũ “4 bài đã chạy, 2 bài mới kiểm tra syntax, 1 bài chờ dữ liệu”
được thay bằng kết quả trên sau khi cài TensorFlow và lấy được CSV gốc từ UCI.
Các cell được gộp hoặc bổ sung kiểm tra nên số cell khác bản trước.

MNIST dùng đủ dữ liệu chính thức: **54.000 train / 6.000 validation / 10.000 test** cho mỗi bài.
Bài e-commerce chọn mô hình bằng validation log loss; EV là mô phỏng theo giả định,
chưa phải kết quả lợi nhuận hoặc tác động khuyến mãi được đo ngoài thực tế.

All seven notebooks now have fresh execution outputs. MNIST uses the complete dataset;
e-commerce uses the original UCI CSV. Toy metrics and assumed EV scenarios retain the
interpretation limits described in each notebook.

### Cách chạy / Run guide

Môi trường đã kiểm tra: **Linux CPU, Python 3.12.14, TensorFlow CPU 2.21.0**.
Từ thư mục gốc repository, dùng môi trường Python riêng:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r labs/requirements-tensorflow.txt
python labs/run_notebooks.py
```

Lệnh mặc định lưu bản chạy mới ở `labs/executed/` và báo cáo ở `labs/validation/latest.json`.
Thêm `--in-place` nếu muốn cập nhật output vào chính notebook. Cần mạng để tải dữ liệu
lần đầu; lần sau có thể dùng cache hoặc đặt `SHOPPERS_CSV` trỏ đến CSV gốc đã tải.

Có thể mở notebook trong Google Colab và **Run all**. Phiên bản thư viện hoặc phần cứng
khác có thể cho metric hơi khác. [Nguồn dữ liệu và checksum](DATA_SOURCES.md) ·
[Môi trường và toàn bộ cách tái chạy](EXECUTION_REPORT.md#reproduce--chạy-lại).

## Kho bài tập Colab mở rộng / Extended Colab archive

Đã bổ sung [**35 notebook bài tập**](archive/README.md) từ kho nguồn 103 mục, gồm Python, biểu diễn từ, logistic regression, mô hình cây, NLP và deep learning. Bản trùng được gộp và bản nguồn của bảy bài chính được liên kết lại. [Danh mục và trạng thái từng bài](archive/README.md).

## Những bài khác tôi đang hệ thống hóa / Other learning topics

| Chủ đề | Nội dung | Ghi chú |
| --- | --- | --- |
| **Linear Regression, K-Means** | Bài tập đầu giai đoạn, có tình huống thiếu CSV hoặc chạy cell chưa đúng thứ tự | Tôi dùng để ôn cách chuẩn bị dữ liệu, debug và chạy lại |
| **Random Forest, XGBoost, Multiclass** | So sánh mô hình, encoding, One-vs-One và các metric | Tiếp tục gom các ví dụ có thể chạy lại |
| **NumPy, ANN** | Tính toán vector và neural network trên dữ liệu bảng | Kết nối với các bài ML nền tảng |
| **Vietnamese sentiment — UIT-VSFC** | Bag-of-Words, Naive Bayes, Logistic OVR | [Ghi chú kỹ thuật](notes/uit-vsfc-sentiment.md) |
| **U-Net / BUSI ultrasound** | Phân đoạn ảnh và đánh giá IoU/Dice | [Ghi chú kỹ thuật](notes/busi-unet.md) |
| **RegimeLens** | HMM, XGBoost và thử nghiệm chuỗi thời gian | [Case Big Data](../projects/regimelens.md) |
| **SNJ RAG** | Từ dense retrieval đến lọc danh mục và hybrid ranking | [Case RAG](../projects/snj-hybrid-rag.md) |

## Cách tôi ghi chép một bài / My mini-lab template

1. **Context / Bối cảnh:** Tôi đang học hoặc giải quyết điều gì?
2. **Input → Output:** Dữ liệu nào đi vào, kết quả mong đợi là gì?
3. **Method / Phương pháp:** Vì sao chọn thuật toán hoặc cấu trúc code này?
4. **Constraints / Ràng buộc:** Dữ liệu, tài nguyên, thời gian và giới hạn kỹ thuật?
5. **Result / Kết quả:** Tôi chạy ra gì, đo bằng gì?
6. **What I learned / Điều rút ra:** Lỗi, cách sửa và bước thử nghiệm kế tiếp.
7. **Source / Nguồn:** Phần tôi làm, phần tham khảo tutorial hoặc phần thuộc đồ án nhóm.

Tôi tiếp tục dùng cấu trúc này cho các notebook còn lại trong kho Colab. Bảy bài hiện tại đã có hướng dẫn, nguồn dữ liệu, output và kết quả kiểm tra mới.

[**Xem danh sách rà soát Colab chi tiết**](REVIEW_QUEUE.md)

