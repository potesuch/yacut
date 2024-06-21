from random import choices

from . import db
from .models import URL_map

SYMBOLS = 'AaBbCcDdEeFfGgHhIiKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'


def get_unique_short_id():
    """
    Генерирует уникальный короткий id для ссылки.

    Генерирует случайную последовательность символов из SYMBOLS длиной 6 символов.
    Проверяет уникальность короткого id в базе данных.
    Если найдено совпадение, генерирует новый id.

    Returns:
    - str: Уникальный короткий id.
    """
    short = ''.join(choices(SYMBOLS, k=6))
    if db.session.scalar(
        db.select(URL_map).filter_by(short=short)
    ) is not None:
        short = get_unique_short_id()
    return short


def is_custom_id_correct(custom_id):
    """
    Проверяет корректность пользовательского короткого id.

    Args:
    - custom_id (str): Пользовательский короткий id для проверки.

    Returns:
    - bool: True, если короткий id состоит только из символов SYMBOLS,
    иначе False.
    """
    for c in custom_id:
        if c not in SYMBOLS:
            return False
    return True
