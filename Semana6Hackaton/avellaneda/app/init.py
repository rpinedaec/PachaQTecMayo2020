import os
import utils
import datetime
import conexion
import clientes
import productos
import tipopago
import empresa
import factura

log = utils.log("INIT")
log.info("Inicio de Programa")

lstClientes = []
lstProductos = []
lstTipoPago = []
lstEmpresa = []



# def cargarObjetos():
#     # SE PONE EL 1 PORQUE EN EL ARCHIVO "conexion" EL 1 ES PARA CONECTARSE CON LA BASE DE DATOS SQL
#     conn = conexion.conexionBDD(1)
#     # LA LINEA SIGUIENTE ES SOLO ****COMO EJEMPLO**** PARA MOSTRAR LOS CLIENTES, PERO DEBERÁ MOSTRAR LA FACTURA ENTERA
#     query ="SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes;"
#     resConn = conn.consultarBDD(query)
#     for row in resConn:
#         cliente = clientes.clientes(row[0],row[1],row[2],row[3])
#         lstClientes.append(cliente)
    
#     for obj in lstClientes:
#         print(obj.nombreCliente)
#     input("Continuar")

#  ██████ ██      ██ ███████ ███    ██ ████████ ███████ ███████ 
# ██      ██      ██ ██      ████   ██    ██    ██      ██      
# ██      ██      ██ █████   ██ ██  ██    ██    █████   ███████ 
# ██      ██      ██ ██      ██  ██ ██    ██    ██           ██ 
#  ██████ ███████ ██ ███████ ██   ████    ██    ███████ ███████

def mantenimientoCliente():
    dicMenuCliente = {"\t- Mostrar Clientes": 1, "\t- Buscar Cliente por DNI": 2, "\t- Actualizar Cliente": 3, "\t- Añadir Cliente": 4, "\t- Eliminar Cliente": 5}
    menuCliente = utils.Menu("Menu Cliente", dicMenuCliente)
    resMenuCliente = menuCliente.mostrarMenu()

#MOSTRAR TODOS LOS CLIENTES
    if(resMenuCliente == 1):
        log.debug("Buscamos Cliente")
        conn = conexion.conexionBDD(1)
        query = "SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDirección")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("¿Desea Continuar?")
        print(resConn)

#BUSCAR LOS CLIENTES POR DNI (FILTRO)
    elif(resMenuCliente == 2):
        log.debug("Buscamos Cliente por DNI")
        print("Escribe el numero de DNI")
        dni = input()

        conn = conexion.conexionBDD(1)
        query = f"SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes WHERE numeroIdCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDirección")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("¿Desea Continuar?")
        print(resConn)

#ACTUALIZAR DATOS DE CLIENTE
    elif(resMenuCliente == 3):
        log.debug("Buscamos Cliente")
        conn = conexion.conexionBDD(1)
        query = "SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que se actualizará:")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDirección")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idclientes = input()
        print("Escriba el nuevo Nombre")
        nombre = input()
        print("Escriba el nuevo DNI")
        dni = input()
        print("Escriba la nueva Dirección")
        direccion = input()
        query = f"UPDATE clientes SET  nombreCliente = '{nombre}', numeroIdCliente = '{dni}', direccionCliente = '{direccion}' WHERE idclientes = {idclientes};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Actualizado")
        else:
            print("Eres un fracaso")
        input("¿Desea Continuar?") 

#AÑADIR NUEVO CLIENTE
    elif(resMenuCliente == 4):
        log.debug("Añadición de cliente")
        print("Escriba el nombre del cliente")
        nombre = input()
        print("Escriba el DNI del cliente")
        dni = input()
        print("Escriba la Dirección del cliente")
        direccion = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO clientes (nombreCliente, numeroIdCliente, direccionCliente) VALUES ('{nombre}', '{dni}', '{direccion}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Añadido")
        else:
            print("Eres un fracaso")

        input("Desea Continuar?")

#ELIMINAR CLIENTE
    elif(resMenuCliente == 5):
        log.debug("Eliminación de cliente")
        conn = conexion.conexionBDD(1)
        query = "SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que se eliminará:")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDirección")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idclientes = input()
        query = f"DELETE FROM clientes WHERE idclientes = {idclientes};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Cliente eliminado")
        else:
            print("Eres un fracaso")
        input("¿Desea Continuar?") 


