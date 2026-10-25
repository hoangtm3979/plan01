# Credit Risk — Source Audit / Đối chiếu mã

The reviewed source is the public personal notebook `Bản_V3_1_deploy.ipynb`. Its historical outputs are retained as claims in the case study, not new validated scores.

| Điểm kiểm tra / Check | Bằng chứng trong mã / Finding | Trạng thái / Status |
| --- | --- | --- |
| Cú pháp / Syntax | Có token thừa sau `except:` ở hàm đổi phần trăm; bản công khai mới đã sửa | FIXED; 13/13 cells parse |
| Điền thiếu / Imputation | `basic_impute` học mode/median riêng trên từng bảng train và holdout | OPEN; dùng train-fitted transformers ở lần chạy tiếp |
| Thời gian / As-of time | Lịch sử tín dụng được tính từ ngày chạy `today`, chưa từ ngày xét hồ sơ | OPEN |
| Nhãn / Outcome | `late`, `default`, `charged off` được gộp; các trạng thái khác thành 0 | OPEN; cần horizon, censoring và thời điểm chốt nhãn |
| Nhánh `default_ind` | Khi dùng cột này làm nhãn, code lịch sử có thể còn giữ nó trong X | OPEN; loại cả nhãn và biến hậu kết quả khỏi đầu vào |
| Đặc trưng / Features | Danh sách loại biến hậu kết quả có sẵn nhưng chưa thay thế feature-availability audit | OPEN |
| Suy luận / Inference | Có export và load artifacts, chưa kiểm tra parity sau một lượt huấn luyện mới | NOT_RUN |
| AUC lịch sử / Saved AUC | Logistic 0.930624; LightGBM 0.935931 | HISTORICAL_OUTPUT; not a new benchmark |

## Cách đọc và tái lập / Reading and reproduction

Notebook dưới `research/` giữ phương pháp lịch sử để có thể giải thích lỗi và quá trình học. Cấu hình `CREDIT_DATA_DIR` phải trỏ đến `loan_2014_18.csv` và `loan_2019_20.csv`; `CREDIT_OUTPUT_DIR` là thư mục output riêng. Dữ liệu khoản vay không được chép vào Git.

Trước khi chạy benchmark tiếp: chốt terminal outcomes và horizon; tạo feature allowlist theo thời điểm; đưa preprocessing vào pipeline; chia development/validation/holdout theo thời gian; khóa cấu hình rồi mới mở holdout. Chưa có số liệu mới cho quy trình này.

**REVISED:** sửa được lỗi cú pháp không có nghĩa đã chứng minh “no leakage”. Cụm đó được bỏ khỏi phần mô tả của bản nguồn mới.
