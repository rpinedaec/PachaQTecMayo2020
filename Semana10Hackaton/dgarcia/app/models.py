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

class TipoDocumento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50), index=True)
    cliente = db.relationship('Cliente', backref='cliente', lazy='dynamic')

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'))
    numero_documento = db.Column(db.String(10))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    factura = db.relationship('Factura', backref='factura', lazy='dynamic')

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    fecha = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    detalle = db.relationship('DetalleFactura', backref='detalle_factura1', lazy='dynamic')

class DetalleFactura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    factura = db.Column(db.Integer, db.ForeignKey('factura.id'))
    producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad = db.Column(db.Integer) 
