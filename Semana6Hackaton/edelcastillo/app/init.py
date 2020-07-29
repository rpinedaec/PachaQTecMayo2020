import utils
import conexion
import clientes
import empresa
import tipopago
import productos
from datetime import date
from datetime import datetime

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []
lstXProductos = []
lstFactura=[]
lstFacDetalle=[]



def cargarObjetos():
    #Limpio las listas para volver a cargarlas
    while len(lstClientes) > 0:
        lstClientes.pop()
    while len(lstTipoPago) > 0:
        lstTipoPago.pop()
    while len(lstEmpresa) > 0:
        lstEmpresa.pop()
    while len(lstProductos) > 0:
        lstProductos.pop()
                
    print("#################################################################################")
    print("############################ FACTURA DE VENTA ###################################")
    print("#################################################################################")
    ####Cargamos los Clienetes Y Elegimos El Cliente
    conn = conexion.conexionBDD(1)
    query = f"select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        cliente = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(cliente)
    print("Escoja el ID del cliente para la factura")
    print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
    for obj in lstClientes:
        print(
            f"\t{obj.idCliente}\t{obj.nombreCliente}\t{obj.nroIdentidicacionCliente}t\t\t{obj.direccionCliente}")
    idcliente=input()
    #####Cargamos las empresas y elegimos las empresas
    query = f"select idempresa as IdEmpresa, rucEmpresa as RUC, nombreEmpresa as 'Razon Social' from empresa;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        empresas1= empresa.empresa(row[0], row[1], row[2])
        lstEmpresa.append(empresas1)
    print("Escoja el ID de la emmpresa para la factura")
    print("\tID\t\tRUC\t\tNOMBRE")
    for obj in lstEmpresa:
        print(
            f"\t{obj.idempresa}\t{obj.rucEmpresa}\t{obj.nombreEmpresa}")
    idempresa = input()
    #####Cargamos los tipos de pagos y elegimos
    query = f"select idtipoPago as IDTipPago,descTipoPago as Nombre from tipopago;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        tipopago1 = tipopago.tipopago(row[0], row[1])
        lstTipoPago.append(tipopago1)
    print("Escoja el ID del tipo de pago para la factura")
    print(f"\tID\t\tNOMBRE")
    for obj in lstTipoPago:
        print(f"\t{obj.idtipopago}\t{obj.desctipopago}")
    idtipopago = input()
    
    #Muestro la fecha
    print("Fecha de la factura")
    dateFecha =date.today()
    ##objDate = datetime.strptime(dateFecha, '%m/%d/%y')
    print(dateFecha)
    
   ########Insertamos el detalle
    filas = 0
    while filas < 20:
        while len(lstProductos) > 0:
            lstProductos.pop()
        query = f"select idproducto as ID, nombreproducto as NOMBRE, valorproducto as PRECIO , igvproducto INCIGV from productos;"
        resconn = conn.consultarBDD(query)
        for row in resconn:
            productos1 = productos.productos(row[0], row[1], row[2], row[3])
            lstProductos.append(productos1)
        print("Escoja el ID del producto para la factura")
        print(f"\tID\t\tNOMBRE\t\tPRECIO\t\tINCIGV")
        for obj in lstProductos:
            print(
                f"\t{obj.idProducto}\t{obj.nombreProducto}\t{obj.valorProducto}\t{obj.igvProducto}")
        idProducto = input()
    
        #Busco el producto por ID para traer el nombre el precio y saber si incluye o no igv 
        query = f"select idproducto as ID, nombreproducto as NOMBRE, valorproducto as PRECIO , igvproducto INCIGV from productos where idproducto='{idProducto}';"
        resconn = conn.consultarBDD(query)
        for row in resconn:
            productosx = productos.productos(row[0], row[1], row[2], row[3])
            lstXProductos.append(productosx)
        print(f"\tID\t\tNOMBRE\t\tPRECIO\t\tINCIGV")
        for obj in lstXProductos:
            print(
                f"\t{obj.idProducto}\t{obj.nombreProducto}\t{obj.valorProducto}\t{obj.igvProducto}")
        DescProducto = obj.nombreProducto
        PrecProducto = obj.valorProducto
        IgvProducto = obj.igvProducto
        print("Ingrese la cantidad deseada")
        cantProducto=input()
        totxproducto=float(cantProducto)*float(PrecProducto)
        dicFacDetalle = {}
        dicFacDetalle.update({"idProducto": idProducto})
        dicFacDetalle.update({"DescProducto": DescProducto})
        dicFacDetalle.update({"PrecProducto": PrecProducto})
        dicFacDetalle.update({"IgvProducto": IgvProducto})
        dicFacDetalle.update({"cantProducto": cantProducto})
        dicFacDetalle.update({"totxproducto": totxproducto})
        lstFacDetalle.append(dicFacDetalle)
        print(f"\tID\t\tNOMBRE\t\tPRECIO\t\tINCIGV\t\tCANTIDAD\t\tTOTAL")
        subtotalcab=0.0
        igvcab=0.0
        totalcab=0.0
        for obj in lstFacDetalle:
            print(
                f"\t{obj['idProducto']}\t{obj['DescProducto']}\t{obj['PrecProducto']}\t{obj['IgvProducto']}\t{obj['cantProducto']}\t{obj['totxproducto']}")
            subtotalcab = subtotalcab + obj['totxproducto']
            if obj['IgvProducto'] == 1:
                igvcab = subtotalcab * 0.18
        totalcab=subtotalcab + igvcab
        filas = filas + 1
        continuar=input("¿desea continuar insertando productos en el detalle de la factura presione C y S para salir")
        if continuar=="C":
            continue
        else:
            break  
    ####Grabamos la cabecera y el detalle 
    mensajefinal=input("¿Desea grabar la factura presione S para grabar o E para salir...:?")
    if mensajefinal=="S":
        ##Grabamos la cabecera de la factura
        conn = conexion.conexionBDD(1)
        query = f"insert into faccabecera(idempresa,idcliente,idtipoPago,fechaFacCabecera,igvFacCabecera,subtotalFacCabecera,totalFacCabecera,estadoFactura)values('{idempresa}','{idcliente}','{idtipopago}', DATE_FORMAT('{dateFecha}', '%d/%m/%y'),'{igvcab}','{subtotalcab}','{totalcab}',1);"
        resConn = conn.ejecutarRetrornoBDD(query)
        for row in resConn:             
            UltimoID = row[0]
        ##Grabamos el detalle de la factura
        for obj in lstFacDetalle:
            conn = conexion.conexionBDD(1)
            query = f"insert into facdetalle(idfacCabecera,idproducto,cantFacDetalle,valorFacDetalle)values({UltimoID},{obj['idProducto']},{obj['cantProducto']},{obj['totxproducto']});"
            resConn = conn.ejecutarBDD(query)
        if(resConn):
            log.debug("Se Creo la factura")
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
            
    else:
        print("Presione ENTER para finalizar...")  
        
