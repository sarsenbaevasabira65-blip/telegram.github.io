Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

load_dotenv()

BOT_TOKEN = os.getenv(8754227384:AAFlaA-7Bq6wVR8wVAOZqUwY86bCjJuJG4k"")
ADMIN_ID = int(os.getenv(1313252587""))
KASPI_NUMBER = os.getenv("+7474513371")
KASPI_NAME = os.getenv("Сабира С")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🔹 Қызметтер
SERVICES = {
    "📸 Фото": "500-1000₸",
    "🎬 Видео": "1000-5000₸",
    "🎨 Анимация": "3000₸",
    "💌 Шақыру": "1500₸",
    "🎤 Дауыс": "500₸",
    "🎵 Ән": "2000₸"
}

# 🔹 Меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
for service in SERVICES:
    menu.add(KeyboardButton(service))


# 🔹 Старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Қызметті таңдаңыз:", reply_markup=menu)


# 🔹 Қызмет таңдау
@dp.message_handler(lambda message: message.text in SERVICES)
async def service_handler(message: types.Message):
    service = message.text
    price = SERVICES[service]
... 
...     text = (
...         f"📌 {service}\n"
...         f"💰 Бағасы: {price}\n\n"
...         f"Төлем жасау үшін:\n"
...         f"Kaspi: {KASPI_NUMBER}\n"
...         f"Аты: {KASPI_NAME}\n\n"
...         f"Төлем жасаған соң чек (скрин) жіберіңіз 📸"
...     )
... 
...     await message.answer(text)
... 
... 
... # 🔹 Скрин қабылдау
... @dp.message_handler(content_types=['photo'])
... async def handle_photo(message: types.Message):
...     user = message.from_user
... 
...     caption = (
...         f"📥 Жаңа төлем!\n"
...         f"👤 @{user.username}\n"
...         f"🆔 {user.id}"
...     )
... 
...     # админге жіберу
...     await bot.send_photo(
...         ADMIN_ID,
...         photo=message.photo[-1].file_id,
...         caption=caption
...     )
... 
...     await message.answer("✅ Қабылданды! Жақында менеджер хабарласады.")
... 
... 
... # 🔹 Қате жағдай
... @dp.message_handler()
... async def fallback(message: types.Message):
...     await message.answer("❗ Менюдан таңдаңыз")
... 
... 
... if __name__ == "__main__":
