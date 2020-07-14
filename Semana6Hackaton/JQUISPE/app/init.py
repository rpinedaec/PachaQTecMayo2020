import utils
import conexion
import clientes
import empresa
import productos
import tipopago

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []

def cargarClientes():
    conn = conexion.conexionBDD(1)
    query1 = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes"
    resconn = conn.consultarBDD(query1)

    for row in resconn:
        cliente = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(cliente)
    print(lstClientes)
    for obj in lstClientes:
        print(obj.nombreCliente)
    input("continuar")

def mantenimientoCliente():
    dicMenuCliente = {  "\t- Listar todos los clientes": 1,
                        "\t- Buscar Cliente por DNI": 2,
                        "\t- Modificar Cliente por ID": 3,
                        "\t- Crear Cliente": 4,
                        "\t- Borrar Cliente": 5}
    menuCliente = utils.Menu("Menu Cliente", dicMenuCliente)
    resMenuCliente = menuCliente.mostrarMenu()
    if(resMenuCliente == 1):
        log.debug("buscamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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
        query = f"select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentificacionCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)
    elif(resMenuCliente == 3):
        log.debug("buscamos cliente")
        #Se abre la conexion con la base de datos
        conn = conexion.conexionBDD(1)
        #Se brinda la instruccion de la base de datos
        query = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
        #Devuelve el resultado de la conexion
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
        query = f"UPDATE clientes SET nombreCliente = '{nombre}', nroIdentificacionCliente = '{dni}',direccionCliente = '{direccion}' where idClientes = '{idcliente}';"
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
        query = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
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

def mantenimientoProductos():
    dicMenuProductos = {  "\t- Buscar Productos Todos": 1,
                        "\t- Buscar Producto por nombre": 2,
                        "\t- Modificar Producto por nombre": 3,
                        "\t- Crear Producto": 4,
                        "\t- Borrar Producto": 5}
    menuProductos = utils.Menu("Menu Producto", dicMenuProductos)
    resMenuProductos = menuProductos.mostrarMenu()
    if(resMenuProductos == 1):
        log.debug("buscamos Producto")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproductos, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        input("continuar???")
        print(resConn)

    elif(resMenuProductos == 2):
        log.debug("buscamos cliente por nombre")
        print("escribe el nombre del producto")
        nombreProducto = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idproductos, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos WHERE nombreProducto = '{nombreProducto}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
        print(resConn)

    elif(resMenuProductos == 3):
        log.debug("buscamos producto a modificar")
        conn = conexion.conexionBDD(1)
        query = "SELECT idproductos, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del producto que desea modificar")
        print("\tID\t\tNombre\t\t\tValor\t\t\tigvProducto")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproducto = input()
        print("Escriba el nuevo valor para Nombre")
        nombre = input()
        print("Escriba el nuevo Valor del Producto")
        valor = input()
        print("Escriba si el producto tiene IGV")
        igvProducto = input()
        query = f"UPDATE productos SET nombreProducto = '{nombre}', valorProducto = '{valor}', igvProducto= '{igvProducto}' WHERE idproductos = '{idproducto}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")


    elif(resMenuProductos == 4):
        print("##Creacion de un producto##")
        print("Escriba el Nombre del producto")
        nombre = input()
        print("Escriba el Valor del producto")
        valor = input()
        print("Escriba el igv del Producto")
        igvProducto = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO productos ( nombreProducto, valorProducto, igvProducto) VALUES ( '{nombre}', '{valor}','{igvProducto}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")


    elif(resMenuProductos == 5):
        log.debug("eliminamos producto")
        conn = conexion.conexionBDD(1)
        query = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea eliminar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idproductos = input()
        
        query = f"DELETE FROM productos WHERE idproductos = {idproductos};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

def mantenimientoEmpresa():
    dicMenuEmpresa = {  "\t- Buscar Empresa Todos": 1,
                        "\t- Buscar Empresa por RUC": 2,
                        "\t- Modificar Empresa por ID": 3,
                        "\t- Crear Empresa": 4,
                        "\t- Borrar Empresa": 5}
    menuEmpresa = utils.Menu("Menu Empresa", dicMenuEmpresa)
    resMenuEmpresa = menuEmpresa.mostrarMenu()
    if(resMenuEmpresa == 1):
        log.debug("buscamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tEmpresa")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        input("continuar???")
        print(resConn)

    elif(resMenuEmpresa == 2):
        log.debug("buscamos empresa por RUC")
        print("escribe el numero de RUC")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa where rucEmpresa = '{ruc}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tEMPRESA")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
        input("continuar???")
        print(resConn)

    elif(resMenuEmpresa == 3):
        log.debug("buscamos Empresa")
        #Se abre la conexion con la base de datos
        conn = conexion.conexionBDD(1)
        #Se brinda la instruccion de la base de datos
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        #Devuelve el resultado de la conexion
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que desea modificar")
        print("\tID\t\tRUC\t\t\tEMPRESA")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idempresa = input()
        print("Escriba el nuevo RUC")
        ruc = input()
        print("Escriba el nuevo nombre de la Empresa")
        nombre = input()
        query = f"UPDATE empresa SET rucEmpresa = '{ruc}10469346884', nombreEmpresa = '{nombre}' WHERE idempresa = '{idempresa}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(resMenuEmpresa == 4):
        print("##Creacion de una Empresa##")
        print("Escriba el Nombre de la Empresa")
        nombre = input()
        print("Escriba el RUC de la Empresa")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO empresa (rucEmpresa,nombreEmpresa) VALUES ('{ruc}','{nombre}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(resMenuEmpresa == 5):
        log.debug("eliminamos Empresa")
        conn = conexion.conexionBDD(1)
        query = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID de la empresa que desea eliminar")
        print("\tID\t\tRUC\t\t\tEMPRESA")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

        idempresa = input()
        
        query = f"delete from clientes where idCliente = {idempresa} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

def mantenimientotipoPago ():
    dicMenuTipoPago = {  "\t- Buscar Tipo de Pago Todos": 1,
                        "\t- Buscar Tipo de Pago por ID": 2,
                        "\t- Modificar Tipo de Pago por ID": 3,
                        "\t- Crear Tipo de Pago": 4,
                        "\t- Borrar Tipo de Pago": 5}
    menuTipoPago = utils.Menu("Menu Tipo de Pago", dicMenuTipoPago)
    resMenuTipoPago = menuTipoPago.mostrarMenu()

    if(resMenuTipoPago == 1):
        log.debug("buscamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipopago, descTipoPago AS Descripcion FROM tipopago;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDESCRIPCION")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        input("continuar???")
        print(resConn)

    elif(resMenuTipoPago == 2):
        log.debug("buscamos Tipo de Pago por ID")
        print("escribe el ID")
        idtipopago = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idtipopago, descTipoPago AS Descripcion FROM tipopago WHERE descTipoPago = '{idtipopago}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tRUC\t\t\tEMPRESA")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")
        input("continuar???")
        print(resConn)

    elif(resMenuTipoPago == 3):
        log.debug("buscamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipopago, descTipoPago AS Descripcion FROM tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID que desea modificar")
        print("\tID\t\tDESCRIPCION")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipopago = input()
        print("Escriba la nueva descripción")
        descripcion = input()
        query = f"UPDATE tipopago SET descTipoPago = '{descripcion}' WHERE idtipopago = {idtipopago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")

    elif(resMenuTipoPago == 4):
        print("##Creacion de un tipo de pago##")
        print("Escriba la descripcion del Tipo de Pago")
        tipopago = input()
        conn = conexion.conexionBDD(1)
        query = f"INSERT INTO tipopago(descTipoPago)VALUES('{tipopago}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")

    elif(resMenuTipoPago == 5):
        log.debug("eliminamos Tipo de Pago")
        conn = conexion.conexionBDD(1)
        query = "SELECT idtipopago, descTipoPago AS Descripcion FROM tipopago;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del tipo de pago que desea eliminar")
        print("\tID\t\tTIPO DE PAGO")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}")

        idtipopago = input()
        
        query = f"DELETE FROM tipopago WHERE idtipopago = {idtipopago};"
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
        mantenimientoProductos()
    elif resMenu == 3:
        log.debug("escogio 3")
        mantenimientoEmpresa()
    elif resMenu == 4:
        log.debug("escogio 4")
        mantenimientotipoPago()
    else:
        log.debug(f"escogio {resMenu}")

stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Crear Factura": 1, "\t- Mantenimientos": 2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("Mostramos el Menu crear Factura")
        ###INGRESAMOS LOS DATOS DEL CLIENTE; SI EL CLIENTE EXISTE EN LA BASE DE DATOS, EL PROGRAMA TRAERA TODOS LOS DATOS DEL CLIENTE, DE LO CONTRARIO CREARA UN NUEVO CLIENTE Y ALMACENARA EN LA BASE DE DATOS
        print("Escriba el numero de DNI")
        dni = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion FROM clientes WHERE nroIdentificacionCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        if resConn==[]:
            print("Ingrese el nombre del cliente")
            nombreCliente=input()
            print("Ingrese la direccion del cliente")
            direccionCliente=input()
            query = f"INSERT INTO clientes (nombreCliente, nroIdentificacionCliente,direccionCliente) VALUES('{nombreCliente}','{dni}','{direccionCliente}');"
            resConn = conn.ejecutarBDD(query)
            query = f"SELECT * FROM clientes"
            resConn = conn.consultarBDD(query)
            idCliente = resConn[-1][0]
        else:
            idCliente = resConn[0][0]
            nombreCliente = resConn[0][1]
            direccionCliente = resConn[0][3]
        ###INGRESAMOS LOS DATOS DE LA EMPRESA
        print("Ingrese el RUC de la empresa")
        ruc = input()
        conn = conexion.conexionBDD(1)
        query = f"SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa WHERE rucEmpresa = '{ruc}';"
        resConn = conn.consultarBDD(query)
        if resConn == []:
            print("Ingrese el nombre de la empresa")
            nombreEmpresa = input()
            query = f"INSERT INTO empresa (rucEmpresa, nombreEmpresa) VALUES('{ruc}','{nombreEmpresa}')"
            resConn =conn.ejecutarBDD(query)
            query = f"SELECT * FROM empresa"
            resConn = conn.consultarBDD(query)
            idEmpresa=resConn[-1][0]
        else:
            idEmpresa=resConn[0][0]
            nombreEmpresa=resConn[0][2]
        #AGREGANDO EL METODO DE PAGO
        print("INGRESE EL METODO DE PAGO")
        log.debug("Mostramos los Metodos de Pago")
        print("""MENU DEL METODO DE PAGO
        \nEscoja una opción\n- Efectivo: 1, \n- Credito: 2""")
        nnn = int(input ())
        if nnn == 1:
            print("Se escogio el metodo de pago Efectivo")
            tipopago = "Efectivo"
            idtipopago = 2
        elif nnn == 2:
            print("Se escogio el metodo de pago a Credito")
            tipopago = "Credito"
            idtipopago = 3
        #AGREGANDO EL ESTADO DE LA FACTURA
        log.debug("Mostramos los posibles estados de la factura")
        print("""MENU DEL ESTADO DE LA FACTURA
        \nEscoja una opción\n- Pagada: 1, \n- Por cobrar: 2""")
        nnn = int(input ())
        if nnn == 1:
            print("Se escogio el estado de Factura Pagada")
            estadofactura = 0
        elif nnn == 2:
            print("Se escogio el estado de factura por Cobrar")
            estadofactura = 1
        
        #COMENZAREMOS A CARGAR EL DETALLE DE LAS FACTURAS;
        subtotal=0.00
        igv=0.00
        listDetalle=[]
        jjj=True
        while jjj == True:
            nombreProducto=input("Ingrese el producto a facturar: ")
            #conn = conexion.conexionBDD(1)
            query = f"SELECT * FROM productos WHERE nombreProducto = '{nombreProducto}';"
            resConn = conn.consultarBDD(query)
            if resConn == []:
                valorProducto=float(input("Ingrese el valor del producto: "))
                print("¿El producto tiene IGV?")
                print("""1. El producto esta exonerado del IGV\n 2. El producto tributa el IGV""")
                nnn=int(input("Ingrese su opción: "))
                if nnn == 1:
                    igvProducto = 0
                elif nnn == 2:
                    igvProducto = 1
                query = f"INSERT INTO productos (nombreProducto, valorProducto,igvProducto) VALUES('{nombreProducto}','{valorProducto}','{igvProducto}');"
                resConn =conn.ejecutarBDD(query)
                query = f"SELECT * FROM productos WHERE nombreProducto = '{nombreProducto}'"
                resConn = conn.consultarBDD(query)
                valorProducto=float(resConn[0][2])
                idProductos=resConn[0][0]
            else:
                print("El precio por unidad del producto seleccionado es: ",resConn[0][2])
                valorProducto=float(resConn[0][2])
                igvProducto=resConn[0][3]
                idProductos=resConn[0][0]

            cantFacDetalle=float(input("Ingrese la cantidad del producto a facturar: "))
            valorFacDetalle=cantFacDetalle*valorProducto
    
            #AGREGAMOS ELEMENTOS A LA LISTA
            listDetalle.append([cantFacDetalle,valorFacDetalle,idProductos])

            if igvProducto == 0:
                igvProducto = 0
            elif igvProducto == 1:
                igvProducto = valorFacDetalle*0.18

            subtotal=subtotal+valorFacDetalle
            igv = igv + igvProducto    

            print("Seleccione una opción?\n1.-Agregar más productos\n2.-Finalizar")
            opcion=int(input("Ingrese su opción: "))
            if opcion == 1:
                jjj=True
            else:
                jjj=False

        #AQUI ENTREGA LOS DATOS DE LA FACTURA
        print("El subtotal de la factura es: ",subtotal)
        print("El igv de la factura es: ",igv)
        total=subtotal+igv
        print("El total de la factura es: ",total)
        #DEBEMOS CREAR LA FACTURA CABECERA
        #### ESTA PARTE SE IRA A PROBAR ###
        query = f"INSERT INTO faccabecera (igvFacCabecera,subtotalFacCabecera,totalFacCabecera,estadoFactura,idCliente,idtipoPago,idempresa) VALUES ('{igv}','{subtotal}','{total}','{estadofactura}','{idCliente}','{idtipopago}','{idEmpresa}');"
        resConn =conn.ejecutarBDD(query)
        query = f"SELECT * FROM faccabecera"
        resConn = conn.consultarBDD(query)
        idFacCabecera=resConn[-1][0]

        #####Comencemos a agregar los detalles de la factura, primero modificamos la lista, agregando el idFacCabecera.
        i=0
        for listDetalle[i] in listDetalle:
            listDetalle[i].insert(2,idFacCabecera)
            cantFacDetalle=listDetalle[i][0]
            valorFacDetalle=listDetalle[i][1]
            idProductos=listDetalle[i][3]
            query=f"INSERT INTO facdetalle (cantFacDetalle, valorFacDetalle,idfacCabecera,idproductos) VALUES ('{cantFacDetalle}','{valorFacDetalle}','{idFacCabecera}','{idProductos}');"
            resConn =conn.ejecutarBDD(query)
        print("SE CREARON LA FACTURA CABECERA Y LA FACTURA DETALLE CORRECTAMENTE")
        input("desea continuar???")
    
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
