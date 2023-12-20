from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired
from app.models import Service


class ServiceForm(FlaskForm):
    name = StringField('Название услуги', validators=[DataRequired()])
    image = FileField('Изображение')
    description = TextAreaField('Описание услуги')
    essence = TextAreaField('Что это такое?')
    development_stages = TextAreaField('Этапы разработки')
    cost_description = TextAreaField('О стоимости услуг')
    cost = StringField('Стоимость услуги')
    demand = TextAreaField('Востребованность')
    submit = SubmitField('Отправить')
