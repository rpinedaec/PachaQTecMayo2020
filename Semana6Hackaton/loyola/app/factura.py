class FacCabecera:
    def __init__(self, idfacCabecera, idempresa, idcliente, idtipoPago, fechaFacCabecera, 
                igvFacCabecera, subtotalFacCabecera, totalFacCabecera, estadoFactura):
        self.idfacCabecera = idfacCabecera
        self.idempresa = idempresa
        self.idcliente = idcliente
        self.idtipoPago = idtipoPago
        self.fechaFacCabecera = fechaFacCabecera
        self.igvFacCabecera = igvFacCabecera
        self.subtotalFacCabecera = subtotalFacCabecera
        self.totalFacCabecera = totalFacCabecera
        self.estadoFactura = estadoFactura

class FacDetalle:
    def __init__(self, idfacDetalle, idproductos, idfacCabecera, cantFacDetalle, valorFacDetalle):
        self.idfacDetalle = idfacDetalle
        self.idproductos = idproductos
        self.idfacCabecera = idfacCabecera
        self.cantFacDetalle = cantFacDetalle
        self.valorFacDetalle = valorFacDetalle



