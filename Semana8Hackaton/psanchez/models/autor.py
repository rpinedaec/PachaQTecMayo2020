from orator import Model


class Autor(Model):

    __table__ = 'autor'
    __primary_key__ = 'autor_id'