###Buscar Factura
def BuscarFactura():  
    dicMenuFactura = {"\t- Buscar Factura Todos": 1,
                  "\t- Buscar Factura por ID": 2}
    menuFactura = utils.Menu("Menu Factura", dicMenuFactura)
    resMenuFactura = menuFactura.mostrarMenu()
    if(resMenuFactura == 1):
        log.debug("buscamos factura")
        conn = conexion.conexionBDD(1)
        query = "select idfacCabecera,e.nombreEmpresa, c.nombreCliente,"
        query = query + " t.descTipoPago,fechaFacCabecera, igvFacCabecera, subtotalFacCabecera, totalFacCabecera, estadoFactura from faccabecera as f"
        query = query + " inner join empresa as e on f.idempresa = e.idempresa"
        query = query + " inner join clientes as c on f.idcliente = c.idcliente"
        query = query + " inner join tipopago as t on f.idtipoPago = t.idtipoPago;"
        resConn = conn.consultarBDD(query)

        print("\tIDFACTURA\tNOMBREEMPRESA\tNOMBRECLIENTE\tIDTIPOGO\tFECHA\tIGV\tSUBTOTAL\tTOTAL\tESTADO")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}\t\t{str(row[6])}\t\t{str(row[7])}")
            print()
            print()
            query = f"select idfaccabecera,a.idproducto,b.nombreproducto,cantfacdetalle,b.valorproducto,valorfacdetalle from facdetalle as a"
            query = query + f" inner join productos as b on a.idproducto=b.idproducto where idfaccabecera='{row[0]}';"
            resConn = conn.consultarBDD(query)
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")
        input("continuar???")
        print(resConn)
    if(resMenuFactura == 2):
        log.debug("buscamos factura")
        conn = conexion.conexionBDD(1)
        query = "select idfacCabecera from faccabecera"
        resConn = conn.consultarBDD(query)
        print("escribe el ID de la factura")
        print(f"\tIDFACTURA")
        for row in resConn:
            print(
                f"\t{str(row[0])}")
        idfactura = input()
        
        query = f"select idfacCabecera,e.nombreEmpresa, c.nombreCliente,"
        query = query + f" t.descTipoPago,fechaFacCabecera, igvFacCabecera, subtotalFacCabecera, totalFacCabecera, estadoFactura from faccabecera as f"
        query = query + f" inner join empresa as e on f.idempresa = e.idempresa"
        query = query + f" inner join clientes as c on f.idcliente = c.idcliente"
        query = query + f" inner join tipopago as t on f.idtipoPago = t.idtipoPago where idfacCabecera='{idfactura}' ;"
        resConn = conn.consultarBDD(query)

        print("\tIDFACTURA\tNOMBREEMPRESA\tNOMBRECLIENTE\tIDTIPOGO\tFECHA\tIGV\tSUBTOTAL\tTOTAL\tESTADO")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}\t\t{str(row[6])}\t\t{str(row[7])}")
            print()
            print()
            query = f"select idfaccabecera,a.idproducto,b.nombreproducto,cantfacdetalle,b.valorproducto,valorfacdetalle from facdetalle as a"
            query = query + \
                f" inner join productos as b on a.idproducto=b.idproducto where idfaccabecera='{row[0]}';"
            resConn = conn.consultarBDD(query)
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")
        input("continuar???")
        print(resConn)
