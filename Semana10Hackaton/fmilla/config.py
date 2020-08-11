import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:SH4wnM3nd3s@localhost/FLminimarket'
    SQLALCHEMY_TRACK_MODIFICATIONS = False