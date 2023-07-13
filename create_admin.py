from getpass import getpass
import sys

from app import create_app
from app.db import db
from app.user.models import User

app = create_app()

with app.app_context():
    username = input('Введите никней пользователя: ')
    full_name = input('Введите фамилию и имя пользователя: ')

    if User.query.filter(User.username == username).count():
        print('Пользователь с таким именем уже существует')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    
    if not password == password2:
        print('Пароли различаются')
        sys.exit(0)
    img_admin = "../static/img/admin.png"

    new_user = User(username=username, full_name= full_name, role='admin', image_user=img_admin)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь id={} с именем {}'.format(new_user.id, new_user.username))