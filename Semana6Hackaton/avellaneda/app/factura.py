class factura:
    def __init__(self, idfacCabecera, idempresa, idclientes, idtipoPago, igvFacCabecera, subtotalFacCabecera, totalFacCabecera, fechaFacCabecera, estadoFactura):
        self.idfacCabecera = idfacCabecera
        self.idempresa = idempresa
        self.idclientes = idclientes
        self.idtipoPago = idtipoPago
        self.igvFacCabecera = igvFacCabecera
        self.subtotalFacCabecera = subtotalFacCabecera
        self.totalFacCabecera = totalFacCabecera
        self.fechaFacCabecera = fechaFacCabecera
        self.estadoFactura = estadoFactura