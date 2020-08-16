from models import pedido
from app import db

class PedidoController():

    def getPedidos():
        mypedido=pedido.Pedido.all()
        return mypedido