#Mantenimiento de la tabla cliente##
def mantenimientoCliente():
    dicMenuCliente = {  "\t- Buscar Cliente Todos": 1,
                        "\t- Buscar Cliente por DNI": 2,
                        "\t- Modificar Cliente por DNI": 3,
                        "\t- Crear Cliente": 4,
                        "\t- Borrar Cliente": 5}
    menuCliente = utils.Menu("Menu Cliente", dicMenuCliente)
    resMenuCliente = menuCliente.mostrarMenu()
    if(resMenuCliente == 1):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        input("continuar???")
        print(resConn)
    elif(resMenuCliente == 2):
        log.debug("buscamos cliente por DNI")
        print("escribe el numero de DNI")
        dni = input()
        conn = conexion.conexionBDD(1)
        query = f"select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuCliente == 3):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea modificar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idcliente = input()
        print("Escriba el nuevo valor para Nombre")
        nombre = input()
        print("Escriba el nuevo valor para DNI")
        dni = input()
        print("Escriba el nuevo valor para Direccion")
        direccion = input()
        query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuCliente == 4):
        print("##Creacion de un cliente##")
        print("Escriba el Nombre del Cliente")
        nombre = input()
        print("Escriba el DNI del Cliente")
        dni = input()
        print("Escriba el Direccion del Cliente")
        direccion = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuCliente == 5):
        log.debug("eliminamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea eliminar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idcliente = input()
        
        query = f"delete from clientes where idCliente = {idcliente} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
####### FIN DEL MANTENIMIENTO DEL CLIENTE #############################################

#MANTENIMIENTO TABLA EMPRESA
def mantenimientoEmpresa():
    dicMenuEmpresa = {"\t- Buscar Empresa Todos": 1,
                      "\t- Buscar Empresa por RUC": 2,
                      "\t- Modificar Empresa por DNI": 3,
                      "\t- Crear Empresa": 4,
                      "\t- Borrar Empresa": 5}
    menuEmpresa = utils.Menu("Menu Empresa", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        log.debug("buscamos empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa as IdEmpresa, rucEmpresa as RUC, nombreEmpresa as 'Razon Social' from empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tRAZON SOCIAL\t\t")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t")

        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 2):
        log.debug("buscamos EMPRESA por ruc")
        print("escribe el nÚmero de ruc")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"select idempresa as IdEmpresa, rucEmpresa as RUC, nombreEmpresa as 'Razon Social' from empresa where rucEmpresa = '{ruc}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tRAZON SOCIAL\t\t")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t")
        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 3):
        log.debug("buscamos empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa as IdEmpresa, rucEmpresa as RUC, nombreEmpresa as 'Razon Social' from empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la Empresa que desea modificar")
        print("\tID\t\tRUC\t\t\tRAZON SOCIAL\t\t")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t")

        idempresa = input()
        print("Escriba el nuevo valor para la Razon Social")
        nombre = input()
        print("Escriba el nuevo valor para el RUC")
        ruc = input()
        query = f"update empresa set nombreEmpresa = '{nombre}', ruc = '{ruc}' where idempresa = {idempresa};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
    elif(resMenuEmpresa == 4):
        print("##Creacion de una empressaa##")
        print("Escriba la Razón Social de la Empresa")
        nombre = input()
        print("Escriba el RUC de la Empresa")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into empresa (rucEmpresa,nombreEmpresa) values('{ruc}','{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
    elif(resMenuEmpresa == 5):
        log.debug("eliminamos empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa as IdEmpresa, rucEmpresa as RUC, nombreEmpresa as 'Razon Social' from empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que desea eliminar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t")

        idempresa = input()

        query = f"delete from empresa where idempresa = {idempresa};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
####### FIN DEL MANTENIMIENTO DEL LA EMPRESA #############################################

#MANTENIMIENTO TABLA PRODUCTOS
def mantenimientoProducto():
    dicMenuProducto = {"\t- Buscar Producto Todos": 1,
                      "\t- Buscar Producto por ID": 2,
                      "\t- Modificar Producto por ID": 3,
                      "\t- Crear Producto": 4,
                      "\t- Borrar Producto": 5}
    menuProducto = utils.Menu("Menu Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if(resMenuProducto == 1):
        log.debug("buscamos producto")
        conn = conexion.conexionBDD(1)
        query = "select idproducto as ID, nombreproducto as NOMBRE, valorproducto as PRECIO , igvproducto INCIGV from productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE\t\t\t\t\tPRECIO\t\tINCIGV")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t")

        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 2):
        log.debug("buscamos PRODUCTO por ID")
        print("escribe el ID del producto")
        idproducto = input()
        conn = conexion.conexionBDD(1)
        query = f"select idproducto as ID, nombreproducto as NOMBRE, valorproducto as PRECIO , igvproducto INCIGV from productos where idproducto='{idproducto}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\tINCIGV")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t")
        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 3):
        log.debug("buscamos producto")
        conn = conexion.conexionBDD(1)
        query = f"select idproducto as ID, nombreproducto as NOMBRE, valorproducto as PRECIO , igvproducto INCIGV from productos where idproducto='{idproducto}';"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del prodcuto que desea modificar")
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\tINCIGV")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t")
        idproducto=input()
        print("Escriba el nuevo valor para el nombre")
        nombre = input()
        print("Escriba el nuevo valor para el precio")
        precio = input()
        print("Escriba el nuevo valor para ver si el porducto incluye o no IGV... 0: incluye, 1: no incluye ")
        incigv = input()
        query = f"update empresa set nombreproducto = '{nombre}', valorproducto = '{precio}', igvproducto='{incigv}'' where idproducto = {idproducto};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
    elif(resMenuProducto == 4):
        print("##Creacion de un Producto##")
        print("Escriba el nombre del producto")
        nombre = input()
        print("Escriba el precio del producto")
        precio = input()
        print("Escriba el valor para ver si el porducto incluye o no IGV... 0: incluye, 1: no incluye ")
        incigv = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into productos (nombreproducto,valorproducto,igvproducto) values('{nombre}','{precio}','{incigv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
    elif(resMenuProducto == 5):
        log.debug("eliminamos empresa")
        conn = conexion.conexionBDD(1)
        query = "select idproducto as ID, nombreproducto as NOMBRE, valorproducto as PRECIO , igvproducto INCIGV from productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del producto que desea eliminar")
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\tINCIGV")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t")

        idproducto = input()

        query = f"delete from productos where idproducto = {idproducto} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
