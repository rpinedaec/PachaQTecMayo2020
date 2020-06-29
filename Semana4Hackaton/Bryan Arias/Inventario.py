import utils
from time import sleep
import os
import json
#Objeto menu
class Menu:
    __log = utils.log("Menu")
    #Constructor
    def __init__ (self, NombreMenu, TuplaMenu):
        self.NombreMenu = NombreMenu
        self.TuplaMenu = TuplaMenu
    #Limpiar la pantall
    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()
    #Metodo para mostrar el menu que se quiera
    def MostrarMenu(self):
        #variable para mantener abierto el menu
        menu = True
        while menu:
            self.limpiarPantalla()
            print("....::::::::.... BIENVENIDO AL SISTEMA\t....::::::::....")
            print(f"....::::::::.... {self.NombreMenu}\t....::::::::....")
            #Recorremos la tupla donde se encuentran las opciones
            for i in self.TuplaMenu:
                print (i)
            print("0. SALIR", end="\n\n")
            print("Elija una opcion:")
            #Manejo de error al momento de ingresar un valor
            try:
                opcion = int(input())
                #Validar que exista la opcion
                if opcion != 9 and (opcion > 3 or opcion < 0):
                    self.__log.info(f"La opcion {opcion} no es valida")
                    print("\nEscoja una opcion valida\n\a")
                    sleep(2)
                else:
                    self.__log.debug(f"La opcion {opcion} es valida del menu {self.NombreMenu}")
                    menu = False
            except Exception as e:
                self.__log.error(e)
                print("\nDigite un número entre 0 - 9\n\a")
                sleep(2)
        return opcion
#Incrementar Automatico el id
class AutoID:
    def __init__(self, Lista):
        self.Lista = Lista
    def IdCliente(self):
        IdCliente = len(self.Lista)+1
        return IdCliente
    def IdEmpleado(self):
        IdEmpleados = len(self.Lista)+1
        return IdEmpleados
    def IdProducto(self):
        IdProductos = len(self.Lista)+1
        return IdProductos

#Validar Existencia del Cliente
class SearchCliente:
    __log = utils.log("SearchCliente")
    def __init__(self, Dni):
        self.Dni = Dni    
    #Recorre datos del fichero en busca del cliente
    def ExistenciaCliente(self):
        ListaCliente = Listacliente()
        #Si la lista no esta vacia
        if len(ListaCliente) > 0:
            #Diccionario para almacenar los DNIs
            DniDic = []
            #Recorre la lista y guarda los DNIs en el diccionario
            for DictCliente in ListaCliente:
                DniDic.append(DictCliente["Dni"])
            #Busca en el diccionario si existe el DNI solicitado
            if DniDic.count(self.Dni) > 0:
                print("\nEl cliente ingresado ya existe\n")
                self.__log.info(f"El DNI {self.Dni} ya existe")
                return "Existe"
            else:
                self.__log.debug(f"El DNI {self.Dni} no existe")
                #print("El cliente ingresado no existe")
                return "No Existe"
        else:
            #print("La lista esta vacia")
            return "Vacio"

class SearchEmpleado:
    __log = utils.log("SearchEmpleado")
    def __init__(self, Dni):
        self.Dni = Dni    
    #Recorre datos del fichero en busca del Empleado
    def ExistenciaEmpleado(self):
        ListaEmpleado = Listaempleados()
        #Si la lista no esta vacia
        if len(ListaEmpleado) > 0:
            #Diccionario para almacenar los DNIs
            DniDic = []
            #Recorre la lista y guarda los DNIs en el diccionario
            for DictEmpleado in ListaEmpleado:
                DniDic.append(DictEmpleado["Dni"])
            #Busca en el diccionario si existe el DNI solicitado
            if DniDic.count(self.Dni) > 0:
                print("\nEl cliente ingresado ya existe\n")
                self.__log.info(f"El DNI {self.Dni} ya existe")
                return "Existe"
            else:
                self.__log.debug(f"El DNI {self.Dni} no existe")
                #print("El cliente ingresado no existe")
                return "No Existe"
        else:
            #print("La lista esta vacia")
            return "Vacio"

