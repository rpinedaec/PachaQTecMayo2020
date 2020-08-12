import os
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
    return "bienvenndos al inicio de mi aplicacion"

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
    elif body == 'addpedidos':
        return addPedidos()
    elif body == 'deletepedido':
        return deletePedido()
    else:
        return msgDefault()

def detallePedido(body):
    pedido = body.replace('mipedido', '')
    pedido = pedido.strip()
    app.logger.debug(pedido)
    mipedido = Pedido.find(int(pedido))
    app.logger.debug(jsonify(mipedido))
    resp = MessagingResponse()
    account_sid = 'AC40e6e46f3f84ccfbf04e59939cc19ace'
    auth_token = '0152f03507dc864170b6e8b16435f674'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body='Twilio HQ',
            persistent_action=[f'{mipedido.ubicacion}'],
            to='whatsapp:+51999042187'
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

def addPedidos():
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))    
    pedidoform = 'Ingrese su pedido en el siguiente orden => ubicacion, cliente id, producto id: ' 
    msg.body(pedidoform)
    for body in pedido:
        elpedido = Pedido.create(str(body))
        app.logger.debug(jsonify(mipedido))
        save()

def deletePedido():
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))    
    findPedidos()
    deletewut = 'Cual desea eliminar?'
    msg.body(deletewut)
    pedidos = Pedido.all()
    idsPedidos = ''
    for objPedidos in pedidos:
        if(idsPedidos == pedidos_id):
            app.logger.debug(objPedidos.id)
            elpedido = Pedido.delete(str(elpedido))
            app.logger.debug(jsonify(mipedido))
            save()
        else:
            break


def findProducto(nroFrom):
    productos = Producto.all()
    app.logger.debug(jsonify(productos))
    idProducto = 0
    for objProducto in productos:
        app.logger.debug(objProducto.id)
        if(nroFrom == objProducto.id):
            idProducto = objProducto.id 
            break
    productos = Producto.all()
    idsProductos = ''
    for objProducto in productos:
        if(objProducto.productos_id == idProducto):
            app.logger.debug(objProducto.id)
            idsProductos += str(objProducto.id) +' '
            break
    respuesta = ''
    if idsProductos == '':
        respuesta = 'No existe ese producto'
    
    resp = MessagingResponse()
    msg = resp.message()
    return str(resp)

    
def addProducto():
    productos = Producto.all()
    app.logger.debug(jsonify(productos))    
    productoform = 'Ingrese el nombre del producto: ' 
    msg.body(pedidoform)
    for body in producto:
        producto = Producto.create(str(Producto))
        app.logger.debug(jsonify(Producto))
        save()

def deleteProducto():
    productos = Producto.all()
    app.logger.debug(jsonify(productos))    
    findProducto()
    deletewutpr = 'Cual desea eliminar?'
    msg.body(deletewutpr)
    productos = Producto.all()
    idsProductos = ''
    for objProducto in prpductos:
        if(idsProductos == productos_id):
            app.logger.debug(objProducto.id)
            elproducto = Producto.create(str(i))
            app.logger.debug(jsonify(elproducto))
            save()
        else:
            break


def findCliente(nroFrom):
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))
    idCliente = 0
    for objCliente in clientes:
        app.logger.debug(objCliente.id)
        if(nroFrom == objCliente.id):
            idCliente = objCliente.id 
            break
    clientes = Cliente.all()
    idsClientes = ''
    for objCliente in clientes:
        if(objCliente.clientes_id == idCliente):
            app.logger.debug(objCliente.id)
            idsClientes += str(objCliente.id) +' '
            break
    respuesta = ''
    if idsClientes == '':
        respuesta = 'No existe ese cliente'
    
    resp = MessagingResponse()
    msg = resp.message()
    return str(resp)

    
def addClientes():
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))    
    clienteform = 'Ingrese el cliente de la siguiente manera: <nombre>, <email>, <telefono>' 
    msg.body(clienteform)
    for body in cliente:
        cliente = Cliente.create(str(cliente))
        app.logger.debug(jsonify(Cliente))
        save()

def deleteCliente():
    clientes = Cliente.all()
    app.logger.debug(jsonify(clientes))    
    findCliente()
    deletewutcl = 'Cual desea eliminar?'
    msg.body(deletewutcl)
    clientes = Cliente.all()
    idsCliente = ''
    for objCliente in clientes:
        if(idsCliente == clientes_id):
            app.logger.debug(objCliente.id)
            elcliente = Cliente.create(str(i))
            app.logger.debug(jsonify(elcliente))
            save()
        else:
            break


    


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
    __fillable__=['ubicacion', 'cliente_id', 'producto_id']