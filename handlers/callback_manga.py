from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from utils.statesform import Selector
from keyboards.type import type_keyboard
import asyncpg

DATABASE_URL = "postgresql://postgres:80156120189fap@localhost/Users"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def handle_manga_callback(callback: CallbackQuery, state: FSMContext, bot: Bot):
    manga_id = callback.data.removeprefix('add_')

    # Получаем ID пользователя
    user_id = callback.from_user.id

    # Подключаемся к базе данных
    connection = await connect_to_db()
    try:
            # Получаем данные пользователя из базы данных
            user_data = await connection.fetchrow("SELECT manga_list FROM usersdata WHERE user_id = $1", user_id)

            if user_data:
                manga_list = user_data["manga_list"] if user_data["manga_list"] else []

                # Проверяем, подписан ли пользователь уже на это аниме
                if manga_id in manga_list:
                    manga_list.remove(manga_id)
                    await callback.answer(f"Удалено из избранного ❌.", show_alert=True)
                else:
                    # Добавляем название аниме в список подписок
                    manga_list.append(manga_id)
                    await callback.answer(f"Добавлено в избранное ✅.", show_alert=True)

                # Обновляем данные пользователя в базе данных
                await connection.execute("UPDATE usersdata SET manga_list = $1 WHERE user_id = $2", manga_list, user_id)

    finally:
        # Всегда закрывайте соединение, даже в случае ошибки
        await close_db_connection(connection)
        