class SearchProducto:
    __log = utils.log("SearchProducto")
    def __init__(self, Producto):
        self.Producto = Producto    
    #Recorre datos del fichero en busca del Producto
    def ExistenciaProducto(self):
        ListaProducto = Listaproductos()
        #Si la lista no esta vacia
        if len(ListaProducto) > 0:
            #Diccionario para almacenar los Productos
            ProductoDic = []
            #Recorre la lista y guarda los Productos en el diccionario
            for DictProducto in ListaProducto:
                ProductoDic.append(DictProducto["NombreProducto"])
            #Busca en el diccionario si existe el Producto solicitado
            if ProductoDic.count(self.Producto) > 0:
                print("\nEl Producto ingresado ya existe\n")
                self.__log.info(f"El Producto {self.Producto} ya existe")
                return "Existe"
            else:
                self.__log.debug(f"El Producto {self.Producto} no existe")
                #print("El Producto ingresado no existe")
                return "No Existe"
        else:
            #print("La lista esta vacia")
            return "Vacio"

class Persona:
    __estado = True
    def __init__(self, Dni, Nombre, Apellido, Edad):
        self.Dni = Dni
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad    
#Clase Cliente que hereda los atributos de Persona
class Cliente(Persona):
    def __init__ (self, Dni, Nombre, Apellido, Edad, IdCliente):
        Persona.__init__(self, Dni, Nombre, Apellido, Edad)
        self.IdCliente = IdCliente
    def DiccionarioCliente(self):
        dc = {
            'Dni': self.Dni,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Edad': self.Edad,
            'IdCliente': self.IdCliente}
        return dc  
    
class Empleado(Persona):
    def __init__ (self, Dni, Nombre, Apellido, Edad, IdEmpleado):
        Persona.__init__(self, Dni, Nombre, Apellido, Edad)
        self.IdEmpleado = IdEmpleado
    def DiccionarioEmpleado(self):
        de = {
            'Dni': self.Dni,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Edad': self.Edad,
            'IdEmpleado': self.IdEmpleado}
        return de

class Producto():
    def __init__(self, NombreProducto, PrecioUnidad, Stock, PrecioTotal, IdProducto):
        self.NombreProducto = NombreProducto
        self.PrecioUnidad = PrecioUnidad
        self.Stock = Stock
        self.PrecioTotal = PrecioTotal
        self.IdProducto = IdProducto
    def DiccionarioProducto(self):
        dp = {
            'NombreProducto': self.NombreProducto,
            'PrecioUnidad': self.PrecioUnidad,
            'Stock': self.Stock,
            'PrecioTotal': self.PrecioTotal,
            'IdProducto': self.IdProducto
        }
        return dp

#Lista de Datos del fichero
def Listacliente():
    __log = utils.log("ListaCliente")
    try:
        cont = fileCliente.leerArchivo()
        ListaCliente = json.loads(cont)
        return ListaCliente
    except Exception as e:
        __log.error(e)
def Listaempleados():
    __log = utils.log("ListaEmpleado")
    try:
        cont = fileEmpleado.leerArchivo()
        ListaEmpleado = json.loads(cont)
        return ListaEmpleado
    except Exception as e:
        __log.error(e)
def Listaproductos():
    __log = utils.log("ListaProductos")
    try:
        cont = fileProductos.leerArchivo()
        ListaProducto = json.loads(cont)
        return ListaProducto
    except Exception as e:
        __log.error(e)

#Metodo para cerrar el sistema
def Salir():
    print("►►►►►► Gracias por usar el Sistema ◄◄◄◄◄◄")
    exit()

