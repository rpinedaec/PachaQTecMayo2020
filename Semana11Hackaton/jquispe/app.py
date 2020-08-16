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
    return "bienvenidos al inicio de mi aplicacion"
########CLIENTE#######
@app.route('/cliente/', methods=['GET'])
def getClientes():
    cliente = Cliente.all()
    return jsonify(cliente)

#RUTA PARA LA CREACION DE CLIENTE
@app.route('/cliente/', methods=['POST'])
def addClientes():
    cliente = Cliente.create(**request.get_json())
    return jsonify(cliente)

#RUTA PARA LA BUSQUEDA DE CLIENTE
@app.route('/cliente/<int:cliente_id>', methods=['GET'])
def get_user(cliente_id):
    cliente = Cliente.find(cliente_id)
    return jsonify(cliente)

#RUTA PARA ACTUALIZAR EL CLIENTE
@app.route('/cliente/<int:cliente_id>', methods=['PATCH'])
def update_user(cliente_id):
    user = Cliente.find_or_fail(cliente_id)
    user.update(**request.get_json())
    return jsonify(user)

########PRODUCTO#######

@app.route('/producto/', methods=['GET'])
def getProductos():
    producto = Producto.all()
    return jsonify(producto)

@app.route('/producto/', methods=['POST'])
def addProductos():
    producto = Producto.create(**request.get_json())
    return jsonify(producto)

@app.route('/producto/<int:producto_id>', methods=['GET'])
def get_product(producto_id):
    producto = Producto.find(producto_id)
    return jsonify(producto)

@app.route('/producto/<int:producto_id>', methods=['PATCH'])
def update_product(producto_id):
    product = Producto.find_or_fail(producto_id)
    product.update(**request.get_json())
    return jsonify(product)

########PEDIDO#######

@app.route('/pedido/', methods=['GET'])
def getPedido():
    pedido = Pedido.all()
    return jsonify(pedido)

@app.route('/pedido/', methods=['POST'])
def addPedido():
    pedido = Pedido.create(**request.get_json())
    return jsonify(pedido)

@app.route('/pedido/<int:pedido_id>', methods=['GET'])
def get_product(pedido_id):
    pedido = Pedido.find(pedido_id)
    return jsonify(pedido)

@app.route('/pedido/<int:pedido_id>', methods=['PATCH'])
def update_product(pedido_id):
    order = Pedido.find_or_fail(producto_id)
    order.update(**request.get_json())
    return jsonify(order)









#RUTA DE WHATASAP
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
    msg.body('Hola bienvenido al sistema de control de pedidos de Jorge Quispe escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
You can give me the following commands:
:black_small_square: *'menu':* el menu principal :rocket:
:black_small_square: *'pedidos'*: busca tus pedidos :cat:
""", use_aliases=True)
    msg.body(response)
    return str(resp)

#DEFINIENDO LA CLASE CLIENTE
class Cliente(db.Model):

    __fillable__ = ['nombre', 'email', 'telefono']

#DEFINIENDO LA CLASE PRODUCTO
class Producto(db.Model):

    __fillable__ = ['nombre']

#DEFINIENDO LA CLASE PEDIDO
class Pedido(db.Model):
    pass