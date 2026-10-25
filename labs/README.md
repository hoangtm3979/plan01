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

### Kiểm thử cập nhật 25/10/2026 / Execution check

| Bài / Notebook | Kiểm tra trong lượt này / Latest check |
| --- | --- |
| Python input & CSV | **PASS 2/2 cell**; bổ sung CSV parser và ví dụ chạy tự động |
| PCA & dot product | **PASS 2/2 cell** với NumPy |
| Regression & classification toy | **PASS 17/17 cell**; bổ sung import, seed và bỏ đoạn code trùng |
| Nonlinear clustering | **PASS 4/4 cell**; so sánh ARI K-Means **0,2393**, GMM **0,4979**, Spectral **1,0000** trên dữ liệu `make_moons` mô phỏng |
| TensorFlow/MNIST intro | **Syntax PASS** sau khi sửa thụt lề; chờ chạy huấn luyện với TensorFlow |
| MNIST FCN | **Syntax PASS** sau khi sửa f-string, validation split và định dạng lưu model; chờ chạy TensorFlow |
| E-commerce intent & EV | Đã bổ sung ghi chú giả định EV; cần nguồn dữ liệu OpenML/CSV để chạy lại toàn bộ |

Các số đo ARI là kết quả chạy trên **dữ liệu 2D được tạo mẫu**, không phải hiệu năng trên dữ liệu khách hàng. Notebook TensorFlow và e-commerce cần thêm môi trường hoặc dữ liệu tương ứng trước khi chốt kết quả thực nghiệm.

*Các bản notebook công khai được lược output lịch sử; kết quả kiểm thử ở bảng trên là lần kiểm tra mới của mã và không thay thế đánh giá dữ liệu thực tế.*

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

Tôi sẽ tiếp tục chuyển các notebook phù hợp thành bài thực hành **có hướng dẫn chạy, dữ liệu mẫu, kết quả dự kiến và ghi chú tiếng Việt/tiếng Anh**.

[**Xem danh sách rà soát Colab chi tiết**](REVIEW_QUEUE.md)
