# SNJ Hybrid RAG Jewelry Advisor / Tư vấn trang sức bằng Hybrid RAG

**Evidence / Bằng chứng:** UIT Advanced ML course report (July 2026), `SNJ_RAG_Colab_Demo_HYBRID_RAG.ipynb` named in report; raw dataset/source not published here.

## English case study

**Context:** Jewelry shoppers describe goals rather than fixed product names: “ruby stones for earrings,” “yellow 8 mm bracelet,” or “certified jade bangle.” Keyword matching alone can confuse loose stones with completed rings or different bracelet types.

**Problem:** Given a Vietnamese natural-language request, identify purchase intent and constraints, retrieve eligible products from a catalog, and produce a grounded response.

**Input:** buyer query, catalog fields (type, gemstone, color, size, weight/ct, price, certification and description). The coursework report lists **376 products and 22 columns**.

**Output:** ranked top-k candidate products, relevant metadata, a concise text explanation and an explicit insufficient-information response when needed. LLM paraphrasing is optional; retrieval is responsible for selection.

**Approach:** intent routing → strict category/attribute filtering → multilingual dense embeddings + TF-IDF → rule-aware/business reranking → template-grounded answer or optional Gemini wording.

**Constraints:** prevent loose-stone/finished-jewelry mismatches; do not invent certification, stock, price or properties; avoid showing outdated product details; protect store data; ensure an abstention path.

**Reported evaluation:** The course report states Category Accuracy@k, Top-1/Top-3 keyword match of **100%** and keyword MRR of **1.00** on the selected internal queries. This **does not establish broad generalization**: the test set is small/domain-curated, and no independent WooCommerce A/B test or conversion uplift has been verified.

**Decision and trade-off:** Domain rules can reduce obvious category errors more reliably than extra prompt instructions. Dense retrieval improves semantic matching; keywords preserve rare stone terms and certificate names. However, hard filters can suppress relevant items when metadata is missing.

**Next validation:** audit the catalog and licenses; split held-out queries by user intent; compare default WooCommerce search, dense-only, lexical-only, hybrid with ablations; report Recall@k/MRR, wrong-category rate, abstention accuracy, latency, hallucination rate; test on snj.vn privately before any public sales operation.

**Role:** Identified as the author's individual UIT project in its report. Code and reported metrics still require a clean replay before making production claims.

## Hồ sơ tiếng Việt

- **Bối cảnh:** khách mua đá quý tìm theo ý định, công dụng, màu, size, mệnh hoặc ngân sách; tên sản phẩm có thể không trùng lời hỏi.
- **Bài toán:** hiểu câu hỏi tiếng Việt, lọc đúng nhóm sản phẩm, xếp hạng và phản hồi có căn cứ từ catalog.
- **Input:** truy vấn người mua + thuộc tính sản phẩm. Báo cáo dùng **376 sản phẩm / 22 cột**.
- **Output:** danh sách sản phẩm Top-k và lý do phù hợp; nếu dữ liệu thiếu thì cần từ chối khẳng định.
- **Phương pháp:** phân loại intent, lọc metadata, tìm kiếm dense + TF-IDF, chấm điểm quy tắc nghiệp vụ, tạo câu trả lời theo template hoặc LLM tùy chọn.
- **Ràng buộc:** không lẫn đá rời và trang sức hoàn thiện, không tự suy diễn giá/chứng thư/tồn kho, không thực hiện giao dịch thật khi dữ liệu chưa xác minh.
- **Bằng chứng:** báo cáo môn học ghi các chỉ số 100% trên tập truy vấn chọn lọc. Đây là **thử nghiệm nhỏ**, chưa chứng minh hiệu quả chuyển đổi bán hàng hay triển khai production.
- **Trade-off:** rule giúp giữ đúng nghiệp vụ nhưng có thể quá chặt với dữ liệu thiếu; LLM làm câu trả lời tự nhiên hơn nhưng không được tự thay đổi kết quả retrieval.
- **Bước tiếp:** chạy lại notebook, đối chiếu WordPress/WooCommerce baseline, mở rộng test set độc lập, đo latency và các trường hợp thất bại.

**IP/privacy boundary / Phạm vi công bố:** No live product API credentials, private catalog export or customer conversations are uploaded.
