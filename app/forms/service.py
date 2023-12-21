from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, InputRequired


class ServiceForm(FlaskForm):
    name = StringField('Название услуги', validators=[DataRequired()])
    image = FileField('Изображение')
    description = TextAreaField('Описание услуги', validators=[DataRequired()])
    essence = TextAreaField('Что это такое?', validators=[DataRequired()])
    development_stages = TextAreaField('Этапы разработки', validators=[DataRequired()])
    cost_description = TextAreaField('О стоимости услуг', validators=[DataRequired()])
    cost = StringField('Стоимость услуги', validators=[DataRequired()])
    demand = TextAreaField('Востребованность', validators=[DataRequired()])
    submit = SubmitField('Отправить')
