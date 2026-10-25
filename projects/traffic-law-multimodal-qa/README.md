# Multimodal Traffic-Law QA / Hỏi đáp luật giao thông bằng văn bản và hình ảnh

[Tiếng Việt](#tiếng-việt) · [English](#english)

> **DEV_REPLAY_TEXT_ONLY:** đã chạy truy hồi trên train snapshot; ảnh/reranker/generation chưa chạy trong đợt này. [Audit](AUDIT.md).

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

Báo cáo nhóm mô tả thử nghiệm Precision@1 từ **0,72 (TF-IDF)** đến **0,88 (BM25 + Cross-Encoder)**, cùng độ chính xác nhận dạng biển khoảng **92%** trong bộ thử nghiệm được báo cáo. Tôi dành bước rà soát tiếp theo để nối lại phiên bản code, tập dữ liệu và các số đo này.

**Bài học:** đối với chatbot tra cứu quy định, chất lượng không chỉ nằm ở câu trả lời mượt mà; bước tìm đúng văn bản, đúng thời điểm và xử lý trường hợp thiếu căn cứ mới là trọng tâm.

## English

### Problem
Our UIT coursework explored a **Vietnamese traffic-law assistant** combining text retrieval with traffic-sign image analysis.

- **Input:** Vietnamese question or sign photo, regulatory text and sign references.
- **Output:** concise source-linked answer and an identified sign category where relevant.
- **Approach:** text normalization, TF-IDF/BM25, optional reranking, HSV/contours/OCR and a structured sign-to-rule mapping.
- **Constraints:** law revisions, image quality, OCR errors, source traceability and response latency.

The group report lists Precision@1 of **0.72** for TF-IDF and **0.88** for BM25 plus Cross-Encoder, and around **92%** sign-image accuracy on its described tests. The next engineering step is to match those figures to the exact runnable experiment, version the legal corpus and evaluate difficult or unanswered queries.

*UIT group coursework.*


## Mã và kiểm tra mới / Code and new checks

[**Notebook truy hồi có output**](notebooks/01_text_retrieval_baselines.ipynb) · [TF-IDF/BM25 và metric](retrieval_baseline.py) · [Bằng chứng](evidence/text_retrieval_replay.json) · [Audit](AUDIT.md)

Đã tìm lại `Question_Traffic.ipynb` và snapshot VLSP. Notebook lịch sử gồm 105 cells, nhiều lần định nghĩa lại hàm và các thử nghiệm generation lỗi; bản [nghiên cứu lưu trữ](research/traffic-law-rag-exploration.ipynb) giữ quá trình này với output cũ đã bỏ. Không dùng nó để xác nhận lại các số 0,72/0,88/92% trong báo cáo.

Lượt mới tách riêng truy hồi văn bản, không dùng ảnh/choices: **395 cặp luật–điều duy nhất**, **530 câu train có nhãn**. Cả 530 câu đều tham chiếu ảnh; 40 câu có ít nhất một điều liên quan không tồn tại trong snapshot. Những câu này vẫn được giữ trong mẫu số.

| Text-only dev replay | Precision@1 | Recall@5 | MRR@10 |
| --- | ---: | ---: | ---: |
| TF-IDF | 0.107547 | 0.137500 | 0.178912 |
| BM25 | 0.060377 | 0.106336 | 0.116705 |

Kết quả thấp cho thấy baseline chỉ dùng câu chữ chưa đủ trong thiết lập này và cần kiểm tra lại data alignment. Chưa thử ảnh, cross-encoder hay generation; đây không phải điểm đa phương thức hoặc đánh giá trên test độc lập. 5/5 kiểm thử metric/retrieval đạt.

```bash
cd projects/traffic-law-multimodal-qa
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
TRAFFIC_LAW_JSON=/path/to/vlsp2025_law.json TRAFFIC_QUESTIONS_JSON=/path/to/vlsp_2025_train.json python run_notebooks.py --in-place
```

Không đặt biến môi trường: chạy ba văn bản giả lập để kiểm tra phần mềm. Dữ liệu VLSP được giữ ngoài Git; corpus là snapshot cuộc thi, chưa đối chiếu hiệu lực pháp luật hiện tại.

**English:** the new run is a text-only development replay with versioned inputs and correct article-level metrics. It exposes label/corpus mismatches and does not validate the historical cross-encoder, sign-image or generated-answer claims.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
