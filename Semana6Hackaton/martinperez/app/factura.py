class facturaCabecera:
    def __init__(self,idfacCabecera, empresa, cliente, tipoPago,fechaFacCabecera
                      ,igvFacCabecera,subtotalFacCabecera,totalFacCabecera,estadoFactura):
        self.idfacCabecera = idfacCabecera
        self.empresa = empresa
        self.cliente = cliente
        self.tipoPago = tipoPago
        self.fechaFacCabecera = fechaFacCabecera
        self.igvFacCabecera = igvFacCabecera
        self.subtotalFacCabecera = subtotalFacCabecera
        self.totalFacCabecera = totalFacCabecera
        self.estadoFactura = estadoFactura


class facDetalle:
    def __init__(self,idFacDetalle, facCabecera, producto, cantidad, valor, afecto):
        self.idFacDetalle = idFacDetalle
        self.facCabecera =  facCabecera
        self.producto = producto
        self.cantidad = cantidad
        self.valor = valor
        self.afecto = afecto



class facDetalleInsertar:
    def __init__(self,idFacDetalle, idfacCabecera, idproducto, cantFacDetalle, valorFacDetalle, afecto):
        self.idFacDetalle = idFacDetalle
        self.idfacCabecera =  idfacCabecera
        self.idproducto = idproducto
        self.cantFacDetalle = cantFacDetalle
        self.valorFacDetalle = valorFacDetalle 
        self.afecto = afecto



