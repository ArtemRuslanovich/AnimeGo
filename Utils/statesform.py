from aiogram.fsm.state import StatesGroup, State

class StatesForm(StatesGroup):
    GET_GENRE = State()
    GET_YEAR = State()

class Selector(StatesGroup):
    FIRST_CH = State()
    FIND_ANIME = State()


