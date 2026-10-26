# Multimodal Traffic-Law QA / Hỏi đáp luật giao thông bằng văn bản và hình ảnh

> **Điểm nổi bật:** Khám phá cách tra cứu luật giao thông bằng tiếng Việt và hướng kết hợp ảnh biển báo, bắt đầu từ đối chứng truy hồi văn bản.

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

### Bối cảnh và bài toán
Trong đồ án nhóm UIT về NLP và xử lý ảnh, nhóm tìm cách giúp người dùng **tra cứu quy định giao thông bằng câu hỏi tiếng Việt hoặc ảnh biển báo**. Thông tin pháp luật cần được gắn với đúng nguồn và hiệu lực theo thời gian.

- **Input:** câu hỏi tiếng Việt hoặc ảnh biển báo JPG/PNG; văn bản quy định và danh mục biển báo.
- **Output:** đoạn thông tin pháp luật phù hợp, câu trả lời ngắn có dẫn nguồn; với ảnh là loại/mã biển được nhận dạng.
- **Ràng buộc:** ngôn ngữ pháp lý, cập nhật văn bản, ánh sáng/góc chụp, lỗi OCR và thời gian phản hồi.

### Hướng giải quyết
1. Chuẩn hóa tiếng Việt, xây chỉ mục và tìm đoạn liên quan bằng TF-IDF/BM25.
2. Dùng mô hình xếp hạng lại để chọn đoạn phù hợp hơn với câu hỏi.
3. Xử lý màu sắc, đường viền và ký tự của ảnh biển báo bằng HSV, contour và OCR.
4. Liên kết loại biển với kho thông tin để diễn giải kết quả và nguồn tham khảo.

Báo cáo nhóm mô tả thử nghiệm Precision@1 từ **0,72 (TF-IDF)** đến **0,88 (BM25 + Cross-Encoder)**, cùng độ chính xác nhận dạng biển khoảng **92%** trong bộ thử nghiệm được báo cáo. Phần thực hành chia sẻ bên dưới tập trung riêng vào đối chứng truy hồi văn bản.

**Bài học:** đối với chatbot tra cứu quy định, chất lượng không chỉ nằm ở câu trả lời mượt mà; bước tìm đúng văn bản, đúng thời điểm và xử lý trường hợp thiếu căn cứ mới là trọng tâm.

## English

> **In one sentence:** I explore Vietnamese traffic-law lookup and sign-image cues, starting with a separately evaluated text-retrieval baseline.

### Problem
Our UIT coursework explored a **Vietnamese traffic-law assistant** combining text retrieval with traffic-sign image analysis.

- **Input:** Vietnamese question or sign photo, regulatory text and sign references.
- **Output:** concise source-linked answer and an identified sign category where relevant.
- **Approach:** text normalization, TF-IDF/BM25, optional reranking, HSV/contours/OCR and a structured sign-to-rule mapping.
- **Constraints:** law revisions, image quality, OCR errors, source traceability and response latency.

The group report lists Precision@1 of **0.72** for TF-IDF and **0.88** for BM25 plus Cross-Encoder, and around **92%** sign-image accuracy on its described tests. The shared worked example below evaluates the text-retrieval baseline separately, with its own data snapshot and metrics.

*UIT group coursework.*


## Thực nghiệm truy hồi văn bản / Text-retrieval experiment

[**Notebook truy hồi có output**](notebooks/01_text_retrieval_baselines.ipynb) · [TF-IDF/BM25 và metric](retrieval_baseline.py) · [Bằng chứng](evidence/text_retrieval_replay.json) · [Audit](AUDIT.md)

Tôi chia sẻ [notebook nghiên cứu môn học](research/traffic-law-rag-exploration.ipynb) và một notebook riêng để so sánh TF-IDF với BM25 trên snapshot VLSP. Bảng dưới áp dụng cho truy hồi văn bản trên tập development; các kết quả đa phương thức trong báo cáo sử dụng thiết lập khác.

Lượt mới tách riêng truy hồi văn bản, không dùng ảnh/choices: **395 cặp luật–điều duy nhất**, **530 câu train có nhãn**. Cả 530 câu đều tham chiếu ảnh; 40 câu có ít nhất một điều liên quan không tồn tại trong snapshot. Những câu này vẫn được giữ trong mẫu số.

| Text-only dev replay | Precision@1 | Recall@5 | MRR@10 |
| --- | ---: | ---: | ---: |
| TF-IDF | 0.107547 | 0.137500 | 0.178912 |
| BM25 | 0.060377 | 0.106336 | 0.116705 |

Trong thiết lập này, truy hồi chỉ dùng câu chữ còn hạn chế với câu hỏi có ảnh. Tôi dùng đối chứng này để định hướng kết hợp thông tin hình ảnh, xếp hạng lại và đánh giá trên tập độc lập. Bộ mã truy hồi và metric có 5 kiểm thử đã chạy đạt.

```bash
cd projects/traffic-law-multimodal-qa
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
TRAFFIC_LAW_JSON=/path/to/vlsp2025_law.json TRAFFIC_QUESTIONS_JSON=/path/to/vlsp_2025_train.json python run_notebooks.py --in-place
```

Không đặt biến môi trường: chạy ba văn bản giả lập để kiểm tra phần mềm. Dữ liệu VLSP được giữ ngoài Git; corpus là snapshot cuộc thi, chưa đối chiếu hiệu lực pháp luật hiện tại.

**English:** this worked example measures article-level text retrieval on development data. Image processing, reranking and answer generation belong to the broader coursework design and are outside this experiment.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
