from flask import render_template, flash, redirect, abort, url_for

from . import app, db
from .models import URL_map
from .forms import URLForm
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """
    Основная страница приложения для создания коротких ссылок.

    GET: Отображает форму для создания короткой ссылки.
    POST: Обрабатывает форму, создает короткую ссылку и отображает результат.

    Возвращает HTML страницы с формой или перенаправляет на созданную короткую
    ссылку.
    """
    form = URLForm()
    if form.validate_on_submit():
        if form.custom_id.data:
            stmt = db.select(URL_map).filter_by(short=form.custom_id.data)
            if db.session.scalar(stmt):
                flash(f'Имя {form.custom_id.data} уже занято!')
                return render_template('index.html', form=form)
            short_id = form.custom_id.data
        else:
            short_id = get_unique_short_id()
        url_map = URL_map(
            original=form.original_link.data,
            short=short_id
        )
        db.session.add(url_map)
        db.session.commit()
        link = url_for('redirect_view', short_id=url_map.short, _external=True)
        flash('Ваша новая ссылка готова:')
        flash(link, category='link')
    return render_template('index.html', form=form)


@app.route('/<short_id>')
def redirect_view(short_id):
    """
    Обработчик для перенаправления по короткой ссылке.

    Args:
    - short_id (str): Короткий id ссылки для перенаправления.

    Перенаправляет на оригинальную длинную ссылку, если она существует в базе
    данных.
    Если ссылка не найдена, возвращает ошибку 404 (Not Found).
    """
    url_map = db.session.scalar(db.select(URL_map).filter_by(short=short_id))
    if url_map is None:
        abort(404)
    return redirect(url_map.original)
