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
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    producto = db.relationship('Producto', backref='product', lazy='dynamic')

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    stock = db.Column(db.Integer)
    precio = db.Column(db.Numeric(10,2))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    det_comprobante_prod = db.relationship('Det_comprobante', backref='det_comprobant_prod', lazy='dynamic')

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8))
    nombre = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    comprobante = db.relationship('Cab_comprobante', backref='cab_comprobant', lazy='dynamic')

class Cab_comprobante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10))
    tipo_comprobante_id = db.Column(db.Integer)
    nro_comprobante = db.Column(db.String(8))
    igv = db.Column(db.Numeric(10,2))
    total = db.Column(db.Numeric(10,2))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    det_comprobante = db.relationship('Det_comprobante', backref='det_comprobant', lazy='dynamic')
    #cliente = db.relationship('Cliente', backref='client', lazy='dynamic')

class Det_comprobante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Numeric(10,2))
    subtotal = db.Column(db.Numeric(10,2))
    cab_comprobante_id = db.Column(db.Integer, db.ForeignKey('cab_comprobante.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    #cab_comprobante_id = db.relationship('Cab_comprobante', backref='cab_comprobante', lazy='dynamic')
    #producto = db.relationship('Producto', backref='produc', lazy='dynamic')


