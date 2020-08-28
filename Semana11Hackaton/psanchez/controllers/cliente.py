from models import cliente
from app import db

class ClienteController():

    def getClientes():
        mycliente=cliente.Cliente.all()
        return mycliente
