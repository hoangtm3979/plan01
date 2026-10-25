# Vietnamese Sentiment Classification — UIT-VSFC
# Phân loại cảm xúc tiếng Việt bằng Machine Learning

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

Tôi thực hành bài toán **phân loại cảm xúc của câu tiếng Việt** bằng những phương pháp ML cổ điển, nhằm hiểu rõ cách biểu diễn từ ngữ trước khi phụ thuộc vào mô hình ngôn ngữ lớn.

- **Input:** văn bản và nhãn từ các tập train/dev/test UIT-VSFC.
- **Output:** nhãn cảm xúc dự đoán, bảng đánh giá và ví dụ sai.
- **Cách làm trong notebook:** tokenizer → vocabulary → Bag-of-Words → tự xây Multinomial Naive Bayes và Logistic Regression One-vs-Rest → chọn tham số trên dev.
- **Ràng buộc:** cách tách từ tiếng Việt, từ ngoài từ điển, mất cân bằng nhãn, thứ tự chia tập và dữ liệu đầu vào.

Bản notebook lưu trên Drive chứa mã triển khai nhưng không có kết quả chạy lưu lại. Tôi sẽ nối bộ dữ liệu có quyền sử dụng, chạy từ đầu và so sánh với majority baseline, confusion matrix và Macro F1.

## English

This learning exercise explores **Vietnamese sentiment classification** with sparse Bag-of-Words features and transparent classical models.

- **Input:** UIT-VSFC train/dev/test texts and labels.
- **Output:** class predictions, error examples and evaluation metrics.
- **Implementation:** tokenization, vocabulary, custom Multinomial Naive Bayes and One-vs-Rest Logistic Regression, tuned on a development split.
- **Focus:** tokenization, class imbalance, train-only vocabulary and robust evaluation.

The archived notebook contains the implementation structure; my next experiment is to reconnect a permitted dataset and establish a reproducible baseline.
