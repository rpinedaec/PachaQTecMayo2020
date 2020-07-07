import utils
import conexion
import clientes
import productos
import empresa
import tipopago
import facturadetalle
from datetime import datetime
from time import sleep

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []
lstFacDetalle = []

def cargarObjetos():
    conn = conexion.conexionBDD(1)
    query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        cliente = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(cliente)

    for obj in lstClientes:
        print(obj.nombreCliente)
    input("continuar")

def crearFactura():

    igv = 0.18
    valorProducto = 0.00
    igvProducto = 0
    igvFacCabecera = 0.00
    subtotalFac = 0.00
    totalFac = 0.00
    fecha = datetime.today().strftime('%Y-%m-%d')

    print(f"La fecha de hoy es: {fecha}")
    idcliente = input("escribe el codigo del Cliente: ")
    idtipopago = input("ingrese el codigo de tipo de pago: ")
    #fecha = input("Ingrese la fecha de la factura (yyyy-mm-dd): ")

    
    log.debug("crear factura")
    conn = conexion.conexionBDD(1)

    stopIngreso = True
    while stopIngreso:
        idproducto = input("ingrese el codigo de  producto: ")
        cantFacDetalle = input("ingrese la cantidad: ")
        masProducto = input("Desea ingresar otro producto Si (1) / No (0): ")
        if masProducto != '1':
            stopIngreso = False
        query = f"select idproducto, valorProducto, igvProducto from productos where idproducto = {idproducto};"
        resconn = conn.consultarBDD(query)
        for row in resconn:
            valorProducto = row[1]
            igvProducto = row[2]

        factdetalle = facturadetalle.facturadetalle(1, 1, idproducto, cantFacDetalle, valorProducto)
        lstFacDetalle.append(factdetalle)

        subtotalFac = valorProducto * int(cantFacDetalle)
        if igvProducto == 1:
            igvFacCabecera += float(subtotalFac) * float(igv)

    totalFac = float(subtotalFac) + igvFacCabecera

    if  totalFac > 0:
        query = "insert into faccabecera (idempresa, idcliente, idtipoPago, fechaFacCabecera, igvFacCabecera, subtotalFacCabecera, totalFacCabecera, estadoFactura) " 
        query += f"values(1, {idcliente}, {idtipopago}, '{fecha}', {igvFacCabecera}, {subtotalFac}, {totalFac}, '1');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente registro de factura")
        else:
            print("Hubo un error")
        sleep(5)

        query = f"select MAX(idfacCabecera) AS 'idFactura' from faccabecera where fechaFacCabecera = '{fecha}';"
        resconn = conn.consultarBDD(query)
        for row in resconn:
            print(row[0])
            idfacCabecera = int(row[0])

        if idfacCabecera > 0:
            for obj in  lstFacDetalle:
                query = "insert into facdetalle (idfacCabecera, idproducto, cantFacDetalle, valorFacDetalle) " 
                query += f"values({idfacCabecera}, {idproducto}, {obj.cantFacDetalle}, {obj.valorFacDetalle});"
                resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente registro de factura detalle")
            else:
                print("Hubo un error")
            sleep(5)
     

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

def mantenimientoProducto():
    dicMenuProducto = { "\t- Buscar todos Productos": 1,
                        "\t- Buscar Producto por codigo de Producto": 2,
                        "\t- Modificar Producto por codigo de Producto": 3,
                        "\t- Crear Producto": 4,
                        "\t- Borrar Producto": 5}
    menuProducto = utils.Menu("Menu Producto", dicMenuProducto) 
    resMenuProducto = menuProducto.mostrarMenu()
    #print(resMenuProducto)
    if(resMenuProducto == 1):
        log.debug("buscamos producto")
        conn = conexion.conexionBDD(1)
        #2query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        input("continuar???")
        print(resConn)      
    elif(resMenuProducto == 2):
        log.debug("buscamos producto por codigo de producto")
        print("escribe el código del producto")
        codigoproducto = input()
        conn = conexion.conexionBDD(1)
        query = f"select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from productos where idproducto = {codigoproducto};"
        print(query)
        resConn = conn.consultarBDD(query)
        print("\tID\t\tProducto\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 3):
        log.debug("buscamos el producto")
        conn = conexion.conexionBDD(1)
        #query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del producto que desea modificar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        print("Escriba el nuevo valor para Nombre")
        nombreproducto = input()
        print("Escriba el nuevo valor para Valor del producto")
        valorproducto = input()
        print("Escriba el nuevo valor para IGV")
        igvproducto = input()
        #query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
        query = f"update productos set nombreProducto = '{nombreproducto}', valorProducto = '{valorproducto}', igvProducto = {igvproducto} where idproducto = {idproducto};"
      
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")                               
    elif(resMenuProducto == 4):
        print("##Creacion de un Producto##")
        print("Escriba el Nombre del Producto")
        nombreproducto = input()
        print("Escriba el valor del Producto")
        valorproducto = input()
        print("Escriba el IGV del Producto")
        igvproducto = input()
        conn = conexion.conexionBDD(1)
        print("hola")
        #query = f"insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
        query = f"insert into productos (nombreProducto, valorProducto, igvProducto) values('{nombreproducto}', '{valorproducto}', '{igvproducto}');"
        #print (query)
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 5):    
        log.debug("eliminamos producto")
        conn = conexion.conexionBDD(1)
        #query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el codigo del producto que desea eliminar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        
        query = f"delete from productos where idproducto = {idproducto} ;"

        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

