import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqllite:///' + os.path.join(basedir, '..', 'app.db')