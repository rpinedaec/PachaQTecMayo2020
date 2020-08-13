from models import Pedido
from app import db

class PedidoController():

    def getpedido():
        mypedido=Pedido.pedido.all()
        return mypedido

