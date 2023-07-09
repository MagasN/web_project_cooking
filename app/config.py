from os import environ, path
from datetime import timedelta
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, '..', 'app.db')
SECRET_KEY = environ.get('SECRET_KEY')
REMEMBER_COOKIE_DURATION = timedelta(days=5)
