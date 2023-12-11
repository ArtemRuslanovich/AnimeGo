import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers.start import command_start_handler, command_help_handler
from settings import Settings
from aiogram import F
from aiogram.filters import Command
from Commands.commands import set_commands

from middlewares.dbmiddleware import Dbsession
import asyncpg


from handlers.anime import find_anime, select_anime
from handlers import form
from handlers.selecttype import command_select_type_handler

from Utils.statesform import StatesForm, Selector
#from Utils.isvalidyear import is_valid_year

dp = Dispatcher()


async def create_pool():
    return await asyncpg.create_pool(user='postgres',
                                    password='80156120189fap',
                                    database='Users', host='localhost',
                                    port='5432',
                                    command_timeout=60)



async def start_bot(bot: Bot):
    await set_commands(bot)
    pool_connect = await create_pool()
    dp.message.register(command_start_handler, Command(commands=['start', 'run', 'пошел ты нахуй']))
    dp.message.register(command_help_handler, Command(commands=['help', 'хелп', 'помощь']))


    dp.message.register(select_anime, F.text == ('Знаю что посмотреть'))

    dp.message.register(find_anime, Selector.FIND_ANIME)

    dp.message.register(command_select_type_handler, F.text == ('Да'))
    dp.message.register(form.command_select_genre_handler, F.text == ('Не знаю'))
    dp.message.register(form.command_select_year_handler, StatesForm.GET_GENRE)
    dp.message.register(form.command_show_examples, StatesForm.GET_YEAR)


    

    dp.update.middleware.register(Dbsession(pool_connect))

dp.startup.register(start_bot)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(Settings.bots.bot_token, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())