from flask import Flask, request
from flask_orator import Orator, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import emoji
import logging

# Creating Flask application
app = Flask(__name__)
DEBUG = True
ORATOR_DATABASES = {
    'postgres': { 
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'semana11hackaton',
        'user': 'postgres',
        'password': 'Jjpn2020.',
        'prefix': ''
    }
}
app.config.from_object(__name__)

# Initializing Orator
db = Orator(app)

if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET'])
def hello():
    return "bienvenidos al inicio de mi aplicacion"

@app.route('/cliente/', methods=['GET'])
def getClientes():
    cliente = Cliente.all()
    return jsonify(cliente)

@app.route('/cliente/', methods=['POST'])
def addClientes():
    cliente = Cliente.create(**request.get_json())
    return jsonify(cliente)

@app.route('/cliente/<int:cliente_id>', methods=['GET'])
def get_user(cliente_id):
    cliente = Cliente.find(cliente_id)
    return jsonify(cliente)

@app.route('/cliente/<int:cliente_id>', methods=['PATCH'])
def update_user(cliente_id):
    user = Cliente.find_or_fail(cliente_id)
    user.update(**request.get_json())
    return jsonify(user)

@app.route('/wtspp/', methods=['POST'])
def whtspp():
    body = request.form.get("Body")
    nroFrom = request.form.get("From")
    app.logger.debug(nroFrom)
    if body == 'menu':
        return sendMenu()
    elif body == 'pedidos':
        return findPedidos(nroFrom)
    elif body.startswith('mipedido'):
        return detallePedido(body)
    else:
        return msgDefault()

def detallePedido(body):
    pedido = body.replace('mipedido', '')
    pedido = pedido.strip()
    app.logger.debug(pedido)
    mipedido = Pedido.find(int(pedido))
    app.logger.debug(jsonify(mipedido))
    resp = MessagingResponse()
    account_sid = 'AC0e345cf7fa8a72b6e64728a9dede5264'
    auth_token = '5a6cfc20a750a9a303c0e950962e0041'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='Twilio HQ',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51926902137'
    )
    msg = resp.message()
    msg.body("Procesando")
    return str(resp)


def findPedidos(nroFrom):
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))
    idCliente = 0
    for objCliente in clientes:
        app.logger.debug(objCliente.telefono)
        if(nroFrom == objCliente.telefono):
            idCliente = objCliente.id 
            break
    pedidos = Pedido.all()
    idsPedidos = ''
    for objPedidos in pedidos:
        if(objPedidos.cliente_id == idCliente):
            app.logger.debug(objPedidos.id)
            idsPedidos += str(objPedidos.id) +' '
            break
    respuesta = ''
    if idsPedidos == '':
        respuesta = 'No hay pedidos para tu numero de telefono'
    else:
        respuesta = 'Escribe el numero de pedido para ver el detalle: ' + idsPedidos
        respuesta += ' en este formato *mipedido <id_pedido>*'
    #pedidos = .where('votes', '>', 100).update(status=2)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)
    return str(resp)


def msgDefault():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Hola bienvenido al sistema de control de pedidos de Roberto Pineda escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
You can give me the following commands:
:black_small_square: *'menu':* el menu principal :rocket:
:black_small_square: *'pedidos'*: busca tus pedidos :cat:
:black_small_square: *'dog'*: Don't worry, we have dogs too! :dog:
:black_small_square: *'meme'*: The top memes of today, fresh from r/memes. :hankey:
:black_small_square: *'news'*: Latest news from around the world. :newspaper:
:black_small_square: *'recipe'*: Searches Allrecipes.com for the best recommended recipes. :fork_and_knife:
:black_small_square: *'recipe <query>'*: Searches Allrecipes.com for the best recipes based on your query. :mag:
:black_small_square: *'get recipe'*: Run this after the 'recipe' or 'recipe <query>' command to fetch your recipes! :stew:
:black_small_square: *'statistics <country>'*: Show the latest COVID19 statistics for each country. :earth_americas:
:black_small_square: *'statistics <prefix>'*: Show the latest COVID19 statistics for all countries starting with that prefix. :globe_with_meridians:
""", use_aliases=True)
    msg.body(response)
    return str(resp)

class Cliente(db.Model):

    __fillable__ = ['nombre', 'email', 'telefono']

class Producto(db.Model):

    __fillable__ = ['nombre']

class Pedido(db.Model):
    pass