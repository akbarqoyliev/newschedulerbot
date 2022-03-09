from aiogram.dispatcher.filters.state import StatesGroup, State

class Schedule(StatesGroup):
    name = State()