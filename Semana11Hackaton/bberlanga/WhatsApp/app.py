from flask import Flask, request
from flask_orator import Orator
from models.cliente import Cliente
from models.detalle_factura import Detalle_factura
from models.factura import Factura
from models.pedido import Pedido
from models.producto import Producto
from flask_orator import Orator, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from flask_http_response import success, result, error
import emoji
import logging
import requests
from db import db

from orator.orm import belongs_to
from orator.orm import has_many

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'Wassp',
        'user': 'postgres',
        'password': '3179billace',
        'prefix': ''
    }
}

db = Orator(app)

@app.route('/')
def ok():
    return 'Flask is working'

@app.route('/inicio',methods=['POST'])
def inicio():
    body = request.form.get("Body")
    nroFrom = request.form.get("From")
    app.logger.debug(nroFrom)
    if body == 'menu':
        return show_menu()
    elif body == '3':
        return show_website()
    elif body == '2':
        return show_erecibo(nroFrom)
    elif body == '1':
        return show_estado(nroFrom)
    else:
        return msg_default()

def msg_default():
    resp=MessagingResponse()
    msg=resp.message()
    msg.body('Hola bienvenido! Este es el centro de control de pedidos.\nEscriba menu para mostrarte las opciones.')
    return str(resp)

def show_website():
    resp=MessagingResponse()
    msg=resp.message()
    msg.body('https://vans.com.pe/')
    return str(resp)

def show_erecibo(nroFrom):
    resp=MessagingResponse()
    msg=resp.message()
    clnt=Cliente.where('número_telefonico',nroFrom[9:100]).first()
    fact=Factura.where('cliente_id',clnt.id).first()
    usr_nombre=clnt.nombre
    msg.body('Hola '+ usr_nombre+" este es tu recibo:"+"\nsub total: "+str(fact.sub_total)+"\n IGV: "+str(fact.IGV)+"\n total: "+str(fact.monto_total))
    return str(resp)

def show_estado(nroFrom):
    resp=MessagingResponse()
    msg=resp.message()
    app.logger.debug(nroFrom[9:100])
    clnt=Cliente.where('número_telefonico',nroFrom[9:100]).first()
    usr_nombre=clnt.nombre
    usr_id=clnt.id
    app.logger.debug(usr_id)
    ped=Pedido.where('cliente_id',usr_id).first()
    usr_fec_entrg=ped.fecha_entrega
    msg.body('Hola '+usr_nombre+', tienes un pedido con entrega para el día '+str(usr_fec_entrg)+'\nEscriba menu para volver a ver las opciones.')
    return str(resp)

def show_menu():
    resp=MessagingResponse()
    msg=resp.message()
    response = emoji.emojize("""
*Eliga alguna de las opciones del menu:*

:black_small_square: Escriba *1* para ver el estado de su *pedido* :package:
:black_small_square: Escriba *2* para ver su *recibo electronico* :receipt:
:black_small_square: Escriba *3* para visitar nuestra *página web* :compass:
return str(resp)
    """, use_aliases=True)
    msg.body(response)
    return str(resp)

#CRUD cliente
#get all
@app.route('/cliente_all')
def clientes_all():
    clnt=Cliente.all()
    return jsonify(clnt)
#get one
@app.route('/cliente/<cliente_id>',methods=['GET'])
def get_clienteid(cliente_id):
    clnt=Cliente.find(int(cliente_id))
    return jsonify(clnt)
#post one
@app.route('/cliente/post', methods=['POST'])
def create_cliente():
    clnt = Cliente.create(**request.get_json())
    return jsonify(clnt)
#patch
@app.route('/cliente/patch/<cliente_id>', methods=['PATCH'])
def update_cliente(cliente_id):
    clnt = Cliente.find_or_fail(cliente_id)
    clnt.update(**request.get_json())
    return jsonify(clnt)