####### FIN DEL MANTENIMIENTO DEL PRODUCTO #############################################

#MANTENIMIENTO TABLA TIPO DE PAGO
def mantenimientoTipPago():
    dicMenuTipPago = {"\t- Buscar Tipo De Pago Todos": 1,
                       "\t- Buscar Tipo De Pago por ID": 2,
                       "\t- Modificar Tipo De Pago por ID": 3,
                       "\t- Crear Tipo De Pago": 4,
                       "\t- Borrar Tipo De Pago": 5}
    menuTipPago = utils.Menu("Menu Tipo De Pago", dicMenuTipPago)
    resMenuTipPago = menuTipPago.mostrarMenu()
    if(resMenuTipPago == 1):
        log.debug("buscamos Tipop de Pago")
        conn = conexion.conexionBDD(1)
        query = "select idtipoPago as IDTipPago,descTipoPago as Nombre from tipopago;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t")

        input("continuar???")
        print(resConn)
    elif(resMenuTipPago == 2):
        log.debug("buscamos PRODUCTO por ID")
        print("escribe el ID del producto")
        idTipPago = input()
        conn = conexion.conexionBDD(1)
        query = f"select idtipoPago as IDTipPago,descTipoPago as Nombre from tipopago where idtipoPago= '{idTipPago}' ;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t")

        input("continuar???")
        print(resConn)
    elif(resMenuTipPago == 3):
        log.debug("buscamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = f"select idtipoPago as IDTipPago,descTipoPago as Nombre from tipopago where idtipoPago= '{idTipPago}' ;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Tipo De Pago que desea modificar")
        print("\tID\t\tNOMBRE")
        for row in resConn:
            print(
                 f"\t{str(row[0])}\t\t{str(row[1])}\t")
        idTipoPago = input()
        print("Escriba el nuevo valor para el nombre")
        nombre = input()
        query = f"update tipopago set descTipoPago = '{nombre}' where IDTipPago = {idTipoPago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
    elif(resMenuTipPago == 4):
        print("##Creación de un Tipo De Pago##")
        print("Escriba el nombre del tipo de pago")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into tipopago (descTipoPago) values('{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
    elif(resMenuTipPago == 5):
        log.debug("eliminamos tipo de pago")
        conn = conexion.conexionBDD(1)
        query = "select idtipoPago as IDTipPago,descTipoPago as Nombre from tipopago;;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE")
        for row in resConn:
            print(
                f"\t{str(row[0])}\t\t{str(row[1])}\t")
        idTipoPago = input()

        query = f"delete from tipopago where idtipoPago = {idTipoPago} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        input("desea continuar???")
####### FIN DEL MANTENIMIENTO DEL TIPO DE PAGO #############################################


def mantenimento(resMenu):
    if resMenu == 1:
        log.debug("escogio 1")
        mantenimientoCliente()
    elif resMenu == 2:
        log.debug("escogio 2")
        mantenimientoProducto()
    elif resMenu == 3:
        log.debug("escogio 3")
        mantenimientoEmpresa()
    elif resMenu == 4:
        log.debug("escogio 4")
        mantenimientoTipPago()
    else:
        log.debug(f"escogio {resMenu}")

stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Crear Factura": 1,
                     "\t- Busqueda y Listado de Facturas": 2, "\t- Mantenimientos": 3}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("Mostramos el Menu crear Factura")
        cargarObjetos()
    if(resMenuInicio == 2):
        log.debug("Mostramos el Menu Buscar Factura")
        BuscarFactura()
    elif(resMenuInicio == 3):
        log.debug("Mostramos los Mantenimientos")
        dicMenuMantenimiento = {"\t- Clientes": 1, "\t- Productos": 2,
                                "\t- Empresa": 3, "\t- Tipo de pago": 4}
        menuMantenimiento = utils.Menu(
            "Menu Mantenimiento", dicMenuMantenimiento)
        resMenuMantenimiento = menuMantenimiento.mostrarMenu()
        mantenimento(resMenuMantenimiento)
    elif(resMenuInicio == 9):
        log.debug("finalizar Programa")
    else:
        log.debug("volvemos a mostrar menu")
        stopMenuInicio = False
