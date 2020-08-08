from flask import Flask
from flask_orator import Orator

app = Flask(__name__)
DEBUG = True
ORATOR_DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'hacakathons11',
        'user': 'postgres',
        'password': '1234',
        
    }
}

db = Orator(app)


class User(db.Model):

    __fillable__ = ['name', 'email']

    def __repr__(self):
        return '<User %r>' % self.name