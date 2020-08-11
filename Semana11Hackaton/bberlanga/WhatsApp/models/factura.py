from orator import Model


class Factura(Model):
    __fillable__ = ['fecha', 'cliente_id', 'sub_total','IGV','monto_total']
    __table__ = 'factura'
