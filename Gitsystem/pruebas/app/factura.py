import utils
class factura:
    __log = utils.log("Factura")
    def __init__(self, idCabecera, nombreEmp, nombreClie, tipo, igv, subtotal, total, fecha):
        self.idCabecera = idCabecera
        self.nombreEmp = nombreEmp
        self.nombreClie = nombreClie
        self.tipo = tipo
        self.igv = igv
        self.subtotal = subtotal
        self.total = total
        self.fecha = fecha 