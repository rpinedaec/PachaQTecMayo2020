from orator import Model


class Libros(Model):

    __table__ = 'libros'
    __primary_key__ = 'libro_id'
