class factura:
    def __init__(self,idFacCabecera,idEmpresa,IdCliente,IdTipoPago,FechaFactura,IgvFacCabecera,SubtotalCabecera,
                 TotalCabecera,IdFacDetalle,Idproducto,CantFacDetalle,ValorFacDetalle,EstadoFactura):
        self.idFacCabecera=idFacCabecera
        self.idEmpresa = idEmpresa
        self.IdCliente = IdCliente
        self.IdTipoPago = IdTipoPago
        self.FechaFactura = FechaFactura
        self.IgvFacCabecera = IgvFacCabecera
        self.SubtotalCabecera = SubtotalCabecera
        self.TotalCabecera = TotalCabecera
        self.IdFacDetalle = IdFacDetalle
        self.Idproducto = Idproducto
        self.CantFacDetalle = CantFacDetalle
        self.ValorFacDetalle = ValorFacDetalle
        self.EstadoFactura = EstadoFactura
