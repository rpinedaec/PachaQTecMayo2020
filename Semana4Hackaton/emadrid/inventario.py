import os
import utils
from time import sleep
import json


#Clase Color: Uso en los mensajes
class Color():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    CEND      = '\033[0;m'

#Clase Persona    
class Persona:
    __estado = True

    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevoEstado):
        __estado = nuevoEstado

    def registro(self):
        self.estado = True
        print("La Persona se ha registrado")

    def desresgistro(self):
        self.estado = False

#Clase Cliente HERENCIA Persona
class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente

    #def comprar(self):
    #    print("El Cliente esta comprando")
    #    print("El Cliente terminó de comprar")
    def dictCliente(self):
        dc = {
             'dni': self.dni,
             'nombre': self.nombre,
             'apellido': self.apellido,
             'edad': self.edad,       
             'codCliente': self.codCliente    
        }
        return dc
    

#Clase Empleado HERENCIA Persona
class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")
    
    def dictEmpleado(self):
        de = {
             'dni': self.dni,
             'nombre': self.nombre,
             'apellido': self.apellido,
             'edad': self.edad,       
             'codEmpleado': self.codEmpleado    
        }
        return de
#Clase Producto
class Producto:
    log = utils.log("Producto")

    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto
        self.log.info("Se creo un producto")

   # def __str__(self):
       # return """Codigo: {} \nNombre: {}""".format(self.codProducto, self.nombreProducto)

    def dictProducto(self):
        dp = {
            'codProducto': self.codProducto,
            'nombreProducto': self.nombreProducto,
            'cantidadProducto': self.cantidadProducto,
            'costoProducto': self.costoProducto
        }
        return dp

    

    #def costearProducto(self):
    #    print("Costeando producto")
    #    print("Producto costeado")
