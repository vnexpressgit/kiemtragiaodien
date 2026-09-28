import pytest
from playwright.sync_api import Page
import random

BASE_URL = "https://vnexpress.net"

# Bảng Scale theo DESIGN.md (mục 5.2 & 5.3)
ALLOWED_SPACINGS = {
    "0px", "2px", "4px", "8px", "12px", 
    "16px", "20px", "24px", "32px", 
    "40px", "48px", "56px", "64px", "80px"
}

ALLOWED_RADII = {
    "0px", "2px", "4px", "8px", "12px", "360px", "50%"
}

def get_random_article_urls(page: Page, count=2):
    page.goto(BASE_URL)
    links = page.locator(".title-news a").all()
    urls = [link.get_attribute("href") for link in links]
    urls = [url for url in urls if url and "vnexpress.net" in url and "video.vnexpress.net" not in url]
    return random.sample(urls, min(count, len(urls)))

def test_f5_1_spacing_scale(page: Page, notifier):
    """F5.1 - Kiểm tra quy tắc Margin & Padding (Spacing Scale)."""
    urls = get_random_article_urls(page, count=1)
    
    for url in urls:
        page.goto(url)
        
        # Quét thử các khối container tiêu biểu
        elements = page.locator(".item-news, .sidebar-1, .header, article.fck_detail p").all()
        
        for el in elements[:15]:  # Giới hạn số lượng check để tối ưu
            try:
                styles = el.evaluate("el => window.getComputedStyle(el)")
                margin_top = styles.get("marginTop")
                margin_bottom = styles.get("marginBottom")
                padding_top = styles.get("paddingTop")
                
                # Check nếu có giá trị ngoài bảng spacing (bỏ qua giá trị auto)
                for val, prop in [(margin_top, "margin-top"), (margin_bottom, "margin-bottom"), (padding_top, "padding-top")]:
                    if val and val != "0px" and val != "auto" and val not in ALLOWED_SPACINGS:
                        # Ghi nhận lỗi nếu giá trị đo được khác biệt hệ thống Design (ví dụ 10px, 15px)
                        notifier.add_error(
                            "F5.1 - Sai Spacing Scale", 
                            url, 
                            f"Phát hiện phần tử có {prop} = {val}, không nằm trong bảng Spacing chuẩn (4, 8, 12, 16, 24, 32...)."
                        )
                        break
            except Exception:
                pass

def test_f5_2_border_radius(page: Page, notifier):
    """F5.2 - Kiểm tra độ bo góc (Border Radius Scale)."""
    page.goto(BASE_URL)
    
    # Quét các nút bấm, ảnh đại diện, input
    ui_elements = page.locator("img, button, .btn, input").all()
    
    for el in ui_elements[:15]:
        try:
            radius = el.evaluate("el => window.getComputedStyle(el).borderRadius")
            # Border radius CSS thường trả về ví dụ "4px" hoặc "4px 4px 0px 0px"
            # Cần tách ra để check từng góc
            corners = radius.split(" ")
            
            for corner in corners:
                if corner and corner != "0px" and corner not in ALLOWED_RADII:
                    notifier.add_error(
                        "F5.2 - Sai Border Radius", 
                        BASE_URL, 
                        f"Phát hiện border-radius = {corner} (không thuộc hệ quy chuẩn 0, 2, 4, 8, 12, 360px)."
                    )
                    break
        except Exception:
            pass

def test_f5_3_divider_usage(page: Page, notifier):
    """F5.3 - Phân tích việc sử dụng Divider thay vì Whitespace."""
    page.goto(BASE_URL)
    
    # Check các đường kẻ phân cách có tuân thủ 1px hoặc 2px không
    borders = page.locator(".item-news").all()
    for el in borders[:10]:
        try:
            border_bottom = el.evaluate("el => window.getComputedStyle(el).borderBottomWidth")
            if border_bottom not in ["0px", "1px", "2px"]:
                notifier.add_error(
                    "F5.3 - Sai độ dày Divider", 
                    BASE_URL, 
                    f"Đường line phân cách dày {border_bottom}, yêu cầu chỉ dùng 1px (Regular) hoặc 2px (Strong)."
                )
                break
        except Exception:
            pass
