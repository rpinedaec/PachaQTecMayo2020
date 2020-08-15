from orator import Model


class Pedido(Model):
    __fillable__ = ['cliente_id', 'factura_id','fecha_despacho','fecha_entrega','estado']
    __table__ = 'pedido'

