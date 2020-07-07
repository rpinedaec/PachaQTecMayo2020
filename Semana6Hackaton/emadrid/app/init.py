import utils
import conexion
import clientes
import productos
import empresa
import tipopago
import factura


log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

def cargarObjetos():
    conn = conexion.conexionBDD(1)
    queryCliente = "select idclientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
    resconn = conn.consultarBDD(queryCliente)
    for row in resconn:
        cliente = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(cliente)

    for obj in lstClientes:
        print(obj.nombreCliente)
    input("continuar")

    queryProducto = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"
    resconn = conn.consultarBDD(queryProducto)
    for row in resconn:
        producto = productos.productos(row[0],row[1],row[2],row[3])
        lstProductos.append(producto)

    for obj in lstProductos:
        print(obj.nombreProducto)
    input("continuar")

    queryEmpresa = "select idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
    resconn = conn.consultarBDD(queryEmpresa)
    for row in resconn:
        empresa = empresa.empresa(row[0],row[1],row[2])
        lstEmpresa.append(empresa)

    for obj in lstEmpresa:
        print(obj.nombreEmpresa)
    input("continuar")

    queryTipoPago = "select idtipopago, descTipoPago as Descripcion from tipopago;"
    resconn = conn.consultarBDD(queryTipoPago)
    for row in resconn:
        tipopago = tipopago.tipopago(row[0],row[1])
        lstTipoPago.append(tipopago)

    for obj in lstTipoPago:
        print(obj.desctipopago)
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
        query = "select idclientes, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"select idclientes, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuCliente == 3):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idclientes, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idclientes = {idcliente};"
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
        query = "select idclientes, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
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


