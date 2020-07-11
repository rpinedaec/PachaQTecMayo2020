import utils
import conexion
import clientes
import productos
import tipopago
import empresa

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

def cargarObjetos():
    conn = conexion.conexionBDD(1)
    query = "select idcliente, nomcliente as Nombre, docidentidad as ID, direccion as Direccion from clientes;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        cliente = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(cliente)

    for obj in lstClientes:
        print(obj.nomcliente)
    input("continuar")
    ##############################################################################
    conn = conexion.conexionBDD(1)
    query = "SELECT idproducto,nombreproducto as Nombre,valorproducto as Valor,igvproducto as IGV FROM productos;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        producto = productos.productos(row[0],row[1],row[2],row[3])
        lstProductos.append(producto)

    for obj in lstProductos:
        print(obj.nombreproducto)
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
        query = "select idCliente, nomcliente as Nombre, docidentidad as ID, direccion as Direccion from clientes;"
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
        query = f"select idcliente, nomcliente as Nombre, docidentidad as ID, direccion as Direccion from clientes where docidentidad = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuCliente == 3):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idCliente, nomcliente as Nombre, docidentidad as ID, direccion as Direccion from clientes;"
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
        query = f"update clientes set nomcliente = '{nombre}', docidentidad = '{dni}',direccion = '{direccion}' where idcliente = {idcliente};"
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
        query = f"insert into clientes (nomcliente, docidentidad,direccion) values('{nombre}','{dni}','{direccion}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuCliente == 5):
        log.debug("eliminamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idcliente, nomcliente as Nombre, docidentidad as ID, direccion as Direccion from clientes;"
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
#############################################################################################################################
def mantenimientoProducto():
    dicMenuProducto = {  "\t- Listar Todos los Productos": 1,
                        "\t- Buscar Producto por Nombre": 2,
                        "\t- Modificar Producto por Nombre": 3,
                        "\t- Crear Producto": 4,
                        "\t- Borrar Producto": 5}
    menuProducto = utils.Menu("Menu Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if(resMenuProducto == 1):
        log.debug("buscamos Producto")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproducto,nombreproducto as Nombre,valorproducto as Valor,igvproducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 2):
        log.debug("buscamos Producto por Nombre")
        print("escribe el Nombre del Producto")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idproducto,nombreproducto as Nombre,valorproducto as Valor,igvproducto as IGV FROM productos where nombreproducto = '{nombre}';"
         
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuProducto == 3):
        log.debug("buscamos Producto")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproducto,nombreproducto as Nombre,valorproducto as Valor,igvproducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Producto que desea modificar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        print("Escriba el nuevo valor para Nombre")
        nombre = input()
        print("Escriba el nuevo valor para Precio")
        precio = input()
        print("Escriba el nuevo valor para IGV")
        igv = input()
        query = f"UPDATE productos SET nombreproducto = '{nombre}', valorproducto = '{precio}',igvproducto = '{igv}' where idproducto = {idproducto};"

        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 4):
        print("##Creacion de un Producto##")
        print("Escriba el Nombre del Producto")
        nombre = input()
        print("Escriba el Valor del Producto")
        precio = input()
        print("Escriba el IGV del Producto")
        igv = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into productos (nombreproducto, valorproducto,igvproducto) values('{nombre}','{precio}','{igv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuProducto == 5):
        log.debug("Eliminamos Producto")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproducto,nombreproducto as Nombre,valorproducto as Valor,igvproducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Producto que desea eliminar")
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

#############################################################################################################################
def mantenimientoEmpresa():
    dicMenuEmpresa = {  "\t- Listar Todas las Empresas": 1,
                        "\t- Buscar Empresa por RUC": 2,
                        "\t- Modificar Empresa por RUC": 3,
                        "\t- Crear Empresa": 4,
                        "\t- Borrar Empresa": 5}
    menuEmpresa = utils.Menu("Menu Empresa", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        log.debug("buscamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucempresa as RUC, nomempresa as Nombre from empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 2):
        log.debug("buscamos Empresa por RUC")
        print("Escribe el RUC de la Empresa")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"select idempresa, rucempresa as RUC, nomempresa as Nombre from empresa where = '{ruc}';"
         
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
        input("continuar???")
        print(resConn)
    elif(resMenuEmpresa == 3):
        log.debug("Buscamos Empresas")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucempresa as RUC, nomempresa as Nombre from empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la Empresa que desea modificar")
        print("\tID\t\tRUC\t\t\tNombre")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idempresa = input()
        print("Escriba el nuevo valor para RUC")
        nombre = input()
        print("Escriba el nuevo valor para Nombre")
        precio = input()
        query = f"UPDATE empresa SET rucempresa = '{nombre}', nomempresa = '{precio}'  where idempresa = {idempresa};"

        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se actualizó correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuEmpresa == 4):
        print("##Creacion de una Empresa##")
        print("Escriba el RUC de la Empresa")
        ruc = input()
        print("Escriba el Nombre de la Empresa")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO empresa(rucempresa,nomempresa) VALUES('{ruc}','{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuEmpresa == 5):
        log.debug("Eliminamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "select idempresa, rucempresa as RUC, nomempresa as Nombre from empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la Empresa que desea eliminar")
        print("\tID\t\tRUC\t\t\tNombre")
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

#############################################################################################################################
def mantenimientoTipopago():
    dicMenuTipopago = {  "\t- Listar Todas los Tipos de Pago": 1,
                        "\t- Buscar Tipos de Pago por Descripción": 2,
                        "\t- Modificar Tipo de Pago por Descripción": 3,
                        "\t- Crear Tipo de Pago": 4,
                        "\t- Borrar Tipo de Pago": 5}
    menuTipopago = utils.Menu("Menu Tipo de Pago", dicMenuTipopago)
    resMenuTipopago = menuTipopago.mostrarMenu()
    if(resMenuTipopago == 1):
        log.debug("buscamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "Select idtipopago,desctipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDescripción")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        input("continuar???")
        print(resConn)
    elif(resMenuTipopago == 2):
        log.debug("buscamos Tipo de Pago por Descripción")
        print("Escribe el Tipo de Pago")
        descrip = input()
        conn = conexion.conexionBDD(1)
        query = f"Select idtipopago,desctipoPago as Descripcion from tipopago where desctipoPago = '{descrip}';"
         
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDescripción")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        input("continuar???")
        print(resConn)
    elif(resMenuTipopago == 3):
        log.debug("Buscamos Tipos de Pagos")
        conn = conexion.conexionBDD(1)
        query = "Select idtipopago,desctipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Tipo de Pago que desea modificar")
        print("\tID\t\tDescripción")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipopago = input()
        print("Escriba el nuevo valor para Tipo de Pago")
        descrip = input()
        
        query = f"update tipopago set desctipoPago =  '{descrip}' where idtipopago = {idtipopago};"

        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("El tipo de Pago Se actualizó Correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuTipopago == 4):
        print("##Creacion de un Tipo de Pago##")
        print("Escriba el Tipo de Pago")
        descrip = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO tipopago(desctipoPago) VALUES('{descrip}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")
    elif(resMenuTipopago == 5):
        log.debug("Eliminamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "Select idtipopago,desctipoPago as Descripcion from tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del Tipo de Pago a Eliminar")
        print("\tID\t\tDescripción")
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
        mantenimientoTipopago()
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
