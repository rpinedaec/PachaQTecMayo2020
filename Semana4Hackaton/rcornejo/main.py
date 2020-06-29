#Hackaton 4: Programa de inventario
#Alumno: Ricardo Cornejo

import os
import utils
from time import sleep
#import json 

#Creación de clases
class Persona:
    __estado = True
    #Constructor
    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #Sacar info variable privada
    @property
    def estado(self):
        return self.__estado
    #Cambiar info variable privada
    @estado.setter
    def estado(self, nuevoEstado):
        __estado = nuevoEstado

    def registro(self):
        self.estado = True
        print("La Persona se ha registrado")

    def desresgistro(self):
        self.estado = False


class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, edad, codCliente): #Constructor
        super().__init__(dni, nombre, apellido, edad) #herencia de clase persona
        self.codCliente = codCliente

    def comprar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado): #constructor de la clase
        super().__init__(dni, nombre, apellido, edad)#Herencia clase persona
        self.codEmpleado = codEmpleado

    def marcarIngreso(self):
        print("El empleado está marcando su ingreso")
        print("El empleado marcó su ingreso")
        
    def marcarSalida(self):
        print("El empleado está marcando su salida")
        print("El empleado marcó su salida")
        
    
class Producto:
    log = utils.log("Producto")

    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto
        self.log.info("¡Se creó un producto!")

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

    def costearProducto(self):
        print("Costeando producto")
        print("Producto costeado")


class Menu: #Esta clase es para no volver a hacer varias veces el menu.
    __log = utils.log("Menu")

    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        
        
        while(opSalir):
            self.limpiarPantalla()
            print("\033[3;34;47m"+
                  "::::::::::::::::::EMPRESA PACHAQTEC:::::::::::::::::"+'\033[0;m')
            print("\033[1;34m"+":::::::::::::::::::" +
                  self.nombreMenu + ":::::::::::::::::::"+'\033[0;m') 
            
            for (key, value) in self.listaOpciones.items():
                print(key, " \t: ", value)
            print("\033[1;34m"+"...................................................."+'\033[0;m')
            print("- Salir:  9")
            print("\033[1;34m"+"...................................................."+'\033[0;m')
            opcion = 100
             
                               
            try:
                print ("- Digita tu opción aquí abajo:")
                opcion = int(input())
            except ValueError as error:
                self.__log.error(error)
                print("Opción invalida, deben ser numeros del 0 al 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value) or opcion == 9):
                   contOpciones += 1
            if(contOpciones == 0):
                print("Digite una opción válida")
                self.__log.debug("No escoge opción")
                sleep(5)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
            return os.system('cls')
            #return os.system('clear')
        clear()



#Variables Globales
log = utils.log("INIT")
fileProducto = utils.fileManager("Productos.txt")
lstProductos = []
lstProductosDic = []


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

def delProducto():
    try:
        res = fileProducto.leerArchivo()
        log.debug(res)
        lstProducto = json.loads(res)
        for dicProducto in lstProducto:
            #codProducto, nombreProducto, cantidadProducto, costoProducto
            objProducto = Producto(dicProducto["codProducto"], dicProducto["nombreProducto"],
                                dicProducto["cantidadProducto"], dicProducto["costoProducto"])
            lstProductos.remove(objProducto)
            lstProductosDic.remove(dicProducto)
        log.debug(lstProductosDic)
        log.debug(lstProductos)
    except Exception as erro:
        log.error(erro)
        
cargaInicial() 
#Aquí está el menu de inicio.
dicOpcionesMenuPrincipal = {"\t- Cliente": 1, "\t- Empleado": 2}
menuPrincipal = Menu("Menu Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()

delProducto()

#Menu productos
dicOpcionesCrearProducto = {"\t- Crear otro": 1, "\t- Mostrar todos": 2}
menuProducto = Menu("Menu de Productos", dicOpcionesCrearProducto)


if(opcionMenuPrincipal == 9):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

elif(opcionMenuPrincipal == 1):#Menu cliente
    dicOpcionesCliente = {"\t- Comprar": 1, "\t- Devolver": 2}
    menuCliente = Menu("Menu Cliente", dicOpcionesCliente)
    res = menuCliente.mostrarMenu()
    
    
elif(opcionMenuPrincipal == 2): #Menu empleado
    dicOpcionesEmpleado = {"\t- Marcar ingreso": 1,
                           "\t- Marcar salida": 2, "\t- Cargar inventario": 3, "\t- Eliminar producto": 4, "\t- Ver productos": 5}
    menuEmpleado = Menu("Menu Empleado", dicOpcionesEmpleado)
    res = menuEmpleado.mostrarMenu()
    
    salirCreacionProducto = True #Creación de producto
    while salirCreacionProducto: 
        if(res == 3):
            print("\033[1;34m"+"...................................................."+'\033[0;m')
            print("Digita el código del producto:")
            codProducto = input()
            print("\033[1;34m"+"...................................................."+'\033[0;m')
            print("Digita el nombre del producto:")
            nomProducto = input()
            print("\033[1;34m"+"...................................................."+'\033[0;m')
            print("Digita el stock del producto:")
            cantProducto = input()
            print("\033[1;34m"+"...................................................."+'\033[0;m')
            print("Digita el precio del producto:")
            costProducto = input()
            
            producto = Producto(codProducto, nomProducto, cantProducto, costProducto)

            print("Haz creado el producto: ", producto)
            fileProducto.borrarArchivo()
            lstProductosDic.append(producto. dictProducto())
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
