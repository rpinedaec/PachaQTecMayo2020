import utils
import conexion
from time import sleep
import datetime


def MantenimientoClientes():

    def printEncabezadoC():
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")
    conn = conexion.conexionBDD(1)
    while True:
        dicMenuCliente = {"Buscar Clientes": 1, "Buscar Cliente por DNI": 2, "Modificar Cliente por ID": 3, "Crear Cliente": 4, "Borrar Cliente": 5, "Salir":9}
        menuCliente = utils.Menu("Cliente",dicMenuCliente)
        menuCliente.printMenu()
        opcionMenuCliente = menuCliente.inputMenu()
        if (opcionMenuCliente == 1):
            query = "select idclientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
            resConn = conn.consultarBDD(query)
            printEncabezadoC()
            input("Continuar?")
            print(resConn)
        if (opcionMenuCliente == 2):
            print("Escribe el numero de DNI")
            dni = input()
            query = f"select idclientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentificacionCliente = '{dni}';"
            resConn = conn.consultarBDD(query)
            printEncabezadoC()
            input("Continuar?")
            print(resConn)
        if (opcionMenuCliente == 3):
            query = "select idclientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del cliente que desea modificar")
            printEncabezadoC()
            idcliente = input()
            print("Escriba el nuevo valor para Nombre")
            nombre = input()
            print("Escriba el nuevo valor para DNI")
            dni = input()
            print("Escriba el nuevo valor para Direccion")
            direccion = input()
            query = f"update clientes set nombreCliente = '{nombre}', nroIdentificacionCliente = '{dni}',direccionCliente = '{direccion}' where idclientes = {idcliente};"
            resConn = conn.ejecutarBDD(query)

            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            input("¿Desea continuar?")
        if (opcionMenuCliente == 4):
            print("Creacion de un cliente")
            print("Escriba el Nombre del Cliente")
            nombre = input()
            print("Escriba el DNI del Cliente")
            dni = input()
            print("Escriba el Direccion del Cliente")
            direccion = input()
            query = f"insert into clientes (nombreCliente, nroIdentificacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            input("¿Desea continuar?")
        if (opcionMenuCliente == 5):
            query = "select idclientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del cliente que desea eliminar")
            printEncabezadoC()
            idcliente = input()
            query = f"delete from clientes where idclientes = {idcliente} ;"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            input("¿Desea continuar?")
        if (opcionMenuCliente == 9):
            break

def MantenimientoProductos():

    def printEncabezadoP():
        print("\tID\t\tProducto\t\t\tPrecio\t\t\tconIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")

    while True:
        dicMenuProductos = {"Buscar Productos": 1, "Buscar Producto por Nombre": 2, "Modificar Producto por ID": 3, "Crear Producto": 4, "Borrar Producto": 5, "Salir":9}
        menuProductos = utils.Menu("Productos",dicMenuProductos)
        menuProductos.printMenu()
        opcionMenuProductos = menuProductos.inputMenu()
        if (opcionMenuProductos == 1):
            conn = conexion.conexionBDD(1)
            query = "select idproductos, nombreProducto as Producto, valorProducto as Precio, igvProducto as conIGV from productos;"
            resConn = conn.consultarBDD(query)
            printEncabezadoP()
            input("Continuar?")
            print(resConn)
        if (opcionMenuProductos == 2):
            print("Escribe el nombre del Producto")
            nomProducto = input()
            conn = conexion.conexionBDD(1)
            query = f"select idproductos, nombreProducto as Producto, valorProducto as Precio, igvProducto as conIGV from productos where nombreProducto = '{nomProducto}';"
            resConn = conn.consultarBDD(query)
            printEncabezadoP()
            input("Continuar?")
            print(resConn)
        if (opcionMenuProductos == 3):
            conn = conexion.conexionBDD(1)
            query = "select idproductos, nombreProducto as Producto, valorProducto as Precio, igvProducto as conIGV from productos;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del producto que desea modificar")
            printEncabezadoP()
            idproducto = input()
            print("Escriba el nuevo nombre para Producto")
            producto = input()
            print("Escriba el nuevo valor para Precio")
            precio = input()
            print("Escriba 1 si su producto tiene igv o 0 si no tiene")
            igvP = input()
            query = f"update productos set nombreProducto = '{producto}',valorProducto = '{precio}', igvProducto = '{igvP}' where idproductos = {idproducto};"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            input("¿Desea continuar?")
        if (opcionMenuProductos == 4):
            print("Creacion de un producto")
            print("Escriba el Nombre del producto")
            producto = input()
            print("Escriba el precio del producto")
            precio = input()
            print("Escriba 1 si su producto tiene igv o 0 si no tiene")
            igvP = input()
            conn = conexion.conexionBDD(1)
            query = f"insert into productos (nombreProducto,valorProducto, igvProducto) values('{producto}','{precio}','{igvP}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("¿Desea continuar?")
        if (opcionMenuProductos == 5):
            conn = conexion.conexionBDD(1)
            query = "select idproductos, nombreProducto as Producto, valorProducto as Precio, igvProducto as conIGV from productos;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del producto que desea eliminar")
            printEncabezadoP()
            idproducto = input()
            query = f"delete from productos where idproductos = {idproducto} ;"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("¿Desea continuar?")
        if (opcionMenuProductos == 9):
            break

