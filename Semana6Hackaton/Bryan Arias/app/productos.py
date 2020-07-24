import utils
class productos:
    __log = utils.log("Productos")
    def __init__(self,idProducto,nombreProducto,valorProducto,igvProducto):
        self.idProducto = idProducto
        self.nombreProducto = nombreProducto
        self.valorProducto = valorProducto
        self.igvProducto = igvProducto