from models import Producto
from app import db

class ProductoController():

    def getProducto():
        myproducto=Producto.producto.all()
        return myproducto

