from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


languages = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ English', callback_data='language:en')
        ],
        [
            InlineKeyboardButton("๐บ๐ฟ O'zbek", callback_data='language:uz')
        ],
        [
            InlineKeyboardButton("๐ท๐บ ะ ัััะบะธะน", callback_data='language:ru')
        ]
    ])