from orator import Model


class Pedido(Model):
    __table__ = 'pedidos'
    __fillable__ = ['ubicacion', 'cliente_id', 'producto_id']