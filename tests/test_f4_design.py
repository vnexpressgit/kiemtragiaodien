import pytest
from playwright.sync_api import Page
import random

BASE_URL = "https://vnexpress.net"

def get_random_article_urls(page: Page, count=3):
    page.goto(BASE_URL)
    links = page.locator(".title-news a").all()
    urls = [link.get_attribute("href") for link in links]
    urls = [url for url in urls if url and "vnexpress.net" in url and "video.vnexpress.net" not in url]
    return random.sample(urls, min(count, len(urls)))

def test_f4_typography_and_design(page: Page, notifier):
    """F4 - Kiểm tra tuân thủ Design System."""
    urls = get_random_article_urls(page, count=2)
    
    for url in urls:
        page.goto(url)
        
        # F4.1: Kiểm tra Font chữ của Tiêu đề (Article Title) - Bắt buộc Merriweather/Georgia
        title_element = page.locator("h1.title-detail")
        if title_element.count() > 0:
            font_family = title_element.evaluate("el => window.getComputedStyle(el).fontFamily").lower()
            if "merriweather" not in font_family and "georgia" not in font_family:
                notifier.add_error("F4.1 - Sai Phông chữ Tiêu đề", url, f"Tiêu đề dùng font '{font_family}', yêu cầu Merriweather/Georgia.")
        
        # F4.2: Kiểm tra Font chữ của Body (Nội dung) - Bắt buộc Arial/Helvetica
        paragraphs = page.locator("article.fck_detail p.Normal").all()
        if paragraphs:
            # Check đoạn đầu để tối ưu
            font_family = paragraphs[0].evaluate("el => window.getComputedStyle(el).fontFamily").lower()
            if "arial" not in font_family and "helvetica" not in font_family and "roboto" not in font_family:
                notifier.add_error("F4.2 - Sai Phông chữ Body", url, f"Nội dung bài viết dùng font '{font_family}', yêu cầu Arial/Helvetica/Roboto.")
        
        # F4.3: Không dùng text-transform: uppercase (Quy tắc Neutral)
        ui_elements = page.locator("nav.main-nav a, .btn").all()
        for el in ui_elements[:10]:
            try:
                text_transform = el.evaluate("el => window.getComputedStyle(el).textTransform")
                if text_transform == "uppercase":
                    notifier.add_error("F4.3 - Vi phạm Tone & Voice", url, "Phát hiện UI Element sử dụng text-transform: uppercase.")
                    break
            except Exception:
                pass
                
        # F4.4: Không lạm dụng Box-shadow (Hệ thống phẳng)
        cards = page.locator(".item-news").all()
        for card in cards[:5]:
            try:
                box_shadow = card.evaluate("el => window.getComputedStyle(el).boxShadow")
                if box_shadow != "none" and box_shadow != "":
                    notifier.add_error("F4.4 - Vi phạm Elevetaion (Box Shadow)", url, f"Khối tin dùng box-shadow: {box_shadow}, yêu cầu flat design.")
                    break
            except Exception:
                pass
