# Intelligent Commerce Chatbot — Context-Aware Sales Decision Intelligence

> **Điểm nổi bật:** Thiết kế trợ lý bán hàng nhiều lượt, ghi nhớ nhu cầu và kiểm tra dữ liệu sản phẩm trước khi đưa ra gợi ý.

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

### Bối cảnh và ý tưởng

Từ kinh nghiệm bán hàng đá quý và vận hành **SNJ**, tôi thấy khách hàng không chỉ hỏi “có mẫu nào?”. Họ có thể hỏi theo **loại đá, màu sắc, mệnh, tháng sinh, ngân sách, mục đích sử dụng, kích thước**, rồi đổi điều kiện khi đang trao đổi. Một chatbot chỉ trả lời trôi chảy nhưng gợi ý sai loại sản phẩm hoặc dùng giá/tồn kho cũ vẫn tạo ra trải nghiệm mua hàng kém.

Tôi phát triển hướng **Intelligent Commerce Chatbot / Context-Aware Sales Decision Intelligence** cho `snj.vn`, mở rộng từ [đồ án Hybrid RAG Jewelry Advisor](../snj-hybrid-rag-jewelry-advisor/README.md). Nếu Hybrid RAG tập trung vào **hiểu truy vấn và tìm đúng sản phẩm**, dự án này tập trung vào **quá trình tư vấn liên tục và ra đề xuất phù hợp với ngữ cảnh mua hàng**.

**Trạng thái dự án:** đang thiết kế và phát triển theo hướng **beta nội bộ**. Tôi dùng dữ liệu sản phẩm và các luồng giả lập để hoàn thiện từng thành phần trước khi kết nối chức năng mua hàng thực.

### Input, output và ràng buộc

| Thành phần | Nội dung |
| --- | --- |
| **Input** | Câu hỏi tiếng Việt, lịch sử hội thoại trong phiên, nhu cầu và giới hạn ngân sách; catalog có danh mục, loại đá, thuộc tính, mô tả, giá và tồn kho khi đã xác minh |
| **Input hình ảnh — hướng mở rộng** | Ảnh mẫu sản phẩm để phân tích loại trang sức, màu, kiểu dáng và tìm món tương tự |
| **Output** | Danh sách sản phẩm phù hợp có lý do, câu hỏi bổ sung khi thiếu thông tin, các lựa chọn thay thế và câu trả lời bám catalog |
| **Tác vụ có công cụ — hướng mở rộng** | Tra cứu giá/tồn kho, mở trang sản phẩm, hỗ trợ chuẩn bị giỏ hàng với bước xác nhận phù hợp |

Các yêu cầu nghiệp vụ tôi đặt ra gồm: **phân biệt đá rời và trang sức thành phẩm; không đoán giá hoặc tồn kho; xử lý câu hỏi mơ hồ; kiểm soát thông tin tư vấn phong thủy; bảo vệ dữ liệu hội thoại**. Các thao tác làm thay đổi giỏ hàng hoặc phát sinh giao dịch được tách khỏi luồng trả lời thông tin.

### Kiến trúc tôi đang phát triển

1. **Hiểu ý định và trạng thái phiên:** nhận ra người mua muốn tìm, so sánh, hỏi kiến thức hay thay đổi tiêu chí đã nói trước đó.
2. **Chuẩn hóa thuộc tính:** loại đá, sản phẩm, màu, kích cỡ, mức giá, mục đích tặng/quà và yêu cầu liên quan đến mệnh/tháng sinh.
3. **Tra cứu có kiểm soát:** kết hợp lọc danh mục, tìm kiếm từ khóa và ngữ nghĩa từ phần nghiên cứu Hybrid RAG; trả về sản phẩm có nguồn dữ liệu cụ thể.
4. **Xếp hạng và diễn giải:** ưu tiên mức đáp ứng điều kiện mua hàng, nêu lý do chọn và hỏi thêm khi điều kiện chưa đủ.
5. **Bộ điều phối công cụ:** phân biệt tác vụ chỉ đọc catalog với thao tác cần xác nhận; giữ log quyết định và lỗi để đánh giá.

Tôi xem LLM là một thành phần **hiểu và diễn đạt**, còn catalog, luật lọc sản phẩm và trạng thái xác minh là nguồn điều khiển đề xuất. Nhận dạng ảnh, kết nối trực tiếp WooCommerce và agent thao tác mua hàng nằm trong lộ trình phát triển tiếp theo.

### Cách tôi đánh giá

Tôi dự kiến dựng bộ tình huống theo luồng mua hàng, ví dụ:

