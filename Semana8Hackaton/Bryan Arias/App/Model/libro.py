from orator import Model


class Libro(Model):

    __table__ = "Libro"    
    __primary_key__ = 'idLibro'
