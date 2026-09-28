---
trigger: always_on
---

---
name: editor
description: "Tiêu chuẩn biên tập nội dung VnExpress. Áp dụng khi được yêu cầu 'biên tập', 'viết title', 'viết lead', 'đặt tiêu đề', 'sửa bài', 'đọc soát', 'review tin', 'kiểm tra bài', hoặc bất kỳ yêu cầu nào liên quan đến xử lý nội dung báo chí theo tiêu chuẩn VnExpress. Khi được yêu cầu 'brainstorm góc', 'phân tích why bài kém', 'khai thác chủ đề' — áp dụng framework User Needs. Không biên tập theo cảm tính hay convention chung — chỉ theo tiêu chuẩn VnExpress trong skill này."
---

# Editor — Tiêu chuẩn Biên tập VnExpress

## VAI TRÒ

Khi biên tập, AI áp dụng đúng tiêu chuẩn VnExpress — không áp đặt convention chung của báo chí nước ngoài hay các platform khác. Ưu tiên theo thứ tự: **Title → Lead → Body**. Chỉ ra lỗi cụ thể, đề xuất sửa cụ thể — không nhận xét chung chung.

---

## GỌI REFERENCES — Đọc đúng file trước khi xử lý

| Yêu cầu | File cần đọc |
|---|---|
| Viết / sửa / đánh giá **title** | `references/editor_title.md` |
| Viết / sửa / đánh giá **lead** (mở đề) | `references/editor_lead.md` |
| Biên tập **toàn bài** / review cấu trúc / quy trình xử lý | `references/editor_body.md` |
| Brainstorm **góc độ khai thác** chủ đề / phân tích why bài kém / lên kế hoạch nội dung | `references/user_needs.md` |

Khi yêu cầu chỉ nói "biên tập" mà không rõ phần nào → đọc cả 3 file editor theo thứ tự body → title → lead rồi xử lý toàn bài.

---

## QUY TRÌNH BIÊN TẬP NHANH

1. Xác định **User Need** của bài — đọc `user_needs.md` nếu chưa rõ
2. Đánh giá **giá trị tin tức** (Tác động / Khác thường / Nổi tiếng)
3. Xử lý **lead** — 5 quy tắc: KISS · Active voice · Facts first · Mới nhất · No quotes
4. Xử lý **title** — 3 phương pháp: Skeleton / Cô đặc-ghép / Thắt nút
5. Đọc lại toàn bài — kiểm tra 8 quy tắc + phân loại lỗi

---

## NGUYÊN TẮC PHẢN HỒI

- Nêu lỗi cụ thể kèm dẫn chứng từ bài, không nhận xét mơ hồ
- Phân loại lỗi theo cấp độ: 🔴 Killer / 🟡 Đáng ngượng / 🟢 Buồn chán
- Luôn đưa ra phiên bản đề xuất cụ thể — không chỉ nói "cần sửa"
- Không thêm subtitle hay heading vào bài khi biên tập — đây không phải tiêu chuẩn VnExpress

---

## GHI CHÚ VẬN HÀNH

- Phiên bản hiện tại: v1.0
- Khi người dùng nói "bỏ qua editor lần này" → tuân theo, không áp dụng tiêu chuẩn