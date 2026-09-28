---
trigger: always_on
---

---
name: product
description: "Công cụ Product cho PM tại VnExpress. Áp dụng khi soạn PRD, đặc tả tính năng, mô tả yêu cầu kỹ thuật, thiết kế luồng UX, review trải nghiệm người dùng, hay bất kỳ công việc nào liên quan đến định nghĩa và mô tả sản phẩm cụ thể. Không cần người dùng nhắc — AI tự nhận diện ngữ cảnh và áp dụng."
---

# Product — Công cụ định nghĩa sản phẩm VnExpress

## GỌI REFERENCES — Đọc đúng file trước khi xử lý

| Yêu cầu | File cần đọc |
|---|---|
| Soạn / cập nhật PRD dưới dạng DOCX (tạo file) | `references/prd-docx.md` + `references/prd.md` |
| Soạn nội dung PRD (không cần file DOCX) | `references/prd.md` |
| Thiết kế UX / mô tả trải nghiệm / review luồng / đánh giá giao diện | `references/ux.md` |

Khi yêu cầu đụng cả hai ("soạn PRD cho tính năng này kèm mô tả UX") → đọc cả `prd.md` và `ux.md`.

**Lần đầu tạo PRD DOCX:** bắt buộc đọc thêm `my-brain/references/style-guide.md` để áp dụng font, màu, bảng đúng chuẩn. Từ lần cập nhật thứ hai: giữ nguyên style hiện có, không đọc lại.

**Cross-references với my-brain:**
- 6 Rõ và framework KPI → `my-brain/references/framework-6-clear.md`
- PR/FAQ và Working Backwards → `my-brain/references/working-backwards.md`

---

## KHI TẠO / CẬP NHẬT PRD DOCX

**Nhận diện tình huống:**

| Người dùng nói | AI làm |
|---|---|
| "Tạo PRD cho tính năng X" | Đọc `prd-docx.md` + `prd.md` + `style-guide.md` → tạo file mới v1.0 |
| "Cập nhật PRD, bổ sung mục Y" | Đọc `prd-docx.md` → nâng version, thêm log, cập nhật nội dung |
| "Đây là PRD cũ, thêm phần Z vào" | Xác định version hiện tại → minor hay major → nâng version, ghi log |
| "Soạn PRD" (không nói DOCX) | Soạn nội dung text, hỏi xem cần xuất DOCX không |

**Quy tắc bất biến khi làm việc với PRD DOCX:**
- Một project = một file duy nhất — không tạo file mới khi cập nhật
- Mỗi lần cập nhật = nâng version + thêm dòng mới vào Change Log
- Tên file theo đúng naming convention: `PRD_{Code}_{ShortName}_v{X.Y}.docx`
- Ngôn ngữ trong PRD: mô tả hành vi và kết quả — không dùng thuật ngữ kỹ thuật

---

## NGUYÊN TẮC LÀM VIỆC

- PRD phải align với 6 Rõ — thiếu bất kỳ mục nào thì chưa đủ để chuyển sang development
- UX decisions đều là quyết định tâm lý — không có "chi tiết không quan trọng"
- Làm ít tính năng nhưng làm thật tốt > làm nhiều tính năng nửa vời
- Bắt đầu từ epicenter, không từ nice-to-have
- Mockup / prototype quan trọng hơn spec chữ — tránh illusion of agreement

---

## GHI CHÚ VẬN HÀNH

- Phiên bản hiện tại: v1.1
- Khi người dùng nói "bỏ qua product skill lần này" → tuân theo