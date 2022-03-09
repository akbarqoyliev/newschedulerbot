from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from googletrans import Translator
trans = Translator()


async def week_keyboard(lang):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=trans.translate('Dushanba',dest=lang).text, callback_data='week:monday'),
                InlineKeyboardButton(text=trans.translate('Payshanba',dest=lang).text, callback_data='week:thursday'),
            ],
            [
                InlineKeyboardButton(text=trans.translate('Seshanba',dest=lang).text, callback_data='week:tuesday'),
                InlineKeyboardButton(text=trans.translate('Juma',dest=lang).text, callback_data='week:friday'),
            ],
            [
                InlineKeyboardButton(text=trans.translate('Chorshanba',dest=lang).text, callback_data='week:wednesday'),
                InlineKeyboardButton(text=trans.translate('Shanba',dest=lang).text, callback_data='week:saturday'),
            ],
            [
                InlineKeyboardButton(text=trans.translate('Yakshanba',dest=lang).text, callback_data='week:sunday'),
            ],
            [
                InlineKeyboardButton(text=trans.translate('❌ Bekor qilish',dest=lang).text, callback_data='week:cancel'),
            ],
        ]
    )
    return keyboard