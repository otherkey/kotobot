import os
import random
import asyncio
from telegram import Bot

# 🔑 Твой токен и Chat ID
TOKEN = "849307760:AAGkDq_Vr8IioCvNP6esi-AR5qWmvXUu6Wg"
CHAT_ID = -1001492099170  # ← твой chat_id из группы

bot = Bot(token=TOKEN)

async def send_cat():
    cat_files = [f for f in os.listdir(".") if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not cat_files:
        print("Котики не найдены!")
        return

    chosen = random.choice(cat_files)
    with open(chosen, "rb") as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo)
    print("Котик отправлен:", chosen)

# 🚀 Запускаем асинхронную функцию
asyncio.run(send_cat())