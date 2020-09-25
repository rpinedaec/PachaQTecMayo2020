from orator import Model


class Productos(Model):

    __table__ = 'Productos'
    __primary_key__ = 'id'
    __fillable__ = ['descripcion', 'cantidad', 'precio']