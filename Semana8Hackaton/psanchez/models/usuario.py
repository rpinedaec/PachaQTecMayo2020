from orator import Model


class usuario(Model):

    __table__ = 'usuario'
    __primary_key__ = 'usuario_id'