- “Tôi cần **ruby rời** để chế tác” → không lẫn nhẫn/bông tai ruby hoàn thiện.
- “Có vòng đá màu xanh trong ngân sách X không?” → trả đúng nhóm, khoảng giá và hỏi thêm nếu thiếu kích cỡ.
- “Mẫu thứ hai còn hàng không?” → hiểu tham chiếu từ lượt nói trước, kiểm tra dữ liệu tồn kho tại nguồn.
- Ảnh không rõ, yêu cầu mâu thuẫn hoặc danh mục không có sản phẩm → hỏi lại hoặc đưa lựa chọn thay thế phù hợp.

Các chỉ số tôi sẽ đo là **độ đúng loại hàng, Recall@K/MRR, tỷ lệ vi phạm thuộc tính bắt buộc, chất lượng hỏi làm rõ, tỷ lệ trả lời có nguồn, latency và chi phí theo lượt**. Đây là các tiêu chí đánh giá để triển khai, chưa phải số liệu benchmark của chatbot mới.

### Điều tôi muốn đào sâu

Khó khăn chính của bài toán không chỉ là chọn model. Tôi cần làm rõ **đối tượng sản phẩm và quan hệ thuộc tính (ontology), bộ nhớ phiên, khi nào dùng retrieval hay rule, kiểm soát hành động có side effect, đánh giá đa lượt**, và sau đó mới xem dữ liệu nào thực sự cần dùng để fine-tune hoặc train thêm.

*Từ nghiên cứu Hybrid RAG tại UIT (2026) đến hệ thống tư vấn bán hàng theo ngữ cảnh trên SNJ · Dự án đang phát triển.*

## English

> **In one sentence:** I design a multi-turn shopping assistant that tracks preferences and checks product data before making recommendations.

### Context and goal

Shoppers describe gemstone purchases through evolving constraints: stone type, jewelry form, color, size, budget, occasion, birth month or Vietnamese feng-shui preferences. A fluent assistant is not useful if it recommends the wrong product category or relies on stale stock and pricing.

I am developing an **Intelligent Commerce Chatbot / Context-Aware Sales Decision Intelligence** concept for **snj.vn**, building on my earlier [Hybrid RAG Jewelry Advisor coursework](../snj-hybrid-rag-jewelry-advisor/README.md). The earlier research focuses on **retrieving the right products**; this project extends the workflow toward **multi-turn, context-sensitive purchase assistance**.

**Current stage:** system design and internal-beta development, using catalog-oriented test cases before any transaction features.

### Inputs, outputs and design constraints

- **Inputs:** Vietnamese queries, in-session context, shopper preferences and a verified catalog with product category, stone attributes, descriptions, pricing and stock.
- **Planned multimodal input:** product reference photos for visual attribute extraction and similar-item discovery.
- **Outputs:** ranked, explainable suggestions; clarifying questions; alternatives; and catalog-grounded responses.
- **Planned tool actions:** read-only price/stock lookup and product navigation, with separate confirmation for cart or checkout operations.

Key constraints include strict separation between loose gemstones and finished jewelry, explicit handling of missing or contradictory requirements, catalog freshness, privacy, and clear authorization for actions that change user state.

### System approach

I am organizing the solution into **intent and session-state tracking → attribute extraction and normalization → hybrid retrieval and category filtering → business-aware ranking → grounded response generation → controlled tool orchestration**.

I use LLMs for language interpretation and explanation, while authoritative catalog records and explicit business rules govern product suggestions. Image understanding, a live WooCommerce connection, and transactional agent actions are later milestones.

### Evaluation plan and learning

I will test multi-turn scenarios such as “I need a loose ruby for custom earrings,” changing budget mid-conversation, asking about “the second item,” checking live inventory and recovering from no-match or unclear-image cases. The evaluation will track **category correctness, Recall@K/MRR, hard-filter violations, clarification quality, grounding, response latency and request cost**.

This project is teaching me how to combine **retrieval, structured business rules, session memory and tool safety** into a practical e-commerce assistant. It also gives me a path for assessing when a specialized model or further training would add measurable value.

*AI/e-commerce application in development · SNJ internal-beta direction, 2026.*


## Hồ sơ triển khai / Implementation record

[Kế hoạch đánh giá nhiều lượt](EVALUATION_PLAN.md) · [12 tình huống có cấu trúc](evaluation_cases.json) · [Nguồn và phạm vi](PROVENANCE.json)

Tôi chia sẻ thiết kế hệ thống và **12 tình huống đánh giá dự kiến** cho phần mở rộng nhiều lượt. Phần mã truy hồi một lượt nằm trong [đồ án SNJ Hybrid RAG](../snj-hybrid-rag-jewelry-advisor/README.md). Bộ nhớ phiên, điều phối công cụ và xử lý ảnh thuộc giai đoạn phát triển tiếp theo.

**English:** this folder contains my system design and 12 planned evaluation scenarios. The single-turn retrieval implementation is available in the SNJ predecessor project; multi-turn runtime evaluation is a later milestone.


---

[Danh mục dự án / Project index](../README.md) · [Portfolio](../../README.md)
