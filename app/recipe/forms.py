from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, TextAreaField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileAllowed



class AddRecipeForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(min=4, max=100)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Название'})
    image_recipe = FileField('Фото блюда', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Разрешенные типы файлов - png, jpg, jpeg, gif. К сожалению рецепт не добавлен, попробуйте ещё раз.')], render_kw={'class': 'input-group-text', 'id': 'inputGroupFile01'})
    decription_recipe = StringField('Краткое описание', validators=[Length(max=200)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Краткое описание'})
    ingredients = TextAreaField('Ингридиенты', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingTextarea2', 'placeholder': 'Шаги приготовления', 'style': 'height: 200px'})
    steps_recipe = TextAreaField('Шаги приготовления', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingTextarea3', 'placeholder': 'Шаги приготовления', 'style': 'height: 200px'})
    servings = IntegerField('Количество порций', validators=[DataRequired(), NumberRange(min=1)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Количество порций'})
    time_cooking = IntegerField('Время приготовления', validators=[DataRequired(), NumberRange(min=1)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Время приготовления'})
    # ingredient_id = IntegerField('Ингредиенты', validators=[DataRequired()])
    submit = SubmitField('Добавить', render_kw={'class': 'btn btn-primary'})

class EditRecipeForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(min=4, max=100)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Название'})
    image_recipe = FileField('Фото блюда', render_kw={'class': 'input-group-text', 'id': 'inputGroupFile02'})
    decription_recipe = StringField('Краткое описание', validators=[Length(max=200)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Краткое описание'})
    ingredients = TextAreaField('Ингридиенты', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingTextarea4', 'placeholder': 'Шаги приготовления', 'style': 'height: 200px'})    
    steps_recipe = TextAreaField('Шаги приготовления', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingTextarea5', 'placeholder': 'Шаги приготовления', 'style': 'height: 200px'})
    servings = IntegerField('Количество порций', validators=[DataRequired(), NumberRange(min=1)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Количество порций'})
    time_cooking = IntegerField('Время приготовления', validators=[DataRequired(), NumberRange(min=1)], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Время приготовления'})
    # ingredient_id = IntegerField('Ингредиенты', validators=[DataRequired()])
    submit = SubmitField('Изменить', render_kw={'class': 'btn btn-primary'})

class CommentForm(FlaskForm):
    recipe_id = HiddenField('ID рецепта', validators=[DataRequired()])
    comment_text = StringField('Добавьте комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})