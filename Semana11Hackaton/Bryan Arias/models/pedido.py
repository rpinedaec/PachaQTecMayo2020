from orator import Model


class Pedidos(Model):

    __table__ = 'Pedidos'
    __primary_key__ = 'id'
    __fillable__ = ['ubicacion', 'cliente', 'producto', 'cantidad']