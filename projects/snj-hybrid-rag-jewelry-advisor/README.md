# SNJ Hybrid RAG Jewelry Advisor / Hệ thống tư vấn trang sức bằng Hybrid RAG

[Tiếng Việt](#tiếng-việt) · [English](#english)

> **PARTIAL_VERIFICATION:** kiểm tra lexical/rules đã chạy; dense chưa chạy mới, catalog gốc cần xác minh 5 ID lặp. [Audit](AUDIT.md).

## Tiếng Việt

### Bối cảnh và bài toán
Trong kinh doanh đá quý, khách hàng thường mô tả **nhu cầu** hơn là tên sản phẩm chính xác: “đá ruby để làm bông tai”, “vòng vàng cỡ 8 mm” hoặc “vòng cẩm thạch có kiểm định”. Tôi chọn bài toán **hiểu yêu cầu tiếng Việt và tìm đúng nhóm sản phẩm** để nghiên cứu Hybrid RAG.

- **Input:** câu hỏi khách hàng và catalog theo loại sản phẩm, đá, màu, kích thước, trọng lượng, giá, chứng thư và mô tả.
- **Output:** danh sách sản phẩm xếp hạng Top-k, thông tin phù hợp và câu trả lời ngắn dựa trên dữ liệu catalog.
- **Dữ liệu trong báo cáo môn học:** **376 sản phẩm, 22 cột**.
- **Ràng buộc:** phân biệt đá rời với trang sức thành phẩm; xử lý thông tin thiếu, tên đá chuyên ngành, thay đổi giá/tồn kho và truy vấn chưa đủ rõ.

### Phương pháp
Tôi thiết kế chuỗi xử lý theo hướng **intent → lọc danh mục/thuộc tính → kết hợp dense retrieval và TF-IDF → reranking theo quy tắc → diễn giải kết quả**. LLM có thể giúp diễn đạt tự nhiên; quyết định chọn sản phẩm vẫn dựa trên bước truy hồi và điều kiện nghiệp vụ.

Điểm tôi muốn giải quyết là **đúng loại hàng trước, diễn đạt hay sau**. Chẳng hạn, khách cần ruby rời để chế tác không nên nhận một danh sách nhẫn ruby hoàn thiện chỉ vì tên đá trùng nhau.

### Kết quả và hướng cải tiến
Báo cáo đồ án ghi nhận các chỉ số truy hồi đạt **100% trên 9 truy vấn nội bộ đã chọn**, với keyword MRR **1,00**. Quy mô kiểm thử còn nhỏ, nên bước tiếp theo của tôi là lập tập câu hỏi độc lập, so sánh với tìm kiếm mặc định WooCommerce, đo tỷ lệ sai danh mục, latency, tình huống không có kết quả và tính cập nhật của catalog.

## English

### Context
Jewelry shoppers often express purchase intent in natural language rather than matching product titles. The core challenge is retrieving the **right kind of item**—for example, loose ruby stones instead of finished ruby earrings.

- **Input:** Vietnamese buyer query and a structured gemstone/jewelry catalog.
- **Output:** ranked Top-k candidates with relevant metadata and a catalog-grounded answer.
- **Dataset in the course report:** **376 items and 22 columns**.
- **Constraints:** strict product-type matching, missing attributes, specialist terminology, and price/stock freshness.

### Approach and learning
I explored intent routing, category and attribute filters, multilingual semantic search plus TF-IDF, business-aware reranking and optional LLM wording. The main design choice was to separate **product selection** from **response generation**.

The coursework reports **100% keyword-based results on its selected internal queries**, including MRR **1.00**. My next step is a broader held-out query set, ablation against lexical/dense-only search and read-only WooCommerce testing on realistic requests.

*Coursework: UIT Advanced Machine Learning, July 2026.*


## Mã, dữ liệu và lần kiểm tra mới / Code, data and fresh checks

| Thành phần / Component | Trạng thái hiện tại / Current evidence |
| --- | --- |
| [Notebook nguồn Hybrid RAG](research/snj-hybrid-retrieval-coursework.ipynb) | Bản Colab đã lưu mới hơn thay cho bản ZIP có 7 cell hỏng newline; 12 code cells syntax PASS |
| [Notebook truy hồi và ràng buộc](notebooks/01_product_retrieval_and_constraints.ipynb) | Đã chạy; TF-IDF + rules trên 12 sản phẩm giả lập, 6/6 tình huống đạt |
| [Mã truy hồi](retrieval.py) và [parser](domain.py) | Lọc cứng loại hàng, giá, size, chứng thư; không nới điều kiện khi không có kết quả |
| [Kiểm thử](tests/test_constraints.py) | 12/12 PASS, gồm 8ly/8ly5/18ly, giá chưa biết, đá rời so với nhẫn và ID trùng |
| Catalog gốc | Đã đối chiếu 376 dòng × 22 cột; chỉ có **371 product_id khác nhau**, 5 ID lặp cần xác minh; không tự gộp |
| Dense MiniLM / generation / WooCommerce | Chưa chạy mới. Trọng số MiniLM không tải được trong môi trường kiểm tra; không gọi API tạo văn bản hay commerce API |

### Chạy bản chia sẻ / Run the shared example

```bash
cd projects/snj-hybrid-rag-jewelry-advisor
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python run_notebooks.py --in-place
```

Catalog đi kèm là [dữ liệu giả lập](data/sample_catalog.csv), không phản ánh hàng hóa/giá SNJ. Đặt `SNJ_CATALOG_PATH` nếu muốn audit catalog riêng; notebook chỉ lưu tổng số và hash. `CatalogRetriever` yêu cầu ID duy nhất và sẽ từ chối catalog chưa giải quyết trùng ID.

Để thử dense retrieval, cài `requirements-dense.txt`, tải model được ghi trong [AUDIT](AUDIT.md) và đặt `SNJ_DENSE_MODEL_DIR`. Output phải báo `dense_lexical_rules`; mặc định là `lexical_rules`. Hai chế độ dùng trọng số khác nhau, không được gọi kết quả lexical là kết quả dense.

**English:** the current checks establish bounded product-filter behavior on fictional examples, plus a schema audit of the original catalog. They do not reproduce the nine-query historical result or establish multi-turn sales performance. [Detailed audit](AUDIT.md) · [Current evidence](evidence/current_checks.json).


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
