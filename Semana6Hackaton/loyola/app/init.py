import utils
import conexion
import clientes
import productos
import factura
import tipopago
import empresa


log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

def cargarCliente():
    conn = conexion.conexionBDD(1)
    query = "select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        cliente = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(cliente)

    for obj in lstClientes:
        print(obj.nombreCliente)
    input("continuar")

def cargarProductos():
    conn = conexion.conexionBDD(1)
    query = "select idProducto, nombreProducto as nombre, valorUniProducto as valorUni, cantidadProducto as cantidad from productos;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        producto = productos.productos(row[0],row[1],row[2],row[3])
        lstProductos.append(producto)

    for obj in lstProductos:
        print(obj.nombreProducto)
    input("continuar")

def cargarEmpresa():
    conn = conexion.conexionBDD(1)
    query = "select idempresa, rucEmpresa as ruc, nombreEmpresa as nombre;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        empresa = empresa.empresa(row[0],row[1],row[2])
        lstEmpresa.append(empresa)

    for obj in lstEmpresa:
        print(obj.idempresa)
    input("continuar")

def cargarTipoPago():
    conn = conexion.conexionBDD(1)
    query = "select idtipopago, desctipopago as descripcion;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        pago = tipoPago.tipopago(row[0],row[1],row[2])
        lstTipoPago.append(pago)

    for obj in lstTipoPago:
        print(obj.idtipopago)
    input("continuar")



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
        query = "select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentificacionCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)

    elif(resMenuCliente == 3):
        log.debug("modificamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"update clientes set nombreCliente = '{nombre}', nroIdentificacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
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
        query = f"insert into clientes (nombreCliente, nroIdentificacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuCliente == 5):
        log.debug("eliminamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
    dicMenuProducto = {  "\t- Agregar Producto": 1,
                        "\t- Borrar Producto": 2,
                        "\t- Mostrar Productos": 3,
                        "\t- Buscar Producto": 4,}

    menuProducto = utils.Menu("Menu Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if(resMenuProducto == 1):
        print("##Usted desea agregar un Producto##")
        nombre = input("Escriba el Nombre del Producto\n")
        valorUni = input("Escriba el valor unitario del producto\n")
        cantidad = input("Escriba la cantidad que desea\n")
        conn = conexion.conexionBDD(1)
        query = f"insert into productos (nombreProducto,valorUniProducto,cantidadProducto) values({nombre}','{valorUni}','{cantidad}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")

    elif(resMenuProducto == 2):
        log.debug("Usted desea eliminar un producto")
        conn = conexion.conexionBDD(1)
        query = "select idProducto, nombreProducto as nombre, valorUniProducto as valorUni, cantidadProducto as cantidad from productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el nombre del producto que quiere eliminar")
        print("\tID\t\tNombre\t\t\tValorUnitario\t\t\tCantidad")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        nombre = input()
        
        query = f"delete from productos where nombre = {nombre} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(resMenuProducto == 3):
        log.debug("mostrar productos")
        conn = conexion.conexionBDD(1)
        query = "select idProducto, nombreProducto as nombre, valorUniProducto as valorUni, cantidadProducto as cantidad from productos;"
        print(query)

    elif(resMenuProducto == 4):
        log.debug("buscamos producto")
        print("escriba el nombre del producto")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = f"select idProducto, nombreProducto as nombre, valorUniProducto as valorUni, cantidadProducto as cantidad from productos where nombreProducto = '{nombre}';"
        resConn = conn.consultarBDD(query)
        try:
            print("\tID\t\tNombre\t\t\tValorUnitario\t\t\tCantidad")
            for row in resConn:
                print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
            input("continuar???")
            print(resConn)
        except Exception as error:
            print(error)

def mantenimientoEmpresa():
    dicMenuEmpresa = {  "\t- Agregar Empresa": 1,
                        "\t- Borrar Empresa": 2,
                        "\t- Mostrar Empresas": 3,
                        "\t- Buscar Empresa": 4,
                        "\t- Modificar Datos de Empresa": 5,}

    menuEmpresa = utils.Menu("Menu Empresa", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        print("##Usted desea agregar una Empresa##")
        ruc = input("Escriba el RUC de la Empresa\n")
        nombre = input("Escriba el Nombre de la Empresa\n")
        conn = conexion.conexionBDD(1)
        query = f"insert into productos (rucEmpresa,nombreEmpresa) values({ruc}','{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")

    elif(resMenuEmpresa == 2):
        log.debug("borrar una empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucEmpresa as ruc, nombreEmpresa as nombre;"
        resConn = conn.consultarBDD(query)
        print("Escoja el nombre de la empresa que quiere borrar")
        print("\tID\t\tRUC\t\t\tNOMBRE")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        nombre = input()
        
        query = f"delete from empresa where nombre = {nombre} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(resMenuEmpresa == 3):
        log.debug("mostrar empresas")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucEmpresa as ruc, nombreEmpresa as nombre;"
        print(query)

    elif(resMenuEmpresa == 4):
        log.debug("buscamos empresa")
        print("escriba el nombre de la empresa")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucEmpresa as ruc, nombreEmpresa as nombre;"
        resConn = conn.consultarBDD(query)
        try:
            print("\tID\t\tRUC\t\t\tNombre")
            for row in resConn:
                print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
            input("continuar???")
            print(resConn)
        except Exception as error:
            print(error)

    elif(resMenuEmpresa == 5):
        log.debug("modificamos empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucEmpresa as ruc, nombreEmpresa as nombre;"
        resConn = conn.consultarBDD(query)
        print("Escoja el nombre de la empresa que desea modificar")
        print("\tID\t\tRUC\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        nombre = input()

        print("Escriba el nuevo nombre de la empresa")
        nombre = input()
        print("Escriba el nuevo RUC de la empresa")
        ruc = input()
    
        query = f"update empresa set nombreEmpresa = '{nombre}', rucEmpresa = '{ruc}' where nombreEmpresa = {nombre};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

def mantenimientoTipoPago():
    dicMenuTipoPago = {  "\t- Agregar Tipo de Pago": 1,
                        "\t- Modificar Tipo de Pago": 2,
                        "\t- Eliminar Tipo de Pago": 3,
                        "\t- Buscar Tipo de Pago": 4,}

    menuTipoPago = utils.Menu("Menu Tipo de Pago", dicMenuTipoPago)
    resMenuTipoPago = menuTipoPago.mostrarMenu()
    if(resMenuTipoPago == 1):
        print("Seleccione el Tipo de Pago:")
        descripcion = {  "\t- Efectivo": 1,
                        "\t- Credito": 2,
                        "\t- Transferencia": 3}

        descripcion = input()
        if(descripcion == 1):
            conn = conexion.conexionBDD(1)
            query = f"insert into tipopago (desctipopago) value('Efectivo');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("desea continuar???")
        elif(descripcion == 2):
            conn = conexion.conexionBDD(1)
            query = f"insert into tipopago (desctipopago) value('Credito');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("desea continuar???")
        elif(descripcion == 3):
            conn = conexion.conexionBDD(1)
            query = f"insert into tipopago (desctipopago) values('Transferencia');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("desea continuar???")

    elif(resMenuTipoPago == 2):

        log.debug("modificamos tipo de pago")
        conn = conexion.conexionBDD(1)
        query = "select idtipopago, desctipopago as descripcion;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Tipo de Pago que desea cambiar")
        print("\tID\t\tTIPO DE PAGO")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipopago = input()

        print("seleccione el nuevo tipo de pago")
        print(descripcion)
        descripcion = input()
    
        query = f"update tipopago set desctipopago = '{descripcion}' where idtipopago = {idtipopago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    
    elif(resMenuTipoPago == 3):
        log.debug("borrar Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "select idtipopago, desctipopago as descripcion;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del tipo de pago que desea eliminar")
        print("\tID\t\tTipo De Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipopago = input()
        
        query = f"delete from tipopago where idtipopago = {idtipopago} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(menuTipoPago == 4):
        log.debug("buscamos tipopago por id")
        input("Continuar?")
        conn = conexion.conexionBDD(1)
        query = "select idtipopago, desctipopago as descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print(query)
        print("escriba el Id del Tipo de Pago")
        idtipopago = input()
        conn = conexion.conexionBDD(1)
        query = f"select idtipopago, desctipopago as descripcion from tipopago where idtipopago = '{idtipopago}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
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
        mantenimientoTipoPago
    else:
        log.debug(f"escogio {resMenu}")

def CreacionFactura():
    conn = conexion.conexionBDD(1)
    query = """idfacCabecera, idempresa, idcliente, idtipoPago, fechaFacCabecera, 
            igvFacCabecer, subtotalFacCabecera, totalFacCabecera, estadoFactura"""
    resConn = conn.consultarBDD(query)

    dicCreacionFactura = {"\t- Agregar Datos": 1,}
    menuFactura = utils.Menu("Menu Factura", dicCreacionFactura)
    resMenuFactura = menuFactura.mostrarMenu()

    if(resMenuFactura == 1):
        idempresa = input("Escriba el ID de su empresa\n")
        idcliente = input("Escriba su ID de cliente\n")
        idtipoPago = input("Escriba su ID de pago\n")
        fechaFacCabecera = input("Escriba la Fecha de Emision de Factura\n") 
        igvFacCabecera = 0.18
        subtotalFacCabecera = input()
        totalFacCabecera = input() 
        estadoFactura = input()
        conn = conexion.conexionBDD(1)
        query = f"""insert into facCabecera (idempresa, idcliente, idtipoPago, fechaFacCabecera, 
                igvFacCabecera, subtotalFacCabecera, totalFacCabecera, estadoFactura) values('{idempresa}','{idcliente}','{idtipoPago}',
                '{fechaFacCabecera}', '{igvFacCabecera}', '{subtotalFacCabecera}', '{totalFacCabecera}', '{estadoFactura}');"""
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")

        conn = conexion.conexionBDD(1)
        query = "select idproducto from productos"
        resConn = conn.ejecutarBDD(query)
        idproductos = input()
        idfacCabecera = "select idfacCabecera from facCabecera;"
        cantFacDetalle = "select count(*) from productos;"
        valorFacDetalle = "select valorProducto from productos;"
        conn = conexion.conexionBDD(1)
        query = f"""insert into facDetalle (idproductos, idfacCabecera, cantFacDetalle, valorFacDetalle) values('{idproductos}','{idfacCabecera}','{cantFacDetalle}',
                '{valorFacDetalle}');"""
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")


stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Propiedades de Factura": 1, "\t- Mantenimientos\t": 2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("Mostramos el Menu propiedades de Factura")
        CreacionFactura()
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