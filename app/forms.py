from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class AddRecipeForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(min=4, max=100)])
    # image_recipe = FileField('Фото блюда', validators=[Regexp('[^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$')])
    decription_recipe = StringField('Краткое описание', validators=[Length(max=200)])
    steps_recipe = TextAreaField('Шаги приготовления', validators=[DataRequired()])
    servings = IntegerField('Количество порций', validators=[DataRequired(), Length(min=1)])
    time_cooking = IntegerField('Время приготовления', validators=[DataRequired(), Length(min=1)])
    # ingredient_id = IntegerField('Ингредиенты', validators=[DataRequired])
    submit = SubmitField('Добавить')