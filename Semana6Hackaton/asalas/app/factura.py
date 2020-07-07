class Factura:
   

    def getNombreEmpresa(self):
        return self.nombreEmpresa

    def getNombreCliente(self):
        return self.nomcliente

    def getProducto(self):
        return self.nombreProducto
        return self.valorProducto
        return self.igvProducto

    def getTipoPago(self):
        return self.desctipopago

    def __init__(self, unidad):
        self.unidad = unidad

    def a_pagar(self):
        total = self.unidad * self.valorProducto
        impuesto = total * self.igvProducto / 100
        return(total + impuesto)
