import os
import utils
from time import sleep
import json


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


class Cliente(Persona):
    log = utils.log("Cliente")
    
    def __init__(self, dni, nombre, apellido, edad, usuaCliente, passwCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.usuaCliente = usuaCliente
        self.passwCliente = passwCliente
        self.log.info("Se añadio Cliente")
    
    def dictCliente(self):
        c = {
            'dniCliente' : self.dni,
            'nombreCliente' : self.nombre,
            'apellCliente' : self.apellido,
            'edadCliente' : self.edad,
            'usuaCliente' : self.usuaCliente,
            'passwCliente' : self.passwCliente
        }
        return c 
    

    def comprar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado, puestoEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado
        self.puestoEmpleado = puestoEmpleado

    def dictEmpleado(self):
        e = {
            'dniEmpleado' : self.dni,
            'nombreEmpleado' : self.nombre,
            'apellEmpleado' : self.apellido,
            'edadEmpleado' : self.edad,
            'codEmpleado' : self.codEmpleado,
            'puestoEmpleado' : self.puestoEmpleado
        }
        return e 
    
    def __str__(self):
        return """Codigo: {}""".format(self.codEmpleado)

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")
    
    def marcarsalida(self):
        print("El empleado esta marcando su salida")
        print("El empleado marco su salida")


class Producto:
    log = utils.log("Producto")

    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto
        self.log.info("Se creo un producto")

    def __str__(self):
        return """Codigo: {} \nNombre: {}""".format(self.codProducto, self.nombreProducto)

    def dictProducto(self):
        d = {
            'codProducto': self.codProducto,
            'nombreProducto': self.nombreProducto,
            'cantidadProducto': self.cantidadProducto,
            'costoProducto': self.costoProducto
        }
        return d

    def contarProducto(self):
        for p in lstProductos:
            print(p['nombreProducto'])
        print("Hay "+str(len(lstProductos))+ " productos") 

    def valorizarProducto(self):
        fltTotal=0.0
        for p in lstProductos:
            fltProd=p['costoProducto']*p['cantidadProducto']
            fltTotal+=fltProd
        print("S/."+str(fltTotal)+ " Soles")


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
            print("\033[1;34m" +
                  ":::::::::::::TIENDA PERU::::::::::::::"+'\033[0;m')
            print("\033[1;34m"+":::::::::::::" +
                  self.nombreMenu + "::::::::::::::"+'\033[0;m')
            for (key, value) in self.listaOpciones.items():
                print(key, " :: ", value)
            print("Salir :: 9")
            opcion = 100
            try:
                print("Escoge tu opcion")
                opcion = int(input())
            except ValueError as error:
                self.__log.error(error)
                print("Opcion invalida deben ser numeros de 0 - 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                   contOpciones += 1
            if(contOpciones == 0):
                print("Escoge una opcion valida")
                self.__log.debug("No escoje opcion")
                sleep(5)
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
fileProducto = utils.fileManager("Productos.txt")
agendaCliente = utils.fileManager("Clientes.txt")
lstProductos = []
lstProductosDic = []
lstClientes = []
lstClientes_Dict=[]

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
    except Exception as erro:
        log.error(erro)


cargaInicial()

dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()


dicOpcionesCrearProducto = {"Crear otro": 1, "Mostrar todos": 2}
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)


if(opcionMenuPrincipal == 9):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

elif(opcionMenuPrincipal == 1):
    
    dniCliente = int(input("DNI del Cliente: "))
    nombreCliente = input("Nombre del Cliente: ")
    apellCliente = input("Apellido del Cliente: ")
    edadCliente = int(input ("Edad del Cliente: "))
    usuaCliente = input("Usuario del Cliente: ")
    passwCliente = input("Password del Cliente: ")
    cliente = Cliente(dniCliente, nombreCliente, apellCliente, edadCliente, usuaCliente, passwCliente)
    lstClientes.append(cliente)
    print("acceso valido para cliente: ", cliente) 
    dicOpcionesCliente = {"Comprar": 1, "Devolver": 2}
    menuCliente = Menu(f"{cliente}", dicOpcionesCliente)
    agendaCliente.borrarArchivo()
    lstClientes_Dict.append(cliente.dictCliente())
    jsonStr = json.dumps(lstClientes_Dict)
    agendaCliente.escribirArchivo(jsonStr)
    res = menuCliente.mostrarMenu()
    if (res == 1):
        cliente.comprar()

elif(opcionMenuPrincipal == 2):
    dniEmpleado = int(input("DNI del Empleado: "))
    nombreEmpleado = input("Nombre del Empleado: ")
    apellEmpleado = input("Apellido del Empleado: ")
    edadEmpleado = int(input ("Edad del Empleado: "))
    codEmpleado = int(input("Codigo del Empleado: "))
    puestoEmpleado = input("Password del Empleado: ")
    empleado = Empleado(dniEmpleado, nombreEmpleado, apellEmpleado, edadEmpleado, codEmpleado, puestoEmpleado)
    print("acceso valido para empleado: ", empleado)
    dicOpcionesEmpleado = {"Marcar Ingreso": 1,
                           "Marcar Salida": 2, "Cargar Inventario": 3, "Contar Inventario":4, "Valorizar Inventario":5}
    menuEmpleado = Menu(f"{empleado}", dicOpcionesEmpleado)
    res = menuEmpleado.mostrarMenu()
    salirCreacionProducto = True
    while salirCreacionProducto:
        if (res == 1):
            empleado.marcarIngreso()
            input()
            res = menuEmpleado.mostrarMenu()
            
        elif (res == 2):
            empleado.marcarsalida()
            input()
            res = menuEmpleado.mostrarMenu()
        elif(res == 3):
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
                    print(
                        f"|{objProducto.nombreProducto} | {objProducto.codProducto} | {objProducto.cantidadProducto} | {objProducto.costoProducto} |")
                sleep(10)
                res = menuEmpleado.mostrarMenu()
                if(res == 1):
                    log.debug(f"ingreso a la opcion {res}")
            else:
                log.debug(
                    f"ingreso a la opcion {resMenuProducto} de menuProducto")
                salirCreacionProducto = False
                break
        elif(res == 4):
            for p in lstProductosDic:
                print(p['nombreProducto'])
            print("Hay "+str(len(lstProductosDic))+ " productos") 
            input()
            res = menuEmpleado.mostrarMenu()
        
        elif(res == 5):
            fltTotal=0.0
            for p in lstProductosDic:
                fltProd=float(p['costoProducto'])*float(p['cantidadProducto'])
                fltTotal+=fltProd
            print("S/."+str(fltTotal)+ " Soles")
            input()
            res = menuEmpleado.mostrarMenu()