from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.chooseLanguages import languages
from keyboards.default.mainMenu import main_menu

import sqlite3
from googletrans import Translator
trans = Translator()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    text = f"Salom! Botga xush kelibsiz.\n"
    text += "Botga haftalik dars jadvallaringizni va ogohlantirish vaqtini kiritib qo'ying, "
    text += "so'ngra bot sizga ogohlantirish vaqti bo'yicha kunlik dars jadvalingizni jo'natadi.\n"
    text += "Botning vazifalari haqida to'liqroq ma'lumot olish uchun /help buyrug'ini bosing."

    language = db.select_user(id=message.from_user.id)[4]
    if not language:
        await message.answer("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Choose language\n🇺🇿 Tilni tanlang\n🇷🇺 Выберите язык", reply_markup=languages)
    else:
        await message.answer(text=trans.translate(text=text,dest=language).text, reply_markup=await main_menu(language))
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)