#Buscar Cliente
def buscarCliente(fileClient, client):
    try: 
        f = open(fileClient, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + fileClient + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = list([(line.split(',')) for line in directory])
        if client in directory:
            return directory[client]
        else:
            return('¡El cliente ' + client + ' no existe!\n')

#Buscar Empleado
def buscarEmpleador(fileEmplead, emplead):
    try: 
        f = open(fileEmplead, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + fileEmplead + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = list([(line.split(',')) for line in directory])
        if emplead in directory:
            return directory[emplead]
        else:
            return('¡El cliente ' + emplead + ' no existe!\n')
#Buscar Producto
def buscarProducto(fileProduct, product):
    try: 
        f = open(fileProduct, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + fileProduct + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = list([(line.split(',')) for line in directory])
        if product in directory:
            return directory[product]
        else:
            return('¡El cliente ' + product + ' no existe!\n')

#Eliminar Producto
def eliminarProducto(fileProduct, product):

    try: 
        f = open(fileProduct, 'r')
    except FileNotFoundError:
        return('¡El Producto ' + fileProduct + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = list([(line.split(',')) for line in directory])
        if product in directory:
            del directory[product]
            for codProducto, nomProducto in directory:
                f.write(codProducto + ',' + nomProducto)
            f.close()
            return ('¡El Producto se ha borrado!\n')
        else:
            return('¡El Producto ' + product + ' no existe!\n')

#Clase Menu
class Menu:
    __log = utils.log("Menu")

    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        while(opSalir):
            self.limpiarPantalla()
            print(Color.BLUE+":::::::::::::BIENVENIDOS EMPRESA ESMR::::::::::::::"+Color.CEND)
            print(Color.BLUE+":::::::::::::::::::" +self.nombreMenu + "::::::::::::::::::"+Color.CEND)
            
            for (key, value) in self.listaOpciones.items():
                print(key, "\t:: ", value)
            #print("Salir \t\t::  9")
            opcion = 100
            try:
                print(Color.CYAN+"Escoge tu opcion"+Color.CEND)
                opcion = int(input())
            except ValueError as error:
                self.__log.error(error)
                print(Color.RED+"Opcion invalida deben ser numeros del 0 al 2"+Color.CEND)
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                   contOpciones += 1
            if(contOpciones == 0):
                print(Color.RED+"Escoge una opcion valida"+Color.CEND)
                self.__log.debug("No escoje opion")
                sleep(3)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
            #return os.system('cls')
            return os.system('clear')
        clear()

#Variables Globales
log = utils.log("INIT")
#Variables Productos
fileProducto = utils.fileManager("Productos.txt")
fileProduct = 'Productos.txt'
lstProductos = []
lstProductosDic = []

#Variables Clientes
fileCliente = utils.fileManager("Clientes.txt")
fileClient = 'Clientes.txt'
lstClientes = []
lstClientesDic = []

#Variables Empleados
fileEmpleados = utils.fileManager("Empleados.txt")
fileEmplead = 'Empleados.txt'
lstEmpleados = []
lstEmpleadosDic = []
#FIN Variables Globales

#Funcion Carga Inicia: Realiza La carga de datos de Productos, Clientes y Empleados
def cargaInicial():
    try:
        res = fileProducto.leerArchivo()
        log.debug(res)
        lstProducto = json.loads(res)
        for dicProducto in lstProducto:
            #codProducto, nombreProducto, cantidadProducto, costoProducto
            objProducto = Producto(dicProducto["codProducto"], dicProducto["nombreProducto"],
                                dicProducto["cantidadProducto"], dicProducto["costoProducto"])
            lstProductos.append(objProducto)
            lstProductosDic.append(dicProducto)
        log.debug(lstProductosDic)
        log.debug(lstProductos)
    except Exception as error:
        log.error(error)
    
    #Try/Carga Cliente
    try:
        resc = fileCliente.leerArchivo()
        log.debug(resc)
        lstCliente = json.loads(resc)
        for dictCliente in lstCliente:
            #dni, nombre, apellido, edad, codCliente
            objCliente = Cliente(dictCliente["dni"],
                                dictCliente["nombre"], dictCliente["apellido"],
                                dictCliente["edad"],dictCliente["codCliente"])
            lstClientes.append(objCliente)
            lstClientesDic.append(dictCliente)
        log.debug(lstClientesDic)
        log.debug(lstClientes)
    except Exception as error:
        log.error(error)
    #FIN Try/Carga Cliente



cargaInicial()

#Menu de Opciones Principal 
dicOpcionesMenuPrincipal = {"Cliente": 1, "Producto": 2, "Empleado": 3, "Salir \t": 0}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()

#Opciones de Crear Producto
dicOpcionesCrearProducto = {"Crear otro Producto": 1, "Mostrar todos los Productos": 2}
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)

#Opciones de Crear Cliente
dicOpcionesCrearCliente = {"Crear otro Cliente": 1, "Mostrar todos los Clientes": 2}
submenuCliente = Menu("Menu X Cliente", dicOpcionesCrearCliente)

#Opciones de Crear Empleado
dicOpcionesCrearEmpleado = {"Crear otro Empleado": 1, "Mostrar todos los Empleado": 2}
submenuEmpleado = Menu("Menu X Empleado", dicOpcionesCrearEmpleado)

if(opcionMenuPrincipal == 0):
    #opcionMenuPrincipal = menuPrincipal.mostrarMenu()
    print("Gracias, Uds salio del sistema")
#Opciones Menu Cliente
elif(opcionMenuPrincipal == 1):
    dicOpcionesCliente = {"Registrar Cliente": 1, "Listar Cliente \t": 2, "Buscar Clientes": 3, "Salir": 4}
    menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
    resc = menuCliente.mostrarMenu()
    salirCreacionCliente = True
    while salirCreacionCliente:
        if(resc == 1):
            print("Digita el DNI del Cliente")
            dni = input()
            print("Digita Nombre del Cliente")
            nombre = input()
            print("Digita Apellido del Cliente")
            apellido = input()            
            print("Digita Edad del Cliente")
            edad = input()
            print("Digita el Codigo del Cliente")
            codCliente = input()
            cliente = Cliente(dni, nombre, apellido, edad,codCliente)
            
            print("Haz creado el Cliente: ", cliente)
            fileCliente.borrarArchivo()
            lstClientesDic.append(cliente.dictCliente())
            lstClientes.append(cliente)
            jsonStrcliente = json.dumps(lstClientesDic)
            fileCliente.escribirArchivo(jsonStrcliente)
            resMenuCliente = menuCliente.mostrarMenu()
            if(resMenuCliente == 1):
                log.debug("ingreso a la opcion 1 de menuCliente")
            elif(resMenuCliente == 2):
                log.debug("ingreso a la opcion 2 de menuCliente")
                for objCliente in lstClientes:
                    print(
                        f"|{objCliente.dni} | {objCliente.nombre} | {objCliente.apellido} | {objCliente.edad} | {objCliente.codCliente}|")
                sleep(1)
                resc = submenuCliente.mostrarMenu()
                if(resc == 2):
                    log.debug(f"ingreso a la opcion {resc}")
            else:
                log.debug(
                    f"ingreso a la opcion {resMenuCliente} de menuCliente")
                salirCreacionCliente = False
                break
        elif(resc == 2):
            print(f"|{'DNI':^16}|{'NOMBRE':^17}|{'APELLIDO':^17}|{'EDAD':^18}|{'COD CLIENTE':^18}|")
            for objCliente in lstClientes:
                    print(f"|{objCliente.dni:^15} | {objCliente.nombre:^15} | {objCliente.apellido:^15} | {objCliente.edad:^15} | {objCliente.codCliente:^15}|")
            sleep(1)
            resc = menuCliente.mostrarMenu()
        elif (resc == 3):
            print("Buscar ---->")
            name = input('Introduce el nombre del cliente: ')
            print(buscarCliente(fileClient, name))
            sleep(1) 
            resc = menuCliente.mostrarMenu()
                     
           # sleep(10)
           # res = menuEmpleado.mostrarMenu()
        elif (resc == 4):
             print(Color.GREEN+"Salio con Exito del Menu Cliente"+Color.CEND)
             sleep(1)
             resc = menuPrincipal.mostrarMenu()
             break             

#Opciones Menu Producto
elif(opcionMenuPrincipal == 2):
    dicOpcionesProducto = {"Registrar Productos": 1,"Listar Productos": 2, "Buscar Producto": 3, "Eliminar Producto": 4, "Inventario \t": 5, "Salir \t\t": 6}
    menuProducto = Menu("Menu de Producto", dicOpcionesProducto)
    res = menuProducto.mostrarMenu()
    salirCreacionProducto = True
    while salirCreacionProducto:
        if(res == 1):
            print("Digita el Codigo del Producto")
            codProducto = input()
            print("Digita el Nombre del Producto")
            nomProducto = input()
            print("Digita la Cantidad del Producto")
            cantProducto = input()
            print("Digita costo del Producto")
            costProducto = input()
            producto = Producto(codProducto, nomProducto,
                                cantProducto, costProducto)

            print("Haz creado el producto: ", producto)
            fileProducto.borrarArchivo()
            lstProductosDic.append(producto.dictProducto())
            lstProductos.append(producto)
            jsonStr = json.dumps(lstProductosDic)
            fileProducto.escribirArchivo(jsonStr)
            resMenuProducto = menuProducto.mostrarMenu()
            if(resMenuProducto == 1):
                log.debug("ingreso a la opcion 1 de menuProducto")
            elif(resMenuProducto == 2):
                log.debug("ingreso a la opcion 2 de menuProducto")
                for objProducto in lstProductos:
                    print(f"|{objProducto.nombreProducto} | {objProducto.codProducto} | {objProducto.cantidadProducto} | {objProducto.costoProducto} |")
                sleep(5)
                res = menuProducto.mostrarMenu()
                if(res == 1):
                    log.debug(f"ingreso a la opcion {res}")
            else:
                log.debug(
                    f"ingreso a la opcion {resMenuProducto} de menuProducto")
                salirCreacionProducto = False
                break
        elif(res==2):
            print(f"|{'COD PRODUCTO':^30}|{'NOMBRE':^30}|{'CANTIDAD':^30}|{'COSTO':^30}|")
            for objProducto in lstProductos:
                    print(f"|{objProducto.codProducto:^30} | {objProducto.nombreProducto:^30} | {objProducto.cantidadProducto:^30} | {objProducto.costoProducto:^30}|")
            sleep(4)
            res = menuProducto.mostrarMenu()
        elif (res==3):
            print("Buscar ---->")
            name = input('Introduce el nombre del Producto: ')
            print(buscarProducto(fileEmplead, name))
            sleep(2)
            res = menuPrincipal.mostrarMenu()         
        elif (res==4):
            print("Eliminar ---->")
            #print("Busca en la lista el producto que deseas quitar")
            #for objProducto in lstProductos:
            #    for (key, value) in objProducto.items():
            #        print(key , " :: ", value )
            print("Escribe el nombre del Producto que quieres Eliminar")
            strNombreEliminar = input()
            for objProducto in lstProductos:
                for (key, value) in objProducto.items():
                    if(value == strNombreEliminar):
                        print(f"Borrar {value}?")
                        lstProductos.remove(objProducto)
            print(lstProductos)

            sleep(5)
            res = menuProducto.mostrarMenu()
        elif (res==5):
            totalV = 0.0
            for p in lstProductos:
                totalV +=p.total
            print(" PRODUCTOS, TOTAL VALORIZADO: ",totalV)

        elif (res==6):
            pass
elif(opcionMenuPrincipal == 3):
    dicOpcionesEmpleado = {"Registrar Empleador": 1, "Listar Empelado": 2, "Buscar Empleado": 3, "Salir \t\t": 4}
    menuEmpleado = Menu("Menu de Empleador", dicOpcionesEmpleado)
    rese = menuEmpleado.mostrarMenu()
    salirCreacionEmpleado = True
    while salirCreacionEmpleado:
        if(rese == 1):
            print("Digita el DNI del Empleado")
            dni = input()
            print("Digita Nombre del Empleado")
            nombre = input()
            print("Digita Apellido del Empleado")
            apellido = input()            
            print("Digita Edad del Empleado")
            edad = input()
            print("Digita el Codigo del Empleado")
            codEmpleado = input()
            empleado = Empleado(dni, nombre, apellido, edad,codEmpleado)
            
            print("Haz creado el Empleado: ", empleado)
            fileEmpleados.borrarArchivo()
            lstEmpleadosDic.append(empleado.dictEmpleado())
            lstEmpleados.append(empleado)
            jsonStrcliente = json.dumps(lstEmpleadosDic)
            fileEmpleados.escribirArchivo(jsonStrcliente)
            resMenuEmpleado = menuEmpleado.mostrarMenu()
            if(resMenuEmpleado == 1):
                log.debug("ingreso a la opcion 1 de menuEmpleado")
            elif(resMenuEmpleado == 2):
                log.debug("ingreso a la opcion 2 de menuEmpleado")
                for objEmpleado in lstEmpleados:
                    print(
                        f"|{objEmpleado.dni} | {objEmpleado.nombre} | {objEmpleado.apellido} | {objEmpleado.edad} | {objEmpleado.codEmpleado}|")
                sleep(2)
                rese = submenuEmpleado.mostrarMenu()
                if(rese == 2):
                    log.debug(f"ingreso a la opcion {resc}")
            else:
                log.debug(
                    f"ingreso a la opcion {resMenuEmpleado} de menuEmpleado")
                salirCreacionCliente = False
                break
        elif(rese == 2):
            print(f"|{'DNI':^16}|{'NOMBRE':^17}|{'APELLIDO':^17}|{'EDAD':^18}|{'COD EMPLEADO':^18}|")
            for objEmpleado in lstEmpleados:
                    print(f"|{objEmpleado.dni:^15} | {objEmpleado.nombre:^15} | {objEmpleado.apellido:^15} | {objEmpleado.edad:^15} | {objEmpleado.codCliente:^15}|")
            sleep(5)
            rese = menuEmpleado.mostrarMenu()
        elif (rese == 3):
            print("Buscar ---->")
            name = input('Introduce el nombre del Empleado: ')
            print(buscarEmpleador(fileEmplead, name))
            sleep(2)          
           # sleep(10)
           # res = menuEmpleado.mostrarMenu()
        elif (rese == 4):
             print(Color.GREEN+"Salio con Exito"+Color.CEND)
             break             
    
        
