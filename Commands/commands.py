from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/back", description="В начало"),
        BotCommand(command="/fav", description="подписки"),
    ]
    scope_default = BotCommandScopeDefault()

    await bot.set_my_commands(commands, scope_default)