#delete
@app.route('/cliente/delete/<cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    clnt = Cliente.find_or_fail(cliente_id)
    clnt.delete()
    return app.response_class('No Content', 204)

#CRUD producto
#get all
@app.route('/producto_all')
def productos_all():
    prdt=Producto.all()
    return jsonify(prdt)
#get one
@app.route('/producto/<producto_id>',methods=['GET'])
def get_productoid(producto_id):
    prdt=Producto.find(int(producto_id))
    return jsonify(prdt)
#post one
@app.route('/producto/post', methods=['POST'])
def create_producto():
    prdt = Producto.create(**request.get_json())
    return jsonify(prdt)
#patch
@app.route('/producto/patch/<producto_id>', methods=['PATCH'])
def update_producto(producto_id):
    prdt = Producto.find_or_fail(producto_id)
    prdt.update(**request.get_json())
    return jsonify(prdt)
#delete
@app.route('/producto/delete/<producto_id>', methods=['DELETE'])
def delete_product(producto_id):
    prdt = Producto.find_or_fail(producto_id)
    prdt.delete()
    return app.response_class('No Content', 204)


#CRUD pedido
#get all
@app.route('/pedido_all')
def pedido_all():
    pedidos=Pedido.all()
    for ped in pedidos:
        id_p=ped.id
        clnt_id=ped.cliente_id
        fct_id=ped.factura_id
        fch_desp=ped.fecha_despacho
        fch_ent=ped.fecha_entrega
        est=ped.estado
        dict_pedido={'id':id_p,'cliente_id':clnt_id,'factura_id':fct_id,'fecha_despacho':fch_desp,'fecha_entrega':fch_ent,'estado':est}
        return dict_pedido
#get one
@app.route('/pedido/<pedido_id>',methods=['GET'])
def get_prodcutoid(pedido_id):
    ped=Pedido.find(int(pedido_id))
    id=ped.id
    clnt_id=ped.cliente_id
    fct_id=ped.factura_id
    fch_desp=ped.fecha_despacho
    fch_ent=ped.fecha_entrega
    est=ped.estado
    dict_pedido={'id':id,'cliente_id':clnt_id,'factura_id':fct_id,'fecha_despacho':fch_desp,'fecha_entrega':fch_ent,'estado':est}
    return dict_pedido
#post one
@app.route('/pedido/post', methods=['POST'])
def create_pedido():
    ped = Pedido.create(**request.get_json())
    return jsonify(ped)
#patch
@app.route('/pedido/patch/<pedido_id>', methods=['PATCH'])
def update_pedido(pedido_id):
    ped = Pedido.find_or_fail(pedido_id)
    ped.update(**request.get_json())
    return jsonify(ped)
#delete
@app.route('/pedido/delete/<pedidoo_id>', methods=['DELETE'])
def delete_pedido(pedido_id):
    ped = Pedido.find_or_fail(pedido_id)
    ped.delete()
    return app.response_class('No Content', 204)
# nroFrom="+51902088243"
# clnt=Cliente.where('número_telefonico','+51902088243').first()
# print(clnt)
# print(clnt.id)




# class Cliente(db.Model):    
#     __fillable__ = ['nombre','correo','número_telefonico']

#     def __repr__(self):
        # return '<User %r>' % self.name
    
#     @has_many
#     def factura(self):
#         return Factura

# class Prodcuto(db.Model):    
#     __fillable__ = ['nombre','precio']

#     def __repr__(self):
#         return '<User %r>' % self.name
    
#     @has_many
#     def detallle_producto(self):
#         return Detalle_Producto

#     @has_many
#     def detallle_factura(self):
#         return Detalle_factura

# class Factura(db.Model):    
#     __fillable__ = ['fecha','sub_total','IGV','monto_total']

#     @has_many
#     def detallle_factura(self):
#         return Detalle_factura

#     @has_many
#     def pedido(self):
#         return Pedido
    
#     @belongs_to
#     def cliente(self):
#         return Cliente

# class Detalle_factura(db.Model):    
#     __fillable__ = ['cantidad','sub_total','IGV','monto_total']
    
#     @belongs_to
#     def factura(self):
#         return Factura
    
#     @belongs_to
#     def producto(self):
#         return Producto

# class Pedido(db.Model):    
#     __fillable__ = ['fecha_despacho','fecha_entrega']

#     @belongs_to
#     def cliente(self):
#         return Cliente
    
#     @belongs_to
#     def detalle_factura(self):
#         return Detalle_factura

