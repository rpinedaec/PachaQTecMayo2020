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
    DetalleCompra = db.relationship('DetalleCompra', backref='detalleCompra', lazy='dynamic')


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    ruc = db.Column(db.Integer)
    direccion = db.Column(db.String(255), index=True)
    Compra = db.relationship('Compra', backref='compra', lazy='dynamic')


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correlativo = db.Column(db.Integer)
    subtotal = db.Column(db.Numeric(10,2))
    igv = db.Column(db.Numeric(10,2))
    total = db.Column(db.Numeric(10,2))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    fecha = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    DetalleCompra = db.relationship('DetalleCompra', backref='DetalleCompra', lazy='dynamic')


class DetalleCompra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Numeric(10,2))
    precio = db.Column(db.Numeric(10,2))
    subtotal = db.Column(db.Numeric(10,2))
    compra_id = db.Column(db.Integer, db.ForeignKey('compra.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))

