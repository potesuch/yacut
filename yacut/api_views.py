from flask import request, url_for

from . import app, db
from .models import URL_map
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_id, is_custom_id_correct


@app.route('/api/id/', methods=['POST'])
def id_view():
    if not request.is_json:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    data = request.get_json()
    # if not data:
    #     raise InvalidAPIUsage('Данные не указаны')
    # for k in data.keys():
    #     if k not in ['custom_id', 'url']:
    #         raise InvalidAPIUsage('Некорректное тело запроса')
    if 'custom_id' in data and data['custom_id']:
        stmt = db.select(URL_map).filter_by(short=data['custom_id'])
        if db.session.scalar(stmt) is not None:
            raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
        if not is_custom_id_correct(data['custom_id']) or len(data['custom_id']) > 16:
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        short_id = data['custom_id']
    else:
        short_id = get_unique_short_id()
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    url_map = URL_map(
        original=data['url'],
        short=short_id
    )
    db.session.add(url_map)
    db.session.commit()
    return url_map.to_dict(), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def retrieve_view(short_id):
    url_map = db.session.scalar(db.select(URL_map).filter_by(short=short_id))
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return {'url': url_map.original}
