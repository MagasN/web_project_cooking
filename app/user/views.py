from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from app.user.forms import LoginForm

# from app.user.model import User
from app.model import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Вход"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            # flash('Вы вошли на сайт')
            return redirect(url_for('index'))    # Переадресация на главную страницу
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('До свидания!')
    return redirect(url_for('index'))