# Truong Minh Hoang — AI Engineering & Business Systems Portfolio

[English](#english) · [Tiếng Việt](#tiếng-việt) · [Project case studies](#project-case-studies--hồ-sơ-dự-án)

> Personal portfolio and public-facing case studies. This repository belongs to the personal GitHub account `hoangtm3979`, independently of any company/organization repository.
>
> **Evidence policy:** Academic/group reports, notebook-recorded results, reproducible runs, deployed demonstrations, and commercial outcomes are different kinds of evidence. They are labeled separately. Nothing here asserts that an internal/synthetic result is a production outcome.

## English

I study Artificial Intelligence at the University of Information Technology (VNU-HCM) while drawing on hands-on experience in e-commerce operations, advertising, sourcing, and business analysis. My focus is building AI systems that connect a clearly defined decision problem with data, modeling, evaluation, deployment, and human review.

**Areas:** tabular machine learning, retrieval-augmented systems, NLP/CV, time-series ML, evaluation, API engineering, and learning-stage MLOps (Docker, cloud deployment, monitoring). Cloud proficiency is a development goal, not a claimed production certification.

**How I present work:** business context → objective → inputs/outputs → constraints → baseline → approach → evidence/results → limitations → reproducibility → ownership/contribution.

## Tiếng Việt

Tôi học ngành Trí tuệ nhân tạo tại UIT – ĐHQG TP.HCM, đồng thời có kinh nghiệm thực hành thương mại điện tử, quảng cáo, tìm nguồn hàng và phân tích kinh doanh. Hướng phát triển của tôi là **AI Engineering gắn với bài toán thực tế**: xác định vấn đề, chuẩn hóa dữ liệu, xây mô hình, đánh giá, triển khai và hỗ trợ người ra quyết định.

**Năng lực đang xây dựng:** Machine Learning dữ liệu bảng, RAG, NLP/CV, chuỗi thời gian, đánh giá mô hình, API và MLOps (Docker, cloud, monitoring). Kỹ năng AWS/GCP đang được củng cố; không tự nhận đã vận hành production nếu thiếu log và bằng chứng.

**Cách đọc mỗi đồ án:** bối cảnh → mục tiêu → input/output → ràng buộc → baseline → giải pháp → kết quả và mức độ kiểm chứng → giới hạn → hướng tái lập → đóng góp cá nhân.

## Learning journey / Nhật ký học tập

Alongside featured projects, the [**AI Learning Labs / Nhật ký Colab**](labs/README.md) captures smaller exercises, copied/adapted tutorials, incomplete experiments, and the steps from fundamentals to applied systems. The connected Drive inventory identified 85 notebook-looking entries under `lapnhan81` and 18 under `hoangaegi89`; **all 101 native Colab JSONs plus 2 differently stored notebook files have now been structurally inspected**. These are not 103 distinct finished projects; see [audit classification](labs/REVIEW_QUEUE.md).

**Seven sanitized learning notebooks** are now public, including Python/CSV basics, PCA vectors, toy regression/classification, nonlinear clustering, TensorFlow/MNIST, an MNIST fully connected network, and E-commerce Intent + Expected Value. Start with the [Colab Learning Journey](labs/README.md) and the [complete source audit & release queue](labs/REVIEW_QUEUE.md). Historical outputs were removed; source inventory and publication safety review **are complete for the 103 notebook-looking entries**, while clean replay/reproducibility is a separate unfinished gate.

**Tiếng Việt:** Không chỉ chọn vài đồ án đẹp. Phần nhật ký ghi cả bài cơ bản, bài đang sửa lỗi, phiên bản thử nghiệm và nguồn bài tập có tham khảo tutorial, để người đọc nhìn thấy năng lực phát triển theo thời gian.

## Project case studies / Hồ sơ dự án

| Project / Dự án | Main evidence / Bằng chứng chính | Public case study |
| --- | --- | --- |
| **Credit Risk Modeling** — Logistic + LightGBM | [Executed Colab notebook](https://github.com/hoangtm3979/credit); notebook outputs; independent leakage audit pending | [Bilingual case](projects/credit-risk.md) |
| **SNJ Hybrid RAG Product Advisor** | UIT course report; 376 catalog items; evaluation is small/internal; source review pending | [Bilingual case](projects/snj-hybrid-rag.md) |
| **RegimeLens Financial Market Regimes** — Rolling HMM + XGBoost | UIT Big Data team report; metrics are report-stated, not reproduced here | [Bilingual case](projects/regimelens.md) |
| **Traffic-Law Text + Sign-Image QA** | UIT NLP team report; implementation/deployment verification pending | [Bilingual case](projects/traffic-law-qa.md) |
| **AEGI PAR — Decision Support Demo** | [Existing personal repository](https://github.com/hoangtm3979/aegi-par-demo); local UI test evidence; no claim of real-world prevention effect | [Bilingual case](projects/par-decision-support.md) |
| **Wine Quality ML Benchmark** | UIT ML team report; model comparisons; source and metric replay pending | [Bilingual case](projects/wine-quality.md) |
| **Commercial Problem-Solving** — marketplace operations, vendor dispute, B2B sourcing | Private receipts/email/certificates; public text only, identities redacted | [Bilingual case](projects/business-cases.md) |
| **Multi-Camera Edge Face Attendance / IoT** | Matched five-person UIT final report names Hoàng and the image-processing role; local MVP, not field/Pi benchmark | [Bilingual case](projects/edge-face-attendance.md) |
| **AEGI Shield / Core / Ops** | Internal synthetic/integration evidence; proprietary code/IP not replicated here | **Limited to high-level, non-sensitive discussion in interviews** |

### Review & interview preparation / Rà soát và luyện phỏng vấn

- [Evidence Register / Sổ bằng chứng](EVIDENCE_REGISTER.md): which outputs were inspected, report-only results, what must be reproduced, and publication boundaries.
- [Interview Drill / Bộ câu hỏi đào sâu song ngữ](INTERVIEW_DRILL.md): ML, RAG, financial time series, NLP/CV, PAR, business operations and AWS/GCP deployment questions.

### Evidence labels / Quy ước bằng chứng

- **Executed notebook / Notebook đã chạy:** code and stored outputs exist; may still need re-execution or audit.
- **Reported academic result / Kết quả trong báo cáo môn học:** reported by a course document, not independently reproduced here.
- **Prototype/demo / Bản mẫu:** demonstrates a bounded workflow, not production readiness.
- **Pending verification / Chờ kiểm chứng:** no public metrics or deployment claim.
- **Private supporting evidence / Bằng chứng riêng tư:** can be discussed with appropriate redaction, not uploaded as raw invoices, customer lists, correspondence, or proprietary data.

### Engineering work in progress / Công việc đang tiếp tục

1. Re-run selected academic notebooks with pinned dependencies and a deterministic evaluation protocol; the source inventory is complete, **fresh reruns are not**.
2. Audit target leakage, train/test boundaries, feature timing, and reliability of reported metrics.
3. Release sanitized code/dataset samples only after confirming rights, team contribution, privacy, and intellectual-property boundaries.
4. Add reproducible Docker/API demonstrations, then independent AWS/GCP deployment with cost limits, logging, security, and teardown instructions.
5. Practice explaining each project in English and Vietnamese, including failures and trade-offs.

**Ethics & ownership:** Team projects are identified as team work. Individual authorship is not asserted for unreviewed portions. AEGI intellectual property, pending patent details, customer/contact lists, private billing records, and personal data are intentionally excluded.

---

_Last reviewed: 2026-10-25. This portfolio is an evolving public index, not a claim that all projects are production-ready._