def MantenimientoEmpresa():
    def printEncabezadoE():
        print("\tID\t\tEmpresa\t\t\tRUC")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}")

    while True:
        dicMenuEmpresa = {"Buscar Empresa": 1, "Buscar Empresa por RUC": 2, "Modificar Empresa por ID": 3, "Crear Empresa": 4, "Borrar Empresa": 5, "Salir":9}
        menuEmpresa = utils.Menu("Empresa",dicMenuEmpresa)
        menuEmpresa.printMenu()
        opcionMenuEmpresa = menuEmpresa.inputMenu()
        if (opcionMenuEmpresa == 1):
            conn = conexion.conexionBDD(1)
            query = "select idempresa, nombreEmpresa as Empresa, rucEmpresa as RUC from empresa;"
            resConn = conn.consultarBDD(query)
            printEncabezadoE()
            input("Continuar?")
            print(resConn)
        if (opcionMenuEmpresa == 2):
            print("Escribe el RUC de la empresa")
            ruc = input()
            conn = conexion.conexionBDD(1)
            query = f"select idempresa, nombreEmpresa as Empresa, rucEmpresa as RUC from empresa where rucEmpresa = '{ruc}';"
            resConn = conn.consultarBDD(query)
            printEncabezadoE()
            input("Continuar?")
            print(resConn)
        if (opcionMenuEmpresa == 3):
            conn = conexion.conexionBDD(1)
            query = "select idempresa, nombreEmpresa as Empresa, rucEmpresa as RUC from empresa;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID de la empresa que desea modificar")
            printEncabezadoE()
            idempresaa = input()
            print("Escriba el nuevo nombre para Empresa")
            empresa = input()
            print("Escriba el nuevo valor para RUC")
            ruc = input()
            query = f"update empresa set nombreEmpresa = '{empresa}', rucEmpresa = '{ruc}' where idempresa = {idempresaa};"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            input("¿Desea continuar?")
        if (opcionMenuEmpresa == 4):
            print("Creacion de una empresa")
            print("Escriba el Nombre de la empresa")
            empresa = input()
            print("Escriba el RUC de la empresa")
            ruc = input()
            conn = conexion.conexionBDD(1)
            query = f"insert into empresa (nombreEmpresa, rucEmpresa) values('{empresa}','{ruc}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("¿Desea continuar?")
        if (opcionMenuEmpresa == 5):
            conn = conexion.conexionBDD(1)
            query = "select idempresa, nombreEmpresa as Empresa, rucEmpresa as RUC from empresa;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID de la empresa que desea eliminar")
            printEncabezadoE()
            idempresaa = input()
            query = f"delete from empresa where idempresa = {idempresaa} ;"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("¿Desea continuar?")
        if (opcionMenuEmpresa == 9):
            break

