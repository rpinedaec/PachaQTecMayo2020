from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from app import login
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreCategoria = db.Column(db.String(64), index=True)
    producto = db.relationship('Producto', backref='product', lazy='dynamic')

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreCliente = db.Column(db.String(100), index=True)
    dniCliente = db.Column(db.String(100), index=True)
    direcccionCliente = db.Column(db.String(100), index=True)
    facturacabecera = db.relationship('FacturaCabecera', backref='facturacabecera', lazy='dynamic')

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreEmpresa = db.Column(db.String(100), index=True)
    direcccionEmpresa = db.Column(db.String(100), index=True)
    facturacabecera = db.relationship('FacturaCabecera', backref='facturacabecera', lazy='dynamic')

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(100), index=True)
    stock = db.Column(db.Integer)
    precio = db.Column(db.Numeric(10,2))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    facturadetalle = db.relationship('FacturaDetalle', backref='facturadetalle', lazy='dynamic')

class FacturaCabecera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    subtotal = db.Column(db.Numeric(10,2))
    igvTotal = db.Column(db.Numeric(10,2))
    total = db.Column(db.Numeric(10,2))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'))
    facturadetalle = db.relationship('FacturaDetalle', backref='facturadetalle', lazy='dynamic')

class FacturaDetalle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    valor = db.Column(db.Numeric(10,2))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    facturacabecera_id = db.Column(db.Integer, db.ForeignKey('factura_cabecera.id'))

class VentaDiaria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venta = db.Column(db.Numeric(10,2))
