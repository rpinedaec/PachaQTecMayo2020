from orator import Model


class Clientes(Model):

    __table__ = 'Clientes'
    __primary_key__ = 'id'
    __fillable__ = ['nombres', 'tipo_doc', 'num_doc', 'num_cel']
