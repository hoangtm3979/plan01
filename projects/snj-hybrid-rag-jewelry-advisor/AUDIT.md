# SNJ — Retrieval Audit / Đối chiếu truy hồi

## Nguồn và phiên bản / Source versions

- Bản ZIP đồ án có notebook Hybrid RAG bị lỗi literal `\n` trong 7 cells.
- Bản Colab/Drive mới hơn có cùng luồng 26 cells, cú pháp đúng và output lịch sử. Đây là nguồn được đưa vào `research/`, sau khi bỏ output và cấu hình riêng.
- Mã `src/rag_engine.py` trong ZIP là bản nhỏ hơn; Streamlit cũ còn là giao diện nháp. Bản module hiện tại được tách từ logic notebook, có thay đổi được khai báo bên dưới. Chưa có xác nhận end-to-end cho Streamlit/LLM.

## Thay đổi hiện tại / Current changes

1. Giữ parser intent của notebook và bổ sung cách đọc “ruby rời”, đơn vị mm, size thập phân.
2. Ràng buộc bắt buộc được lọc trước ranking; giá chưa xác định không đạt điều kiện ngân sách. Size 8, 8.5, 18 được so riêng. Chứng thư phải có dữ liệu, không suy ra chỉ từ lời yêu cầu.
3. Reindex catalog trước khi dùng ma trận truy hồi để tránh sai hàng. ID trùng bị từ chối.
4. Tie được xếp ổn định theo product_id. No-match trả rỗng, không chọn mặc định sản phẩm khác điều kiện.
5. Không gọi API ngoài; không gắn cam kết đổi trả hoặc công dụng sản phẩm vào template.

Dense mode: `0.40 × normalized_dense + 0.25 × normalized_TF-IDF + 0.30 × rule` (business score hiện 0). Lexical mode: `0.65 × normalized_TF-IDF + 0.30 × rule`. Rule score ở bản module thể hiện các trường yêu cầu đã qua filter; không phải bản tái lập điểm rule cũ. OR chỉ hỗ trợ nhóm thuộc tính phẳng; yêu cầu lồng nhau hoặc mơ hồ cần hỏi lại ở lớp hội thoại.

## Điều đã và chưa xác nhận / Validation scope

12 unit tests và 6 tình huống notebook dùng 12 sản phẩm giả lập. Catalog riêng đã audit: 376 dòng, 22 cột, 371 ID duy nhất; 5 ID trùng không phải các dòng hoàn toàn giống nhau. Cần đối chiếu SKU/variant ở nguồn, không tự bỏ một bản ghi.

Model dự kiến: [Sentence Transformers multilingual MiniLM L12 v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2), revision `e8f8c211226b894fcb81acc59f3b34ba3efd5f42`, embedding 384 chiều. Cấu hình tải được nhưng trọng số bị chặn khi chuyển sang máy chủ lưu model; **fresh dense evaluation NOT_RUN**. Không thay thế bằng model khác để ghi PASS.

100%/MRR 1.00 là số lịch sử trên 9 câu nội bộ với điều kiện keyword “any”, không phải relevance judgments độc lập. Chưa có ablation lexical/dense/hybrid trên cùng tập query holdout, chưa đánh giá WooCommerce, multi-turn, p95 latency hoặc sales conversion.
