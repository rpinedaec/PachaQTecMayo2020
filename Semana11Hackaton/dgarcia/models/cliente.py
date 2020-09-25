from orator import Model


class Cliente(Model):
    __table__ = 'clientes'
    __fillable__ = ['nombre', 'email', 'telefono']