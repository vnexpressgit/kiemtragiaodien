import pytest
import os
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from utils.notifier import TelegramNotifier

@pytest.fixture(scope="session")
def notifier():
    """Khởi tạo Telegram Notifier dùng chung cho toàn bộ session."""
    return TelegramNotifier()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Cấu hình Playwright context."""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """Khởi tạo page với cấu hình tối ưu (chặn tải ảnh, quảng cáo)."""
    page = context.new_page()
    
    # Tối ưu hóa: Chặn tải hình ảnh, font, css không cần thiết, và tracking script
    page.route("**/*", lambda route: route.abort() 
        if route.request.resource_type in ["image", "media", "font"] 
        or "google-analytics" in route.request.url 
        or "ads" in route.request.url
        else route.continue_()
    )
    yield page
    page.close()

def pytest_sessionfinish(session, exitstatus):
    """Gửi report Telegram khi toàn bộ test session kết thúc."""
    notifier = TelegramNotifier()
    if notifier.has_errors():
        notifier.send_report()
