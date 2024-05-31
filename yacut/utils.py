from random import choices

from . import db
from .models import URL_map

SYMBOLS = 'AaBbCcDdEeFfGgHhIiKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'


def get_unique_short_id():
    short = ''.join(choices(SYMBOLS, k=6))
    if db.session.scalar(
        db.select(URL_map).filter_by(short=short)
    ) is not None:
        short = get_unique_short_id()
    return short


def is_custom_id_correct(custom_id):
    for c in custom_id:
        if c not in SYMBOLS:
            return False
    return True
