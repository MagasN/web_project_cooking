from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, EqualTo, Length

# from app.user.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Никнейм", validators=[DataRequired(), Length(min=5, max=40)], render_kw={"class": "form-control"}
    )
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField("Запомнить меня", default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField("Войти", render_kw={"class": "btn btn-primary"})
    register = SubmitField("Регистрация", render_kw={"class": "btn btn-primary"})


class RegisterForm(FlaskForm):
    username = StringField(
        "Никнейм", validators=[DataRequired(), Length(min=5, max=40)], render_kw={"class": "form-control"}
    )
    full_name = StringField("Фамилия Имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField(
        "Пароль", validators=[DataRequired(), Length(min=8, max=40)], render_kw={"class": "form-control"}
    )
    password2 = PasswordField(
        "Повторите пароль", validators=[DataRequired(), EqualTo("password")], render_kw={"class": "form-control"}
    )
    submit = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-primary"})


class UserProfileForm(FlaskForm):
    submit = SubmitField("Редактировать", render_kw={"class": "btn btn-primary"})


class EditProfileForm(FlaskForm):
    full_name = StringField("Фамилия имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    image_user = FileField("Загрузите фото", render_kw={"class": "input-group-text", "id": "inputGroupFile02"})
    submit = SubmitField("Сохранить", render_kw={"class": "btn btn-primary"})
