import asyncio
from datetime import datetime
from aiogram import Bot
from aiogram.types import Message
from bs4 import BeautifulSoup
import aiohttp
import asyncpg
from aiogram import Bot
from aiogram.enums import ParseMode
from Utils.form.description_parser import description_parser
import logging


logging.basicConfig(level=logging.INFO)

async def notification_handler(message: Message, bot: Bot):
    # Замените эту строку подключения на свою базу данных
    DATABASE_URL = "postgresql://postgres:80156120189fap@localhost/Users"

    async def connect_to_db():
        return await asyncpg.connect(DATABASE_URL)

    async def close_db_connection(connection):
        await connection.close()

    connection = await connect_to_db()

    try:
        # Выполняем SQL-запрос
        query = "SELECT anime_list FROM users;"
        result = await connection.fetch(query)
        
        for anime_url in result:
            anime_url = anime_url['anime_list'].replace('_', '-') if anime_url['anime_list'] else None
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://animego.org/anime/{anime_url}") as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Добавьте код для парсинга даты и других данных о сериях
                    date_str = soup.find('div', class_='col-6 col-sm-3 col-md-3 col-lg-3 text-right text-truncate').text.strip()
                    date = datetime.strptime(date_str, '%d %b %Y')

                    # Проверка, если серия вышла сегодня
                    if date.date() == datetime.today().date():
                        anime_url = anime_url.replace('-', '_') if anime_url else None
                        query = "SELECT user_id, anime_list FROM users WHERE $1 = ANY(anime_list);"
                        result = await connection.fetch(query, anime_url)

                        # Проверяем каждого пользователя
                        for record in result:
                            user_id, user_anime_list = record['user_id'], record['anime_list']
                            
                            # Проверяем, подписан ли пользователь на указанное аниме
                            if anime_url in user_anime_list:
                                async def send_description_message(anime_url):
                                    poster_url, title, description, rating, anime_id = await description_parser(anime_url)
                                    message_text = f"<b>{title}</b>\n\n" \
                                                f"Рейтинг: {rating}\n" \
                                                f"{description}\n" \
                                                f"{anime_url}" \
                                                f"Новая серия! {date}"
                                    bot.send_photo(chat_id=user_id, photo=poster_url, caption=message_text, parse_mode=ParseMode.HTML)
                                
                                await send_description_message(anime_url)
                    else:
                        return False
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
    finally:
        await close_db_connection(connection)
    
    await asyncio.sleep(86400)