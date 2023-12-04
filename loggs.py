import logging
from logging.handlers import TimedRotatingFileHandler


log_file_path = "D:\ХУЙНЯ\log.txt"

def config_log(log_file_path):
# Создаем ротируемый обработчик логов, который будет создавать новый файл каждые трое суток
    handler = TimedRotatingFileHandler(
        filename=log_file_path,
        when="midnight",
        interval=1,
        backupCount=3  # Хранить последние три файла
    )

    # Уровень логгирования
    handler.setLevel(logging.INFO)

    # Формат лог-записей
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Создаем логгер
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)

    return logger
