import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncpg
from schedule import every
from datetime import datetime
from bs4 import BeautifulSoup
import aiohttp

DATABASE_URL = "postgresql://postgres:80156120189fap@localhost/Users"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def send_description_message(bot, user_id, anime_url, date):
    # Реализуйте логику отправки сообщения пользователю
    pass

async def process_anime_list_entry(bot, anime_list_entry):
    try:
        anime_list = anime_list_entry['anime_list']

        if anime_list and isinstance(anime_list, list):
            for anime_url in anime_list:
                anime_url = anime_url.replace('_', '-') if anime_url else None
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://animego.org/anime/{anime_url}") as response:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')

                        date_div = soup.find('div', class_='col-6 col-sm-3 col-md-3 col-lg-3 text-right text-truncate')
                        if date_div:
                            date_str = date_div.text.strip()

                            russian_month_names = {
                                'января': 'January',
                                'февраля': 'February',
                                'марта': 'March',
                                'апреля': 'April',
                                'мая': 'May',
                                'июня': 'June',
                                'июля': 'July',
                                'августа': 'August',
                                'сентября': 'September',
                                'октября': 'October',
                                'ноября': 'November',
                                'декабря': 'December'
                            }
                            for russian_month, english_month in russian_month_names.items():
                                date_str = date_str.replace(russian_month, english_month)

                            date = datetime.strptime(date_str, '%d %B %Y')

                            if date.date() == datetime.today().date():
                                anime_url = anime_url.replace('-', '_') if anime_url else None
                                connection = await connect_to_db()
                                query = "SELECT user_id, anime_list FROM usersdata WHERE $1 = ANY(anime_list);"
                                result = await connection.fetch(query, anime_url)

                                for record in result:
                                    user_id, user_anime_list = record['user_id'], record['anime_list']

                                    if anime_url in user_anime_list:
                                        await send_description_message(bot, user_id, anime_url, date)
    except Exception as e:
        logging.exception(f"An error occurred during processing anime list entry: {e}")

async def notification_job():
    try:
        connection = await connect_to_db()
        query = "SELECT anime_list FROM usersdata;"
        result = await connection.fetch(query)

        bot = Bot(token="YOUR_BOT_TOKEN")  # Замените "YOUR_BOT_TOKEN" на реальный токен вашего бота
        tasks = [process_anime_list_entry(bot, anime_list_entry) for anime_list_entry in result]
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
    finally:
        await close_db_connection(connection)