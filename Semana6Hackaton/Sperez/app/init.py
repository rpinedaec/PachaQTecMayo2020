import utils
import conexion
import cliente
import empresa
import productos
import tipopago

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

def cargarObjetos():
    conn = conexion.conexionBDD(1)
    query = "select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        clientes = cliente.cliente(row[0],row[1],row[2],row[3])
        lstClientes.append(clientes)

    for obj in lstClientes:
        print(obj.nombreCliente)
    
    conn = conexion.conexionBDD(1)
    query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        empresas = empresa.empresa(row[0],row[1],row[2])
        lstEmpresa.append(empresas)

    for obj in lstEmpresa:
        print(obj.nombreEmpresa)
    

    conn = conexion.conexionBDD(1)
    query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Precio, igvProducto as IGV FROM productos;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        producto = productos.productos(row[0],row[1],row[2],row[3])
        lstProductos.append(producto)

    for obj in lstProductos:
        print(obj.nombreProducto)

    conn = conexion.conexionBDD(1)
    query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        tipopagos = tipopago.tipopago(row[0],row[1])
        lstTipoPago.append(tipopagos)

    for obj in lstTipoPago:
        print(obj.descTipoPago)
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
        query = "select idCliente, nombreCliente as Nombre, nroidentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"select idCliente, nombreCliente as Nombre, nroidentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuCliente == 3):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroidentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"update clientes set nombreCliente = '{nombre}', nroidentificacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
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
        query = f"insert into clientes (nombreCliente, nroidentificacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuCliente == 5):
        log.debug("eliminamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroidentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
    dicMenuProducto = {  "\t- Buscar todos los Productos": 1,
                        "\t- Buscar Producto por IGV": 2,
                        "\t- Modificar Producto por otro": 3,
                        "\t- Crear Producto": 4,
                        "\t- Borrar Borrar Producto": 5}
    menuProducto = utils.Menu("Menu Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if(resMenuProducto == 1):
        log.debug("buscamos productos")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Precio, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tPrecio\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 2):
        log.debug("buscamos producto por IGV")
        print("escribe 1 si el producto cuenta con IGV")
        igv = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idproducto, nombreProducto as Nombre, valorProducto as Precio, igvProducto as IGV FROM productos where igvProducto ='{igv}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tPrecio\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 3):
        log.debug("buscamos producto")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Precio, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del producto que desea modificar")
        print("\tID\t\tNombre\t\t\tPrecio\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        print("Escriba el nuevo valor para Nombre de producto")
        nombre = input()
        print("Escriba el nuevo valor para precio de producto")
        precio = input()
        print("Escriba 1 si cuenta con IGV o 0 si no cuenta con IGV")
        igv = input()
        query = f"UPDATE productos SET nombreProducto = '{nombre}', valorProducto = '{precio}', igvProducto = '{igv}' WHERE idproducto = '{idproducto}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 4):
        print("##Creacion de un producto##")
        print("Escriba el Nombre del producto")
        nombre = input()
        print("Escriba el precio del producto")
        precio = float(input())
        print("Escriba 1 si el producto cuenta con IGV o 0 si no cuenta")
        igv = input()

        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO productos(nombreProducto, valorProducto, igvProducto) VALUES ('{nombre}','{precio}','{igv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 5):
        log.debug("eliminamos producto")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Precio, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del producto que desea eliminar")
        print("\tID\t\tNombre\t\t\tPrecio\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        
        query = f"DELETE FROM productos WHERE idproducto = '{idproducto}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

def mantenimientoEmpresa():
    dicMenuEmpresa = {  "\t- Buscar todas las empresas": 1,
                        "\t- Buscar Empresa por RUC": 2,
                        "\t- Modificar Empresa por RUC": 3,
                        "\t- Crear Empresa": 4,
                        "\t- Borrar Empresa": 5}
    menuEmpresa = utils.Menu("Menu Empresa", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        log.debug("buscamos empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tNombre Empresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 2):
        log.debug("buscamos Empresa por RUC")
        print("escribe el numero de RUC")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa where rucEmpresa = '{ruc}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tNombre Empresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 3):
        log.debug("buscamos empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que desea modificar")
        print("\tID\t\tRUC\t\t\tNombre Empresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idcliente = input()
        print("Escriba el nuevo RUC")
        ruc = input()
        print("Escriba el nombre de la Empresa")
        empresa = input()
        query = f"UPDATE empresa SET rucEmpresa = '{ruc}', nombreEmpresa = '{empresa}' WHERE idempresa = '{idcliente}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuEmpresa == 4):
        print("##Creacion de una empresa")
        print("Escriba el RUC de la empresa")
        ruc = input()
        print("Escriba el Nombre de la Empresa")
        empresa = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO empresa (rucEmpresa, nombreEmpresa) VALUES ('{ruc}','{empresa}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuEmpresa == 5):
        log.debug("eliminamos empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que desea eliminar")
        print("\tID\t\tRUC\t\t\tNombre Empresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idEmpresa = input()
        
        query = f"DELETE FROM empresa WHERE idempresa = {idEmpresa};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

def mantenimientoTipoPago():
    dicMenuTipoPago = {  "\t- Buscar todos los tipos de pagos": 1,
                        "\t- Buscar Tipo de pago por descripcion": 2,
                        "\t- Modificar Tipo de pago por descripcion": 3,
                        "\t- Crear Tipo de Pago": 4,
                        "\t- Borrar Tipo de Pago": 5}
    menuTipoPago = utils.Menu("Menu Tipo de Pago", dicMenuTipoPago)
    resMenuTipoPago = menuTipoPago.mostrarMenu()
    if(resMenuTipoPago == 1):
        log.debug("buscamos tipo de pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        input("continuar???")
        print(resConn)
    elif(resMenuTipoPago == 2):
        log.debug("buscamos Tipo de pago por Descripcion")
        print("escribe la Descripcion de Tipo de Pago")
        descTipoPago = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago where descTipoPago = '{descTipoPago}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        input("continuar???")
        print(resConn)
    elif(resMenuTipoPago == 3):
        log.debug("buscamos tipo de pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del tipo de pago que desea modificar")
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipoPago = input()
        print("Escriba la nueva descripcion")
        descTipoPago = input()

        query = f"UPDATE tipopago SET descTipoPago = '{descTipoPago}' WHERE idtipoPago = '{idtipoPago}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuTipoPago == 4):
        print("##Creacion de un Tipo de Pago")
        print("Escriba el Tipo de Pago")
        descTipoPago = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO tipopago(descTipoPago) VALUES('{descTipoPago}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuTipoPago == 5):
        log.debug("eliminamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de tipo de pago que desea eliminar")
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipoPago = input()
        
        query = f"DELETE FROM tipopago WHERE idtipoPago = '{idtipoPago}';"
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
        cargarObjetos()
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
