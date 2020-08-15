from orator import Model


class Producto(Model):
    __fillable__ = ['nombre', 'precio']
    __table__ = 'producto'
