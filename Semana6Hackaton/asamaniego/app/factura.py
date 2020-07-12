class factura:
    def __init__(self,fechaFacCabecera, igvFacFactura, subtotalFacCabecera, totalFacCabecera, idempresa,idTipoPago, idcliente, estadoFactura):
        self.fechaFacCabecera = fechaFacCabecera,
        self.igvFacFactura = igvFacFactura
        self.subtotalFacCabecera = subtotalFacCabecera
        self.totalFacCabecera = totalFacCabecera
        self.idempresa = idempresa
        self.idTipoPago = idTipoPago
        self.idcliente = idcliente
        self.estadoFactura = estadoFactura



    
    

class detallefactura(factura):
    def __init__(self, fechaFacCabecera, igvFacFactura, subtotalFacCabecera, totalFacCabecera, idempresa, idTipoPago, idcliente, estadoFactura, listDetalle):
        super().__init__(fechaFacCabecera, igvFacFactura, subtotalFacCabecera, totalFacCabecera, idempresa, idTipoPago, idcliente, estadoFactura)
        self.listDetalle = listDetalle


    def grabarDetalle(self, listaCarrito):
        #insert into facCabecera (fechaFacCabecera, igvFacFactura,subtotalFacCabecera, totalFacCabecera, idempresa, idTipoPago, idcliente, estadoFactura) values(now(),30.45,670,1000,2,2,11,1);
        #insert into facDetalle (cantFactDetalle,idfacCabecera, idproducto, valorFacDetalle) values(12,7, 5,100);
        #insert into facDetalle (cantFactDetalle,idfacCabecera, idproducto, valorFacDetalle) values(8,7, 3,100);




    