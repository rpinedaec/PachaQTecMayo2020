import utils

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

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
#Clientes
def mantenimientoCliente():
    dicMenuCliente = {  "\t- Buscar Cliente Todos": 1,
                        "\t- Modificar Cliente por DNI": 2,
                        "\t- Crear Cliente": 3,
                        "\t- Borrar Cliente": 4}
    menuCliente = utils.Menu("Menu Cliente", dicMenuCliente)
    resMenuCliente = menuCliente.mostrarMenu()
    if(resMenuCliente == 1):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idcliente, nombrecliente as Nombre, nroidentidicacioncliente as ID, direccioncliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        print("Si desea continuar escriba 1, para salir 2")
        input("Ingrese su opción: ")
        print(resConn)
    elif(resMenuCliente == 2):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idclientes, nombrecliente as Nombre, nroidentidicacioncliente as ID, direccioncliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("Elija el ID del cliente que desea modificar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idclientes = input()
        print("Escriba el nuevo valor para Nombre")
        nombre = input()
        print("Escriba el nuevo valor para DNI")
        dni = input()
        print("Escriba el nuevo valor para Direccion")
        direccion = input()
        query = f"update clientes set nombrecliente = '{nombre}', nroidentidicacioncliente = '{dni}',direccioncliente = '{direccion}' where idclientes = {idclientes};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")

        print("Si desea continuar escriba 1, para salir 2")
        input("Ingrese su opción: ")
    elif(resMenuCliente == 3):
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
    elif(resMenuCliente == 4):
        log.debug("eliminamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea eliminar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idcliente = input()
        
        query = f"delete from clientes where idcliente = {idcliente} ;"
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
    elif resMenu == 3:
        log.debug("escogio 3")
    elif resMenu == 4:
        log.debug("escogio 4")
    else:
        log.debug(f"escogio {resMenu}")
#Producto
def mantenimientoProducto():
    dicMenuProducto = {  "\t- Buscar Producto Todos": 1,
                        "\t- Modificar Producto por ID": 2,
                        "\t- Crear Producto": 3,
                        "\t- Borrar Producto": 4}
    menuProducto = utils.Menu("Menu Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if(resMenuProducto == 1):
        log.debug("buscamos Producto")
        conn = conexion.conexionBDD(1)
        query = "select idproductos as ID, nombreproducto as Nombre, valorproducto as Valor, igvproducto as IGV from productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        print("Si desea continuar escriba 1, para salir 2")
        input("Ingrese su opción: ")
        print(resConn)
    elif(resMenuCliente == 2):
        log.debug("buscamos producto")
        conn = conexion.conexionBDD(1)
        query = "select idproductos as ID, nombrecliente as Nombre, valorproducto as Valor, igvproducto as IGV from productos;"
        resConn = conn.consultarBDD(query)
        print("Elija el ID del producto que desea modificar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproductos = input()
        print("Escriba el nuevo valor para Nombre")
        nombre = input()
        print("Escriba el nuevo valor para Valor")
        valor = input()
        print("Escriba el nuevo valor para IGV")
        igv = input()
        query = f"update clientes set nombreproducto = '{nombre}',valorproducto = '{valor}', igvproducto = '{igv}' where idproductos = {idproductos};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente.")
        else:
            print("Hubo un error. Intente nuevamente.")

        print("Si desea continuar escriba 1, para salir 2")
        input("Ingrese su opción: ")
    elif(resMenuCliente == 3):
        print("##Creacion de un Producto##")
        print("Escriba el ID del Producto")
        ide = input()
        print("Escriba el Nombre del Producto")
        nombre = input()
        print("Escriba el Valor del Producto")
        valor = input()
        print("Escriba el IGV del Producto")
        igv = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into productos (idproductos,nombreproducto,valorproducto,igvproducto) values('{ide}','{nombre}','{valor}','{igv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente.")
        else:
            print("Hubo un error. Intente nuevamente.")
        
        print("Si desea continuar escriba 1, para salir 2")
        input("Ingrese su opción: ")
    elif(resMenuCliente == 4):
        log.debug("eliminamos producto")
        conn = conexion.conexionBDD(1)
        query = "select idproductos as ID, nombreproducto as Nombre, valorproducto as Valor, igvproducto as IGV from productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea eliminar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")

        idproductos = input()
        
        query = f"delete from productos where idproductos = {idproductos} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente.")
        else:
            print("Hubo un error, intente nuevamente.")
        
        input("desea continuar???")

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
