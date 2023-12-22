from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from utils.statesform import Selector
from keyboards.type import type_keyboard
import asyncpg

async def handle_yes_callback(callback: CallbackQuery,state: FSMContext):
    await state.set_state(Selector.FIRST_CH)
    await callback.message.answer(f"Время сделать выбор", reply_markup=type_keyboard)
    await callback.answer()

DATABASE_URL = "postgresql://postgres:80156120189fap@localhost/Users"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def handle_sub_callback(callback: CallbackQuery, state: FSMContext, bot: Bot):
    anime_id = callback.data.removeprefix('subscribe_')

    # Получаем ID пользователя
    user_id = callback.from_user.id

    # Подключаемся к базе данных
    connection = await connect_to_db()
    try:
            # Получаем данные пользователя из базы данных
            user_data = await connection.fetchrow("SELECT anime_list FROM usersdata WHERE user_id = $1", user_id)

            if user_data:
                anime_list = user_data["anime_list"] if user_data["anime_list"] else []

                # Проверяем, подписан ли пользователь уже на это аниме
                if anime_id in anime_list:
                    anime_list.remove(anime_id)
                    await callback.answer(f"Вы успешно отписались ❌.", show_alert=True)
                else:
                    # Добавляем название аниме в список подписок
                    anime_list.append(anime_id)
                    await callback.answer(f"Вы успешно подписались ✅.", show_alert=True)

                # Обновляем данные пользователя в базе данных
                await connection.execute("UPDATE usersdata SET anime_list = $1 WHERE user_id = $2", anime_list, user_id)

    finally:
        # Всегда закрывайте соединение, даже в случае ошибки
        await close_db_connection(connection)
        



