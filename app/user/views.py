from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from getpass import getpass

from app.user.forms import LoginForm, RegisterForm, UserProfileForm, EditProfileForm
from app.user.models import User
from app.db import db

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Вход"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

@blueprint.route('/process_login', methods=['POST'])
def process_login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            # flash('Вы вошли на сайт')
            return redirect(url_for('index'))    # Переадресация на главную страницу
    flash('Неправильное имя пользователя или пароль.')
    return redirect(url_for('user.login'))

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))  
    title = "Регистрация"
    register_form = RegisterForm()
    return render_template('register.html', page_title=title, form=register_form)

@blueprint.route('/process_register',  methods=['GET', 'POST'])
def process_register():
    form = RegisterForm()
    
    user = User.query.filter(User.username == form.username.data).count()
    if user:
        flash('Такой никнейм уже используется')
        return redirect(url_for('user.register'))
       
    if form.validate_on_submit():
        
        user = User(username=form.username.data, full_name=form.full_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!')
        return redirect(url_for('user.login'))
    
    flash('Пароли не совпадают')
    return redirect(url_for('user.register'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Возвращайся!')
    return redirect(url_for('index'))

@blueprint.route('/<username>')
@login_required
def user(username):
    form = UserProfileForm()
    title = "Профиль"
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_profile.html', user=user, page_title=title, form=form)

@blueprint.route('/edit/<username>', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = EditProfileForm()
    title = "Редактирование профиля"
    user = User.query.filter_by(username=username).first_or_404()
    
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        db.session.commit()
        flash('Ваши изменения были сохранены.')
        return redirect(url_for('user.user', username=current_user.username))
    elif request.method == 'GET':
        form.full_name.data = current_user.full_name
    return render_template('edit_user_profile.html', user=user, page_title=title, form=form)