# ██████  ██████   ██████  ██████  ██    ██  ██████ ████████  ██████  ███████ 
# ██   ██ ██   ██ ██    ██ ██   ██ ██    ██ ██         ██    ██    ██ ██      
# ██████  ██████  ██    ██ ██   ██ ██    ██ ██         ██    ██    ██ ███████ 
# ██      ██   ██ ██    ██ ██   ██ ██    ██ ██         ██    ██    ██      ██ 
# ██      ██   ██  ██████  ██████   ██████   ██████    ██     ██████  ███████

def mantenimientoProductos():
    dicMenuProductos = {"\t- Mostrar Productos": 1, "\t- Buscar Producto por Nombre": 2, "\t- Actualizar Producto": 3, "\t- Añadir Producto": 4, "\t- Eliminar Producto": 5}
    menuProductos = utils.Menu("Menu Productos", dicMenuProductos)
    resMenuProductos = menuProductos.mostrarMenu()

#MOSTRAR TODOS LOS PRODUCTOS
    if(resMenuProductos == 1):
        log.info("mostrar todos los productos")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproductos, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("¿Continuará?")
        print(resConn)

#BUSCAR LOS PRODUCTOS POR ID (FILTRO)
    elif(resMenuProductos == 2):
        log.info("buscar productos por ID")
        print("Escribe el nombre del producto:")
        nombre = input()

        conn = conexion.conexionBDD(1)
        query = f"SELECT idproductos, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos WHERE nombreProducto = '{nombre}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("¿Continuará?")
        print(resConn)

#ACTUALIZAR DATOS DE PRODUCTO
    elif(resMenuProductos == 3):
        log.info("actualizar productos")
        conn = conexion.conexionBDD(1)
    #EL QUERY-CRUD ACÁ SOLO VA A BUSCAR, MAS ABAJO TIENE QUE SER EL DE ACTUALIZAR POR LA VARIABLE QUE SE HAYA PEDIDO
        query = "SELECT idproductos, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del producto que se actualizará:")
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        
        idproductos = input()
        print("Escriba el nuevo nombre")
        nombre = input()
        print("Escriba el nuevo precio")
        precio = input()
    #ACA RECIÉN VIENE EL QUERY-CRUD DEL UPDATE Y POR ESO ES EJECUTAR EN VEZ DE CONSULTAR
        query = f"UPDATE productos SET nombreProducto = '{nombre}', valorProducto = '{precio}' WHERE idproductos = {idproductos};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Producto actualizado")
        else:
            print("Eres un fracaso")
        input("¿Continuará?")

#AÑADIR NUEVO PRODUCTO
    elif(resMenuProductos == 4):
        log.info("Añadición de productos")
        print("Escriba el nombre del producto")
        nombre =  input()
        print("Escriba el precio del producto")
        precio = input()
        print("Escriba manualmente el calculo del IGV")
        igv = input()
        # impuesto = int(precio * 3)
        # igv = input(impuesto)
        # igv = precio * 2
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO productos (nombreProducto, valorProducto, igvProducto) VALUES ('{nombre}', '{precio}', '{igv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Producto añadido")
        else:
            print("Eres un fracaso")
        input("¿Continuará?")

#ELIMINAR PRODUCTO POR NOMBRE
    elif(resMenuProductos == 5):
        log.info("van a eliminar un producto")
        conn = conexion.conexionBDD(1)
    #EL QUERY-CRUD ACÁ SOLO VA A BUSCAR, MAS ABAJO TIENE QUE SER EL DE ACTUALIZAR POR LA VARIABLE QUE SE HAYA PEDIDO
        query = "SELECT idproductos, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escriba el ID del producto que se eliminará:")
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
    
        idproductos = input()
        query = f"DELETE FROM productos WHERE idproductos = {idproductos};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Producto eliminado")
        else:
            print("Eres un fracaso")
        input("¿Continuará?")


# ███████ ███    ███ ██████  ██████  ███████ ███████  █████  
# ██      ████  ████ ██   ██ ██   ██ ██      ██      ██   ██ 
# █████   ██ ████ ██ ██████  ██████  █████   ███████ ███████ 
# ██      ██  ██  ██ ██      ██   ██ ██           ██ ██   ██ 
# ███████ ██      ██ ██      ██   ██ ███████ ███████ ██   ██

