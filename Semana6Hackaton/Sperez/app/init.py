import utils
import conexion
import cliente
import empresa
import productos
import tipopago
import psycopg2
import query

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
             
        #Si no existe el cliente volver a pedir id
        OpcionMenuFacturaCliente = True
        while OpcionMenuFacturaCliente:
        #Listamos a todos los clientes
            conn = conexion.conexionBDD(1)
            
            querys = query.Querys()
            SqlClientes = querys.SelectAllClientes()
            Clientes = conn.consultarBDD(SqlClientes)
            #Cabecera
            print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
            #Mostrar Datos
            for tplCliente in Clientes:
                print(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3], sep="\t")
            IdCliente = input("Ingrese Id del Cliente:\n")
            try:
                SqlClientes = querys.SelectIdCliente(IdCliente)
                ResulClientes = conn.consultarBDD(SqlClientes)
                lstCliente = []
                lstEmpresa = []
                lstProducto = []
                lstTipo = []
                lstCabecera = []
                #Si no existe el cliente volver a pedir id
                if ResulClientes:
                    #Insertamos los datos al Objeto Cliente
                    for tplCliente in ResulClientes:
                        ObjCliente = clientes.clientes(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3])
                        lstCliente.append(ObjCliente)
                        __log.debug("Se ingreso bien el ObjCliente")            
                      
                    OpcionMenuFacturaEmpresa = True
                    while OpcionMenuFacturaEmpresa:
                        #Ingreso de la empresa
                        SqlEmpresas = querys.SelectAllEmpresas()
                        Empresas = ConecBDMysql.consultarBDD(SqlEmpresas)
                        #Cabecera
                        print("ID", "Numero Ruc", "Nombre\t", sep="\t")
                        #Mostrar Datos
                        for tplEmpresa in Empresas:
                          print(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2], sep="\t")          
                        IdEmpresa = input("Ingrese Id de la Empresa:\n")
                        SqlEmpresas = querys.SelectIdEmpresa(IdEmpresa)
                        ResulEmpresas = ConecBDMysql.consultarBDD(SqlEmpresas)
                        if ResulEmpresas:
                          for tplEmpresa in ResulEmpresas:
                            ObjEmpresa = empresa.empresa(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2])
                            lstEmpresa.append(ObjEmpresa)
                            __log.debug("Se ingreso bien el ObjEmpresa")
                          
                          OpcionMenuFacturaTipo = True
                          while OpcionMenuFacturaTipo:
                            SqlTipo = querys.SelectAllTipos()
                            Tipos = ConecBDMysql.consultarBDD(SqlTipo)
                            #Cabecera
                            print("ID", "Nombre\t", sep="\t")
                            #Mostrar Datos
                            for tplTipo in Tipos:
                              print(tplTipo[0], tplTipo[1], sep="\t")
                            IdTipo = input("Ingrese Id del tipo de pago:\n")
                            SqlTipo = querys.SelectIdTipo(IdTipo)
                            ResulTipo = ConecBDMysql.consultarBDD(SqlTipo)
                            if ResulTipo:
                              for tplTipo in ResulTipo:
                                ObjTipo = tipopago.tipopago(tplTipo[0], tplTipo[1])
                                lstTipo.append(ObjTipo)
                                __log.debug("Se ingreso bien el ObjTipo")
                              #Recorrer datos 
                              for datosEmpresa in lstEmpresa:
                                idEmp = datosEmpresa.idempresa
                                __log.info(f"El id Empresa es {idEmp}")
                              for datosCliente in lstCliente:
                                idClie = datosCliente.idCliente
                                __log.info(f"El id Cliente es {idClie}")
                              for datosTipo in lstTipo:
                                idTip = datosTipo.idtipopago
                                __log.info(f"El id Tipo es {idTip}")
                              #Insertar a la tabla faccabecera
                              igvProd = 0
                              subTotal = 0
                              Total = 0
                              SqlFacCabecera = querys.InsertCabecera(str(idEmp), str(idClie), str(idTip), str(igvProd), str(subTotal), str(Total))
                              ConecBDMysql.ejecutarBDD(SqlFacCabecera)
                              #Mostrar todas las Cabeceras
                              SqlAllCabecera = querys.SelectAllCabecera()
                              ResulAllCabecera = ConecBDMysql.consultarBDD(SqlAllCabecera)
                              print("ID", "Empresa\t", "Cliente\t", "Tipo Pago", sep="\t")
                              for tplCabecera in ResulAllCabecera:
                                print(tplCabecera[0], tplCabecera[1], "", tplCabecera[2], tplCabecera[3], sep="\t")
                              #Solicitamos ID cabecera
                              IdCab = input("Ingrese Id de Cabecera a llenar:\n")                                                         
                              OpcionMenuFacturaProducto = True
                              while OpcionMenuFacturaProducto:
                                #Todos los productos
                                SqlProducto = querys.SelectAllProductos()
                                Productos = ConecBDMysql.consultarBDD(SqlProducto)
                                #Cabecera
                                print("ID", "Nombre\t", "Valor", "Igv", sep="\t")
                                #Mostrar Datos
                                for tplProducto in Productos:
                                  print(tplProducto[0], tplProducto[1]+"\t", tplProducto[2], tplProducto[3], sep="\t")
                                IdProducto = input("Ingrese Id del producto:\n")
                                SqlProducto = querys.SelectIdProducto(IdProducto)
                                ResulProducto = ConecBDMysql.consultarBDD(SqlProducto)
                                if ResulProducto:
                                  for tplProducto in ResulProducto:
                                    ObjProducto = productos.productos(tplProducto[0], tplProducto[1], tplProducto[2], tplProducto[3])
                                    lstProducto.append(ObjProducto)
                                    __log.debug("Se ingreso bien el ObjProducto")
                                  #Producto elegido
                                  for datosProductos in lstProducto:
                                    nombreproducto = datosProductos.nombreProducto
                                    idProd = datosProductos.idProducto
                                    igvProd = datosProductos.igvProducto
                                    valorProd = datosProductos.valorProducto     
                                    __log.debug("Datos del producto en cada variable")
                                  #Buscar Cabecera
                                  SqlIdCabecera = querys.SelectIdCabecera(IdCab)
                                  ResulIdCab = ConecBDMysql.consultarBDD(SqlIdCabecera)
                                  #Llenamos obj Cabecera
                                  for tplCabecera in ResulIdCab:
                                    ObjCabecera = factura.factura(tplCabecera[0], tplCabecera[1], tplCabecera[2], tplCabecera[3], tplCabecera[4], tplCabecera[5], tplCabecera[6], tplCabecera[7])
                                    lstCabecera.append(ObjCabecera)
                                    __log.debug("Se ingreso bien el ObjCabecera")
                                  for datosCabecera in lstCabecera:
                                    idCabe = datosCabecera.idCabecera
                                    nomEmp = datosCabecera.nombreEmp
                                    nomCli = datosCabecera.nombreClie
                                    tippago = datosCabecera.tipo
                                    igvCab = datosCabecera.igv
                                    __log.debug(f"Datos de la cabecera en cada variable")                             
                                  #Cantidad de productos
                                  CantProducto = int(input(f"¿Cuantos {nombreproducto} desea?\n"))  
                                  __log.info(type(valorProd))
                                  valorTotal = float(valorProd) * CantProducto
                                  __log.info(type(valorTotal))
                                  #Insertar facdetalle
                                  SqlFacDetalle = querys.InsertDetalle(idCabe, idProd, CantProducto, valorTotal)
                                  ConecBDMysql.ejecutarBDD(SqlFacDetalle)
                                  igvProducto = float(igvCab)
                                  if igvProd == 1:
                                    igvProducto = (valorTotal * 0.18) + igvProducto
                                  else:
                                    igvProducto += 0
                                  #Modificar facCabecera
                                  SqlModiCabcera = querys.UpdateCabecera(idCabe, igvProducto)
                                  ConecBDMysql.ejecutarBDD(SqlModiCabcera)
                                  __log.info("Se agrego correctamente")
                                  #Buscar Cabecera
                                  ResulIdCab = ConecBDMysql.consultarBDD(SqlIdCabecera)
                                  #Llenamos obj Cabecera
                                  for tplCabecera in ResulIdCab:
                                    ObjCabecera = factura.factura(tplCabecera[0], tplCabecera[1], tplCabecera[2], tplCabecera[3], tplCabecera[4], tplCabecera[5], tplCabecera[6], tplCabecera[7])
                                    lstCabecera.append(ObjCabecera)
                                    __log.debug("Se ingreso bien el ObjCabecera")
                                  #Actualiza los datos de la cabecera a mostrar(IGV, SUBTOTAL Y TOTAL)
                                  for datosCabecera in lstCabecera:
                                    fechaCab = datosCabecera.fecha
                                    igvCab = datosCabecera.igv
                                    subtotalCab = datosCabecera.subtotal
                                    totalCab = datosCabecera.total
                                    __log.debug(f"Datos de la cabecera en cada variable")
                                  op = True
                                  while op:
                                    #Preguntar si quiere agregar mas productos
                                    CondProd = input("¿Desea ingresar otro producto? S/N \n")
                                    if CondProd == "S" or CondProd == "s":
                                      OpcionMenuFacturaProducto = True
                                      op = False
                                    elif CondProd == "N" or CondProd == "n":
                                      __log.info("Mostrar Factura")
                                      print(f"Empresa: {nomEmp} \t\t Fecha: {fechaCab}")
                                      print(f"Cliente: {nomCli}")
                                      print(f"Tipo de Pago: {tippago}")
                                      SqlDetalle = querys.SelectDetalle(idCabe)
                                      ResulDetalle = ConecBDMysql.consultarBDD(SqlDetalle)
                                      print("Cantidad", "Producto", "Valor Unit.", "Valor Total", sep="\t")
                                      for tplDetalle in ResulDetalle:
                                        print(tplDetalle[0], tplDetalle[1], tplDetalle[2], tplDetalle[3], sep="\t\t")
                                      print(f"\tSubtotal: {subtotalCab}")
                                      print(f"\tIgv:\t {igvCab}")
                                      print(f"\tTotal:\t {totalCab}")
                                      sleep(3)
                                      opfin = True
                                      while opfin:
                                        fin = input("Nueva Factura (N).\nRegresar (R).\nSalir(S).\nIngrese Opcion: ")
                                        #Ingresar Nueva Factura
                                        if fin == "N" or fin == "n":
                                          opfin = False
                                          op = False
                                          OpcionMenuFacturaProducto = False
                                          OpcionMenuFacturaTipo = False
                                          OpcionMenuFacturaEmpresa = False
                                          OpcionMenuFacturaCliente = True
                                        #Regresar al menu operaciones
                                        elif fin == "R" or fin == "r":
                                          opfin = False
                                          op = False
                                          OpcionMenuFacturaProducto = False
                                          OpcionMenuFacturaTipo = False
                                          OpcionMenuFacturaEmpresa = False
                                          OpcionMenuFacturaCliente = False
                                          OpcionMenuMysql = True
                                        #Salir del Sistema
                                        elif fin == "S" or fin == "s":
                                          utils.Salir()
                                        else:
                                          print("Ingrese una opcion valida\a")
                                          opfin= True
                                          sleep(1)
                                    else:
                                      print("Ingrese una opcion valida\a")
                                      op = True
                                      sleep(1)
                                else:
                                  print("Ingrese un producto de la lista\a")
                                  OpcionMenuFacturaProducto = True
                                  sleep(1)
                            else:
                              print("Ingrese un tipo de pago de la lista\a")
                              OpcionMenuFacturaTipo = True
                              sleep(1)
                        else:
                          print("Ingrese una empresa de la lista\a")
                          OpcionMenuFacturaEmpresa = True
                          sleep(1)
                    for datosCliente in lstCliente:
                        print(datosCliente.nombreCliente)
                        OpcionMenuFacturaCliente = False
                    else:
                      print("El cliente no existe:\n")
                      OpcionMenuFacturaCliente = True
                      sleep(1)
            except Exception as e:
                __log.info(e)
                OpcionMenuFacturaCliente = True
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
