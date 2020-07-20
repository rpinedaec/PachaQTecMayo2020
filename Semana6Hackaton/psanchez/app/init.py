import utils
import connect
import clientes
import factura
import productos
import empresa
import querysdb
import tipopago
import random
import os

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

MenuInicio = True
while MenuInicio:
    dicMenuInicio = {"\t- Facturacion": 1, "\t- Mantenimientos": 2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("mostramos el Menu Factura")
        VerFacturas = Facturacion.MenuFacturacion()

    elif(resMenuInicio == 2):
        log.debug("Mostramos los Mantenimientos")
        VerProductos = Mantenimiento.MenuMantenimiento()

    elif(resMenuInicio == 9):
        log.debug("finalizar Programa")
        print("Saliendo del programa. Adiós!")
        return os.system('clear')
        exit()
    else:
        log.debug("volvemos a mostrar menu")
        MenuInicio = False

class Mantenimiento:

    def MenuMantenimiento():
        mm = True
        while mm:
        dicMenuMantenimiento = {"\t- Clientes": 1, "\t- Producto": 2, "\t- Empresa": 3, "\t- Tipo de Pago": 4}
        menuMant = utils.Menu("Menu de Mantenimiento", dicMenuMantenimiento)
        resMenuMantenimiento = menuMant.mostrarMenu()
        if (resMenuMantenimiento == 1):
            log.debug("mantenimiento clientes")
            MantenimientoClnts = Mantenimiento.MenuClientes()

        elif (resMenuMantenimiento == 2):
            log.debug("mantenimiento clientes")
            MantenimientoClnts = Mantenimiento.MenuProducto()

        elif (resMenuMantenimiento == 3):
            log.debug("mantenimiento clientes")
            MantenimientoClnts = Mantenimiento.MenuEmpresa()

        elif (resMenuMantenimiento == 4):
            log.debug("mantenimiento clientes")
            MantenimientoClnts = Mantenimiento.MnenuTipoPago()

        elif(resMenuMantenimiento == 9):
            log.debug("Finalizar Programa")
            print("Saliendo del programa. Adiós!")
            return os.system('clear')
            exit()
        else:
            log.debug("volvemos a mostrar menu")
            mm = False

    def MenuClientes():
        #Opciones MenuClientes
        dicMenuClt = {  "\t- Buscar Todos": 1,
                        "\t- Buscar por DNI": 3,
                        "\t- Modificar": 2,
                        "\t- Crear": 3,
                        "\t- Borrar": 5}
        menuClts = utils.Menu("Menu", dicMenuClt)
        resMenuClts = menuClts.mostrarMenu()
        #Op 1---------------------------------------------------------------
        if (resMenuClts==1):
            log.debug("buscamos todos los clientes")   
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.clientes(selectallcliente)
            resconn = conn.consultarBDD(query)
            print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
            for row in resconn:
                cliente = clientes.selectallcliente(row[0],row[1],row[2],row[3])
                lstClientes.append(cliente)

            for obj in lstClientes:
                print(obj.nombreCliente)
            sleep (3)
            print("Regresando al Menu")
        # Op 2 -------------------------------------------------------------
        elif (resMenuClts==2):
            log.debug("buscamos cliente por DNI")
            print("Ingresa el No. de DNI")
            dni = input()
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.clientes(selectidclient)
            resConn = conn.consultarBDD(query)
            print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
            for row in resConn:
                print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
            sleep (3)
            print("Regresando al Menu")
        #Op 3 ---------------------------------------------------------------
        elif(resMenuClts==3):
            log.debug("modificamos cliente")
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.clientes(selectallcliente)
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
            query = querysdb.QueryDB.clientes(updatecliente)
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se actualizo correctamente")
            else:
                print("Hubo un error. Intente nuevamente.")
                sleep(0.5)
        #Op 4 -----------------------------------------------------------------
        elif(resMenuClts == 4):
            print("Escriba el Nombre del Cliente")
            nombre = input()
            print("Escriba el DNI del Cliente")
            dni = input()
            print("Escriba el Direccion del Cliente")
            direccion = input()
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.clientes(insertcliente)
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
        #Op 5 ----------------------------------------------------------------
        elif(resMenuClts == 5):
            log.debug("eliminamos cliente")
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.clientes(selectallcliente)
            resConn = conn.consultarBDD(query)
            print("Escoja el ID del cliente que desea eliminar")
            print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
            for row in resConn:
                print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
            idcliente = input()
            query = querysdb.QueryDB.clientes(deletecliente)
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            
            print("Si desea continuar escriba 1, para salir 2")
            input("Ingrese su opción: ")
            print("Listo")
    def MenuProducto():
    def MenuEmpresa():
    def MnenuTipoPago():

class Facturacion():

    def MenuFacturacion():
        dicMenuFactura = {"\t- Ver Todas": 1, "\t- Emitir una nueva": 2}
        menuFactura = utils.Menu("Menu Facturacion", dicMenuFactura)
        resMenuFactura = menuFactura.mostrarMenu()
        if (resMenuFactura == 1):
            log.debug("Buscamos todas las facturas")
            FacturasTodas = Facturacion.VerResumen()
        elif (resMenuFactura == 2):
            log.debug("Emitimos Factura")
            FacturasNueva = Facturacion.EmitirFactura()
    def VerResumen():

    def EmitirFactura():
        ingresandoprod = True
        while ingresandoprod:
            print("Ubica el producto que deseas anadir")
            log.debug("mostrando producto")   
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.producto(selectallproductos)
            resconn = conn.consultarBDD(query)
            print("ID", "Nombre\t", "Precio\t", "IGV", sep="\t")
            for row in resconn:
                productosf = producto.selectallproductos(row[0],row[1],row[2],row[3])
                lstProductos.append(productosf)
                print(lstProductos)
            productoseleccionado = int(input("Escribe el ID del producto que deseas anadir"))
            print("Ahora escribe en numero la cantidad de productos")
            cantproductos = int(input("Escribe un numero: "))
            idfaccab = int(input(random.randint(100, 200)))
            print("Ahora elige tu metodo de pago")
            conn = conexion.conexionBDD(1)
            query = querysdb.QueryDB.tipopago(selectalltipopago)
            resconn = conn.consultarBDD(query)
            print("ID", "Nombre\t", sep="\t")
            for row in resconn:
                tipopagof = tipopago.selectalltipopago(row[0],row[1])
                lstTipoPago.append(tipopagof)
                print(lstTipoPago)
            tipodepagoselec = int(input("Escribe el ID del tipo de pago que deseas anadir"))
            pasounofac = querysdb.Factura.cabecera()
            pasodosfac = querysdb.Factura.productos()
            MasProductos = True
            while MasProductos:
                ProdAdicional = input("¿Desea ingresar otro producto? S/N \n")
                if ProdAdicional == "S" or ProdAdicional == "s":
                    return ingresandoprod
                elif ProdAdicional == "N" or ProdAdicional == "n":  
                    print("Ahora ubica tu nombre")
                    conn = conexion.conexionBDD(1)
                    query =querysdb.QueryDB.clientes(selectallcliente)
                    resconn = conn.ejecutarBDD(query)
                    print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                    for row in resconn:
                    cliente = clientes.selectallcliente(row[0],row[1],row[2],row[3])
                    lstClientes.append(cliente)
                    print(lstClientes)
                    idecliente = int(input("Escribe tu numero de ID: "))
                    pasotresfac = querysdb.Factura.cliente()
                    print("Ahora ubica tu empresa")
                    conn = conexion.conexionBDD(1)
                    query =querysdb.QueryDB.empresa(selectallempresa)
                    resconn = conn.ejecutarBDD(query)
                    print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                    for row in resconn:
                    empresaf = empresa.selectallempresa(row[0],row[1],row[2])
                    lstEmpresa.append(empresaf)
                    print(lstEmpresa)
                    idempresa = int(input("Escribe tu numero de ID: "))
                    pasocuatrofac = querysdb.Factura.empresa()


                    

                      
 