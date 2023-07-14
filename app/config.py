import os
from datetime import timedelta
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'app.db')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(days=5)
    UPLOAD_FOLDER_USER = os.path.join(basedir, 'static/uploads/users')
    MAX_CONTENT_LENGTH = 10 * 1000 * 1000
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
