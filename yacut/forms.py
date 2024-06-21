from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional, Length


class URLForm(FlaskForm):
    """
    Форма для ввода данных при создании короткой ссылки.

    Attributes:
    - original_link (StringField): Поле для ввода длинной ссылки.
    - custom_id (StringField): Поле для ввода пользовательского короткого id (опционально).
    - submit (SubmitField): Кнопка для отправки формы.
    """
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired('Обязательное поле'), Length(1, 256)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Optional(), Length(1, 16)]
    )
    submit = SubmitField('Создать')