#Clase Listar el cual mostrara el listado de Clientes, Empleados y Productos
class Listar():
    def __init__(self, Lista, TipoPersona):
        self.Lista = Lista
        self.TipoPersona = TipoPersona
    def ListarPersona(self):
        #Verificamos si es Cliente, Empleado o Producto
        if self.TipoPersona == "Cliente" :
            __log = utils.log("ListarClientes")
        else:
            __log = utils.log("ListarEmpleados")
        #Si no hay datos mandar mensaje
        if len(self.Lista) > 0:
            for DiccionarioCliente in self.Lista:
                for (key, value) in DiccionarioCliente.items():
                    if key == "Dni":
                        print(value, end=" | ")
                    if key == "Nombre":
                        print(value, end="\t| ")
                    if key == "Apellido":
                        print(value, end="\t\t| ")
                    if key == "Edad":
                        print(value, end="\t| ")
                    if self.TipoPersona == "Cliente":
                        if key == "IdCliente":
                            print(value, end="\n")
                    else:
                        if key == "IdEmpleado":
                            print(value, end="\n")
            __log.debug(f"Existen un total de {value} personas")
            print(f"\nExisten un total de {value} personas\n")
        else:
            __log.info("No hay datos en la lista")
            print("No hay datos en la lista")
    def ListarProducto(self):
        #Verificamos si es Producto
        __log = utils.log("ListarProducto")
        #Si no hay datos mandar mensaje
        if len(self.Lista) > 0:
            #Contadores
            y = 0
            x = 0
            for DiccionarioProducto in self.Lista:
                for (key, value) in DiccionarioProducto.items():
                    if key == "NombreProducto":
                        print(value, end=" \t\t| ")
                    if key == "PrecioUnidad":
                        print(value, end="\t\t| ")
                    if key == "Stock":
                        print(value, end="\t| ")
                        y += value
                    if key == "PrecioTotal":
                        print(value, end="\t| ")
                        x += value
                    if key == "IdProducto": 
                        print(value, end="\n")                    
            __log.debug(f"Existen un total de {value} productos")
            print(f"\nExisten un total de {value} productos")
            print(f"Existen un total de {y} productos en Stock")
            print(f"El precio total es de {x} \n")
        else:
            __log.info("No hay datos en la lista")
            print("No hay datos en la lista")
        


