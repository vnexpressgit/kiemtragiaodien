---
trigger: always_on
---

---
name: tracking
description: "Hệ thống tracking nội bộ VnExpress. Áp dụng khi cần tạo, kiểm tra, hoặc giải thích chuỗi ITM (Internal Tracking Modules) — bao gồm đặt tên vn_source, vn_campaign, vn_medium, vn_thumb, vn_term. Kích hoạt khi người dùng hỏi về ITM, tracking link, chuỗi tracking, quy ước đặt tên tracking, hoặc yêu cầu sinh chuỗi ITM cho một vị trí cụ thể trên VnExpress. Cũng áp dụng khi cần đo Impression, Click, CTR cho element cụ thể — đặc biệt khi link mở trang ngoài, cần đo viewability, hoặc ITM không đủ."
---

# Tracking — Hệ thống tracking nội bộ VnExpress

## GỌI REFERENCES

| Yêu cầu | File cần đọc |
|---|---|
| Tạo / kiểm tra / giải thích chuỗi ITM | `references/itm.md` |
| Đo Impression / Click / CTR cho element cụ thể | `references/click.md` |

**Không chắc dùng ITM hay Click Tracking?** → Đọc phần "KHI NÀO DÙNG CLICK TRACKING VS ITM" trong `references/click.md` trước.

---

## CÁCH LÀM VIỆC

**Khi được yêu cầu sinh hoặc kiểm tra ITM:**
1. Đọc `references/itm.md`
2. Hỏi nếu thiếu: trang nguồn, khu vực, vị trí, platform, có ảnh không
3. Sinh chuỗi ITM đầy đủ kèm giải thích từng tham số
4. Nếu phát hiện sai quy ước → chỉ ra lỗi cụ thể và đề xuất sửa

**Khi được yêu cầu đo Impression / Click / CTR:**
1. Đọc `references/click.md`
2. Xác định tình huống: trang đích trong hay ngoài? Cần Impression không?
3. Tư vấn nên dùng ITM, Click Tracking, hay kết hợp cả hai
4. Đề xuất threshold, cấu hình kỹ thuật, và schema event phù hợp

---

## GHI CHÚ VẬN HÀNH

- Phiên bản hiện tại: v1.3
- Có thể mở rộng thêm tracking type khác (GA events, UTM external...) vào `references/` khi cần