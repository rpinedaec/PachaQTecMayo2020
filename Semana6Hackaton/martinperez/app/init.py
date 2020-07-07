import utils
import conexion
import clientes
import empresa
import productos
import tipopago
import factura

log = utils.log("INIT")
log.info("inicio del programa")
lstClientes = []
lstTipoPago = []
lstEmpresa = []
lstProductos = []
lstFacturaCabecera = []
lstFacturaDetalle = []
MsjContinuar = "Enter para continuar..."
NumeroBDD = 1

query_Productos="" 
query_Clientes="" 
query_Empresa=""
query_TipoPago = ""
query_FacturaCabecera = ""
query_FacturaDetalle = ""

if NumeroBDD ==2: 
    query_Productos = 'select "idproducto", "nombreProducto", "valorProducto","igvProducto" from "productos"'
    query_Clientes = 'select idCliente, "nombreCliente", "nroIdentidicacionCliente", "direccionCliente" from "clientes"'
    query_Empresa = 'select "idempresa", "rucEmpresa", "nombreEmpresa" from "empresa"'
    query_TipoPago = 'select "idtipoPago", "descTipoPago" from "tipoPago"'
    query_FacturaCabecera = 'select c."idfacCabecera", e."nombreEmpresa" empresa '
    query_FacturaCabecera += ',cli."nombreCliente" cliente, tp."descTipoPago" tipoPago '
    query_FacturaCabecera += ',c."fechaFacCabecera",c."igvFacCabecera",c."subtotalFacCabecera" '
    query_FacturaCabecera += ',c."totalFacCabecera",c."estadoFactura" '
    query_FacturaCabecera += 'from "facCabecera" as c ' 
    query_FacturaCabecera += 'inner join empresa as e on c.idempresa = e.idempresa '
    query_FacturaCabecera += 'inner join clientes as cli on c.idcliente = cli.idcliente '
    query_FacturaCabecera += 'inner join "tipoPago" as tp on tp."idtipoPago" = c."idtipoPago" '
    query_FacturaDetalle = ' select idfacDetalle, idfacCabecera, p.nombreProducto producto '
    query_FacturaDetalle += ' ,d.cantFacDetalle cantidad,d.valorFacDetalle valor, p.igvProducto afecto '
    query_FacturaDetalle += ' from facdetalle d inner join productos p on d.idproducto = p.idproducto '
else: 
    query_Productos = "select idproducto,nombreProducto,valorProducto,igvProducto from productos"
    query_Clientes = "select idCliente, nombreCliente, nroIdentidicacionCliente, direccionCliente from clientes" 
    query_Empresa = "select idempresa, rucEmpresa, nombreEmpresa from empresa"
    query_TipoPago = "select idtipoPago, descTipoPago from tipopago"
    query_FacturaCabecera = "select c.idfacCabecera, e.nombreEmpresa 'empresa'"
    query_FacturaCabecera += ",cli.nombreCliente 'cliente', tp.descTipoPago 'tipoPago'"
    query_FacturaCabecera += ",c.fechaFacCabecera,c.igvFacCabecera,c.subtotalFacCabecera "
    query_FacturaCabecera += ",c.totalFacCabecera,c.estadoFactura "
    query_FacturaCabecera += "from faccabecera c "
    query_FacturaCabecera += "inner join empresa e on c.idempresa = e.idempresa "
    query_FacturaCabecera += "inner join clientes cli on c.idcliente = cli.idcliente "
    query_FacturaCabecera += "inner join tipopago tp on c.idtipoPago = tp.idtipoPago "
    query_FacturaDetalle = "select idfacDetalle, idfacCabecera, p.nombreProducto producto "
    query_FacturaDetalle += ",d.cantFacDetalle cantidad,d.valorFacDetalle valor, p.igvProducto afecto "
    query_FacturaDetalle += "from facdetalle d inner join productos p on d.idproducto = p.idproducto "
 

#   Cargando Clientes
def cargarClientes(): 
    conn = conexion.conexionBDD(NumeroBDD)
    resconn = conn.consultarBDD(query_Clientes)
    lstClientes.clear() 
    for row in resconn:
        clienteF = clientes.clientes(row[0],row[1],row[2],row[3])
        lstClientes.append(clienteF)
