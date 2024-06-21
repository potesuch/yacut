# Flask приложение Yacut

Это веб-приложение на Flask для создания коротких ссылок.

## Установка

Для запуска этого приложения вам потребуется Python 3.x и следующие зависимости:

```sh
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF
```

## Настройка

Перед запуском приложения убедитесь, что вы сконфигурировали базу данных в файле settings.py. По умолчанию используется SQLite.
Запуск

Выполните следующие команды для запуска приложения:

```sh
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Приложение будет доступно по адресу [http://localhost:5000](http://localhost:5000).

## Использование
### Создание короткой ссылки через API

Вы можете создать короткую ссылку, отправив POST запрос на /api/id/ с JSON телом:

```json
{
  "url": "https://example.com",
  "custom_id": "mylink"
}
```

Если custom_id не указан, будет сгенерирован уникальный короткий идентификатор.
Получение оригинальной ссылки по короткому идентификатору

Для получения оригинальной ссылки, отправьте GET запрос на /api/id/<short_id>/.

### Веб-интерфейс

Откройте главную страницу приложения для использования веб-интерфейса создания коротких ссылок.

## Структура проекта

    - __init__.py: Основной файл приложения.
    - views.py: Определение маршрутов и их обработчиков.
    - models.py: Определение модели URL_map для хранения отображений между длинными и короткими ссылками.
    - forms.py: Определение формы URLForm для ввода данных при создании коротких ссылок.
    - utils.py: Утилиты для генерации уникальных коротких идентификаторов и проверки их корректности.
    - error_handlers.py: Обработчики ошибок для различных исключений, включая некорректное использование API и ошибку 404.
    - api_views.py: Определение маршрутов API и их обработчиков.

## Дополнительная информация

Это приложение создано с использованием Flask, Flask-SQLAlchemy для работы с базой данных и WTForms для валидации форм. Оно включает API для создания и получения коротких ссылок, а также веб-интерфейс для удобства пользователей.
