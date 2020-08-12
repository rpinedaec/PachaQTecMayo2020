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
        'database': 'hackaton11MartinPerez',
        'user': 'postgres',
        'password': 'passmysqlmartin',
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
    return "Martin Perez bienvenidos a mi aplicacion"

@app.route('/cliente/', methods=['GET'])
def getClientes():
    cliente = Cliente.all()
    return jsonify(cliente)

@app.route('/cliente/', methods=['POST'])
def addClientes(): 
    #app.logger.debug(request.args["nombre"])  
    cliente = Cliente.create(request.args)
    return jsonify(cliente)

@app.route('/clienteId/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = Cliente.find(cliente_id)
    return jsonify(cliente)


@app.route('/cliente/<int:cliente_id>', methods=['PATCH'])
def update_user(cliente_id):
    user = Cliente.find_or_fail(cliente_id)
    user.update(request.args)
    return jsonify(user)

@app.route('/clientedelete/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    Clients = Cliente.find_or_fail(cliente_id)
    Clients.delete() 
    return jsonify(Clients)






@app.route('/producto/', methods=['GET'])
def getProducto():
    producto = Producto.all()
    return jsonify(producto)


@app.route('/producto/', methods=['POST'])
def addProductos(): 
    #app.logger.debug(request.args["nombre"])  
    Products = Producto.create(request.args)
    return jsonify(Products)

@app.route('/productoId/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    ProductoId = Producto.find(producto_id)
    return jsonify(ProductoId)


@app.route('/producto/<int:producto_id>', methods=['PATCH'])
def update_prod(producto_id):
    prod = Producto.find_or_fail(producto_id)
    prod.update(request.args)
    return jsonify(prod)

@app.route('/productodelete/<int:producto_id>', methods=['DELETE'])
def delete_prod(producto_id):
    Products = Producto.find_or_fail(producto_id)
    Products.delete() 
    return jsonify(Products)








@app.route('/pedido/', methods=['GET'])
def getPedido():
    Pedid = Pedido.all()
    return jsonify(Pedid)

@app.route('/pedido/', methods=['POST'])
def addPedidos():
    try:
        cliente_id = request.args["cliente_id"]
        cliente = Cliente.find_or_fail(cliente_id)
        try:
            producto_id = request.args["producto_id"]
            Productox = Producto.find_or_fail(producto_id)
            Pedidss = Pedido.create(request.args)
            return jsonify(Pedidss) 
        except: 
            resp1 =  [{'Respuesta':'Producto No Existe 1'}]
            return jsonify(resp1)
    except:
        resp2 =  [{'Respuesta':'Cliente No Existe 2'}]
        return jsonify(resp2)


@app.route('/pedidoId/<int:pedido_id>', methods=['GET'])
def get_pedido(pedido_id):
    pedidoss = Pedido.find(pedido_id)
    return jsonify(pedidoss)



@app.route('/pedido/<int:pedido_id>', methods=['PATCH'])
def update_pedi(pedido_id):  
    try:
        clie_id = request.args["cliente_id"] 
        try: 
            if int(clie_id)>int(0): 
                clienteId = Cliente.find_or_fail(clie_id) 
            else:
                respCli2 =  [{'Respuesta':'Cliente No Existe'}]
                return jsonify(respCli2)
        except:
            respCli1 =  [{'Respuesta':'Cliente No Existe'}]
            return jsonify(respCli1)
    except: 
        pass

    try:
        producto_id = request.args["producto_id"]
        try:
            if int(producto_id)>int(0): 
                ProductId = Producto.find_or_fail(producto_id) 
            else:
                resp1 =  [{'Respuesta':'Producto No Existe'}]
                return jsonify(resp1)   
        except:
            resp2 =  [{'Respuesta':'Producto No Existe'}]
            return jsonify(resp2)   
    except:
        pass
    app.logger.debug("aqui 2")  

    pedi = Pedido.find(pedido_id)
    pedi.update(request.args)
    return jsonify(pedi)


@app.route('/pedidodelete/<int:pedido_id>', methods=['DELETE'])
def delete_pedid(pedido_id):
    Pedids = Pedido.find_or_fail(pedido_id)
    Pedids.delete() 
    return jsonify(Pedids)

 


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
    account_sid = 'ACd15fc0c9f1dafce5df1dc3d67c6e9c37'
    auth_token = '3c1eccba27a9ba8fe695d37c4b204a98'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='FARMACIA',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51927248582'
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
    msg.body('Hola bienvenido al sistema de control de pedidos de Martin Perez escribe *menu* para ver tus opciones')
    return str(resp)

def sendMenu():
    resp = MessagingResponse()
    msg = resp.message()
    response = emoji.emojize("""
*Hola!!! escribe las siguientes opciones* :wave:
You can give me the following commands:
:black_small_square: *'menu':* el menu principal :rocket:
:black_small_square: *'pedidos'*: busca tus pedidos :cat:
:black_small_square: *'perro'*: Don't worry, we have dogs too! :dog:
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

    __fillable__ = ['ubicacion', 'cliente_id', 'producto_id']


