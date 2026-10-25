# Multimodal Traffic-Law QA / Chatbot luật giao thông đa phương thức

**Evidence:** Two UIT coursework reports on Drive (NLP and Python for Machine Learning / VLSP 2025-themed project). **Team project.** Code and cloud deployment have not been independently inspected.

## English

**Context:** People often ask questions in Vietnamese or show an image of a traffic sign, yet rules are published as dense legal text.

**Problem:** Retrieve a relevant passage for a natural-language question or interpret visual sign cues and map them to a legal-information answer.

**Input:** a Vietnamese text question (coursework design caps inputs at 512 tokens), or a JPG/PNG traffic-sign image, plus a structured corpus of traffic regulations and sign references.

**Output:** short Vietnamese answer with source reference and, for image requests, a predicted sign type/code and confidence where measurable.

**Approach as described in the reports:**
1. Normalize text/Unicode and optionally tokenize Vietnamese.
2. Rank candidate passages with TF-IDF or BM25; rerank with a bi-/cross-encoder where resources permit.
3. For sign images, inspect HSV color, geometry/contours and OCR tokens.
4. Map a detected sign to a structured knowledge base; package a short, cited answer via API/UI.

**Reported outcomes (not reproduced):** One group report cites Precision@1 **0.72 TF-IDF vs 0.88 BM25 + Cross-Encoder** and sign vision accuracy of about **92%**, with 1.5–2.2 s response time. Some report material uses placeholders/example tables, and no runnable repository or live Cloud Run revision was verified in this review. Treat the figures as **unverified report values**, not deploy/service-level claims.

**Key constraints:** sign ambiguity under blur/lighting, OCR failures, outdated/repealed legal texts, source traceability, latency, differences between classification confidence and legal correctness, and privacy of uploaded photos.

**Next evidence required:** inspect executable notebooks/Dockerfile; pin the exact law corpus and effective dates; independently score labeled examples; show confusion matrix and query split; test abstention when source is missing; verify actual GCP service logs and deployment revision before listing Cloud Run on a résumé.

**Individual contribution:** Named as a member in the group report; precise task ownership requires confirmation from commit history/team records.

## Tiếng Việt

- **Bối cảnh:** người dùng hỏi luật bằng tiếng Việt hoặc đưa ảnh biển báo; nội dung luật khó tra cứu trực tiếp.
- **Bài toán:** kết hợp xử lý ngôn ngữ tự nhiên và thị giác máy tính để truy hồi nguồn luật phù hợp, không tự suy diễn điều khoản.
- **Input:** câu hỏi tiếng Việt/ảnh JPG-PNG + dữ liệu quy định và danh mục biển báo.
- **Output:** câu trả lời ngắn có nguồn; với ảnh là nhãn/loại biển và mô tả kèm mức tin cậy nếu có đo.
- **Phương pháp:** TF-IDF/BM25, reranking; HSV, contour, OCR; ánh xạ biển báo sang văn bản luật.
- **Bằng chứng:** báo cáo nhóm ghi Precision@1 **0,72 → 0,88** và độ chính xác ảnh khoảng **92%**, nhưng chưa đối chiếu với code, dataset và deployment.
- **Ràng buộc:** luật có thể thay đổi, ảnh kém chất lượng, nhiễu OCR, thiếu dữ liệu, latency và căn cứ pháp lý.
- **Bước tiếp:** tái lập metric, sửa các phần báo cáo còn dạng mẫu, xác minh Docker/Cloud Run, kiểm soát phiên bản dữ liệu pháp luật.

**Boundary:** This is an educational retrieval assistant, **not authoritative legal advice**.
