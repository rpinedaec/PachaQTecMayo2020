from orator import Model


class Cliente(Model):
    __fillable__ = ['nombre', 'correo', 'número_telefonico']
    __table__ = 'cliente'

