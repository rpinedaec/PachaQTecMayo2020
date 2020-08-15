from app import Cliente
from app import db

class ClienteController():
    def getClientes(self, mycliente):
        mycliente=Cliente.all()
        return mycliente