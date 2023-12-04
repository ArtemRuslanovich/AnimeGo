from aiogram.fsm.state import StatesGroup, State

class StatesForm(StatesGroup):
    GET_GENRE = State()
    GET_YEAR = State()

class Selector(StatesGroup):
    FIND_ANIME = State()
    FIND_FILM = State()
    FIND_CARTOON = State()
    FIND_SHOW = State()

