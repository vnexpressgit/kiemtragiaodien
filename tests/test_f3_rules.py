import pytest
import re
from playwright.sync_api import Page

BASE_URL = "https://vnexpress.net"

def test_f3_1_datetime_format(page: Page, notifier):
    """F3.1 - Kiểm tra định dạng thời gian."""
    page.goto(BASE_URL)
    # Lấy thử bài viết đầu tiên
    first_article = page.locator(".title-news a").first
    if first_article.count() > 0:
        url = first_article.get_attribute("href")
        if url and "vnexpress.net" in url:
            page.goto(url)
            date_element = page.locator("span.date").first
            if date_element.count() > 0:
                date_text = date_element.inner_text().strip()
                # Pattern mẫu: Thứ hai, 18/9/2023, 10:22 (GMT+7)
                pattern = r"^(Thứ hai|Thứ ba|Thứ tư|Thứ năm|Thứ sáu|Thứ bảy|Chủ nhật), \d{1,2}/\d{1,2}/\d{4}, \d{2}:\d{2} \(GMT\+7\)$"
                if not re.match(pattern, date_text):
                    notifier.add_error("F3.1 - Lỗi Format Thời gian", url, f"Chuỗi thời gian '{date_text}' không đúng chuẩn.")

def test_f3_2_truncation_rules(page: Page, notifier):
    """F3.2 - Quy tắc cắt chữ."""
    page.goto(BASE_URL)
    titles = page.locator(".title-news a").all_inner_texts()
    
    for title in titles:
        if "..." in title:
            notifier.add_error("F3.2 - Lỗi Cắt chữ Title", BASE_URL, f"Title '{title}' chứa dấu '...' không hợp lệ.")
            
    leads = page.locator("p.description a").all_inner_texts()
    for lead in leads:
        if "..." in lead:
            if not lead.endswith("..."):
                notifier.add_error("F3.2 - Lỗi Cắt chữ Sapo", BASE_URL, "Sapo chứa '...' nhưng không nằm ở cuối câu.")
            elif not lead.endswith(" ..."):
                notifier.add_error("F3.2 - Lỗi Cắt chữ Sapo", BASE_URL, "Thiếu khoảng trắng trước dấu '...' ở Sapo.")

def test_f3_3_number_formatting(page: Page, notifier):
    """F3.3 - Định dạng và làm tròn số."""
    # Logic demo, quét các nhãn số lượng comment
    page.goto(BASE_URL)
    comments = page.locator("span.count_cmt").all_inner_texts()
    for comment in comments:
        if comment:
            # Kiểm tra nếu chứa số có hàng nghìn, phải là dấu chấm
            if "," in comment and "M" not in comment and "K" not in comment:
                notifier.add_error("F3.3 - Sai định dạng số", BASE_URL, f"Số lượng '{comment}' dùng sai dấu phân cách.")
                
            # Kiểm tra quy tắc làm tròn (ví dụ chứa M thì chỉ 1 chữ số thập phân)
            if "M" in comment or "K" in comment:
                if "." in comment or "," in comment:
                    # vd: 1,3M
                    decimal_part = re.search(r"[,.](\d+)[MK]", comment)
                    if decimal_part and len(decimal_part.group(1)) > 1:
                        notifier.add_error("F3.3 - Sai làm tròn số", BASE_URL, f"Số lượng '{comment}' làm tròn nhiều hơn 1 chữ số thập phân.")

def test_f3_4_staff_directory_layout(page: Page, notifier):
    """F3.4 - Bố cục trang nhân sự (Giả lập đường dẫn)."""
    # Thay url_staff bằng đường dẫn thật của trang danh bạ tòa soạn
    url_staff = f"{BASE_URL}/toa-soan" 
    response = page.goto(url_staff)
    if response.status == 200:
        container = page.locator(".staff-container")
        if container.count() > 0:
            # CSS max-width & margin auto
            max_width = container.evaluate("el => window.getComputedStyle(el).maxWidth")
            margin = container.evaluate("el => window.getComputedStyle(el).margin")
            
            if max_width != "1200px":
                notifier.add_error("F3.4 - Layout Tòa soạn", url_staff, f"max-width là {max_width}, yêu cầu 1200px.")
            
            # Logic quét 2 item/row và thứ tự BBT, BOD có thể thêm ở đây