def mantenimientoEmpresa():
    dicMenuEmpresa = {"\t- Mostrar Empresas": 1, "\t- Buscar Empresa por Nombre": 2, "\t- Actualizar Empresa": 3, "\t- Añadir Empresa": 4, "\t- Eliminar Empresa": 5}
    menuEmpresa = utils.Menu("Menu Empresas", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()

#MOSTRAR TODAS LAS EMPRESAS
    if(resMenuEmpresa == 1):
        log.info("van a mostrar empresas")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tNOMBRE")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
        input("¿Desea Continuar?")
        print(resConn)

#BUSCAR LAS EMPRESAS POR ID (FILTRO)
    elif(resMenuEmpresa == 2):
        log.debug("Buscamos Empresa por RUC")
        print("Escribe el numero de RUC")
        ruc = input()

        conn = conexion.conexionBDD(1)
        query = f"SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa where rucEmpresa = '{ruc}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tNOMBRE")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
        input("¿Desea Continuar?")
        print(resConn)

#ACTUALIZAR DATOS DE LAS EMPRESAS
    elif(resMenuEmpresa == 3):
        log.debug("actualizar empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que se actualizará:")
        print("\tID\t\tRUC\t\t\tNOMBRE")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        rucEmpresa = input()
        print("Escriba el nuevo RUC")
        ruc = input()
        print("Escriba el nuevo Nombre")
        nombre = input()
        query = f"UPDATE empresa SET rucEmpresa = '{ruc}', nombreEmpresa = '{nombre}' WHERE rucEmpresa = {rucEmpresa};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Actualizado")
        else:
            print("Eres un fracaso")
        input("¿Desea Continuar?") 

#AÑADIR NUEVA EMPRESA
    elif(resMenuEmpresa == 4):
        log.debug("Añadición de empresa")
        print("Escriba el RUC de la empresa")
        ruc = input()
        print("Escriba el nombre de la empresa")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO empresa (rucEmpresa, nombreEmpresa) VALUES ('{ruc}', '{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Añadida")
        else:
            print("Eres un fracaso")

        input("Desea Continuar?")

#ELIMINAR EMPRESA
    elif(resMenuEmpresa == 5):
        log.debug("Eliminación de empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que se eliminará:")
        print("\tID\t\tRUC\t\t\tNOMBRE")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idempresa = input()
        query = f"DELETE FROM empresa WHERE idempresa = {idempresa};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Cliente eliminado")
        else:
            print("Eres un fracaso")
        input("¿Desea Continuar?") 


# ████████ ██ ██████   ██████  ███████     ██████  ███████     ██████   █████   ██████   ██████  
#    ██    ██ ██   ██ ██    ██ ██          ██   ██ ██          ██   ██ ██   ██ ██       ██    ██ 
#    ██    ██ ██████  ██    ██ ███████     ██   ██ █████       ██████  ███████ ██   ███ ██    ██ 
#    ██    ██ ██      ██    ██      ██     ██   ██ ██          ██      ██   ██ ██    ██ ██    ██ 
#    ██    ██ ██       ██████  ███████     ██████  ███████     ██      ██   ██  ██████   ██████  

def mantenimientoPagos():
    dicMenuPagos = {"\t- Mostrar Tipos de Pago": 1, "\t- Actualizar Tipos de Pago": 2, "\t- Añadir Tipos de Pago": 3, "\t- Eliminar Tipos de Pago": 4}
    menuPagos = utils.Menu("Menu Tipos de Pago", dicMenuPagos)
    resMenuPagos = menuPagos.mostrarMenu()
    
#MOSTRAR TODOS LOS TIPOS DE PAGO
    if(resMenuPagos == 1):
        log.debug("buscan tipos de pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipoPago;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tTipos de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        input("¿Desea Continuar?")
        print(resConn)

#ACTUALIZAR DATOS DEL TIPO DE PAGO
    elif(resMenuPagos == 2):
        log.debug("quieren actualizar tipos de pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipoPago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del tipo de pago que se actualizará:")
        print("\tID\t\tTipos de Pago")
        for row in resConn:
             print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipoPago = input()
        print("Escriba el nuevo Tipo de Pago")
        nombre = input()
        query = f"UPDATE tipoPago SET descTipoPago = '{nombre}' WHERE idtipoPago = {idtipoPago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Actualizado")
        else:
            print("Eres un fracaso")
        input("¿Desea Continuar?") 

