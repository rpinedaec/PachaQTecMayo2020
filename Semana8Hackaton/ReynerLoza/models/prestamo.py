from orator import Model


class Prestamos(Model):

    __table__ = 'prestamos'
    __primary_key__ = 'prestamo_id'
