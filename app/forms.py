from flask_wtf import FlaskForm
from wtforms import SearchField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class AddRecipeForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired, Length(min=4, max=100)])
    decription_recipe = StringField('Краткое описание', validators=[Length(max=200)])
    steps_recipe = TextAreaField('Шаги приготовления', validators=[DataRequired])
    servings = IntegerField('Количество порций', validators=[DataRequired])