#AÑADIR NUEVO TIPO DE PAGO
    elif(resMenuPagos == 3):
        log.debug("Añadición de tipos de pago")
        print("Escriba el tipo de pago")
        nombre = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO tipoPago (descTipoPago) VALUES ('{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Añadido")
        else:
            print("Eres un fracaso")

        input("Desea Continuar?")

#ELIMINAR TIPO DE PAGO
    elif(resMenuPagos == 4):
        log.debug("Eliminación de tipo depago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipoPago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del tipo de pago que se eliminará:")
        print("\tID\t\tTipos de Pago")
        for row in resConn:
             print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipoPago = input()
        query = f"DELETE FROM idtipoPago WHERE idtipoPago = {idtipoPago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Tipo de Pago eliminado")
        else:
            print("Eres un fracaso")
        input("¿Desea Continuar?") 


#   █████▒▄▄▄       ▄████▄  ▄▄▄█████▓ █    ██  ██▀███   ▄▄▄      
# ▓██   ▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▒████▄    
# ▒████ ░▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒██  ▀█▄  
# ░▓█▒  ░░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ░██▄▄▄▄██ 
# ░▒█░    ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒ ▓█   ▓██▒
#  ▒ ░    ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
#  ░       ▒   ▒▒ ░  ░  ▒       ░    ░░▒░ ░ ░   ░▒ ░ ▒░  ▒   ▒▒ ░
#  ░ ░     ░   ▒   ░          ░       ░░░ ░ ░   ░░   ░   ░   ▒   
#              ░  ░░ ░                  ░        ░           ░  ░

def cargarObjetos():
    conn = conexion.conexionBDD(1)
    query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
    resConn = conn.consultarBDD(query)
    print("\tID\t\tEMPRESA\t\t\tRUC")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}")
    print("Escriba ID de Empresa")
    idempresa = input()
    print("Escriba DNI de cliente")
    dni = input()
    query = f"SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes WHERE numeroIdCliente = '{dni}';"
    resConn = conn.consultarBDD(query)
    y = resConn[0]
    idclientes = y[0]
    query = "SELECT idtipoPago, descTipoPago as Descripcion FROM tipoPago;"
    resConn = conn.consultarBDD(query)
    print("\tID\t\tTipo de Pago")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}")
    print("Escriba ID de Tipo de Pago")
    idtipoPago = input()
    lstFacDetalle = []
    subtotal = 0
    IGV = 0

    while True:
        query = "SELECT idproducto, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNOMBRE\t\t\tPRECIO\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")
        print("Escriba el ID del producto")
        idproducto = input()
        print("Escriba cantidad del producto")
        cantidad = int(input())
        query = f"SELECT idproducto, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos WHERE nombreProducto = '{idproducto}';"
        resconn = conn.consultarBDD(query)
        t = resconn[0]
        precio = t[0]
        igv = t[1]
        totalunitario = precio*cantidad
        igvMonto = igv*18*totalunitario/100
        dictFacDetalle = {}
        dictFacDetalle.update({"idproducto":idproducto})
        dictFacDetalle.update({"cantidad":cantidad})
        dictFacDetalle.update({"totalunitario":totalunitario})
        dictFacDetalle.update({"igvValor":igvMonto})
        lstFacDetalle.append(dictFacDetalle)

        subtotal = subtotal + totalunitario
        IGV = IGV + igvMonto

        opcion = input("Agregar un producto? y/n -> ")
        if(opcion == "y"):
            print("Agrega un producto")
        elif(opcion == "n"):
            break

    total = subtotal + IGV
    f = datetime.datetime.now()

    query = f"INSERT INTO facCabecera (fechaFacCabecera, igvFacCabecera, subtotalFacCabecera, totalFacCabecera, idempresa, idtipoPago, idclientes, estadoFactura) VALUES ('{f}','{IGV}','{subtotal}','{total}','{idempresa}','{idtipoPago}','{idclientes}','E');"
    resConn = conn.ejecutarBDD(query)
    query3 = "SELECT idfacCabecera as cabecera from facCabecera;"
    resConn = conn.consultarBDD(query3)
    i = resConn[0]
    idfacCabeza = i[0]

    for dic in lstFacDetalle:
        cant = dic.get("cantidad")
        idprod = dic.get("idproducto")
        valorprod = dic.get("totalunitario")
        query = f"INSERT INTO facDetalle (cantFacDetalle, idfacCabecera, idproductos, valorFacDetalle) values ('{cant}','{idfacCabeza}','{idprod}','{valorprod}')"
        resConn = conn.ejecutarBDD(query)
        log.info("Estan generando factura")
    input("Añadida")

    query = f"SELECT A.fechaFacCabecera as Fecha,
                B.nombreEmpresa as Empresa,
                C.nombreCliente as Cliente,
                D.tipoPago as TipoPago 
                from facCabecera A LEFT JOIN Empresa B 
                on a.idempresa = B.idempresa LEFT JOIN Clientes C 
                on a.idclientes = C.idclientes LEFT JOIN TipoPago D 
                on a.idtipoPago = D.idtipoPago WHERE idfacCabecera = '{idfacCabeza}';"
    resConn = conn.consultarBDD(query)
    print("\tFECHA\t\t\t\tEMPRESA\t\t\tCLIENTE\t\t\tTIPO DE PAGO")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")

    query = f"SELECT A.cantFacDetalle as Cantidad,
                B.nombreProducto as Producto,
                C.valorProducto as Precio,
                A.valorProducto as Importe from facdetalle a LEFT JOIN productos B 
                on A.idproductos = B.idproductos WHERE A.idfacCabecera = '{idfacCabeza}';"
    resConn = conn.consultarBDD(query)
    print("\tCANTIDAD\tPRODUCTO\t\tMONTO\t\t\tTOTAL")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")


    query =f"SELECT subtotalFacCabecera as Subtotal, igvFacCabecera as IGV, totalFacCabecera as Total from facCabecera where idfacCabecera = '{idfacCabeza}';"
    resConn = conn.consultarBDD(query)
    print("\tSUBTOTAL\tIGV\t\tTOTAL")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
    input("ADIOS!")


