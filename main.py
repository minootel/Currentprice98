import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
import telegram

# دریافت توکن و چت آی‌دی از ENV
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TOKEN)

def get_price():
    url = "https://www.tala.ir"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    try:
        price_tag = soup.find("span", {"id": "l_geram18"})  # طلای ۱۸ عیار
        price = price_tag.text.strip()
    except Exception as e:
        price = "❌ دریافت قیمت ممکن نشد."

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"""
🟡 قیمت طلای ۱۸ عیار:
💰 {price} تومان
⏰ {now}
"""
    return message

while True:
    msg = get_price()
    try:
        bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print("خطا در ارسال پیام:", e)
    time.sleep(60)  # هر ۶۰ ثانیه
