import os
from datetime import timedelta
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'app.db')
SECRET_KEY = os.environ.get('SECRET_KEY')
REMEMBER_COOKIE_DURATION = timedelta(days=5)
# UPLOAD_FOLDER = os.path.join(basedir, '..', 'uploads')
MAX_CONTENT_LENGTH = 10 * 1000 * 1000