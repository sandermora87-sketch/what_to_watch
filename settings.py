# what_to_watch/settings.py
import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()


class Config(object):
    # Читаем значения из окружения.
    # Если переменной нет, используем значение по умолчанию (опционально)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                        'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-for-local-only')
