import pytest
from playwright.sync_api import Page
import random

BASE_URL = "https://vnexpress.net"

def get_random_article_urls(page: Page, count=3):
    page.goto(BASE_URL)
    links = page.locator(".title-news a").all()
    urls = [link.get_attribute("href") for link in links]
    # Lọc các link của vnexpress
    urls = [url for url in urls if url and "vnexpress.net" in url and "video.vnexpress.net" not in url]
    return random.sample(urls, min(count, len(urls)))

def test_f2_editor_rules(page: Page, notifier):
    urls = get_random_article_urls(page)
    
    for url in urls:
        page.goto(url)
        
        # F2.1: Độc lập Title & Lead
        title = page.locator("h1.title-detail").inner_text().strip() if page.locator("h1.title-detail").count() > 0 else ""
        lead = page.locator("p.description").inner_text().strip() if page.locator("p.description").count() > 0 else ""
        
        if title and lead and title == lead:
            notifier.add_error("F2.1 - Trùng lặp Title và Lead", url, "Tiêu đề giống hệt đoạn Sapo.")
            
        # F2.2: Kiểm soát độ dài Lead
        if lead:
            word_count = len(lead.split())
            if word_count > 40:
                notifier.add_error("F2.2 - Sapo dài quá quy định", url, f"Lead dài {word_count} từ, vượt giới hạn 40 từ.")
                
        # F2.3: Quy tắc mở đầu Lead
        if lead and lead.startswith('"'):
            notifier.add_error("F2.3 - Mở đầu Sapo sai quy tắc", url, "Lead bắt đầu bằng dấu ngoặc kép (trích dẫn).")
            
        # F2.4: Cấu trúc Thân bài (Không dùng thẻ h2, h3)
        article_body = page.locator("article.fck_detail")
        if article_body.count() > 0:
            h2_count = article_body.locator("h2").count()
            h3_count = article_body.locator("h3").count()
            if h2_count > 0 or h3_count > 0:
                notifier.add_error("F2.4 - Sai cấu trúc thẻ thân bài", url, f"Phát hiện {h2_count} thẻ h2 và {h3_count} thẻ h3 trong nội dung bài viết.")
                
        # F2.5: Động từ dẫn nguồn
        if article_body.count() > 0:
            body_text = article_body.inner_text().lower()
            banned_words = ["khẳng định", "cáo buộc", "tuyên bố", "chỉ trích", "thú nhận", "thì thầm", "thét lên", "nghẹn ngào"]
            found_words = [word for word in banned_words if word in body_text]
            if found_words:
                notifier.add_error("F2.5 - Lạm dụng động từ mạnh", url, f"Bài viết chứa các từ nên hạn chế: {', '.join(found_words)}.")
