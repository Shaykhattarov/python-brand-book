from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField


class DiscussionForm(FlaskForm):
    name = StringField('Имя')
    email = EmailField('Почта')
    phone = StringField('Телефон')
    submit = SubmitField('Отправить')

