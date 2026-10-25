# PAR — Public Source Reading Guide

| Mục / Entry | Nguồn công khai / Public source | Ý nghĩa / Scope |
| --- | --- | --- |
| UI | [submission_overlay](https://github.com/hoangtm3979/aegi-par-demo/tree/main/submission_overlay) | HTML/CSS/JS, interaction and request state |
| API acceptance | [acceptance/ui12_api.py](https://github.com/hoangtm3979/aegi-par-demo/blob/main/acceptance/ui12_api.py) | Defined demo API cases |
| Browser acceptance | [acceptance/ui12_browser.py](https://github.com/hoangtm3979/aegi-par-demo/blob/main/acceptance/ui12_browser.py) | Defined browser/UI scenarios |
| Release manifest | [UI_RELEASE.json](https://github.com/hoangtm3979/aegi-par-demo/blob/main/UI_RELEASE.json) | UI 1.1 release and historical deployment acceptance |
| Production evidence | [PRODUCTION_ACCEPTANCE_UI_1.1.md](https://github.com/hoangtm3979/aegi-par-demo/blob/main/PRODUCTION_ACCEPTANCE_UI_1.1.md) | External smoke recorded on 25 September 2026 |
| Scope | [AUTHORITY_FREEZE_20260925.md](https://github.com/hoangtm3979/aegi-par-demo/blob/main/AUTHORITY_FREEZE_20260925.md) | Backend identity and bounded offline-evaluation claims |

For source review: follow scenario selection → request creation → pending/upload state → response acceptance → reset/cancellation. Check that a late response cannot overwrite a new case and that deletion is confirmed only after API success.

The public repo is the canonical code location; this portfolio does not duplicate proprietary backend sources. No installation, deployment, live mutation, fresh 40-case run or user-effectiveness study was performed in the portfolio review. The historical acceptance commit is `6136c4b19db235c47d4a7cbe588f1e4b714e0364`; UI 1.2 frontend files in the repository should not be inferred to have identical deployment acceptance without their own evidence.
