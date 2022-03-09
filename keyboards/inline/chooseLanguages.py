from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


languages = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 English', callback_data='language:en')
        ],
        [
            InlineKeyboardButton("🇺🇿 O'zbek", callback_data='language:uz')
        ],
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data='language:ru')
        ]
    ])