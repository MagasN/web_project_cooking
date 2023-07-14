from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, TextAreaField, IntegerField, PasswordField, FileField, SubmitField, SearchField
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

class EditRecipeForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(min=4, max=100)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Название'})
    # image_recipe = FileField('Фото блюда', validators=[Regexp('[^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$')])
    decription_recipe = StringField('Краткое описание', validators=[Length(max=200)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Краткое описание'})
    steps_recipe = TextAreaField('Шаги приготовления', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingTextarea2', 'placeholder': 'Шаги приготовления', 'style': 'height: 200px'})
    servings = IntegerField('Количество порций', validators=[DataRequired(), NumberRange(min=1)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Количество порций'})
    time_cooking = IntegerField('Время приготовления', validators=[DataRequired(), NumberRange(min=1)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Время приготовления'})
    # ingredient_id = IntegerField('Ингредиенты', validators=[DataRequired()])
    submit = SubmitField('Изменить', render_kw={'class': 'btn btn-primary'})

class CommentForm(FlaskForm):
    recipe_id = HiddenField('ID рецепта', validators=[DataRequired()])
    comment_text = StringField('Добавьте комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})