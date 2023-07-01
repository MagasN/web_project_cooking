from getpass import getpass
import sys

from app import create_app
from app.model import User, db

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

    new_user = User(username=username, full_name= full_name, role='admin')    # Можно переписать, чтобы роль запрашивалась
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь id={} с именем {}'.format(new_user.id, new_user.username))