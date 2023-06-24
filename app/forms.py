from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField, FileField, SubmitField, SearchField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange


class AddRecipeForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(min=4, max=100)], render_kw={'placeholder': 'Название'})
    # image_recipe = FileField('Фото блюда', validators=[Regexp('[^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$')])
    decription_recipe = StringField('Краткое описание', validators=[Length(max=200)], render_kw={'placeholder': 'Краткое описание'})
    steps_recipe = TextAreaField('Шаги приготовления', validators=[DataRequired()], render_kw={'placeholder': 'Шаги приготовления', 'style': 'height: 200px'})
    servings = IntegerField('Количество порций', validators=[DataRequired(), NumberRange(min=1)], render_kw={'placeholder': 'Количество порций'})
    time_cooking = IntegerField('Время приготовления', validators=[DataRequired(), NumberRange(min=1)], render_kw={'placeholder': 'Время приготовления'})
    # ingredient_id = IntegerField('Ингредиенты', validators=[DataRequired()])
    submit = SubmitField('Добавить')