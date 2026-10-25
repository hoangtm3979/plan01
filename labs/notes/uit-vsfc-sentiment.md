# Vietnamese Sentiment Classification (UIT-VSFC) — Learning Note
# Phân loại cảm xúc tiếng Việt — Ghi chú bài tập

**Evidence / Bằng chứng:** private student notebook `02410008-Truong Minh Hoang.ipynb` (8 code cells inspected; **0 historically executed** in the retrieved file). The notebook references `/mnt/data/UIT-VSFC.zip`, which is **not** bundled with the public portfolio.

## English

- **Context:** classic Vietnamese-language sentiment classification without depending on large language models.
- **Question:** can sparse word features and simple, inspectable classifiers predict sentiment labels?
- **Input:** train/dev/test text-label splits from the UIT-VSFC dataset.
- **Output:** class predictions, accuracy/label metrics, high-confidence error list and class-weight vocabulary explanations.
- **Implementation described in code:** tokenizer → vocabulary → bag-of-words features → custom Multinomial Naive Bayes and one-vs-rest Logistic Regression → hyperparameter selection on dev → final evaluation on test.
- **Constraints:** dataset not included, licensing/label splits need verification; train-only vocabulary, unknown tokens, Vietnamese word segmentation and class imbalance require audit.
- **Observed status:** notebook source read, **not run in this review**; no public accuracy is claimed. Test labels appear in the notebook when constructing the union of class identifiers; before a serious benchmark, define the class list strictly from the training protocol and preserve untouched test data.
- **Next:** obtain permitted dataset, pin preprocessing/tokenizer, run train/dev/test without leakage and report confusion matrix + macro F1 beside majority-class baseline.

## Tiếng Việt

- **Bối cảnh/bài toán:** phân loại cảm xúc câu tiếng Việt bằng ML cổ điển.
- **Input:** tập train/dev/test có câu và nhãn; **Output:** nhãn dự đoán, lỗi sai và từ có trọng số.
- **Cách làm đã thấy trong code:** tách từ, BoW, tự viết MultinomialNB và Logistic OVR, chọn siêu tham số trên dev.
- **Ràng buộc:** chưa công bố dataset, không có log chạy hoàn chỉnh; cần kiểm tra cách tách từ, nhãn lớp, mất cân bằng và chia tập.
- **Kết luận:** bằng chứng là *mã bài tập đã đọc*, **chưa có benchmark tái lập**.

**Disclosure:** no original UIT-VSFC dataset or private Drive URL is published.
