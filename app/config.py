import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'app.db')

SECRET_KEY = 'Mj*WCmi1y~vwjS0JA4hu4Qf|NaZ}rB?q|ef*c0'

REMEMBER_COOKIE_DURATION = timedelta(days=5)