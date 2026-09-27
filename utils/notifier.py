import os
import requests
import json

class TelegramNotifier:
    _instance = None
    _errors = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TelegramNotifier, cls).__new__(cls)
            cls._errors = []
        return cls._instance

    def add_error(self, test_name, url, detail):
        """Gom nhóm các lỗi phát hiện được trong quá trình test."""
        self._errors.append({
            "test_name": test_name,
            "url": url,
            "detail": detail
        })

    def has_errors(self):
        return len(self._errors) > 0

    def send_report(self):
        """Gửi báo cáo tổng hợp qua Telegram API."""
        bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        
        if not bot_token or not chat_id:
            print("Warning: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not set.")
            return

        message = "<b>🚨 BÁO CÁO LỖI HỆ THỐNG VNEXPRESS 🚨</b>\n\n"
        
        for idx, error in enumerate(self._errors, 1):
            message += f"<b>{idx}. {error['test_name']}</b>\n"
            message += f"🔗 URL: {error['url']}\n"
            message += f"❌ Lỗi: {error['detail']}\n\n"

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print("Đã gửi báo cáo Telegram thành công.")
        except Exception as e:
            print(f"Lỗi khi gửi báo cáo Telegram: {e}")