def MantenimientoTipoPago():

    def printEncabezadoTP():
        print("\tID\t\tTipo de Pago")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

    while True:
        dicMenuTIPP = {"Mostrar tipo de pago": 1, "Modificar tipo de pago por ID": 2, "Crear tipo de pago": 3, "Borrar tipo de pago": 4, "Salir":9}
        menuTIPP = utils.Menu("Tipo de pago",dicMenuTIPP)
        menuTIPP.printMenu()
        opcionmenuTIPP = menuTIPP.inputMenu()
        if (opcionmenuTIPP == 1):
            conn = conexion.conexionBDD(1)
            query = "select idtiPopago, tipoPagocol as TipoPago from tipoPago;"
            resConn = conn.consultarBDD(query)
            printEncabezadoTP()
            input("Continuar?")
            print(resConn)
        if (opcionmenuTIPP == 2):
            conn = conexion.conexionBDD(1)
            query = "select idtiPopago, tipoPagocol as TipoPago from tipoPago;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del tipo de pago que desea modificar")
            printEncabezadoTP()
            idtp = input()
            print("Escriba el nuevo tipo de pago")
            tp = input()
            query = f"update tipoPago set tipoPagocol = '{tp}' where idtiPopago = {idtp};"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            input("¿Desea continuar?")
        if (opcionmenuTIPP == 3):
            print("Creacion de un tipo de pago")
            print("Escriba el tipo de pago")
            tp = input()
            conn = conexion.conexionBDD(1)
            query = f"insert into tipoPago (tipoPagocol) values('{tp}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("¿Desea continuar?")
        if (opcionmenuTIPP == 4):
            conn = conexion.conexionBDD(1)
            query = "select idtiPopago, tipoPagocol as TipoPago from tipoPago;"
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del tipo de pago que desea eliminar")
            printEncabezadoTP()
            idtp = input()
            query = f"delete from tipoPago where idtiPopago = {idtp} ;"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input("¿Desea continuar?")
        if (opcionmenuTIPP == 9):
            break
    
