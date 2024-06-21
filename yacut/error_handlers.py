from flask import render_template

from . import app


class InvalidAPIUsage(Exception):
    """
    Класс исключения для некорректного использования API.

    Attributes:
    - status_code (int): Код статуса HTTP для возврата.
    - message (str): Сообщение об ошибке.
    """
    status_code = 400

    def __init__(self, message, status_code=None):
        """
        Инициализация исключения.

        Args:
        - message (str): Сообщение об ошибке.
        - status_code (int, optional): Код статуса HTTP (по умолчанию 400).
        """
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    """
    Обработчик ошибки InvalidAPIUsage.

    Args:
    - error (InvalidAPIUsage): Исключение InvalidAPIUsage, которое вызвалось.

    Возвращает JSON с сообщением об ошибке и соответствующим статусом HTTP.
    """
    return error.to_dict(), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    """
    Обработчик ошибки 404 (страница не найдена).

    Args:
    - error (werkzeug.exceptions.NotFound): Исключение ошибки 404.

    Возвращает шаблон 404.html и статус 404 (Not Found).
    """
    return render_template('404.html'), 404
