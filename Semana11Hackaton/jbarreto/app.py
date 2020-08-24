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
        'password': 'base009',
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

@app.route('/pedido/', methods=['GET'])
def getPedidos():
    pedido = Pedido.all()
    return jsonify(pedido)

@app.route('/pedido/', methods=['POST'])
def addPedidos():
    pedido = Pedido.create(**request.get_json())
    return jsonify(pedido)

@app.route('/pedido/<int:pedido_id>', methods=['GET'])
def get_pedido(pedido_id):
    pedido = Pedido.find(pedido_id)
    return jsonify(pedido)

@app.route('/pedido/<int:pedido_id>', methods=['PATCH'])
def update_pedido(pedido_id):
    pedido = Pedido.find_or_fail(pedido_id)
    pedido.update(**request.get_json())
    return jsonify(pedido)

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
    miproducto = Producto.find(mipedido.producto_id)
    app.logger.debug(jsonify(miproducto))
    micliente = Cliente.find(mipedido.cliente_id)
    app.logger.debug(jsonify(micliente))
    resp = MessagingResponse()
    # account_sid = 'ACF37B84D5247086F0307ECDDC90DA30D0'
    # auth_token = '9E7634782B973D055BBE14BAA90406D7'
    account_sid = 'ACf37b84d5247086f0307ecddc90da30d0'
    auth_token = '9e7634782b973d055bbe14baa90406d7'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            # from_='whatsapp:+14439607515',
            from_='whatsapp:+14155238886',
            body='Twilio HQ',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51992787417'
    )
    msg = resp.message()
    #msg.body("Procesando")
    response = f"""
*Pedido # {mipedido.id}*
*'Cliente'*
'Id': {micliente.id}
'Nombre': {micliente.nombre}
'Email': {micliente.email}
'Telefono': {micliente.telefono}
*'Producto(s)'*
'Id': {miproducto.id}
'Nombre': {miproducto.nombre}
"""
    msg.body(response)

    return str(resp)

def findPedidos(nroFrom):
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))
    idCliente = 0
    lstTelefono = nroFrom.split('+')
    telefono = lstTelefono[1]
    telefono = '+' + telefono
    for objCliente in clientes:
        app.logger.debug(objCliente.telefono)
        if(objCliente.telefono == telefono):
            idCliente = objCliente.id
            break
    pedidos = Pedido.all()
    idsPedidos = ''
    for objPedidos in pedidos:
        if(objPedidos.cliente_id == idCliente):
            app.logger.debug(objPedidos.id)
            if idsPedidos:
                idsPedidos += ' | '
            idsPedidos += str(objPedidos.id) 
    respuesta = ''
    if idsPedidos == '':
        respuesta = 'No hay pedidos para tu numero de telefono: ' + telefono
    else:
        #respuesta = 'Escribe el numero de pedido para ver el detalle: ' + idsPedidos
        #respuesta += ' en este formato *mipedido <id_pedido>*'
        respuesta = f"""
*Tienes los # de pedido:* {idsPedidos}
Escribe el # de pedido para ver el detalle, en este formato *mipedido <id_pedido>*'
"""
    #pedidos = .where('votes', '>', 100).update(status=2)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)
    return str(resp)


def msgDefault():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Hola bienvenido al sistema de control de pedidos de Jacqueline escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
:black_small_square: *'menu':* el menu principal
:black_small_square: *'pedidos'*: busca tus pedidos
:black_small_square: *'mipedido'*: busca tu número de pedido
""", use_aliases=True)

    msg.body(response)
    return str(resp)

class Cliente(db.Model):

    __fillable__ = ['nombre', 'email', 'telefono']

class Producto(db.Model):

    __fillable__ = ['nombre']

class Pedido(db.Model):
    pass