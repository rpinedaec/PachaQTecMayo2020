from flask import Flask
from flask_orator import Orator
from models.cliente import Cliente
from flask_orator import Orator, jsonify

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'Wassp',
        'user': 'postgres',
        'password': '3179billace',
        'prefix': ''
    }
}

db = Orator(app)
clnt=Cliente.find(1)
print(clnt.nombre)