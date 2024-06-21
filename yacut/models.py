import datetime as dt

from flask import url_for

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from yacut import db


class URL_map(db.Model):
    """
    Модель для хранения отображений между длинными и короткими ссылками.

    Attributes:
    - id (int): Уникальный идентификатор записи (первичный ключ).
    - original (str): Длинная ссылка.
    - short (str): Короткая ссылка.
    - timestamp (datetime): Время создания записи.

    Methods:
    - to_dict(): Преобразует объект в словарь для сериализации в JSON.
    """
    id: Mapped[int] = mapped_column(primary_key=True)
    original: Mapped[str] = mapped_column(String(256))
    short: Mapped[str] = mapped_column(String(16))
    timestamp: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.timezone.utc),
    )

    def to_dict(self):
        """
        Преобразует объект URL_map в словарь.

        Возвращает:
        - dict: Словарь с полями 'url' (длинная ссылка) и 'short_link' (короткая ссылка).
        """
        return {
            'url': self.original,
            'short_link': url_for(
                'redirect_view', short_id=self.short, _external=True
            )
        }