#   Cargando Empresa
def cargarEmpresa():
    conn = conexion.conexionBDD(NumeroBDD)
    resconn2 = conn.consultarBDD(query_Empresa)
    lstEmpresa.clear() 
    for row in resconn2:
        empresaF = empresa.empresa(row[0],row[1],row[2])
        lstEmpresa.append(empresaF) 
#   Cargando Empresa
def cargarProductos():
    conn = conexion.conexionBDD(NumeroBDD)
    resconn3 = conn.consultarBDD(query_Productos)
    lstProductos.clear() 
    for row in resconn3:
        productoF = productos.productos(row[0],row[1],row[2],row[3])
        lstProductos.append(productoF) 
#   Cargando Tipo pago
def cargarTipoPago():
    conn = conexion.conexionBDD(NumeroBDD)
    resconn4 = conn.consultarBDD(query_TipoPago)
    lstTipoPago.clear() 
    for row in resconn4:
        tipoPagoF = tipopago.tipopago(row[0],row[1])
        lstTipoPago.append(tipoPagoF)
#   Cargando CabeceraFactura
def cargarCabeceraFactura():
    conn = conexion.conexionBDD(NumeroBDD)
    query_FacCabecera = query_FacturaCabecera 
    if NumeroBDD ==2:
        query_FacCabecera = query_FacturaCabecera + ' order by c."idfacCabecera" asc '
    else:
        query_FacCabecera = query_FacturaCabecera + " order by c.idfacCabecera asc "
    resconn4 = conn.consultarBDD(query_FacCabecera)
    lstFacturaCabecera.clear() 
    for row in resconn4:
        documentF = factura.facturaCabecera(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        lstFacturaCabecera.append(documentF)


dicMenuMantenimientoGeneral = {    "\t- Todos: ": 1,"\t- Buscar: ": 2
                            ,"\t- Modificar: ": 3,"\t- Crear: ": 4,"\t- Borrar: ": 5}


def mantenimientoTipoPago():
    cargarTipoPago()
    generalTrue = True
    while generalTrue: 
        menuMostrar = utils.Menu("Administrador de Tipo de Pago", dicMenuMantenimientoGeneral)
        resmenuMostrar = menuMostrar.mostrarMenu()        
        if(resmenuMostrar == 1):
            log.debug("mostrando tipo pago")
            utils.listaSimple(lstTipoPago,4,1)
        elif(resmenuMostrar == 2):
            log.debug("buscamos tipo de pago")
            nombreBuscar = input("nombre: ")
            conn = conexion.conexionBDD(NumeroBDD) 
            query = query_TipoPago
            if NumeroBDD==2:
                query = query_TipoPago +' where "descTipoPago" like '+  f" '%{nombreBuscar}%';"
            elif NumeroBDD !=2:
                query = query_TipoPago + f" where descTipoPago like '%{nombreBuscar}%';"
            resConn2 = conn.consultarBDD(query)
            lstTemp = []      
            for row in resConn2:
                FilaTempF = tipopago.tipopago(row[0],row[1])
                lstTemp.append(FilaTempF) 
            utils.listaSimple(lstTemp,3,1) 
        elif(resmenuMostrar == 3):
            log.debug("actualizar tipo pago")
            conn = conexion.conexionBDD(NumeroBDD)  
            utils.listaSimple(lstTipoPago,4,0)
            idBuscar = utils.validarIDEnLista(lstTipoPago,"9999=Cancelar / ID a modificar: ",4)
            if idBuscar != "": 
                nombre = input("Descripción: ") 
                query = ""
                if NumeroBDD==2:
                    query = 'update "tipoPago" set "desctipopago" = ' + f"'{nombre}'"+', "idtipoPago" = ' +f"'{nombre}'"
                    query += ' where "idempresa" =' + f" {idBuscar};"
                else:
                    query = f"update tipopago set descTipoPago = '{nombre}'  where idtipoPago = {idBuscar};"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarTipoPago()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")
                input(MsjContinuar)
            else:
                input("Operación Cancelada.")
        elif(resmenuMostrar == 4): 
            nombre = input("Descripción: ") 
            conn = conexion.conexionBDD(NumeroBDD)
            query = ""
            if NumeroBDD==2:
                query = 'insert into "tipoPago" ("descTipoPago") values( '+ f" '{nombre}');"
            else:
                query = f"insert into tipopago (descTipoPago) values('{nombre}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                cargarTipoPago()
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input(MsjContinuar)
        elif(resmenuMostrar == 5):
            log.debug("eliminamos tipo pago")
            conn = conexion.conexionBDD(NumeroBDD)
            utils.listaSimple(lstTipoPago,4,0)
            idbuscar = utils.validarIDEnLista(lstTipoPago,"9999=Cancelar / ID a modificar: ",4)
            if idbuscar != "":
                query = ""
                if NumeroBDD==2:
                    query = 'delete from "tipoPago" where "idtipoPago" = '+ f"{idbuscar} ;"
                else:
                    query = f"delete from tipopago where idtipoPago = {idbuscar} ;"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarTipoPago()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")        
                input(MsjContinuar)
            else:
                input("Operacion cancelada.")
        elif(resmenuMostrar == 9):
            generalTrue = False


def mantenimientoEmpresa():
    cargarEmpresa()
    generalTrue = True
    while generalTrue: 
        menuMostrar = utils.Menu("Administrador de Empresas", dicMenuMantenimientoGeneral)
        resmenuMostrar = menuMostrar.mostrarMenu()        
        if(resmenuMostrar == 1):
            log.debug("mostrando empresas")
            utils.listaSimple(lstEmpresa,3,1)
        elif(resmenuMostrar == 2):
            log.debug("buscamos empresas por nombre")
            nombreBuscar = input("Razon Social: ")
            conn = conexion.conexionBDD(NumeroBDD) 
            query = query_Empresa
            if NumeroBDD==2:
                query = query_Empresa +' where "nombreEmpresa" like '+  f" '%{nombreBuscar}%';"
            elif NumeroBDD !=2:
                query = query_Empresa + f" where nombreEmpresa like '%{nombreBuscar}%';"
            resConn2 = conn.consultarBDD(query)
            lstTemp = []      
            for row in resConn2:
                FilaTempF = empresa.empresa(row[0],row[1],row[2])
                lstTemp.append(FilaTempF) 
            utils.listaSimple(lstTemp,3,1) 
        elif(resmenuMostrar == 3):
            log.debug("actualizar empresa")
            conn = conexion.conexionBDD(NumeroBDD)  
            utils.listaSimple(lstEmpresa,3,0)
            idBuscar = utils.validarIDEnLista(lstEmpresa,"9999=Cancelar / ID a modificar: ",3)
            if idBuscar != "":
                Ruc = input("Ruc: ") 
                nombre = input("Razon Social: ") 
                query = ""
                if NumeroBDD==2:
                    query = 'update "empresa" set "rucEmpresa" = ' + f"'{Ruc}'"+', "nombreEmpresa" = ' +f"'{nombre}'"
                    query += ' where "idempresa" =' + f" {idBuscar};"
                else:
                    query = f"update empresa set rucEmpresa = '{Ruc}', nombreEmpresa = '{nombre}'  where idempresa = {idBuscar};"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarEmpresa()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")
                input(MsjContinuar)
            else:
                input("Operación Cancelada.")
        elif(resmenuMostrar == 4): 
            ruc = input("Ruc: ") 
            nombre = input("Razon Social: ") 
            conn = conexion.conexionBDD(NumeroBDD)
            query = ""
            if NumeroBDD==2:
                query = 'insert into "empresa" ("rucEmpresa", "nombreEmpresa") values( '+ f" '{ruc}','{nombre}');"
            else:
                query = f"insert into empresa (rucEmpresa, nombreEmpresa) values('{ruc}','{nombre}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                cargarEmpresa()
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input(MsjContinuar)
        elif(resmenuMostrar == 5):
            log.debug("eliminamos empresa")
            conn = conexion.conexionBDD(NumeroBDD)
            utils.listaSimple(lstEmpresa,3,0)
            idbuscar = utils.validarIDEnLista(lstEmpresa,"9999=Cancelar / ID a modificar: ",3)
            if idbuscar != "":
                query = ""
                if NumeroBDD==2:
                    query = 'delete from "empresa" where "idempresa" = '+ f"{idbuscar} ;"
                else:
                    query = f"delete from empresa where idempresa = {idbuscar} ;"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarEmpresa()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")        
                input(MsjContinuar)
            else:
                input("Operacion cancelada.")
        elif(resmenuMostrar == 9):
            generalTrue = False


def mantenimientoProductos():
    cargarProductos()
    ProductoTrue = True
    while ProductoTrue: 
        menuProducto = utils.Menu("Administrador de Productos", dicMenuMantenimientoGeneral)
        resMenuProducto = menuProducto.mostrarMenu()        
        if(resMenuProducto == 1):
            log.debug("mostrando productos")
            utils.listaSimple(lstProductos,2,1)
        elif(resMenuProducto == 2):
            log.debug("buscamos Producto por nombre")
            nombreBuscarProducto = input("Nombre: ")
            conn = conexion.conexionBDD(NumeroBDD) 
            query = query_Productos
            if NumeroBDD==2:
                query = query_Productos +' where "nombreProducto" like'+  f" '%{nombreBuscarProducto}%';"
            elif NumeroBDD !=2:
                query = query_Productos + f" where nombreProducto like '%{nombreBuscarProducto}%';"
            resConn2 = conn.consultarBDD(query)
            lstProductosTemp = []      
            for row in resConn2:
                ProductoF = productos.productos(row[0],row[1],row[2],row[3])
                lstProductosTemp.append(ProductoF) 
            utils.listaSimple(lstProductosTemp,2,1) 
        elif(resMenuProducto == 3):
            log.debug("actualizar producto")
            conn = conexion.conexionBDD(NumeroBDD)  
            utils.listaSimple(lstProductos,2,0)
            idProducto = utils.validarIDEnLista(lstProductos,"9999=Cancelar / ID a modificar: ",2)
            if idProducto != "":
                nombre = input("Nombre: ") 
                Valor = utils.validarFloat("Valor: ")
                ingresoBinario = True
                afecto = 0
                while ingresoBinario:
                    afecto = utils.validarEntero("Afecto Igv?  Si=1 / No=0 :")
                    if afecto<2:
                        ingresoBinario=False
                query = ""
                if NumeroBDD==2:
                    query = 'update "productos" set "nombreProducto" = ' + f"'{nombre}'"+', "valorProducto" = ' +f"'{Valor}'"+ ',"igvProducto" = '+ f"'{afecto}'"
                    query += ' where "idProducto" =' + f" {idProducto};"
                else:
                    query = f"update productos set nombreProducto = '{nombre}', valorProducto = '{Valor}',igvProducto = '{afecto}' where idProducto = {idProducto};"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarProductos()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")
                input(MsjContinuar)
            else:
                input("Operación Cancelada.")
        elif(resMenuProducto == 4): 
            nombre = input("Nombre: ") 
            Valor = utils.validarFloat("Valor: ")
            ingresoBinario = True
            afecto = 0
            while ingresoBinario:
                afecto = utils.validarEntero("Afecto Igv?  Si=1 / No=0 :")
                if afecto<2:
                    ingresoBinario=False
            conn = conexion.conexionBDD(NumeroBDD)
            query = ""
            if NumeroBDD==2:
                query = 'insert into "productos" ("nombreProducto", "valorProducto","igvProducto") values( '+ f" '{nombre}','{Valor}','{afecto}');"
            else:
                query = f"insert into productos (nombreProducto, valorProducto,igvProducto) values('{nombre}','{Valor}','{afecto}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                cargarProductos()
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input(MsjContinuar)
        elif(resMenuProducto == 5):
            log.debug("eliminamos producto")
            conn = conexion.conexionBDD(NumeroBDD)
            utils.listaSimple(lstProductos,2,0)
            idProducto = utils.validarIDEnLista(lstProductos,"9999=Cancelar / ID a modificar: ",2)
            if idProducto != "":
                query = ""
                if NumeroBDD==2:
                    query = 'delete from "productos" where "idProducto" = '+ f"{idProducto} ;"
                else:
                    query = f"delete from productos where idProducto = {idProducto} ;"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarProductos()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")        
                input(MsjContinuar)
            else:
                input("Operacion cancelada.")
        elif(resMenuProducto == 9):
            ProductoTrue = False


def mantenimientoCliente():
    cargarClientes()
    ClienteTrue = True
    while ClienteTrue: 
        menuCliente = utils.Menu("Administrador de Clientes", dicMenuMantenimientoGeneral)
        resMenuCliente = menuCliente.mostrarMenu()        
        if(resMenuCliente == 1):
            log.debug("mostrando cliente")
            utils.listaSimple(lstClientes,1,1)
        elif(resMenuCliente == 2):
            log.debug("buscamos cliente por DNI")
            dni = utils.validarEntero("DNI: ")
            conn = conexion.conexionBDD(NumeroBDD) 
            query = query_Clientes
            if NumeroBDD==2:
                query = query_Clientes +' where "nroIdentidicacionCliente" like'+  f" '%{dni}%';"
            elif NumeroBDD !=2:
                query = query_Clientes + f" where nroIdentidicacionCliente like '%{dni}%';"
            resConn2 = conn.consultarBDD(query)
            lstClientesTemp = []      
            for row in resConn2:
                clienteF = clientes.clientes(row[0],row[1],row[2],row[3])
                lstClientesTemp.append(clienteF) 
            utils.listaSimple(lstClientesTemp,1,1) 
        elif(resMenuCliente == 3):
            log.debug("buscamos cliente")
            conn = conexion.conexionBDD(NumeroBDD) 
            utils.listaSimple(lstClientes,1,0)
            idcliente = utils.validarIDEnLista(lstClientes,"9999=Cancelar / ID a modificar: ",1)
            if idcliente != "":
                nombre = input("Nombre: ") 
                dni = utils.validarEntero("DNI: ") 
                direccion = input("Dirección: ")
                query = ""
                if NumeroBDD==2:
                    query = 'update clientes set "nombreCliente" =  ' + f"'{nombre}'"+', "nroIdentidicacionCliente" = ' +f"'{dni}'"+ ',"direccionCliente" = '+ f"'{direccion}'"
                    query += ' where "idCliente" =' + f" {idcliente};"
                else:
                    query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
                    
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarClientes()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")
                input(MsjContinuar)
            else:
                input("Operación Cancelada.")
        elif(resMenuCliente == 4): 
            nombre = input("Nombre: ")
            dni = utils.validarEntero("DNI: ")
            direccion = input("Dirección: ")
            conn = conexion.conexionBDD(NumeroBDD)
            query = ""
            if NumeroBDD==2:
                query = 'insert into "clientes" ("nombreCliente", "nroIdentidicacionCliente","direccionCliente") values( '+ f" '{nombre}','{dni}','{direccion}');"
            else:
                query = f"insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
            resConn = conn.ejecutarBDD(query)
            if(resConn):
                cargarClientes()
                print("Se ejecuto correctamente")
            else:
                print("Hubo un error")
            input(MsjContinuar)
        elif(resMenuCliente == 5):
            log.debug("eliminamos cliente")
            conn = conexion.conexionBDD(NumeroBDD)
            utils.listaSimple(lstClientes,1,0)
            idcliente = utils.validarIDEnLista(lstClientes,"9999=Cancelar / ID a modificar: ",1)
            if idcliente != "":
                query = ""
                if NumeroBDD==2:
                    query = 'delete from "clientes" where "idCliente" = '+ f"{idcliente} ;"
                else:
                    query = f"delete from clientes where idCliente = {idcliente} ;"
                resConn = conn.ejecutarBDD(query)
                if(resConn):
                    cargarClientes()
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error")        
                input(MsjContinuar)
            else:
                input("Operacion cancelada.")
        elif(resMenuCliente == 9):
            ClienteTrue = False


def mantenimento():
    valorTrue = True
    while valorTrue:
        dicMenuMantenimiento = {"\t- Clientes": 1, "\t- Productos": 2,
                                "\t- Empresa": 3, "\t- Tipo de pago": 4}
        menuMantenimiento = utils.Menu("Menu Mantenimiento", dicMenuMantenimiento)
        resMenu = menuMantenimiento.mostrarMenu()
        if resMenu == 1:
            log.debug("escogio 1 - Clientes")
            mantenimientoCliente()
        elif resMenu == 2:
            log.debug("escogio 2 - Productos")
            mantenimientoProductos()
        elif resMenu == 3:
            log.debug("escogio 3 - Empresa")
            mantenimientoEmpresa()
        elif resMenu == 4:
            log.debug("escogio 4 - Tipo Pago")
            mantenimientoTipoPago()
        elif resMenu == 9:
            valorTrue = False
        else:
            log.debug(f"escogio {resMenu}")

dicMenuFacturaGeneral = {    "\t- Listar Todas: ": 1,"\t- Buscar Por ID: ": 2,"\t- Crear Factura: ": 3}
def Facturas():
    cargarCabeceraFactura()
    valorTrue = True
    while valorTrue:
        menuMantenimiento = utils.Menu("Menu Facturas", dicMenuFacturaGeneral)
        resMenu = menuMantenimiento.mostrarMenu()
        if resMenu == 1:
            log.debug("escogio 1 - Listar") 
            utils.listaSimple(lstFacturaCabecera,5,1)
        elif resMenu == 2:
            log.debug("escogio 2 - Buscar")
            Buscar = utils.validarEntero("Correlativo: ")
            conn = conexion.conexionBDD(NumeroBDD) 
            query = query_FacturaCabecera
            if NumeroBDD==2:
                query = query_FacturaCabecera +' where c.idfacCabecera ='+  f" '{Buscar}';"
            elif NumeroBDD !=2:
                query = query_FacturaCabecera + f" where c.idfacCabecera ='{Buscar}';"
            resConn2 = conn.consultarBDD(query)
            lstGeneralTemp = []
            for row in resConn2:
                GeneralF = factura.facturaCabecera(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                lstGeneralTemp.append(GeneralF)
                
            queryDetalle = query_FacturaDetalle
            if NumeroBDD==2:
                queryDetalle = query_FacturaDetalle +' where d.idfacCabecera ='+  f" '{Buscar}';"
            elif NumeroBDD !=2:
                queryDetalle = query_FacturaDetalle + f" where d.idfacCabecera ='{Buscar}';"
            resConnD = conn.consultarBDD(queryDetalle)
            lstGeneralDetalleTemp = []
            for row in resConnD:
                GeneralDetalleF = factura.facDetalle(row[0],row[1],row[2],row[3],row[4],row[5])
                lstGeneralDetalleTemp.append(GeneralDetalleF)
            
            utils.listaSimple(lstGeneralTemp,5,0)
            utils.listaSimple(lstGeneralDetalleTemp,6,1)
        elif resMenu == 3:
            log.debug("escogio 3 - Crear")
            print("Selecciona la Empresa: ")
            cargarEmpresa()
            utils.listaSimple(lstEmpresa,3,0)
            idEmpresa = utils.validarIDEnLista(lstEmpresa,"9999=Cancelar / ID: ",3)
            if idEmpresa==9999:
                valorTrue = False
                return
            print("Selecciona el Cliente: ")
            cargarClientes()
            utils.listaSimple(lstClientes,1,0)
            idCliente = utils.validarIDEnLista(lstClientes,"9999=Cancelar / ID: ",1)
            if idCliente==9999:
                valorTrue = False
                return
            print("Selecciona el Tipo de Pago: ")
            cargarTipoPago()
            utils.listaSimple(lstTipoPago,4,0)
            idTipoPago = utils.validarIDEnLista(lstTipoPago,"9999=Cancelar / ID: ",4)
            if idTipoPago==9999:
                valorTrue = False
                return
            limpiarDetalleFactura()
            print("Selecciona los Productos: ")
            cargarProductos()
            utils.listaSimple(lstProductos,2,0)
            agregandoProdTrue = True
            while agregandoProdTrue:
                valorProducto = 0.00
                afecto = 0
                idProducto = utils.validarIDEnLista(lstProductos,"ID: ",2)
                cantProducto = utils.validarEntero("Cantidad: ")
                #idProducto,nombreProducto,valorProducto,igvProducto
                for p in lstProductos:  
                    if(p.idProducto==idProducto):
                        valorProducto=p.valorProducto
                        afecto = p.igvProducto
                valorDetalle = valorProducto*cantProducto
                documentF = factura.facDetalleInsertar(0,0,idProducto,cantProducto,valorDetalle,afecto)
                lstFacturaDetalle.append(documentF)
                agregarOtro = utils.validarEntero("0=Finalizar / 1=agregar: ")
                if agregarOtro ==0:
                    agregandoProdTrue = False
            SubTotal = 0.00
            SubTotalSinIgv = 0.00
            #   idFacDetalle, idfacCabecera, idproducto, cantFacDetalle, valorFacDetalle, afecto
            for detalle in lstFacturaDetalle:
                if detalle.afecto==1:
                    SubTotal+=float(detalle.valorFacDetalle)
                else:
                    SubTotalSinIgv+=float(detalle.valorFacDetalle)
            Igv = SubTotal*0.18
            # SubTotal=SubTotal*1.18
            SubTotalFinal = SubTotal + SubTotalSinIgv
            Total = SubTotalFinal + Igv

            connInsertar = conexion.conexionBDD(NumeroBDD) 
            query_Insertar = ""
            if NumeroBDD==2: 
                query_Insertar = ' insert into "faccabecera" ("idempresa", "idcliente","idtipoPago","fechaFacCabecera" '
                query_Insertar += ' ,"igvFacCabecera","subtotalFacCabecera","totalFacCabecera","estadoFactura" )'
                query_Insertar += ' values( '+ f" '{idEmpresa}','{idCliente}','{idTipoPago}',now(),'{Igv}','{SubTotalFinal}','{Total}',1);"
            else:
                query_Insertar = " insert into faccabecera (idempresa, idcliente,idtipoPago,fechaFacCabecera "
                query_Insertar += " ,igvFacCabecera,subtotalFacCabecera,totalFacCabecera,estadoFactura ) "
                query_Insertar += " values( "+ f" '{idEmpresa}','{idCliente}','{idTipoPago}',now(),'{Igv}','{SubTotalFinal}','{Total}',1);"
            
            resConnInsertar = connInsertar.ejecutarBDD_ReturnID(query_Insertar)
            if(resConnInsertar>0):
                #cargarCabeceraFactura() 
                Intguardados = 0  
                query_InsertarDetalle = "" 
                #idFacDetalle, idfacCabecera, idproducto, cantFacDetalle, valorFacDetalle, afecto
                for detalle in lstFacturaDetalle:
                    if NumeroBDD==2:
                        query_InsertarDetalle = ' insert into "facdetalle" ("idfacCabecera", "idproducto","cantFacDetalle","valorFacDetalle") '
                        query_InsertarDetalle += ' values( '+ f" '{resConnInsertar}','{detalle.idproducto}','{detalle.cantFacDetalle}','{detalle.valorFacDetalle}');"
                    else:
                        query_InsertarDetalle = " insert into facdetalle (idfacCabecera, idproducto,cantFacDetalle,valorFacDetalle) "
                        query_InsertarDetalle += " values( "+ f" '{resConnInsertar}','{detalle.idproducto}','{detalle.cantFacDetalle}','{detalle.valorFacDetalle}');"
                    resConnInsertarDetalle = connInsertar.ejecutarBDD(query_InsertarDetalle)
                    
                    print(resConnInsertarDetalle)
                    if(resConnInsertarDetalle):
                        Intguardados+=1
                if(Intguardados>0):
                    print("Se ejecuto correctamente")
                else:
                    print("Hubo un error detalle")
            else:
                print("Hubo un error")
            cargarCabeceraFactura()
            input(MsjContinuar)
        elif resMenu == 9:
            valorTrue = False
        else:
            log.debug(f"escogio {resMenu}")





stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Crear Factura": 1, "\t- Mantenimientos": 2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("Mostramos el Menu crear Factura")
        Facturas()
    elif(resMenuInicio == 2):
        log.debug("Mostramos los Mantenimientos")
        mantenimento()
    elif(resMenuInicio == 9):
        log.debug("finalizar Programa")
        stopMenuInicio = False
    else:
        log.debug("volvemos a mostrar menu")
        stopMenuInicio = False

