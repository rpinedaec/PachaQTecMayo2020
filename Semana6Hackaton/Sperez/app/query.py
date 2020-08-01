class Querys:
    


    #Clientes

    def SelectAllClientes(self):
        query = "SELECT idCliente, nombreCliente AS Nombre, nroidentificacionCliente AS ID, direccionCliente AS Direccion FROM cliente;"
        return query
    
    def SelectDniCliente(self, dni):
        query = "SELECT idCliente, nombreCliente AS Nombre, nroidentificacionCliente AS ID, direccionCliente AS Direccion FROM "+self.dato+".cliente where nroidentificacionCliente = '"+dni+"';"
        return query

    def SelectIdCliente(self, id):
        query = "SELECT idCliente, nombreCliente AS Nombre, nroidentificacionCliente AS ID, direccionCliente AS Direccion FROM "+self.dato+".cliente where idCliente = '"+id+"';"
        return query

    def UpdateCliente(self, Id, Nombre, Dni, Direccion):
        query = "UPDATE "+self.dato+".clientes set nombreCliente = '"+Nombre+"', nroidentificacionCliente = '"+Dni+"',direccionCliente = '"+Direccion+"' where idCliente = "+Id+";"
        return query

    def InsertCliente(self, Nombre, Dni, Direccion):
        query = "INSERT INTO "+self.dato+".cliente (nombreCliente, nroidentificacionCliente,direccionCliente) values('"+Nombre+"','"+Dni+"','"+Direccion+"');"
        return query

    def DeleteCliente(self, Id):
        query = "DELETE FROM "+self.dato+".cliente where idCliente = '"+Id+"' ;"
        return query

    #Productos

    def SelectAllProductos(self):
        query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM "+self.dato+".productos;"
        return query
    
    def SelectNomProducto(self, NombreProd):
        query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM "+self.dato+".productos where nombreProducto = '"+NombreProd+"';"
        return query

    def SelectIdProducto(self, id):
        query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM "+self.dato+".productos where idproducto = '"+id+"';"
        return query

    def UpdateProducto(self, Id, NombreProd, Valor, Igv):
        query = "UPDATE "+self.dato+".productos SET nombreProducto = '"+NombreProd+"', valorProducto = "+Valor+", igvProducto = "+Igv+" WHERE idproducto = "+Id+";"
        return query

    def InsertProducto(self, NombreProd, Valor, Igv):
        query = "INSERT INTO "+self.dato+".productos ( nombreProducto, valorProducto, igvProducto) VALUES ( '"+NombreProd+"', "+Valor+", "+Igv+");"
        return query

    def DeleteProducto(self, Id):
        query = "DELETE FROM "+self.dato+".productos WHERE idproducto = "+Id+" ;"
        return query

    #Empresa

    def SelectAllEmpresas(self):
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM "+self.dato+".empresa;"
        return query
    
    def SelectRucEmpresa(self, NumRuc):
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM "+self.dato+".empresa where rucEmpresa = '"+NumRuc+"';"
        return query

    def SelectIdEmpresa(self, id):
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM "+self.dato+".empresa where idempresa = '"+id+"';"
        return query

    def UpdateEmpresa(self, Id, NumRuc, NombreEmp):
        query = "UPDATE "+self.dato+".empresa SET rucEmpresa = '"+NumRuc+"', nombreEmpresa  = '"+NombreEmp+"' WHERE idempresa = "+Id+";"
        return query

    def InsertEmpresa(self, NumRuc, NombreEmp):
        query = "INSERT INTO "+self.dato+".empresa ( rucEmpresa, nombreEmpresa) VALUES ('"+NumRuc+"', '"+NombreEmp+"');"
        return query

    def DeleteEmpresa(self, Id):
        query = "DELETE FROM "+self.dato+".empresa WHERE idEmpresa = "+Id+";"
        return query

    #Tipo de Pago

    def SelectAllTipos(self):
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM "+self.dato+".tipopago;"
        return query
    
    def SelectNomTipo(self, NombreTipo):
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM "+self.dato+".tipopago WHERE descTipoPago = '"+NombreTipo+"';"
        return query

    def SelectIdTipo(self, id):
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM "+self.dato+".tipopago WHERE idtipoPago = '"+id+"';"
        return query

    def UpdateTipo(self, Id, NombreTipo):
        query = "UPDATE "+self.dato+".tipopago SET descTipoPago = '"+NombreTipo+"' WHERE idtipoPago = "+Id+";"
        return query

    def InsertTipo(self, NombreTipo):
        query = "INSERT INTO "+self.dato+".tipopago(descTipoPago)VALUES('"+NombreTipo+"');"
        return query

    def DeleteTipo(self, Id):
        query = "DELETE FROM "+self.dato+".tipopago WHERE idtipoPago = "+Id+";"
        return query

    #faccabecera

    def InsertCabecera(self, idEmpresa, idCliente, idTipoPago, igvProd, subTotal, Total):
        query = "INSERT INTO "+self.dato+".faccabecera (idempresa, idcliente, idtipoPago, fechaFacCabecera, igvFacCabecera, subtotalFacCabecera, totalFacCabecera, estadoFactura) VALUES ('"+idEmpresa+"', '"+idCliente+"', '"+idTipoPago+"', sysdate(), '"+igvProd+"', '"+subTotal+"', '"+Total+"', '1');"
        return query

    def SelectAllCabecera(self):
        query = """SELECT c.idfacCabecera, e.nombreEmpresa, cl.nombreCliente, t.descTipoPago, c.igvFacCabecera, c.subtotalFacCabecera, c.totalFacCabecera, c.fechaFacCabecera 
        FROM """+self.dato+""".faccabecera c 
        INNER JOIN """+self.dato+""".empresa e ON c.idempresa = e.idempresa 
        INNER JOIN """+self.dato+""".clientes cl ON c.idcliente = cl.idcliente 
        INNER JOIN """+self.dato+""".tipopago t ON c.idtipoPago = t.idtipoPago;"""
        return query

    def SelectIdCabecera(self, id):
        query = """SELECT c.idfacCabecera, e.nombreEmpresa, cl.nombreCliente, t.descTipoPago, c.igvFacCabecera, c.subtotalFacCabecera, c.totalFacCabecera, c.fechaFacCabecera 
        FROM """+self.dato+""".faccabecera c 
        INNER JOIN """+self.dato+""".empresa e ON c.idempresa = e.idempresa 
        INNER JOIN """+self.dato+""".clientes cl ON c.idcliente = cl.idcliente 
        INNER JOIN """+self.dato+""".tipopago t ON c.idtipoPago = t.idtipoPago 
        WHERE c.idfacCabecera = '"""+id+"""';"""
        return query    
    
    def UpdateCabecera(self, idCabecera,igvCabecera):
        query = """ UPDATE """+self.dato+""".faccabecera SET igvFacCabecera = '"""+str(igvCabecera)+"""', 
        subtotalFacCabecera = ("""+str("""SELECT SUM(valorFacDetalle) 
        FROM """+self.dato+""".facdetalle WHERE idfacCabecera = '"""+str(idCabecera)+"""'""")+"""), 
        totalFacCabecera = ((""" +str("""SELECT SUM(valorFacDetalle) 
        FROM """+self.dato+""".facdetalle WHERE idfacCabecera = '"""+str(idCabecera)+"""') + '"""+str(igvCabecera)+"""'""" )+""") WHERE idfacCabecera = '"""+str(idCabecera)+"""';"""
        return query
    
    #facdetalle

    def InsertDetalle(self, idfacCabecera, idProducto, cantprod, valortotal):
        query = "INSERT INTO "+self.dato+""".facdetalle 
        (idfacCabecera, idproducto, cantFacDetalle, valorFacDetalle) VALUES
        ('"""+str(idfacCabecera)+"', '"+str(idProducto)+"', '"+str(cantprod)+"', '"+str(valortotal)+"');"""
        return query

    def SelectDetalle(self, idfaccabecera):        
        query = """SELECT d.cantFacDetalle, p.nombreProducto, p.valorProducto, d.valorFacDetalle 
        FROM """+self.dato+""".facdetalle d 
        INNER JOIN """+self.dato+""".productos p ON d.idproducto = p.idproducto 
        WHERE d.idfacCabecera = '"""+str(idfaccabecera)+"""';"""
        return query