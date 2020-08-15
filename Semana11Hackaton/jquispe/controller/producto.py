from models import producto
from app import db

class ProductoController():

    def getProductos():
        myproducto=producto.Producto.all()
        return myproducto