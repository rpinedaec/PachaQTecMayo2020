from orator import Model


class Detalle_factura(Model):
    __fillable__ = ['factura_id', 'cantidad','sub_total','IGV','monto_total']
    __table__ = 'detalle_factura'
