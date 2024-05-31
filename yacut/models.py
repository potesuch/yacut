import datetime as dt

from flask import url_for

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from yacut import db


class URL_map(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    original: Mapped[str] = mapped_column(String(256))
    short: Mapped[str] = mapped_column(String(16))
    timestamp: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.timezone.utc),
    )

    def to_dict(self):
        return {
            'url': self.original,
            'short_link': url_for('redirect_view', short_id=self.short, _external=True)
        }