#      /\__\         /\  \         /\__\         /\__\    
#     /::|  |       /::\  \       /::|  |       /:/  /    
#    /:|:|  |      /:/\:\  \     /:|:|  |      /:/  /     
#   /:/|:|__|__   /::\~\:\  \   /:/|:|  |__   /:/  /  ___ 
#  /:/ |::::\__\ /:/\:\ \:\__\ /:/ |:| /\__\ /:/__/  /\__\
#  \/__/~~/:/  / \:\~\:\ \/__/ \/__|:|/:/  / \:\  \ /:/  /
#        /:/  /   \:\ \:\__\       |:/:/  /   \:\  /:/  / 
#       /:/  /     \:\ \/__/       |::/  /     \:\/:/  /  
#      /:/  /       \:\__\         /:/  /       \::/  /   
#      \/__/         \/__/         \/__/         \/__/  


def mantenimiento(resMenu):
    if resMenu==1:
        log.debug("Escogió 1")
        mantenimientoCliente()
    elif resMenu==2:
        log.debug("Escogió 2")
        mantenimientoProductos()
    elif resMenu==3:
        log.debug("Escogió 3")
        mantenimientoEmpresa()
    elif resMenu==4:
        log.debug("Escogió 4")
    else:
        log.debug(f"Escogió {resMenu}")

    
stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Mostrar Factura": 1, "\t- Mantenimiento": 2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()

    if(resMenuInicio == 1):
        log.debug("Muestra el menu para crear factura")
        cargarObjetos()

    elif(resMenuInicio == 2):
        log.debug("Muestra el mantenimiento")
        dicMenuMantenimiento = {"\t- Clientes": 1, "\t- Productos": 2, "\t- Empresa": 3, "\t- Tipo de Pago": 4}
        menuMantenimiento = utils.Menu("Menu Mantenimiento", dicMenuMantenimiento)
        resMenuMantenimiento = menuMantenimiento.mostrarMenu()
        mantenimiento(resMenuMantenimiento)

    elif(resMenuInicio == 9):
        log.debug("Finaliza el programa")
        break

    else:
        log.debug("Volvemos a mostrar menu")
        stopMenuInicio = False