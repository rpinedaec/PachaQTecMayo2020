import utils
class factura:
    __log = utils.log("Factura")
    def __init__(self, idCabecera, nombreEmpresa, nombreCliente, tipo, igv, subTotal, total, fecha):
        self.idCabecera = idCabecera
        self.nombreEmpresa = nombreEmpresa
        self.nombreCliente = nombreCliente
        self.tipo = tipo
        self.igv = igv
        self.subTotal = subTotal
        self.total = total
        self.fecha = fecha