##MANTENIMIENTO PRODUCTOS
def mantenimientoProductos():
    dicMenuProducto = {  "\t- Buscar Producto Todos": 1,
                        "\t- Buscar Producto por ID": 2,
                        "\t- Modificar Producto por ID": 3,
                        "\t- Crear Producto": 4,
                        "\t- Borrar Producto": 5}
    menuProducto = utils.Menu("Menu Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if(resMenuProducto == 1):
        log.debug("buscamos Producto")
        conn = conexion.conexionBDD(1)
        query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 2):
        log.debug("buscamos Producto por ID")
        print("escribe el ID")
        codProducto = input()
        conn = conexion.conexionBDD(1)
        query = f"select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos where idproducto = '{codProducto}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 3):
        log.debug("buscamos Producto")
        conn = conexion.conexionBDD(1)
        query = "select idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el COD del Producto que desea modificar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        print("Escriba el nuevo valor para Nombre Producto")
        nombreProducto = input()
        print("Escriba el nuevo valor para Valor del Producto")
        valorProducto = input()
        print("Escriba el nuevo valor para el IGV")
        igv = input()
        query = f"update productos set nombreProducto = '{nombreProducto}', valorProducto = '{valorProducto}',igvProducto = '{igv}' where idproducto = {idproducto};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 4):
        print("##Creacion de un Producto##")
        print("Escriba el Nombre del Producto")
        nombreProducto = input()
        print("Escriba el Valor del Producto")
        valorProducto = input()
        print("Escriba el IGV")
        igv = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into productos (nombreProducto, valorProducto,igvProducto) values('{nombreProducto}','{valorProducto}','{igv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 5):
        log.debug("eliminamos Producto")
        conn = conexion.conexionBDD(1)
        query = "select idproducto as ID, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el COD Producto que desea eliminar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        
        query = f"delete from productos where idProductos = {idproducto} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

##MANTENIMIENTO EMPRESA
def mantenimientoEmpresa():
    dicMenuEmpresa = {  "\t- Buscar Empresas Registradas": 1,
                        "\t- Buscar Empresa por RUC": 2,
                        "\t- Modificar Empresa por RUC": 3,
                        "\t- Crear Empresa": 4,
                        "\t- Borrar Empresa": 5}
    menuEmpresa = utils.Menu("Menu Empresa", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        log.debug("buscamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRuc\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 2):
        log.debug("buscamos Empresa por RUC")
        print("escribe el RUC")
        rucEmpresa = input()
        conn = conexion.conexionBDD(1)
        query = f"select idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa FROM empresa where rucEmpresa = '{rucEmpresa}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRuc\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 3):
        log.debug("buscamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el RUC de la Empresa que desea modificar")
        print("\tID\t\tRuc\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idEmpresa = input()
        print("Escriba el nuevo ID Empresa")
        rucEmpresa = input()
        print("Escriba el nuevo Ruc de Empresa")
        nombreEmpresa = input()
        print("Escriba el nuevo Nombre de Empresa")
     
        query = f"update empresa set rucEmpresa = '{rucEmpresa}', nombreEmpresa = '{nombreEmpresa}' where idempresa = {idEmpresa};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuEmpresa == 4):
        print("##Creacion de una Empresa##")
        print("Escriba el RUC de la Empresa")
        rucEmpresa = input()
        print("Escriba el Nombre de la Empresa")
        nombreEmpresa = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into empresa (rucEmpresa, nombreEmpresa) values('{rucEmpresa}','{nombreEmpresa}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuEmpresa == 5):
        log.debug("eliminamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "select rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de Empresa que desea eliminar")
        print("\tID\t\tRuc\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idempresa = input()
        
        query = f"delete from empresa where idempresa = {idempresa} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

##MANTENIMIENTO TIPOPAGO
def mantenimientoTipoPago():
    dicMenuTipoPago = {  "\t- Buscar Tipos de Pagos Registrados": 1,
                        "\t- Buscar Tipos de Pagos por ID": 2,
                        "\t- Modificar Tipos de Pagos por ID": 3,
                        "\t- Crear Tipos de Pagos": 4,
                        "\t- Borrar Tipos de Pagos": 5}
    menuTipoPago = utils.Menu("Menu Tipos de Pagos", dicMenuTipoPago)
    resMenuTipoPago = menuTipoPago.mostrarMenu()
    if(resMenuTipoPago == 1):
        log.debug("buscamos Tipo Pago")
        conn = conexion.conexionBDD(1)
        query = "Select idtipopago, descTipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRuc\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        input("continuar???")
        print(resConn)
    elif(resMenuTipoPago == 2):
        log.debug("buscamos Tipo Pago por ID")
        print("escribe el ID")
        idTipoPago = input()
        conn = conexion.conexionBDD(1)
        query = f"select idtipopago, descTipoPago as Descripcion from tipopago where idtipopago = '{idTipoPago}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDescripcion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        input("continuar???")
        print(resConn)
    elif(resMenuTipoPago == 3):
        log.debug("buscamos Tipo Pago")
        conn = conexion.conexionBDD(1)
        query = "select idtipopago, descTipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del tipo pago que desea modificar")
        print("\tID\t\tDescripcion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idTipoPago = input()
        print("Escriba el nuevo ID Tipo Pago")
        descTipoPago = input()
        print("Escriba el nuevo Nombre del Tipo Pago")
        
        query = f"update tipopago set descTipoPago = '{descTipoPago}' where idtipopago = {idTipoPago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuTipoPago == 4):
        print("##Creacion de un Tipo Pago##")
        print("Escriba la Descripcion del Tipo Pago")
        descTipoPago = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into tipopago (descTipoPago) values('{descTipoPago}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuTipoPago == 5):
        log.debug("eliminamos Tipo Pago")
        conn = conexion.conexionBDD(1)
        query = "Select idtipopago, descTipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Tipo Pago que desea eliminar")
        print("\tID\t\tDescripcion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idTipoPago = input()
        
        query = f"delete from tipopago where idtipopago = {idTipoPago} ;"
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
        mantenimientoProductos()
    elif resMenu == 3:
        mantenimientoEmpresa()
    elif resMenu == 4:
        mantenimientoTipoPago
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
