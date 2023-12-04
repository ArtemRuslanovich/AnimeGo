import datetime

async def is_valid_year(year_str):
    try:
        # Пробуем преобразовать строку в число
        year = int(year_str)
        # Проверяем, является ли год валидным (например, больше 1900 и меньше текущего года + 1)
        return 1900 <= year <= datetime.datetime.now().year + 1
    except ValueError:
        # Если возникает ошибка при преобразовании в число, год не является валидным
        return "Не могу определить такой год, попробуй еще раз"