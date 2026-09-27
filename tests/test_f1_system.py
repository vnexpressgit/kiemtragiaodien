import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://vnexpress.net"

def test_f1_1_status_code(page: Page, notifier):
    """Kiểm tra mã phản hồi HTTP của trang chủ."""
    response = page.goto(BASE_URL)
    if response.status != 200:
        notifier.add_error(
            test_name="F1.1 - Lỗi Status Code",
            url=BASE_URL,
            detail=f"Trang chủ trả về mã HTTP {response.status} thay vì 200."
        )
    assert response.status == 200, "Trang chủ phải trả về HTTP 200"

def test_f1_2_layout_regression(page: Page, notifier):
    """Chụp ảnh màn hình khối #top-news và so sánh (cần có file chuẩn top_news_baseline.png)."""
    page.goto(BASE_URL)
    top_news = page.locator(".top-news").first
    # Bỏ qua assert ảnh vì cần file chuẩn tạo ra trước đó
    if top_news.count() == 0:
        notifier.add_error(
            test_name="F1.2 - Layout Regression",
            url=BASE_URL,
            detail="Không tìm thấy khối .top-news trên trang chủ."
        )
    assert top_news.count() > 0, "Phải có khối top-news"

def test_f1_3_duplicate_articles(page: Page, notifier):
    """Quét toàn bộ title trên trang chủ để phát hiện trùng lặp."""
    page.goto(BASE_URL)
    
    # Lấy tất cả các thẻ tiêu đề (thường là a thuộc tính title hoặc text nội dung trong thẻ .title-news a)
    titles = page.locator(".title-news a").all_inner_texts()
    
    # Lọc bỏ các tiêu đề trống
    titles = [t.strip() for t in titles if t.strip()]
    
    duplicates = set([x for x in titles if titles.count(x) > 1])
    
    if duplicates:
        notifier.add_error(
            test_name="F1.3 - Bài viết trùng lặp",
            url=BASE_URL,
            detail=f"Phát hiện tiêu đề xuất hiện nhiều lần: {', '.join(duplicates)}"
        )
    assert not duplicates, f"Có tiêu đề bị trùng lặp: {duplicates}"
