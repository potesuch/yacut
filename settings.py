import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Конфигурационный класс для настройки параметров приложения.

    Attributes:
    - SQLALCHEMY_DATABASE_URI (str): URI базы данных, получаемый из переменной окружения DATABASE_URI.
    - SQLALCHEMY_TRACK_MODIFICATIONS (bool): Флаг для отслеживания изменений объектов SQLAlchemy.
    - SECRET_KEY (str): Секретный ключ приложения, получаемый из переменной окружения SECRET_KEY.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
