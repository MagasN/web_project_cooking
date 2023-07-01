import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'app.db')

SECRET_KEY = 'key'

REMEMBER_COOKIE_DURATION = timedelta(days=5)
