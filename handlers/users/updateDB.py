from aiogram.types import CallbackQuery

from loader import dp, db, bot
from keyboards.inline.callbackdata import lang_callback
from keyboards.default.mainMenu import main_menu

from googletrans import Translator
trans = Translator()

text = f"Salom! Botga xush kelibsiz.\n"
text += "Botga haftalik dars jadvallaringizni va ogohlantirish vaqtini kiritib qo'ying, "
text += "so'ngra bot sizga ogohlantirish vaqti bo'yicha kunlik dars jadvalingizni jo'natadi.\n"
text += "Botning vazifalari haqida to'liqroq ma'lumot olish uchun /help buyrug'ini bosing."

@dp.callback_query_handler(lang_callback.filter())
async def update_lang(call: CallbackQuery):
    lang = str(call.data)
    lang = lang[lang.index(':')+1:]
    db.update_language(language=lang, id=call.from_user.id)
    await call.message.answer(trans.translate(text,dest=lang).text, reply_markup=await main_menu(lang))