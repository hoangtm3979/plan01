# SNJ Hybrid RAG Jewelry Advisor / Hệ thống tư vấn trang sức bằng Hybrid RAG

[Tiếng Việt](#tiếng-việt) · [English](#english)

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
Báo cáo đồ án ghi nhận các chỉ số truy hồi đạt **100% trên nhóm truy vấn thử nghiệm đã chọn**, với keyword MRR **1,00**. Quy mô kiểm thử còn nhỏ, nên bước tiếp theo của tôi là lập tập câu hỏi độc lập, so sánh với tìm kiếm mặc định WooCommerce, đo tỷ lệ sai danh mục, latency, tình huống không có kết quả và tính cập nhật của catalog.

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
