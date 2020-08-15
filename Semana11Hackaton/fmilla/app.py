from flask import Flask, request
from flask_orator import Orator, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
import logging
import emoji

DEBUG = True
ORATOR_DATABASES = {
    'postgres': { 
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'hackatons11',
        'user': 'postgres',
        'password': 'SH4wnM3nd3s',
        'prefix': ''
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)

# Initializing Orator
db = Orator(app)

if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET'])
def hello():
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

@app.route('/cliente/<int:cliente_id>', methods=['DELETE'])
def delete_user(cliente_id):
    user = Cliente.find_or_fail(cliente_id)
    user.delete()
    return jsonify(user)

@app.route('/producto/', methods=['GET'])
def getProductos():
    producto = Producto.all()
    return jsonify(producto)

@app.route('/producto/', methods=['POST'])
def addProductos():
    producto = Producto.create(**request.get_json())
    return jsonify(producto)

@app.route('/producto/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto = Producto.find(producto_id)
    return jsonify(producto)

@app.route('/producto/<int:producto_id>', methods=['PATCH'])
def update_producto(producto_id):
    producto = Producto.find_or_fail(producto_id)
    producto.update(**request.get_json())
    return jsonify(producto)

@app.route('/producto/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = Producto.find_or_fail(producto_id)
    producto.delete()
    return jsonify(producto)

@app.route('/pedido/', methods=['GET'])
def getPedidos():
    pedido = Pedido.all()
    return jsonify(pedido)

@app.route('/pedido/', methods=['POST'])
def addPedidos():
    pedido = Pedido.create(**request.get_json())
    return jsonify(pedido)

@app.route('/pedido/<int:id>', methods=['GET'])
def get_pedido(id):
    pedido = Pedido.find(id)
    return jsonify(pedido)

@app.route('/pedido/<int:id>', methods=['PATCH'])
def update_pedido(id):
    pedido = Pedido.find_or_fail(id)
    pedido.update(**request.get_json())
    return jsonify(pedido)

@app.route('/pedido/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    pedido = Pedido.find_or_fail(id)
    pedido.delete()
    return jsonify(pedido)

@app.route('/wtspp/', methods=['POST'])
def whtspp():
    body = request.form.get("Body")
    nroFrom = request.form.get("From")
    numero = request.form.get("Body")
    app.logger.debug(nroFrom)
    if body == 'menu':
        return sendMenu()
    elif body.startswith('+'):
        return findPedidos(numero)
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
    account_sid = 'ACaf6f85fbf5807f7c7845376520428061'
    auth_token = '99cb1420e4f132ab1657e817c89e6e1c'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='Twilio HQ',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51980141882'
    )
    msg = resp.message()
    msg.body("Procesando")
    
    return str(resp)


def findPedidos(numero):
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))
    idCliente = 0
    for objCliente in clientes:
        app.logger.debug(objCliente.telefono)
        if(numero == objCliente.telefono):
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
    msg.body('Hola bienvenido al sistema de control de pedidos de Fiorella Milla escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
:black_small_square: *Escribe tu numero de celular para ver tus pedidos*(El numero debe tener el codigo de país) :rocket:
""", use_aliases=True)
    msg.body(response)
    return str(resp)

class Cliente(db.Model):
    
    __fillable__ = ['nombre', 'email', 'telefono']

class Producto(db.Model):

    __fillable__ = ['nombre']

class Pedido(db.Model):
    __fillable__ = ['ubicacion','cliente_id','producto_id']