log = utils.log("Principal")
OpcionMenuPrincipal = True
while OpcionMenuPrincipal:
    #Llamamos al menu principal
    TuplaMenuPrincipal = ("1. EMPLEADO", "2. CLIENTE")
    MenuPrincipal = Menu("MENU PRINCIPAL\t", TuplaMenuPrincipal)
    MostrarMenuPrincipal = MenuPrincipal.MostrarMenu()

    #Verificar que opcion a elegido
    if MostrarMenuPrincipal == 1:
        OpcionMenuEmpleado = True
        while OpcionMenuEmpleado:
            TuplaMenuEmpleado = ("1. Agregar Empleado", "2. Listar Empleado", "3. Agregar Producto", "9. Regresar")
            MenuEmpleado = Menu("MENU EMPLEADO\t", TuplaMenuEmpleado)
            MostrarMenuEmpleado = MenuEmpleado.MostrarMenu()
            #Nombre del archivo a crear
            fileEmpleado = utils.fileManager("Empleados.txt")
            fileEmpleado.CrearArchivo()
            #Agregar los datos a una lista
            ListaEmpleado = Listaempleados()
            #Verificar que opcion se eligio
            if MostrarMenuEmpleado == 1:
                OpcionEmpleado = True
                while OpcionEmpleado:
                    #Verificar existencia del Empleado por su DNI
                    Dni = input("Ingrese DNI: ")                
                    ValidarEmpleado = SearchEmpleado(Dni)
                    ExistenciaEmpleado = ValidarEmpleado.ExistenciaEmpleado()
                    #Autoincrementar el ID
                    Auto_ID = AutoID(ListaEmpleado)
                    IdEmpleado = Auto_ID.IdEmpleado()
                    log.debug(ExistenciaEmpleado)                
                    TuplaValidaEmpleado = ("1. Ingresar Nuevamente", "2. Listar Empleado", "9. Regresar")
                    MenuValidaEmpleado = Menu("MENU DATOS EMPLEADO", TuplaValidaEmpleado)
                    #Valida existencia del Empleado
                    if ExistenciaEmpleado == "Existe":
                        sleep(2)
                        #Si existe muestra al menu de datos Empleado
                        MostrarMenuValidaEmpleado = MenuValidaEmpleado.MostrarMenu()
                        if MostrarMenuValidaEmpleado == 1:
                            OpcionMenuEmpleado = True
                            OpcionEmpleado = False
                        elif MostrarMenuValidaEmpleado == 2:
                            #Header para la lista de Empleados
                            print("Dni", "Nombre", "Apellido\t", "Edad", "Id Empleado", sep="\t| ", end="\n")
                            Lista = Listar(ListaEmpleado, "Empleado")
                            ListarEmpleado = Lista.ListarPersona()
                            #Validar que sea una opcion correcta
                            try:
                                opcion = int(input("1. Regresar \n2. Salir \n"))
                                if opcion == 1:
                                    log.debug(f"La opcion {opcion} en valida")
                                    OpcionMenuEmpleado = True
                                elif opcion == 2:
                                    log.debug("Eligio salir del sistema")
                                    Salir()
                                else:
                                    log.debug("Opcion no valida salir del sistema")
                                    print("Ingresó una opcion no valida\a")
                                    Salir()
                            except Exception as e:
                                log.info(f"Eligio una opcion invalida y salió del sistema. {e}")
                                print("Ingresó una opcion no valida\a")
                                Salir()
                        elif MostrarMenuValidaEmpleado == 9:
                            print("Eligió regresar al menú del Empleado")
                            OpcionEmpleado = False
                            OpcionMenuEmpleado = True
                            sleep(2)
                        else:
                            Salir()                        
                    else:
                        #Sigue agregando al Empleado
                        Nombre = input("Ingrese el Nombre: ")
                        Apellido = input("Ingrese los Apellidos: ")
                        Edad = input("Ingrese su Edad: ")                    
                        empleado = Empleado(Dni, Nombre, Apellido, Edad, IdEmpleado)
                        print(f"Se agrego al Empleado {Nombre} {Apellido}")
                        log.debug(f"Se agrego al Empleado {Nombre} {Apellido}")
                        #Agregar a la lista el nuevo Empleado
                        ListaEmpleado.append(empleado.DiccionarioEmpleado())
                        #Guardamos en el archivo a todos los Empleado
                        JsonInsert = json.dumps(ListaEmpleado)
                        fileEmpleado.escribirArchivo(JsonInsert)
                        OpcionEmpleado = False
                        sleep(2)
            elif MostrarMenuEmpleado == 2:
                #Header para la lista de Empleados
                print("Dni", "Nombre", "Apellido\t", "Edad", "Id Empleado", sep="\t| ", end="\n")
                Lista = Listar(ListaEmpleado, "Empleado")
                ListarEmpleado = Lista.ListarPersona()
                #Validar que sea una opcion correcta
                try:
                    opcion = int(input("1. Regresar \n2. Salir \n"))
                    if opcion == 1:
                        log.debug(f"La opcion {opcion} en valida")
                        OpcionMenuEmpleado = True
                        OpcionEmpleado = False
                    elif opcion == 2:
                        log.debug("Eligio salir del sistema")
                        Salir()
                    else:
                        log.debug("Opcion no valida salir del sistema")
                        print("Ingresó una opcion no valida\a")
                        Salir()
                except Exception as e:
                    log.info(f"Eligio una opcion invalida y salió del sistema. {e}")
                    print("Ingresó una opcion no valida\a")
                    Salir()
            elif MostrarMenuEmpleado == 3:
                #Nombre del archivo a crear
                fileProductos = utils.fileManager("Productos.txt")
                fileProductos.CrearArchivo()
                OpcionProducto = True
                while OpcionProducto:
                    #Verificar existencia del Producto por su Nombre
                    NombreProducto = input("Ingrese Nombre de Producto: ")   
                    ValidarProducto = SearchProducto(NombreProducto)
                    ExistenciaProducto = ValidarProducto.ExistenciaProducto()
                    ListaProducto = Listaproductos()
                    #Autoincrementar el ID
                    Auto_ID = AutoID(ListaProducto)
                    IdProducto = Auto_ID.IdProducto()
                    log.debug(ExistenciaProducto)                
                    TuplaValidaProducto = ("1. Ingresar Nuevamente", "2. Listar Producto", "9. Regresar")
                    MenuValidaProducto = Menu("MENU DATOS PRODUCTOS", TuplaValidaProducto)
                    #Valida existencia del Producto
                    if ExistenciaProducto == "Existe":
                        sleep(2)
                        #Si existe muestra al menu de datos Producto
                        MostrarMenuValidaProducto = MenuValidaProducto.MostrarMenu()
                        if MostrarMenuValidaProducto == 1:
                            OpcionProducto = True
                        elif MostrarMenuValidaProducto == 2:
                            fileProductos = utils.fileManager("Productos.txt")
                            fileProductos.CrearArchivo()
                            ListaProducto = Listaproductos()
                            #Header para la lista de Clientes
                            print("Producto", "Precio Unidad", "Stock", "Precio Total", "Id Producto", sep="\t| ", end="\n")
                            ListaProductos = Listar(ListaProducto, "Producto")
                            ListarProductos = ListaProductos.ListarProducto()
                            #Validar que sea una opcion correcta
                            try:
                                opcion = int(input("1. Comprar \n9. Regresar \n0. Salir \n"))
                                #Opcion para comprar Productos
                                if opcion == 1:
                                    log.debug(f"La opcion {opcion} en valida")
                                    fileProductos = utils.fileManager("Productos.txt")
                                    fileProductos.CrearArchivo()
                                    ListaProducto = Listaproductos()
                                    #Header para la lista de Clientes
                                    print("Producto", "Precio Unidad", "Stock", "Precio Total", "Id Producto", sep="\t| ", end="\n")
                                    ListaProductos = Listar(ListaProducto, "Producto")
                                    ListarProductos = ListaProductos.ListarProducto()
                                    Prod = input("Escriba el nombre del producto que desea comprar: ")
                                    #Cambiar Stock de los productos comprados
                                    for DicProd in ListaProducto:
                                        if (DicProd['NombreProducto'] == Prod):
                                            StockProd = DicProd['Stock']
                                            CantProd = int(input(f"Cuantos {Prod} desea comprar.\nStock Distonible: {StockProd} \n"))
                                            NuevoStock = StockProd - CantProd
                                            DicProd['Stock'] = NuevoStock
                                            NuevoPrecio = NuevoStock * DicProd['PrecioUnidad']
                                            DicProd['PrecioTotal'] = NuevoPrecio
                                            print(f"Usted a comprado {CantProd} {Prod}s")
                                            sleep(3)
                                    JsonInsert = json.dumps(ListaProducto)
                                    fileProductos.escribirArchivo(JsonInsert)
                                elif opcion == 9:
                                    log.debug(f"La opcion {opcion} en valida")
                                    OpcionMenuCliente = True
                                elif opcion == 0:
                                    log.debug("Eligio salir del sistema")
                                    Salir()
                                else:
                                    log.debug("Opcion no valida salir del sistema")
                                    print("Ingresó una opcion no valida\a")
                                    Salir()
                            except Exception as e:
                                log.info(f"Eligio una opcion invalida y salió del sistema. {e}")
                                print("Ingresó una opcion no valida\a")
                                Salir()
                        elif MostrarMenuValidaProducto == 9:
                            print("Eligió regresar al menú del Empleado")
                            OpcionProducto = False
                            OpcionMenuProducto = True
                            sleep(2)
                        else:
                            Salir()                        
                    else:
                        #Sigue agregando al Producto
                        PrecioUnidad = float(input(f"Ingrese el precio del producto {NombreProducto}: "))
                        Stock = int(input(f"Ingrese el stock disponible del producto {NombreProducto}: "))
                        PrecioTotal = PrecioUnidad * Stock
                        producto = Producto(NombreProducto, PrecioUnidad, Stock, PrecioTotal, IdProducto)
                        print(f"Se agrego al Producto {NombreProducto}")
                        log.debug(f"Se agrego al Producto {NombreProducto}")
                        #Agregar a la lista el nuevo Producto
                        ListaProducto.append(producto.DiccionarioProducto())
                        #Guardamos en el archivo a todos los Producto
                        JsonInsert = json.dumps(ListaProducto)
                        fileProductos.escribirArchivo(JsonInsert)
                        OpcionProducto = False
                        sleep(2)

            #Volver al menu principal
            elif MostrarMenuEmpleado == 9:
                OpcionMenuPrincipal = True
                OpcionMenuEmpleado = False
                OpcionEmpleado = False
            else:
                log.debug("Salir del Sistema")
                print("Eligió salir del sistema")
                Salir()

    elif MostrarMenuPrincipal == 2:
        OpcionMenuCliente = True
        while OpcionMenuCliente:
            #Mostrar el menu Cliente
            TuplaMenuCliente = ("1. Agregar Cliente", "2. Listar Cliente", "3. Listar Productos", "9. Regresar")
            MenuCliente = Menu("MENU CLIENTE\t", TuplaMenuCliente)
            MostrarMenuCliente = MenuCliente.MostrarMenu()
            #Nombre del archivo a crear
            fileCliente = utils.fileManager("Clientes.txt")
            fileCliente.CrearArchivo()
            #Agregar los datos a una lista
            ListaCliente = Listacliente()
            #Verificar que opcion se eligio
            if MostrarMenuCliente == 1:
                OpcionCliente = True
                while OpcionCliente:
                    #Verificar existencia del Cliente por su DNI
                    Dni = input("Ingrese DNI: ")
                    ValidarCliente = SearchCliente(Dni)
                    ExistenciaCliente = ValidarCliente.ExistenciaCliente()
                    #Autoincrementar el ID
                    Auto_ID = AutoID(ListaCliente)
                    IdCliente = Auto_ID.IdCliente()
                    log.debug(ExistenciaCliente)                
                    TuplaValidaCliente = ("1. Ingresar Nuevamente", "2. Listar Clientes", "9. Regresar")
                    MenuValidaCliente = Menu("MENU DATOS CLIENTE", TuplaValidaCliente)
                    #Valida existencia del Cliente
                    if ExistenciaCliente == "Existe":
                        sleep(2)
                        #Si existe muestra al menu de datos cliente
                        MostrarMenuValidaCliente = MenuValidaCliente.MostrarMenu()
                        if MostrarMenuValidaCliente == 1:
                            OpcionCliente = True
                        elif MostrarMenuValidaCliente == 2:
                            #Header para la lista de Clientes
                            print("Dni", "Nombre", "Apellido\t", "Edad", "Id Cliente", sep="\t| ", end="\n")
                            Lista = Listar(ListaCliente, "Cliente")
                            ListarCliente = Lista.ListarPersona()
                            #Validar que sea una opcion correcta
                            try:
                                opcion = int(input("1. Regresar \n2. Salir \n"))
                                if opcion == 1:
                                    log.debug(f"La opcion {opcion} en valida")
                                    OpcionMenuCliente = True
                                    OpcionCliente = False
                                elif opcion == 2:
                                    log.debug("Eligio salir del sistema")
                                    Salir()
                                else:
                                    log.debug("Opcion no valida salir del sistema")
                                    print("Ingresó una opcion no valida\a")
                                    Salir()
                            except Exception as e:
                                log.info(f"Eligio una opcion invalida y salió del sistema. {e}")
                                print("Ingresó una opcion no valida\a")
                                Salir()
                        elif MostrarMenuValidaCliente == 9:
                            print("Eligió regresar al menú del cliente")
                            OpcionCliente = False
                            OpcionMenuCliente = True
                            sleep(2)
                        else:
                            Salir()                        
                    else:
                        #Sigue agregando al clientes
                        Nombre = input("Ingrese el Nombre: ")
                        Apellido = input("Ingrese los Apellidos: ")
                        Edad = input("Ingrese su Edad: ")                    
                        cliente = Cliente(Dni, Nombre, Apellido, Edad, IdCliente)
                        print(f"Se agrego al cliente {Nombre} {Apellido}")
                        log.debug(f"Se agrego al cliente {Nombre} {Apellido}")
                        #Agregar a la lista el nuevo Cliente
                        ListaCliente.append(cliente.DiccionarioCliente())
                        #Guardamos en el archivo a todos los Clientes
                        JsonInsert = json.dumps(ListaCliente)
                        fileCliente.escribirArchivo(JsonInsert)
                        OpcionCliente = False
                        sleep(2)
            elif MostrarMenuCliente == 2:
                #Header para la lista de Clientes
                print("Dni", "Nombre", "Apellido\t", "Edad", "Id Cliente", sep="\t| ", end="\n")
                Lista = Listar(ListaCliente, "Cliente")
                ListarCliente = Lista.ListarPersona()
                #Validar que sea una opcion correcta
                try:
                    opcion = int(input("1. Regresar \n2. Salir \n"))
                    if opcion == 1:
                        log.debug(f"La opcion {opcion} en valida")
                        OpcionMenuCliente = True
                        OpcionCliente = False
                    elif opcion == 2:
                        log.debug("Eligio salir del sistema")
                        Salir()
                    else:
                        log.debug("Opcion no valida salir del sistema")
                        print("Ingresó una opcion no valida\a")
                        Salir()
                except Exception as e:
                    log.info(f"Eligio una opcion invalida y salió del sistema. {e}")
                    print("Ingresó una opcion no valida\a")
                    Salir()
            elif MostrarMenuCliente == 3:
                fileProductos = utils.fileManager("Productos.txt")
                fileProductos.CrearArchivo()
                ListaProducto = Listaproductos()
                #Header para la lista de Clientes
                print("Producto", "Precio Unidad", "Stock", "Precio Total", "Id Producto", sep="\t| ", end="\n")
                ListaProductos = Listar(ListaProducto, "Producto")
                ListarProductos = ListaProductos.ListarProducto()
                #Validar que sea una opcion correcta
                try:
                    opcion = int(input("1. Comprar \n9. Regresar \n0. Salir \n"))
                    #Opcion para comprar Productos
                    if opcion == 1:
                        log.debug(f"La opcion {opcion} en valida")
                        fileProductos = utils.fileManager("Productos.txt")
                        fileProductos.CrearArchivo()
                        ListaProducto = Listaproductos()
                        #Header para la lista de Clientes
                        print("Producto", "Precio Unidad", "Stock", "Precio Total", "Id Producto", sep="\t| ", end="\n")
                        ListaProductos = Listar(ListaProducto, "Producto")
                        ListarProductos = ListaProductos.ListarProducto()
                        Prod = input("Escriba el nombre del producto que desea comprar: ")
                        #Cambiar Stock de los productos comprados
                        for DicProd in ListaProducto:
                            if (DicProd['NombreProducto'] == Prod):
                                StockProd = DicProd['Stock']
                                CantProd = int(input(f"Cuantos {Prod} desea comprar.\nStock Distonible: {StockProd} \n"))
                                NuevoStock = StockProd - CantProd
                                DicProd['Stock'] = NuevoStock
                                NuevoPrecio = NuevoStock * DicProd['PrecioUnidad']
                                DicProd['PrecioTotal'] = NuevoPrecio
                                print(f"Usted a comprado {CantProd} {Prod}s")
                                sleep(3)
                        JsonInsert = json.dumps(ListaProducto)
                        fileProductos.escribirArchivo(JsonInsert)
                        OpcionMenuCliente = True
                    elif opcion == 9:
                        log.debug(f"La opcion {opcion} en valida")
                        OpcionMenuCliente = True
                    elif opcion == 0:
                        log.debug("Eligio salir del sistema")
                        Salir()
                    else:
                        log.debug("Opcion no valida salir del sistema")
                        print("Ingresó una opcion no valida\a")
                        Salir()
                except Exception as e:
                    log.info(f"Eligio una opcion invalida y salió del sistema. {e}")
                    print("Ingresó una opcion no valida\a")
                    Salir()
            #Volver al menu principal
            elif MostrarMenuCliente == 9:
                OpcionMenuPrincipal = True
                OpcionMenuCliente = False
                OpcionCliente = False
            else:
                log.debug("Salir del Sistema")
                print("Eligió salir del sistema")
                Salir()
    else:
        Salir()