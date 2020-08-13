from flask import Flask, request
from flask_orator import Orator, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from models.cliente import Clientes
from models.producto import Productos
from models.pedido import Pedidos
#from flask_http_response import success, result, error
#import requests
from twilio.rest import Client
import emoji

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'Hackaton11',
        'user': 'postgres',
        'password': 'admin',
        'prefix': ''
    }
}

db = Orator(app)

@app.route('/', methods=['GET'])
def hello():
    return "bienvindos al inicio de mi aplicacion"
    
@app.route('/Cliente/', methods=['GET'])
def getClientes():
    cliente = Clientes.all()
    return jsonify(cliente)

@app.route('/Cliente/', methods=['POST'])
def addClientes():
    cliente = Clientes.create(**request.get_json())
    return jsonify(cliente)

@app.route('/Cliente/<int:cliente_id>', methods=['GET'])
def get_Cliente(cliente_id):
    cliente = Clientes.find(cliente_id)
    return jsonify(cliente)

@app.route('/Cliente/<int:cliente_id>', methods=['PATCH'])
def update_Cliente(cliente_id):
    cliente = Clientes.find_or_fail(cliente_id)
    cliente.update(**request.get_json())
    return jsonify(cliente)

@app.route('/Productos/', methods=['GET'])
def getProductos():
    productos = Productos.all()
    return jsonify(productos)

@app.route('/Productos/', methods=['POST'])
def addProductos():
    productos = Productos.create(**request.get_json())
    return jsonify(productos)

@app.route('/Productos/<int:productos_id>', methods=['GET'])
def get_Productos(productos_id):
    productos = Productos.find(productos_id)
    return jsonify(productos)

@app.route('/Productos/<int:productos_id>', methods=['PATCH'])
def update_Productos(productos_id):
    productos = Productos.find_or_fail(productos_id)
    productos.update(**request.get_json())
    return jsonify(productos)

@app.route('/Pedidos/', methods=['GET'])
def getPedidos():
    pedidos = Pedidos.all()
    return jsonify(pedidos)

@app.route('/Pedidos/', methods=['POST'])
def addPedidos():
    pedidos = Pedidos.create(**request.get_json())
    return jsonify(pedidos)

@app.route('/Pedidos/<int:pedidos_id>', methods=['GET'])
def get_Pedidos(pedidos_id):
    pedidos = Pedidos.find(pedidos_id)
    return jsonify(pedidos)

@app.route('/Pedidos/<int:pedidos_id>', methods=['PATCH'])
def update_Pedidos(pedidos_id):
    pedidos = Pedidos.find_or_fail(pedidos_id)
    pedidos.update(**request.get_json())
    return jsonify(pedidos)



@app.route('/wtspp/', methods=['POST'])
def whtspp():
    body = request.form.get("Body")
    nroFrom = request.form.get("From")
    #app.logger.debug(nroFrom)
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
    mipedido = Pedidos.find(int(pedido))
    app.logger.debug(mipedido.ubicacion)
    app.logger.debug(jsonify(mipedido))
    resp = MessagingResponse()
    app.logger.debug(resp)
    account_sid = 'ACc508aaa6f2b09adc129fd28ec456deef'# Accont_sid Twilio personal
    auth_token = '86001932c3e41b844a2dd17b79f600c2'#Auth_token Twilio personal
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='Twilio HQ',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51917750571'
    )
    msg = resp.message()
    msg.body("Procesando")
    return str(resp)


def findPedidos(nroFrom):
    clientes = Clientes.all()
    app.logger.debug(nroFrom)
    #app.logger.debug(jsonify(clientes))
    idCliente = 0
    for objCliente in clientes:
        #app.logger.debug(objCliente.num_cel)
        if(nroFrom == objCliente.num_cel):
            idCliente = objCliente.id 
            break
    pedidos = Pedidos.all()
    idsPedidos = ''
    for objPedidos in pedidos:
        if(objPedidos.cliente == idCliente):
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
    msg.body('Hola bienvenido al control de pedidos escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
:black_small_square: *'menu':* el menu principal :rocket:
:black_small_square: *'pedidos'*: busca tus pedidos :boom:
""", use_aliases=True)
    msg.body(response)
    return str(resp)
