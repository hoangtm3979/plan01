# Multimodal Traffic-Law QA / Hỏi đáp luật giao thông bằng văn bản và hình ảnh

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
