import asyncio
import logging
import sys
import schedule
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from schedule import every
from utils.notification import notification_job
from handlers.start import command_start_handler, command_help_handler, command_back_handler, command_fav_handler
from utils.settings import Settings
from aiogram import F
from aiogram.filters import Command
from Commands.commands import set_commands
from middlewares.dbmiddleware import Dbsession
from handlers.manga import select_manga, search_manga
from callbacks.callback_manga import handle_manga_callback
from callbacks.callback import handle_yes_callback, handle_sub_callback
from handlers.anime import find_anime, select_anime
from handlers import form
from handlers.selecttype import command_select_type_handler
from utils.postgresdata import create_pool
from utils.statesform import StatesForm, Selector

dp = Dispatcher()



async def start_bot(bot: Bot):
    await set_commands(bot)
    pool_connect = await create_pool()
    dp.message.register(command_start_handler, Command(commands=['start']))
    dp.message.register(command_help_handler, Command(commands=['help']))
    dp.message.register(command_back_handler, Command(commands=['back']))
    dp.message.register(command_fav_handler, Command(commands=['fav']))

    #dp.message.register(notification_handler)


    dp.message.register(select_anime, F.text == ('найти'))
    dp.message.register(select_manga, F.text == ('манга'))

    dp.message.register(find_anime, Selector.FIND_ANIME)
    dp.message.register(search_manga, Selector.FIND_MANGA)

    dp.callback_query.register(handle_yes_callback, F.data.startswith('Да'))
    dp.callback_query.register(handle_sub_callback, F.data.startswith('subscribe'))
    dp.callback_query.register(handle_manga_callback, F.data.startswith('add'))


    dp.message.register(command_select_type_handler, F.text == ('Да'))
    dp.message.register(form.command_select_genre_handler, F.text == ('не знаю'))
    dp.message.register(form.command_select_year_handler, StatesForm.GET_GENRE)
    dp.message.register(form.command_show_examples, StatesForm.GET_YEAR)


    

    dp.update.middleware.register(Dbsession(pool_connect))

dp.startup.register(start_bot)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(Settings.bots.bot_token, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)
    every().hour.do(asyncio.run, notification_job)

    while True:
        await dp.loop.run_until_complete(schedule.run_pending())
        await asyncio.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())