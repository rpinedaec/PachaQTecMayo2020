import os
basedir = os.path.abspath(os.path.dirname(__file__))

# 'postgres://username:password@localhost:5432/dbname'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:passmysqlmartin@localhost/dbs10HackatonMartinPerez'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


