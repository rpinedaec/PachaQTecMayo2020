
class QueryDB:
    QueryDB = query

    def clientes(self,selectallcliente,selectidcliente,updatecliente,insertcliente,deletecliente):
        self.selectallcliente = "select idclientes, nombrecliente as Nombre, nroidentificacioncliente as DNI, direccioncliente as Direccion from clientes;"
        self.selectidcliente = "select idclientes, nombrecliente as Nombre, nroidentificacioncliente as DNI, direccioncliente as Direccion FROM clientes where nroidentificacioncliente = '"+dni+"';"
        self.updatecliente = "update clientes set nombrecliente = '"+nombre+"', nroidentificacioncliente = '"+dni+"',direccioncliente = '"+direccion"' where idclientes = "+Id+" ;"
        self.insertcliente = "insert into clientes (nombrecliente, nroidentificacioncliente, direccioncliente) values('"+Nombre+"','"+Dni+"','"+Direccion+"');"
        self.deletecliente = "delete from clientes where idcliente = '"+Id+"' ;"

    def producto(self,selectallproductos,selectidproductos,updateproductos,insertproductos,deleteproductos):
        self.selectallproductos = "select idproductos, nombreproducto as Nombre, valorproducto as Precio, igvproducto as IGV from productos;"
        self.selectidproductos = "select idproductos, nombreproducto as Nombre, valorproducto as Precio, igvproducto as IGV from productos where idproductos = '"+Id+"';"
        self.updateproductos = "update productos set nombreproducto = '"+nombre+"', valorproducto = '"+dni+"', igvproducto = '"+direccion"' where idproductos = "+Id+" ;"
        self.insertproductos = "insert into productos (nombreproducto, valorproducto, igvproducto) values('"+Nombre+"','"+Precio+"','"+IGV+"');"
        self.deleteproductos = "delete from productos where idproductos = '"+Id+"' ;"
    
    def empresa(self,selectallempresa,selectidempresa,updateempresa,insertempresa,deleteempresa):
        self.selectallempresa = "select idempresa, rucempresa as Ruc, nombreempresa as Razon_Social from empresa;"
        self.selectidempresa = "select idempresa, rucempresa as Ruc, nombreempresa as Razon_Social from empresa where idempresa = '"+Id+"';"
        self.updateempresa = "update empresa set rucempresa = '"+ruc+"', nombreempresa = '"+nombre+"' where idempresa = "+Id+" ;"
        self.insertempresa = "insert into empresa (rucempresa, nombreemoresa) values('"+ruc+"','"+nombre+"');"
        self.deleteempresa = "delete from empresa where idempresa = '"+Id+"' ;"
    
    def facturadetalle(self,selectdnicliente,selectidcliente,updatecliente,insertcliente,deletecliente):
