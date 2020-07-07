class Querys:

    def __init__(self, dato):
        self.dato = dato

    #Crear BASE DE DATOS

    def CreateDB(self):
        query = "CREATE DATABASE IF NOT EXISTS "+self.dato+";"
        return query

    #Clientes

    def SelectAllClientes(self):
        query = "SELECT idCliente, nombreCliente AS Nombre, nroIdentidicacionCliente AS ID, direccionCliente AS Direccion FROM "+self.dato+".clientes;"
        return query

    def SelectDniCliente(self, dni):
        query = "SELECT idCliente, nombreCliente AS Nombre, nroIdentidicacionCliente AS ID, direccionCliente AS Direccion FROM "+self.dato+".clientes where nroIdentidicacionCliente = '"+dni+"';"
        return query

    def SelectIdCliente(self, id):
        query = "SELECT idCliente, nombreCliente AS Nombre, nroIdentidicacionCliente AS ID, direccionCliente AS Direccion FROM "+self.dato+".clientes where idCliente = '"+id+"';"
        return query

    def UpdateCliente(self, Id, Nombre, Dni, Direccion):
        query = "UPDATE "+self.dato+".clientes set nombreCliente = '"+Nombre+"', nroIdentidicacionCliente = '"+Dni+"',direccionCliente = '"+Direccion+"' where idCliente = "+Id+";"
        return query

    def InsertCliente(self, Nombre, Dni, Direccion):
        query = "INSERT INTO "+self.dato+".clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('"+Nombre+"','"+Dni+"','"+Direccion+"');"
        return query

    def DeleteCliente(self, Id):
        query = "DELETE FROM "+self.dato+".clientes where idCliente = '"+Id+"' ;"
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
        query = "SELECT idtipopago, descTipoPago as Descripcion FROM "+self.dato+".tipopago;"
        return query

    def SelectNomTipo(self, NombreTipo):
        query = "SELECT idtipopago, descTipoPago as Descripcion FROM "+self.dato+".tipopago WHERE descTipoPago = '"+NombreTipo+"';"
        return query

    def SelectIdTipo(self, id):
        query = "SELECT idtipopago, descTipoPago as Descripcion FROM "+self.dato+".tipopago WHERE idtipopago = '"+id+"';"
        return query

    def UpdateTipo(self, Id, NombreTipo):
        query = "UPDATE "+self.dato+".tipopago SET descTipoPago = '"+NombreTipo+"' WHERE idtipopago = "+Id+";"
        return query

    def InsertTipo(self, NombreTipo):
        query = "INSERT INTO "+self.dato+".tipopago(descTipoPago)VALUES('"+NombreTipo+"');"
        return query

    def DeleteTipo(self, Id):
        query = "DELETE FROM "+self.dato+".tipopago WHERE idtipopago = "+Id+";"
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

    #Crear Tablas

    def CreateTablas(self):
        query = """
        CREATE TABLE IF NOT EXISTS `"""+self.dato+"""`.`empresa` ( 
            `idempresa` INT(11) NOT NULL AUTO_INCREMENT,
            `rucEmpresa` VARCHAR(45) NOT NULL, 
            `nombreEmpresa` VARCHAR(45) NOT NULL,
            PRIMARY KEY (`idempresa`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
             
        CREATE TABLE IF NOT EXISTS `"""+self.dato+"""`.`tipoPago` (
            `idtipoPago` INT(11) NOT NULL AUTO_INCREMENT,
            `descTipoPago` VARCHAR(45) NOT NULL,
            PRIMARY KEY (`idtipoPago`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
        
        CREATE TABLE IF NOT EXISTS `"""+self.dato+"""`.`clientes` (
            `idcliente` INT(11) NOT NULL AUTO_INCREMENT,
            `nombreCliente` VARCHAR(45) NOT NULL,
            `nroIdentidicacionCliente` VARCHAR(45) NOT NULL,
            `direccionCliente` VARCHAR(200) NOT NULL,
            PRIMARY KEY (`idcliente`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
            
        CREATE TABLE IF NOT EXISTS `"""+self.dato+"""`.`productos` (
            `idproducto` INT(11) NOT NULL AUTO_INCREMENT,
            `nombreProducto` VARCHAR(45) NOT NULL,
            `valorProducto` DECIMAL(18,2) NOT NULL,
            `igvProducto` TINYINT(4) NOT NULL,
            PRIMARY KEY (`idproducto`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
            
        CREATE TABLE IF NOT EXISTS `"""+self.dato+"""`.`facCabecera` (
            `idfacCabecera` INT(11) NOT NULL AUTO_INCREMENT,
            `idempresa` INT(11) NOT NULL,
            `idcliente` INT(11) NOT NULL,
            `idtipoPago` INT(11) NOT NULL,
            `fechaFacCabecera` DATETIME NOT NULL DEFAULT NOW(),
            `igvFacCabecera` DECIMAL(18,2) NOT NULL,
            `subtotalFacCabecera` DECIMAL(18,2) NOT NULL,
            `totalFacCabecera` DECIMAL(18,2) NOT NULL,
            `estadoFactura` CHAR(1) NOT NULL,
            PRIMARY KEY (`idfacCabecera`),
            INDEX `fk_facCabecera_empresa1_idx` (`idempresa` ASC) VISIBLE,
            INDEX `fk_facCabecera_tipoPago1_idx` (`idtipoPago` ASC) VISIBLE,
            INDEX `fk_facCabecera_clientes1_idx` (`idcliente` ASC) VISIBLE,
            CONSTRAINT `fk_facCabecera_empresa1`
                FOREIGN KEY (`idempresa`)
                REFERENCES `"""+self.dato+"""`.`empresa` (`idempresa`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `fk_facCabecera_tipoPago1`
                FOREIGN KEY (`idtipoPago`)
                REFERENCES `"""+self.dato+"""`.`tipoPago` (`idtipoPago`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `fk_facCabecera_clientes1`
                FOREIGN KEY (`idcliente`)
                REFERENCES `"""+self.dato+"""`.`clientes` (`idcliente`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
            CREATE TABLE IF NOT EXISTS `"""+self.dato+"""`.`facDetalle` (
            `idfacDetalle` INT(11) NOT NULL AUTO_INCREMENT,
            `idfacCabecera` INT(11) NOT NULL,
            `idproducto` INT(11) NOT NULL,
            `cantFacDetalle` INT(11) NOT NULL,
            `valorFacDetalle` DECIMAL(18,2) NOT NULL,
            PRIMARY KEY (`idfacDetalle`),
            INDEX `fk_facDetalle_facCabecera_idx` (`idfacCabecera` ASC) VISIBLE,
            INDEX `fk_facDetalle_productos1_idx` (`idproducto` ASC) VISIBLE,
            CONSTRAINT `fk_facDetalle_facCabecera`
                FOREIGN KEY (`idfacCabecera`)
                REFERENCES `"""+self.dato+"""`.`facCabecera` (`idfacCabecera`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `fk_facDetalle_productos1`
                FOREIGN KEY (`idproducto`)
                REFERENCES `"""+self.dato+"""`.`productos` (`idproducto`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
            SET SQL_MODE=@OLD_SQL_MODE;
            SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
            SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
            """
        return query 