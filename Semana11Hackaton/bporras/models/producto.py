from orator import Model


class Producto(Model):
    __table__ = 'productos'
    __fillable__ = ['nombre']