def mantenimientoEmpresa():
    dicMenuEmpresa = { "\t- Buscar datos de Empresa": 1,
                        "\t- Modificar datos de Empresa por codigo de Empresa": 2,
                      }
    menuEmpresa = utils.Menu("Menu Producto", dicMenuEmpresa) 
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        log.debug("buscamos Empresa")
        conn = conexion.conexionBDD(1)
        #2query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        query = "select idempresa, rucEmpresa as RUC, nombreEmpresa as Empresa from empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tEmpresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        input("continuar???")
        print(resConn)   
    elif(resMenuEmpresa == 2):
        log.debug("buscamos la empresa")
        conn = conexion.conexionBDD(1)
        #query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        # query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from productos;"
        # resConn = conn.consultarBDD(query)
        query = "select idempresa, rucEmpresa as RUC, nombreEmpresa as Empresa from empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que desea modificar")
        print("\tID\t\tRUC\t\t\tEmpresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idempresa = input()
        print("Escriba el nuevo valor para Nombre")
        nombreempresa = input()
        print("Escriba el nuevo valor para el RUC")
        rucempresa = input()
      
        #query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
        #query = f"update productos set nombreProducto = '{nombreproducto}', valorProducto = '{valorproducto}', igvProducto = {igvproducto} where idproducto = {idproducto};"
        query = f"update empresa set rucEmpresa = '{rucempresa}', nombreEmpresa = '{nombreempresa}' where idempresa = {idempresa};"

        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")  

def mantenimientoTipoPago():
    dicMenuTipoPago = { "\t- Buscar tipo de pago": 1,
                        "\t- Buscar tipo de pago por codigo de tipo de pago": 2,
                        "\t- Modificar tipo de pago por codigo de tipo de pago": 3,
                        "\t- Crear tipo de pago": 4,
                        "\t- Borrar tipo de pago": 5}
    menuTipoPago= utils.Menu("Menu TipoPago", dicMenuTipoPago) 
    resMenuTipoPago = menuTipoPago.mostrarMenu()
    if(resMenuTipoPago == 1):
        log.debug("buscamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        #2query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        #query = "select idempresa, rucEmpresa as RUC, nombreEmpresa as Empresa from empresa;"
        query = "Select idtipopago, descTipoPago as Descripcion from tipopago;"
      
        resConn = conn.consultarBDD(query)
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        input("continuar???")
        print(resConn)

    elif(resMenuTipoPago == 2):
        log.debug("buscamos tipo de pago por codigo de tipo de pago")
        print("escribe el código del producto")
        codigotipopago = input()
        conn = conexion.conexionBDD(1)
        query = "Select idtipopago, descTipoPago as Descripcion from tipopago where descTipoPago = 'Efectivo';"
       
        print(query)
        resConn = conn.consultarBDD(query)
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        input("continuar???")
        print(resConn)

    elif(resMenuTipoPago == 3):
        log.debug("buscamos el tipo de pago")
        conn = conexion.conexionBDD(1)
        #query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        query = "Select idtipopago, descTipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)

        print("Escoja el codigo de tipo de pago que desea modificar")
        print("\tcodigo\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        
        codigotipopago = input()    
        print("Escriba el nuevo valor para tipo de pago")
        desctipopago = input()    
        #query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
        #query = f"update productos set nombreProducto = '{nombreproducto}', valorProducto = '{valorproducto}', igvProducto = {igvproducto} where idproducto = {idproducto};"
        query = f"update tipopago set descTipoPago = '{desctipopago}' where idtipopago = '{codigotipopago}';"

        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")   

    elif(resMenuTipoPago == 4):
        print("##Creacion de un tipo de pago##")
        print("Escriba el Tipo de Pago")
        desctipopago = input()
      
        conn = conexion.conexionBDD(1)
        #print("hola")
        #query = f"insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
        query = f"insert into tipopago(descTipoPago) values('{desctipopago}');"
        #INSERT INTO tipopago(descTipoPago)VALUES('Efectivo');
        #print (query)
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(resMenuTipoPago == 5):    
        log.debug("eliminamos un tipo de pago")
        conn = conexion.conexionBDD(1)
        #query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        #query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from productos;"
        query = "Select idtipopago, descTipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el codigo del tipo de pago que desea eliminar")
        print("\tcodigo\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        codigotipopago = input()
        
        query = f"delete from tipopago where idtipopago = {codigotipopago} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

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
        mantenimientoTipoPago()
    else:
        log.debug(f"escogio {resMenu}")



stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Crear Factura": 1, "\t- Mantenimientos": 2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("Mostramos el Menu crear Factura")
        #cargarObjetos()
        crearFactura()
    elif(resMenuInicio == 2):
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
