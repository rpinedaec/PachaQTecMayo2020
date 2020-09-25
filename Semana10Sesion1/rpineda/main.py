from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from markupsafe import escape
from utils.utils import log
from flask_orator import Orator
from models.user import User

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'flbdd',
        'user': 'postgres',
        'password': 'pachaqtec',
        'prefix': ''
    }
}

db = Orator(app)
env_path = Path('.')/'.env'
load_dotenv(dotenv_path = env_path)

@app.route('/')
def inicio():
    return "Hola desde Flask Pachaqtec"

@app.route('/rpineda/<username>')
def miFuncion(username):
    return 'Hola %s' % escape(username)

@app.route('/rpineda/<n1>/<n2>')
def miFuncion2(n1, n2):
    suma = int(n1) + int(n2)
    return f"Hola Roberto la suma de los numero es: {suma}"

@app.route('/rpineda/<operacion>/<n1>/<n2>')
def operaciones(operacion, n1, n2):
    app.logger.debug(f"Operacion: {operacion}")
    app.logger.debug(f"N1: {n1}")
    app.logger.debug(f"N2: {n2}")
    try:
        if operacion == 'suma':
            resultado = int(n1) + int(n2)
        elif operacion == 'resta':
            resultado = int(n1) - int(n2)
        elif operacion == 'multiplicacion':
            resultado = int(n1) * int(n2)
        elif operacion == 'division':
            resultado = int(n1) / int(n2)
        else:
            return f"{operacion} no es una operacion valida"
    except ZeroDivisionError as divisionError:
        return f"{operacion} no es una operacion valida porque no se puede dividir para 0 :{divisionError}"
    except Exception as error:
        return "hay otro tipo de error"
    return f"Hola Roberto la {operacion} de los numero es: {resultado}"

@app.route('/user/<username>')
def addUser(username):
    strUser = str(username)
    app.logger.debug(f"usuario: {strUser}")
    user = User()
    user.name = username
    user.email='no@email.com'
    user.save()
    return "Usuario Creado"

@app.route('/users/')
def getUsers():
    users = User.all()
    for obj in users:
        
