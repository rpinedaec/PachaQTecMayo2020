import os
from flask import Flask, request
from flask_orator import Orator, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import emoji
import logging
from models.cliente import Cliente
from models.pedido import Pedido
from models.producto import Producto


# Configuration

ORATOR_DATABASES = {
    'postgres': { 
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'hackatons11',
        'user': 'postgres',
        'password': '1234',
        'prefix': ''
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)

# Initializing Orator
db = Orator(app)

if __name__ == '__main__':
    app.run(debug = True)

#routes
@app.route('/', methods=['GET'])
def hello():
    return "Bienvenidos al inicio de mi aplicacion"
#CRUD clientes
@app.route('/clientes/', methods=['GET'])
def get_allclients():
    cliente = Cliente.all()
    return jsonify(cliente)

@app.route('/clientes/', methods=['POST'])
def add_client():
    nombre = request.get_json()["nombre"]
    email = request.get_json()["email"]
    telefono = request.get_json()["telefono"]
    Cliente.create(nombre = nombre, email = email, telefono = telefono) 
    return jsonify(request.get_json())

@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def get_client(cliente_id):
    cliente = Cliente.find(cliente_id)
    return jsonify(cliente)

@app.route('/clientes/<int:cliente_id>', methods=['PATCH'])
def update_client(cliente_id):
    cliente = Cliente.find_or_fail(cliente_id)
    cliente.update(**request.get_json())
    return jsonify(cliente)

@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def delete_client(cliente_id):
    cliente = Cliente.find_or_fail(cliente_id)
    cliente.destroy(cliente_id)
    return jsonify(cliente)
# CRUD productos
@app.route('/productos/', methods=['GET'])
def get_allproducts():
    producto = Producto.all()
    return jsonify(producto)

@app.route('/productos/', methods=['POST'])
def add_product():
    nombre = request.get_json()["nombre"]
    Producto.create(nombre = nombre) 
    return jsonify(request.get_json())

@app.route('/productos/<int:producto_id>', methods=['GET'])
def get_product(producto_id):
    producto = Producto.find(producto_id)
    return jsonify(producto)

@app.route('/productos/<int:producto_id>', methods=['PATCH'])
def update_product(producto_id):
    producto = Producto.find_or_fail(producto_id)
    producto.update(**request.get_json())
    return jsonify(producto)

@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def delete_product(producto_id):
    producto = Producto.find_or_fail(producto_id)
    producto.destroy(producto_id)
    return jsonify(producto)
# CRUD Pedidos
@app.route('/pedidos/', methods=['GET'])
def get_allpedidos():
    pedido = Pedido.all()
    return jsonify(pedido)

@app.route('/pedidos/', methods=['POST'])
def add_pedido():
    ubicacion = request.get_json()["ubicacion"]
    cliente_id = request.get_json()["cliente_id"]
    producto_id = request.get_json()["producto_id"]   
    Pedido.create(ubicacion = ubicacion, cliente_id = cliente_id, producto_id = producto_id) 
    return jsonify(request.get_json())

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def get_pedido(pedido_id):
    pedido = Pedido.find(pedido_id)
    return jsonify(pedido)

@app.route('/pedidos/<int:pedido_id>', methods=['PATCH'])
def update_pedido(pedido_id):
    pedido = Pedido.find_or_fail(pedido_id)
    pedido.update(**request.get_json())
    return jsonify(pedido)

@app.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
def delete_pedido(pedido_id):
    pedido = Pedido.find_or_fail(pedido_id)
    pedido.destroy(pedido_id)
    return jsonify(pedido)

#Chatbot Whatsapp
@app.route('/wtspp/', methods=['POST'])
def whtspp():
    body = request.form.get("Body")
    nroFrom = request.form.get("From")
    app.logger.debug(nroFrom[9:])
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
    account_sid = 'AC363bb259d783c872befae66bf491241b'
    auth_token = '6c3079f9596e32a456df388e1c296ef8'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='Twilio HQ',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51964291427'
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
        if(nroFrom[9:] == objCliente.telefono):
            idCliente = objCliente.id 
            break
    app.logger.debug(idCliente)
    pedidos = Pedido.all()
    idsPedidos = ''
    for objPedidos in pedidos:
        if(objPedidos.cliente_id == idCliente):
            app.logger.debug(objPedidos.id)
            idsPedidos += str(objPedidos.id) +' '
            break
    respuesta = ''
    if idsPedidos == '':
        respuesta = 'No hay pedidos para tu número de telefono'
    else:
        respuesta = 'Escribe el número de pedido para ver el detalle: ' + idsPedidos
        respuesta += ' en este formato *mipedido <id_pedido>*'
    #pedidos = .where('votes', '>', 100).update(status=2)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)
    return str(resp)

def msgDefault():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Hola bienvenido al sistema de control de pedidos de Bruce Porras')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola :wave:!!! escribe las siguientes opciones:*
You can give me the following commands:
:black_small_square: *'menu':* el menu principal :memo:
:black_small_square: *'pedidos'*: busca tus pedidos :white_check_mark:

""", use_aliases=True)
    msg.body(response)
    return str(resp)

