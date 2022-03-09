from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db

from googletrans import Translator
trans = Translator()


async def main_menu(lang):
    menuKeyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=trans.translate("📇 Bugungi jadval", dest=lang).text)
            ],
            [
                KeyboardButton(text=trans.translate("📑 Mening jadvallarim", dest=lang).text)
            ],
            [
                KeyboardButton(text=trans.translate("➕ Jadval qo'shish", dest=lang).text)
            ],
            [
                KeyboardButton(text=trans.translate("⚙️ Sozlamalar", dest=lang).text)
            ],
        ],
        resize_keyboard=True
    )
    return menuKeyboard