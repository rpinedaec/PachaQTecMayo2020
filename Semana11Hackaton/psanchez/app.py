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
        'database': 'hackatons11',
        'user': 'postgres',
        'password': 'pachaqtec',
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
    app.logger.info(data)
    return "bienvindos al inicio de mi aplicacion"

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
    account_sid = 'AC84e4419e70ff440ea1d46e8166d9b9d3'
    auth_token = 'ea715c72685e9aac85bdeb12352ea5c9'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='Pedido 1',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51943555069'
    )
    msg = resp.message()
    msg.body("Aún está en la tienda")
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
    msg.body('Hola bienvenido al sistema de control de pedidos de PACHAQTEC escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
• *Menu:* el menu principal :rocket:
• *Productos:* Ver lista de productos :tomato:
• *Consulta tu pedido:* Ver estado de tu pedido con tu número :package: 
• *Revisa tu pedido*: Escribe mipedido y tu número de pedido (ej. mipedido 1)
""", use_aliases=True)
    msg.body(response)
    return str(resp)

class Cliente(db.Model):

    __fillable__ = ['nombre', 'email', 'telefono']

class Producto(db.Model):

    __fillable__ = ['nombre']

class Pedido(db.Model):
    pass