def crearFactura():
    conn = conexion.conexionBDD(1)
    query = "select idempresa, nombreEmpresa as Empresa, rucEmpresa as RUC from empresa;"
    resConn = conn.consultarBDD(query)
    print("\tID\t\tEmpresa\t\t\tRUC")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}")

    print("Seleccione el ID de la empresa")
    idempresa = input()
    print("Ingrese DNI del cliente")
    dnicliente = input()

    query = f"select idclientes from clientes where nroIdentificacionCliente = '{dnicliente}';"
    resConn = conn.consultarBDD(query)
    x = resConn[0]
    idcliente = x[0]


    query = "select idtiPopago, tipoPagocol as TipoPago from tipoPago;"
    resConn = conn.consultarBDD(query)
    print("\tID\t\tTipo de Pago")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}")

    print("Seleccione el ID del tipo de pago")
    idtipopago = input()
    lstFacDetalle = []

    subtotal = 0
    IGV = 0
    while True:
        query = "select idproductos, nombreProducto as Producto, valorProducto as Precio, igvProducto as conIGV from productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tProducto\t\t\tPrecio\t\t\tconIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")

        print("Seleccione el ID del producto")
        idproducto = input()
        print("Ingrese cantidad del producto")
        cantidad = int(input())

        query = f"select valorProducto, igvProducto from productos where idproductos = '{idproducto}';"
        resconn = conn.consultarBDD(query)
        t = resconn[0]
        precio = t[0]
        igv = t[1]
        totalunitario = precio*cantidad
        igvValor = igv*18*totalunitario/100
        dictFacDetalle = {}
        dictFacDetalle.update({"idproducto":idproducto})
        dictFacDetalle.update({"cantidad":cantidad})
        dictFacDetalle.update({"totalunitario":totalunitario})
        dictFacDetalle.update({"igvValor":igvValor})
        lstFacDetalle.append(dictFacDetalle)

        subtotal = subtotal + totalunitario
        IGV = IGV + igvValor

        opcion = input("Desea agregar un producto? Si/No -> ")
        if(opcion == "Si"):
            print("Agrega un producto")
        elif(opcion == "No"):
            break

    total = subtotal + IGV
    f = datetime.datetime.now()

    query = f"insert into faccabecera (fechaFacCabecera,igvFacturaCabecera,subtotalFacCabecera,totalFacCabecera,empresa_idempresa,tipoPago_idtipoPago,clientes_idclientes,estadoFactura) values ('{f}','{IGV}','{subtotal}','{total}','{idempresa}','{idtipopago}','{idcliente}','E');"
    resConn = conn.ejecutarBDD(query)

    query1 = "select MAX(idfacCabecera) as id from faccabecera;"
    resConn = conn.consultarBDD(query1)
    i = resConn[0]
    idfaccb = i[0]

    for dic in lstFacDetalle:
        cant = dic.get("cantidad")
        idpro = dic.get("idproducto")
        valorpro = dic.get("totalunitario")
        query = f"insert into facdetalle (cantFacDetalle,facCabecera_idfacCabecera,productos_idproductos,valorProducto) values ('{cant}','{idfaccb}','{idpro}','{valorpro}')"
        resConn = conn.ejecutarBDD(query)

    input("Generar factura... ")

    query = f"select a.fechaFacCabecera as Fecha,b.nombreEmpresa as Empresa,c.nombreCliente as Cliente,d.tipoPagocol as TipoPago from faccabecera a left join empresa b on a.empresa_idempresa = b.idempresa left join clientes c on a.clientes_idclientes=c.idclientes left join tipopago d on a.tipoPago_idtipoPago=d.idtipoPago where idfacCabecera = '{idfaccb}';"
    resConn = conn.consultarBDD(query)
    print("\tFecha\t\t\t\tEmpresa\t\t\tCliente\t\t\tTipoPago")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")

    print("\t-----------------------------------------------------------------------------------------------------------")

    query = f"select a.cantFacDetalle as Cantidad,b.nombreProducto as Producto,b.valorProducto as Precio,a.valorProducto as Importe from facdetalle a left join productos b on a.productos_idproductos = b.idproductos where a.facCabecera_idfacCabecera = '{idfaccb}';"
    resConn = conn.consultarBDD(query)
    print("\tCantidad\tProducto\t\tPrecio\t\t\tImporte")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t\t{str(row[3])}")

    print("\t-----------------------------------------------------------------------------------------------------------")

    query =f"select subtotalFacCabecera as Subtotal,igvFacturaCabecera as IGV,totalFacCabecera as Total from faccabecera where idfacCabecera = '{idfaccb}';"
    resConn = conn.consultarBDD(query)
    print("\tSubtotal\tIGV\t\tTotal")
    for row in resConn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

    input("Cerrar? ")

while True:
    dictMenuPrincipal = {"Crear Factura": 1, "Mantenimientos": 2, "Salir":9}
    MenuPrincipal = utils.Menu("Principal",dictMenuPrincipal)
    MenuPrincipal.printMenu()
    opcionMenuPrincipal = MenuPrincipal.inputMenu()

    if(opcionMenuPrincipal == 1):
        crearFactura()

    elif(opcionMenuPrincipal == 2):
        while True:
            dicMenuMantenimiento = {"Clientes": 1, "Productos": 2,"Empresa": 3, "Tipo de pago": 4, "Salir":9}
            menuMantenimiento = utils.Menu("Mantenimiento",dicMenuMantenimiento)
            menuMantenimiento.printMenu()
            opcionMenuMantenimiento = menuMantenimiento.inputMenu()

            if(opcionMenuMantenimiento == 1):
                MantenimientoClientes()

            elif(opcionMenuMantenimiento == 2):
                MantenimientoProductos()

            elif(opcionMenuMantenimiento == 3):
                MantenimientoEmpresa()

            elif(opcionMenuMantenimiento == 4):
                MantenimientoTipoPago()

            elif(opcionMenuMantenimiento == 9):
                break
            
            else:
                print("Elige la opcion correcta")

    elif(opcionMenuPrincipal == 9):
        break

