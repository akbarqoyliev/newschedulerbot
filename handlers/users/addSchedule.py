import uuid
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from loader import dp, db, bot
from keyboards.inline.callbackdata import lang_callback
from keyboards.inline.weekDays import week_keyboard
from keyboards.default.mainMenu import main_menu
from states.schedule import Schedule

from uuid import uuid4
from googletrans import Translator
trans = Translator()


@dp.message_handler(text=["➕ Jadval qo'shish","➕ Add a table","➕ Добавить стол"])
async def select_name(msg: Message):
    lang = db.select_user(id=msg.from_user.id)[4]
    await msg.answer(trans.translate("Jadvalga nom bering", dest=lang).text)
    await Schedule.name.set()

@dp.message_handler(state=Schedule.name)
async def set_name(msg: Message, state: FSMContext):
    user = db.select_user(id=msg.from_user.id)
    lang = user[4]
    table_id = str(uuid4())
    db.add_schedule(user_id=msg.from_user.id,table_id=table_id,table_name=msg.text)
    await state.update_data(table_id=table_id)
    await msg.answer(text=trans.translate("Jadval nomi muvoffaqiyatli saqlandi.\nEndi jadvalni to'ldiring!").text, reply_markup=await week_keyboard(lang))
    await state.finish()

# @dp.message_handler(text=[])
# async def send_photo(msg: Message):
#     await msg.answer()