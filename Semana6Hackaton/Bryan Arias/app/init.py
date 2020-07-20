import utils
import conexion
import querys
import clientes
import empresa
import productos
import tipopago
import factura
from time import sleep

__log = utils.log("Principal")
__log.info("Inicio del Sistema")
OpcionMenuPrincipal = True
while(OpcionMenuPrincipal):
    #Llamamos al menu principal
    TuplaMenuPrincipal = ("1. MYSQL", "2. POSTGRE", "3. ORACLE 11G")
    MenuPrincipal = utils.Menu("MENU PRINCIPAL\t", TuplaMenuPrincipal)
    MostrarMenuPrincipal = MenuPrincipal.MostrarMenu()
    #Tupla del menu para cada gestor de base de datos (Todos tienen el mismo menu)
    TuplaGestorBD = ("1. CREAR BASE DE DATOS", "2. CREAR TABLAS", "3. YA TENGO TODO CREADO","4. REGRESAR")
    #Verificar la opcion elegida
    if(MostrarMenuPrincipal == 1):
      __log.info("Inicio Menu Mysql")
      #Menu BD MYSQL
      OpcionMenuGestor = True
      while(OpcionMenuGestor):
        GestorBD = utils.Menu("BASE MYSQL\t", TuplaGestorBD)
        MostrarBDMysql = GestorBD.MostrarMenu()
        if(MostrarBDMysql == 1):
          __log.info("Inicio Menu Crear Base de Datos")
          #Credenciales de la base de datos
          UsuarioBD = input("Ingrese su usuario de la BD:\n")
          ClaveBD = input("Ingrese su clave de la BD:\n")
          HostBD = input("Ingrese host de la BD:\n")
          BDMysql = conexion.conexionBDD(1, UsuarioBD, ClaveBD, HostBD, "mydb")
          #Verificar si estan correcta las credenciales
          ConexionMysql = BDMysql.conexion()
          if(ConexionMysql):
            #Si esta bien la conexion pide nombre de la BD a crear
            NombreBD = input("Ingrese nombre de la base de datos:\n")
            query = querys.Querys(NombreBD)
            consulta = query.CreateDB()
            BDMysql.CreateDB(consulta)
            print("La Base de Datos se a creado correctamente")
            OpcionMenuGestor = True
            sleep(2)
          else:
            print("Error al ingresar a la Base de Datos")
            OpcionMenuGestor = True
            sleep(2)
        elif(MostrarBDMysql == 2):
          __log.info("Inicio Menu Crear Tablas")
          try:
            #Crear las tablas
            NuevaBDMysql = conexion.conexionBDD(1, UsuarioBD, ClaveBD, HostBD, NombreBD)
            ConexionNuevaMysql = NuevaBDMysql.conexion()
            print("Se van a crear las tablas necesarias...")
            if(ConexionNuevaMysql):
              #Se crean las tablas automaticamente del archivo query.py
              consulta1 = query.CreateTablas()
              NuevaBDMysql.ejecutarBDD(consulta1)
              print("Se han creado todas las tablas correctamente")
              sleep(2)
            else:
              print("Hubo un error al crear las tablas")
              sleep(2)
          except Exception as e:
            #Primero se tiene que crear la base de datos
            __log.info(f"No hay datos{e}")
            print("Primero debe crear la base de datos")
            sleep(2)
        #Si ya tiene creado la base de datos
        elif(MostrarBDMysql == 3):
          __log.info("Inicio Menu Todo Creado")
          #Mantenerce en el menu de Operaciones
          OpcionMenuMysql = True
          while OpcionMenuMysql:
            #Controlar error si no existen datos
            try:
              ConecBDMysql = conexion.conexionBDD(1, UsuarioBD, ClaveBD, HostBD, NombreBD)
              #Mostrar menu para mantenimiento o factura
              TuplaMenuMysql = ("1. CREAR FACTURA", "2. MANTENIMIENTOS", "3. REGRESAR")
              MenuMyql = utils.Menu("MENU OPERACIONES\t", TuplaMenuMysql)
              MostrarMenuMysql = MenuMyql.MostrarMenu()
              if(MostrarMenuMysql == 1):
                #Menu Factura
                __log.info("Inicio Menu Crear Factura")
                
                #Si no existe el cliente volver a pedir id
                OpcionMenuFacturaCliente = True
                while OpcionMenuFacturaCliente:
                  #Listamos a todos los clientes
                  query = querys.Querys(NombreBD)
                  SqlClientes = query.SelectAllClientes()
                  Clientes = ConecBDMysql.consultarBDD(SqlClientes)
                  #Cabecera
                  print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                  #Mostrar Datos
                  for tplCliente in Clientes:
                    print(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3], sep="\t")
                  IdCliente = input("Ingrese Id del Cliente:\n")
                  try:
                    SqlClientes = query.SelectIdCliente(IdCliente)
                    ResulClientes = ConecBDMysql.consultarBDD(SqlClientes)
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
                        SqlEmpresas = query.SelectAllEmpresas()
                        Empresas = ConecBDMysql.consultarBDD(SqlEmpresas)
                        #Cabecera
                        print("ID", "Numero Ruc", "Nombre\t", sep="\t")
                        #Mostrar Datos
                        for tplEmpresa in Empresas:
                          print(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2], sep="\t")          
                        IdEmpresa = input("Ingrese Id de la Empresa:\n")
                        SqlEmpresas = query.SelectIdEmpresa(IdEmpresa)
                        ResulEmpresas = ConecBDMysql.consultarBDD(SqlEmpresas)
                        if ResulEmpresas:
                          for tplEmpresa in ResulEmpresas:
                            ObjEmpresa = empresa.empresa(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2])
                            lstEmpresa.append(ObjEmpresa)
                            __log.debug("Se ingreso bien el ObjEmpresa")
                          
                          OpcionMenuFacturaTipo = True
                          while OpcionMenuFacturaTipo:
                            SqlTipo = query.SelectAllTipos()
                            Tipos = ConecBDMysql.consultarBDD(SqlTipo)
                            #Cabecera
                            print("ID", "Nombre\t", sep="\t")
                            #Mostrar Datos
                            for tplTipo in Tipos:
                              print(tplTipo[0], tplTipo[1], sep="\t")
                            IdTipo = input("Ingrese Id del tipo de pago:\n")
                            SqlTipo = query.SelectIdTipo(IdTipo)
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
                              SqlFacCabecera = query.InsertCabecera(str(idEmp), str(idClie), str(idTip), str(igvProd), str(subTotal), str(Total))
                              ConecBDMysql.ejecutarBDD(SqlFacCabecera)
                              #Mostrar todas las Cabeceras
                              SqlAllCabecera = query.SelectAllCabecera()
                              ResulAllCabecera = ConecBDMysql.consultarBDD(SqlAllCabecera)
                              print("ID", "Empresa\t", "Cliente\t", "Tipo Pago", sep="\t")
                              for tplCabecera in ResulAllCabecera:
                                print(tplCabecera[0], tplCabecera[1], "", tplCabecera[2], tplCabecera[3], sep="\t")
                              #Solicitamos ID cabecera
                              IdCab = input("Ingrese Id de Cabecera a llenar:\n")                                                         
                              OpcionMenuFacturaProducto = True
                              while OpcionMenuFacturaProducto:
                                #Todos los productos
                                SqlProducto = query.SelectAllProductos()
                                Productos = ConecBDMysql.consultarBDD(SqlProducto)
                                #Cabecera
                                print("ID", "Nombre\t", "Valor", "Igv", sep="\t")
                                #Mostrar Datos
                                for tplProducto in Productos:
                                  print(tplProducto[0], tplProducto[1]+"\t", tplProducto[2], tplProducto[3], sep="\t")
                                IdProducto = input("Ingrese Id del producto:\n")
                                SqlProducto = query.SelectIdProducto(IdProducto)
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
                                  SqlIdCabecera = query.SelectIdCabecera(IdCab)
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
                                  SqlFacDetalle = query.InsertDetalle(idCabe, idProd, CantProducto, valorTotal)
                                  ConecBDMysql.ejecutarBDD(SqlFacDetalle)
                                  igvProducto = float(igvCab)
                                  if igvProd == 1:
                                    igvProducto = (valorTotal * 0.18) + igvProducto
                                  else:
                                    igvProducto += 0
                                  #Modificar facCabecera
                                  SqlModiCabcera = query.UpdateCabecera(idCabe, igvProducto)
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
                                      SqlDetalle = query.SelectDetalle(idCabe)
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
              elif(MostrarMenuMysql == 2):
                __log.info("Inicio Menu Mantenimientos")
                #OpcionMenuMysql = True
                #Menu Mantenimiento
                OpcionMenuMant = True
                while OpcionMenuMant:
                  TuplaMenuMant = ("1. CLIENTES", "2. PRODUCTOS", "3. EMPRESA", "4. TIPO DE PAGO", "5. REGRESAR")
                  MenuMant = utils.Menu("MENU MANTENIMIENTO\t", TuplaMenuMant)
                  MostrarMenuMant = MenuMant.MostrarMenu()
                  #Escoger a que tabla se hara mantenimiento
                  if(MostrarMenuMant == 1):
                    __log.info("Inicio Menu Clientes")
                    OpcionMenuCliente = True
                    while OpcionMenuCliente:
                      #Mantenimiento a la tabla clientes
                      TuplaMenuCliente = ("1. LISTAR A TODOS LOS CLIENTES", "2. BUSCAR CLIENTE POR DNI", "3. MODIFICAR CLIENTE POR DNI", "4. CREAR CLIENTE", "5. BORRAR CLIENTE", "6. REGRESAR")
                      MenuCliente = utils.Menu("MENU MANTENIMIENTO\t", TuplaMenuCliente)
                      MostrarMenuCliente = MenuCliente.MostrarMenu()
                      queryClientes = querys.Querys(NombreBD)
                      #Declarar lista
                      lstClientes = []
                      #Listar todos los clientes
                      if MostrarMenuCliente == 1:
                        __log.info("Inicio Lista clientes")
                        AllClientes = queryClientes.SelectAllClientes()
                        resulAllClientes = ConecBDMysql.consultarBDD(AllClientes)
                        #Cabecera
                        print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                        #Mostrar Datos
                        for tplCliente in resulAllClientes:
                          print(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3], sep="\t")
                        sleep(3)
                      #Buscar Cliente por DNI
                      elif MostrarMenuCliente == 2:
                        __log.info("Inicio Buscar")
                        Dni = input("Ingrese Dni a buscar:\n")
                        DniCliente = queryClientes.SelectDniCliente(Dni)
                        resulDniCliente = ConecBDMysql.consultarBDD(DniCliente)
                        #Cabecera
                        print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                        #Mostrar Datos
                        for tplCliente in resulDniCliente:
                          print(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3], sep="\t")
                        sleep(3)
                      #Modificar Cliente
                      elif MostrarMenuCliente == 3:
                        __log.info("Modificar Cliente")
                        #Buscar cliente a modificar
                        Id = input("Ingrese id del Cliente a modificar:\n")
                        IdCliente = queryClientes.SelectIdCliente(Id)
                        resulIdCliente = ConecBDMysql.consultarBDD(IdCliente)
                        #Cabecer
                        print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                        #Resultado
                        for tplCliente in resulIdCliente:
                          print(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3], sep="\t")
                          #Ingresar nuevos datos
                          Nombre = input("Ingrese el nuevo valor para Nombre:\n")
                          Dni = input(f"Ingrese el nuevo valor de dni para {Nombre}: \n")
                          Direccion = input(f"Ingrese el nuevo valor de direccion para {Nombre}: \n")
                          #query para modificar
                          ModiCliente = queryClientes.UpdateCliente(Id, Nombre, Dni, Direccion)
                          resulModiCliente = ConecBDMysql.ejecutarBDD(ModiCliente)
                          #Verificar si modifico al cliente
                          if(resulModiCliente):
                            print(f"Se a modificado el cliente {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuCliente == 4:
                        __log.info("Crear Cliente")
                        #Ingresar Nuevos Clientes
                        print("...:::Creacion de un Cliente:::...")
                        Nombre = input("Ingrese Nombre del Cliente Nuevo:\n")
                        Dni = input(f"Ingrese Dni del Cliente {Nombre}:\n")
                        Direccion = input(f"Ingrese Direccion del Cliente {Nombre}:\n")
                        #query Insertar
                        InsertCliente = queryClientes.InsertCliente(Nombre, Dni, Direccion)
                        resulInsertCliente = ConecBDMysql.ejecutarBDD(InsertCliente)
                        #Verificar si inserto al cliente
                        if(resulInsertCliente):
                          print(f"Se inserto al cliente {Nombre}")
                        else:
                          print("Hubo un error al insertar el cliente")
                      elif MostrarMenuCliente == 5:
                        __log.info("Borrar Cliente")
                        #Buscar cliente a eliminar
                        Id = input("Ingrese id del Cliente a eliminar:\n")
                        IdCliente = queryClientes.SelectIdCliente(Id)
                        resulIdCliente = ConecBDMysql.consultarBDD(IdCliente)
                        #Cabecera
                        print("ID", "Nombre\t", "DNI\t", "Direccion", sep="\t")
                        #Resultado
                        for tplCliente in resulIdCliente:
                          print(tplCliente[0], tplCliente[1], tplCliente[2], tplCliente[3], sep="\t")
                          #query para eliminar
                          EliCliente = queryClientes.DeleteCliente(Id)
                          resulEliCliente = ConecBDMysql.ejecutarBDD(EliCliente)
                          #Verificar si elimino al cliente
                          if(resulEliCliente):
                            print(f"Se a eliminado el cliente {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuCliente == 6:
                        __log.info("Regresar")
                        OpcionMenuCliente = False
                      elif(MostrarMenuCliente == 0):
                        __log.info("Salir del sistema")
                        utils.Salir()
                      else:
                        print("Escoja un opcion valida")
                        sleep(2)
                  elif(MostrarMenuMant == 2):
                    __log.info("Inicio Menu Productos")
                    OpcionMenuProducto = True
                    while OpcionMenuProducto:
                      #Mantenimiento a la tabla Productos
                      TuplaMenuProducto = ("1. LISTAR A TODOS LOS PRODUCTOS", "2. BUSCAR PRODUCTOS POR NOMBRE", "3. MODIFICAR PRODUCTOS POR ID", "4. CREAR PRODUCTOS", "5. BORRAR PRODUCTOS", "6. REGRESAR")
                      MenuProducto = utils.Menu("MENU MANTENIMIENTO\t", TuplaMenuProducto)
                      MostrarMenuProducto = MenuProducto.MostrarMenu()
                      queryProductos = querys.Querys(NombreBD)
                      #Declarar lista
                      lstProductos = []
                      #Listar todos los Productos
                      if MostrarMenuProducto == 1:
                        __log.info("Inicio Lista Productos")
                        AllProductos = queryProductos.SelectAllProductos()
                        resulAllProductos = ConecBDMysql.consultarBDD(AllProductos)
                        #Cabecera
                        print("ID", "Nombre\t", "Valor", "Igv", sep="\t")
                        #Mostrar Datos
                        for tplProducto in resulAllProductos:
                          print(tplProducto[0], tplProducto[1]+"\t", tplProducto[2], tplProducto[3], sep="\t")
                        sleep(3)
                      #Buscar Producto por Id
                      elif MostrarMenuProducto == 2:
                        __log.info("Inicio Buscar")
                        NombreProd = input("Ingrese nombre del producto a buscar:\n")
                        NombreProducto = queryProductos.SelectIdProducto(NombreProd)
                        resulNombreProducto = ConecBDMysql.consultarBDD(NombreProducto)
                        #Cabecera
                        print("ID", "Nombre\t", "Valor", "Igv", sep="\t")
                        #Mostrar Datos
                        for tplProducto in resulNombreProducto:
                          print(tplProducto[0], tplProducto[1]+"\t", tplProducto[2], tplProducto[3], sep="\t")
                        sleep(3)
                      #Modificar Producto
                      elif MostrarMenuProducto == 3:
                        __log.info("Modificar Producto")
                        #Buscar Producto a modificar
                        Id = input("Ingrese id del Producto a modificar:\n")
                        IdProducto = queryProductos.SelectIdProducto(Id)
                        resulIdProducto = ConecBDMysql.consultarBDD(IdProducto)
                        #Cabecera
                        print("ID", "Nombre\t", "Valor", "Igv", sep="\t")
                        #Resultado
                        for tplProducto in resulIdProducto:
                          print(tplProducto[0], tplProducto[1]+"\t", tplProducto[2], tplProducto[3], sep="\t")
                          #Ingresar nuevos datos
                          Nombre = input("Ingrese el nuevo valor para Nombre:\n")
                          Valor = input(f"Ingrese el nuevo valor de valor para {Nombre}: \n")
                          Igv = input(f"Ingrese el nuevo valor de igv para {Nombre}: \n")
                          #query para modificar
                          ModiProducto = queryProductos.UpdateProducto(Id, Nombre, Valor, Igv)
                          resulModiProducto = ConecBDMysql.ejecutarBDD(ModiProducto)
                          #Verificar si modifico al Producto
                          if(resulModiProducto):
                            print(f"Se a modificado el Producto {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuProducto == 4:
                        __log.info("Crear Producto")
                        #Ingresar Nuevos Productos
                        print("...:::Creacion de un Producto:::...")
                        Nombre = input("Ingrese Nombre del Producto Nuevo:\n")
                        Valor = input(f"Ingrese Valor del Producto {Nombre}:\n")
                        Igv = input(f"Ingrese Igv del Producto {Nombre}:\n")
                        #query Insertar
                        InsertProducto = queryProductos.InsertProducto(Nombre, Valor, Igv)
                        resulInsertProducto = ConecBDMysql.ejecutarBDD(InsertProducto)
                        #Verificar si inserto al Producto
                        if(resulInsertProducto):
                          print(f"Se inserto al Producto {Nombre}")
                        else:
                          print("Hubo un error al insertar el Producto")
                      elif MostrarMenuProducto == 5:
                        __log.info("Borrar Producto")
                        #Buscar Producto a eliminar
                        Id = input("Ingrese id del Producto a eliminar:\n")
                        IdProducto = queryProductos.SelectIdProducto(Id)
                        resulIdProducto = ConecBDMysql.consultarBDD(IdProducto)
                        #Cabecera
                        print("ID", "Nombre\t", "Valor", "Igv", sep="\t")
                        #Resultado
                        for tplProducto in resulIdProducto:
                          print(tplProducto[0], tplProducto[1]+"\t", tplProducto[2], tplProducto[3], sep="\t")
                          #query para eliminar
                          EliProducto = queryProductos.DeleteProducto(Id)
                          resulEliProducto = ConecBDMysql.ejecutarBDD(EliProducto)
                          #Verificar si elimino al Producto
                          if(resulEliProducto):
                            print(f"Se a eliminado el Producto {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuProducto == 6:
                        __log.info("Regresar")
                        OpcionMenuProducto = False
                      elif(MostrarMenuProducto == 0):
                        __log.info("Salir del sistema")
                        utils.Salir()
                      else:
                        print("Escoja un opcion valida")
                        sleep(2)
                  elif(MostrarMenuMant == 3):
                    __log.info("Inicio Menu Empresa")
                    OpcionMenuEmpresa = True
                    while OpcionMenuEmpresa:
                      #Mantenimiento a la tabla Empresa
                      TuplaMenuEmpresa = ("1. LISTAR A TODOS LOS EMPRESA", "2. BUSCAR EMPRESA POR NOMBRE", "3. MODIFICAR EMPRESA POR ID", "4. CREAR EMPRESA", "5. BORRAR EMPRESA", "6. REGRESAR")
                      MenuEmpresa = utils.Menu("MENU MANTENIMIENTO\t", TuplaMenuEmpresa)
                      MostrarMenuEmpresa = MenuEmpresa.MostrarMenu()
                      queryEmpresas = querys.Querys(NombreBD)
                      #Declarar lista
                      lstEmpresas = []
                      #Listar todos los Empresas
                      if MostrarMenuEmpresa == 1:
                        __log.info("Inicio Lista Empresa")
                        AllEmpresas = queryEmpresas.SelectAllEmpresas()
                        resulAllEmpresas = ConecBDMysql.consultarBDD(AllEmpresas)
                        #Cabecera
                        print("ID", "Numero Ruc", "Nombre\t", sep="\t")
                        #Mostrar Datos
                        for tplEmpresa in resulAllEmpresas:
                          print(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2], sep="\t")
                        sleep(3)
                      #Buscar Empresa por Ruc
                      elif MostrarMenuEmpresa == 2:
                        __log.info("Inicio Buscar")
                        RucEmp = input("Ingrese numero de Ruc de la empresa a buscar:\n")
                        RucEmpresa = queryEmpresas.SelectRucEmpresa(RucEmp)
                        resulRucEmpresa = ConecBDMysql.consultarBDD(RucEmpresa)
                        #Cabecera
                        print("ID", "Numero Ruc", "Nombre\t", sep="\t")
                        #Mostrar Datos
                        for tplEmpresa in resulRucEmpresa:
                          print(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2], sep="\t")
                        sleep(3)
                      #Modificar Empresa
                      elif MostrarMenuEmpresa == 3:
                        __log.info("Modificar Empresa")
                        #Buscar Empresa a modificar
                        Id = input("Ingrese id de la Empresa a modificar:\n")
                        IdEmpresa = queryEmpresas.SelectIdEmpresa(Id)
                        resulIdEmpresa = ConecBDMysql.consultarBDD(IdEmpresa)
                        #Cabecera
                        print("ID", "Numero Ruc", "Nombre\t", sep="\t")
                        #Resultado
                        for tplEmpresa in resulIdEmpresa:
                          print(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2], sep="\t")
                          #Ingresar nuevos datos
                          Nombre = input("Ingrese el nuevo valor para Nombre:\n")
                          NumRuc = input(f"Ingrese el nuevo valor de valor para {Nombre}: \n")
                          #query para modificar
                          ModiEmpresa = queryEmpresas.UpdateEmpresa(Id, NumRuc, Nombre)
                          resulModiEmpresa = ConecBDMysql.ejecutarBDD(ModiEmpresa)
                          #Verificar si modifico al Empresa
                          if(resulModiEmpresa):
                            print(f"Se a modificado el Empresa {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuEmpresa == 4:
                        __log.info("Crear Empresa")
                        #Ingresar Nuevos Empresa
                        print("...:::Creacion de un Empresa:::...")
                        Nombre = input("Ingrese Nombre del Empresa Nuevo:\n")
                        NumRuc = input(f"Ingrese Ruc de la Empresa {Nombre}:\n")
                        #query Insertar
                        InsertarEmpresa = queryEmpresas.InsertEmpresa(NumRuc, Nombre)
                        resulInsertEmpresa = ConecBDMysql.ejecutarBDD(InsertarEmpresa)
                        #Verificar si inserto al Empresa
                        if(resulInsertEmpresa):
                          print(f"Se inserto al Empresa {Nombre}")
                        else:
                          print("Hubo un error al insertar el Empresa")
                        sleep(2)
                      elif MostrarMenuEmpresa == 5:
                        __log.info("Borrar Empresa")
                        #Buscar Empresa a eliminar
                        Id = input("Ingrese id del Empresa a eliminar:\n")
                        IdEmpresa = queryEmpresas.SelectIdEmpresa(Id)
                        resulIdEmpresa = ConecBDMysql.consultarBDD(IdEmpresa)
                        #Cabecera
                        print("ID", "Numero Ruc", "Nombre\t", sep="\t")
                        #Resultado
                        for tplEmpresa in resulIdEmpresa:
                          print(tplEmpresa[0], tplEmpresa[1], tplEmpresa[2], sep="\t")
                          #query para eliminar
                          EliEmpresa = queryEmpresas.DeleteEmpresa(Id)
                          resulEliEmpresa = ConecBDMysql.ejecutarBDD(EliEmpresa)
                          #Verificar si elimino al Empresa
                          if(resulEliEmpresa):
                            print(f"Se a eliminado el Empresa {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuEmpresa == 6:
                        __log.info("Regresar")
                        OpcionMenuEmpresa = False
                      elif(MostrarMenuEmpresa == 0):
                        __log.info("Salir del sistema")
                        utils.Salir()
                      else:
                        print("Escoja un opcion valida")
                        sleep(2)
                  elif(MostrarMenuMant == 4):
                    __log.info("Inicio Menu Tipo de Pago")
                    OpcionMenuTipo = True
                    while OpcionMenuTipo:
                      #Mantenimiento a la tabla Tipo de Pago
                      TuplaMenuTipo = ("1. LISTAR A TODOS LOS TIPOS DE PAGO", "2. BUSCAR TIPOS DE PAGO POR NOMBRE", "3. MODIFICAR TIPOS DE PAGO POR ID", "4. CREAR TIPOS DE PAGO", "5. BORRAR TIPOS DE PAGO", "6. REGRESAR")
                      MenuTipo = utils.Menu("MENU MANTENIMIENTO\t", TuplaMenuTipo)
                      MostrarMenuTipo = MenuTipo.MostrarMenu()
                      queryTipos = querys.Querys(NombreBD)
                      #Declarar lista
                      lstTipos = []
                      #Listar todos los Tipos
                      if MostrarMenuTipo == 1:
                        __log.info("Inicio Lista Tipo de Pago")
                        AllTipos = queryTipos.SelectAllTipos()
                        resulAllTipos = ConecBDMysql.consultarBDD(AllTipos)
                        #Cabecera
                        print("ID", "Nombre\t", sep="\t")
                        #Mostrar Datos
                        for tplTipo in resulAllTipos:
                          print(tplTipo[0], tplTipo[1], sep="\t")
                        sleep(3)
                      #Buscar Tipo por Ruc
                      elif MostrarMenuTipo == 2:
                        __log.info("Inicio Buscar")
                        NomTipo = input("Ingrese nombre del tipo de pago a buscar:\n")
                        NombreTipo = queryTipos.SelectNomTipo(NomTipo)
                        resulNombreTipo = ConecBDMysql.consultarBDD(NombreTipo)
                        #Cabecera
                        print("ID", "Nombre\t", sep="\t")
                        #Mostrar Datos
                        for tplTipo in resulNombreTipo:
                          print(tplTipo[0], tplTipo[1], sep="\t")
                        sleep(3)
                      #Modificar Tipo
                      elif MostrarMenuTipo == 3:
                        __log.info("Modificar Tipo")
                        #Buscar Tipo a modificar
                        Id = input("Ingrese id del Tipo de Pago a modificar:\n")
                        IdTipo = queryTipos.SelectIdTipo(Id)
                        resulIdTipo = ConecBDMysql.consultarBDD(IdTipo)
                        #Cabecera
                        print("ID", "Nombre\t", sep="\t")
                        #Resultado
                        for tplTipo in resulIdTipo:
                          print(tplTipo[0], tplTipo[1], sep="\t")
                          #Ingresar nuevos datos
                          Nombre = input("Ingrese el nuevo valor para Nombre:\n")
                          #query para modificar
                          ModiTipo = queryTipos.UpdateTipo(Id, Nombre)
                          resulModiTipo = ConecBDMysql.ejecutarBDD(ModiTipo)
                          #Verificar si modifico al Tipo
                          if(resulModiTipo):
                            print(f"Se a modificado el Tipo {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuTipo == 4:
                        __log.info("Crear Tipo")
                        #Ingresar Nuevos Tipo
                        print("...:::Creacion de un Tipo de Pago:::...")
                        Nombre = input("Ingrese Nombre del Tipo de Pago Nuevo:\n")
                        #query Insertar
                        InsertarTipo = queryTipos.InsertTipo(Nombre)
                        resulInsertTipo = ConecBDMysql.ejecutarBDD(InsertarTipo)
                        #Verificar si inserto al Tipo
                        if(resulInsertTipo):
                          print(f"Se inserto al Tipo de Pago {Nombre}")
                        else:
                          print("Hubo un error al insertar el Tipo de Pago")
                        sleep(2)
                      elif MostrarMenuTipo == 5:
                        __log.info("Borrar Tipo de Pago")
                        #Buscar Tipo de Pago a eliminar
                        Id = input("Ingrese id del Tipo de Pago a eliminar:\n")
                        IdTipo = queryTipos.SelectIdTipo(Id)
                        resulIdTipo = ConecBDMysql.consultarBDD(IdTipo)
                        #Cabecera
                        print("ID", "Nombre\t", sep="\t")
                        #Resultado
                        for tplTipo in resulIdTipo:
                          print(tplTipo[0], tplTipo[1], sep="\t")
                          #query para eliminar
                          EliTipo = queryTipos.DeleteTipo(Id)
                          resulEliTipo = ConecBDMysql.ejecutarBDD(EliTipo)
                          #Verificar si elimino al Tipo de Pago
                          if(resulEliTipo):
                            print(f"Se a eliminado el Tipo de Pago {Id}")
                          else:
                            print("Hubo un error al modificar")
                        sleep(3)
                      elif MostrarMenuTipo == 6:
                        __log.info("Regresar")
                        OpcionMenuTipo = False
                      elif(MostrarMenuTipo == 0):
                        __log.info("Salir del sistema")
                        utils.Salir()
                      else:
                        print("Escoja un opcion valida")
                        sleep(2)
                  elif(MostrarMenuMant == 5):
                    __log.info("Inicio Menu Regresar")
                    OpcionMenuMant = False
                    print("Regresar")
                  elif(MostrarMenuMant == 0):
                    __log.info("Salir del sistema")
                    utils.Salir()
                  else:
                    print("Escoja un opcion valida")
                    sleep(2)
              elif(MostrarMenuMysql == 3):
                __log.info("Inicio Menu Regresar")
                OpcionMenuMysql = False
                print("Regresar Menu")
              elif(MostrarMenuMysql == 0):
                __log.info("Salir del sistema")
                utils.Salir()
              else:
                print("Escoja un opcion valida")
                sleep(2)
            except Exception as e:
              #Peticion de credenciales si tiene todo creado manualmente
              __log.info("La base de datos fue creada manualmente")
              UsuarioBD = input("Ingrese su usuario de la BD:\n")
              ClaveBD = input("Ingrese su clave de la BD:\n")
              HostBD = input("Ingrese host de la BD:\n")
              NombreBD = input("Ingrese el nombre de la BD:\n")
              ConecBDMysqlExep = conexion.conexionBDD(1, UsuarioBD, ClaveBD, HostBD, NombreBD)
              ConecNuevaMysqlExep = ConecBDMysqlExep.conexion()
              if ConecNuevaMysqlExep:
                OpcionMenuMysql = True
              else:
                OpcionMenuMysql = False
                print("Error en las credenciales")
                sleep(2)
        elif MostrarBDMysql == "4":
          break
        else:
          utils.Salir()
    elif(MostrarMenuPrincipal == 2):
      __log.info("Inicio Menu Postgre")
      #Menu BD POSTGRE
      #OpcionMenuPostgre = True
      #while(OpcionMenuPostgre):
      #  GestorBD = Menu("BASE POSTGRE\t", TuplaGestorBD)
      #  MostrarBDPostgre = GestorBD.MostrarMenu()
    elif(MostrarMenuPrincipal == 3):
      __log.info("Inicio Menu Oracle 11g")
      #Menu BD ORACLE 11G
      #OpcionMenuOracle = True
      #while(OpcionMenuOracle):
      #  GestorBD = Menu("BASE ORACLE 11G\t", TuplaGestorBD)
      #  MostrarBDOracle = GestorBD.MostrarMenu()
    else:
      utils.Salir()

