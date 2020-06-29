import os
import utils
from time import sleep


class Persona:
    __estado = True

    def __init__(self,idPersona, dni, nombre, apellido, edad):
        self.idPersona = idPersona
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




class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado
    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")



class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente
    def compar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")




class Producto:
    log = utils.log("Producto")
    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto
        # self.unidadMedida = unidadMedida
        self.log.info("Se creo un producto")
    def __str__(self):
        return """Codigo: {} \nNombre: {}""".format(self.codProducto, self.nombreProducto)

    def costearProducto(self):
        print("Costeando producto")
        print("Producto costeado")

class Menu:
    log = utils.log("Menu")

    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        while(opSalir):
            self.limpiarPantalla()
            print("\033[1;34m" +
                  ":::::::::::::EMPRESA PACHAQTEC::::::::::::::"+'\033[0;m')
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
                self.log.error(error)
                print("Opcion invalida deben ser numeros de 0 - 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                   contOpciones += 1
            if(contOpciones == 0):
                print("Escoge una opcion valida")
                self.log.debug("No escoje opion")
                sleep(5)
            else:
                opSalir = False
        return opcion

    def limpiarPantalla(self):
        def clear():
            #return os.system('cls')
            return os.system('clear')
        clear()


log = utils.log("INIT")


dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()
lstProductos = []

dicOpcionesCrearProducto = {"Crear otro": 1, "Mostrar todos": 2}
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)

fileProducto = utils.fileManager("Productos")


if(opcionMenuPrincipal == 9):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

elif(opcionMenuPrincipal == 1):
    dicOpcionesCliente = {"Comprar": 1, "Devolver": 2}
    menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
    res = menuCliente.mostrarMenu()
    if(res == 1):
        log.info("escogio la opcion 1")
    if(res == 9):
        log.info("escogio la opcion de salir")

elif(opcionMenuPrincipal == 2):
    dicOpcionesEmpleado = {"Marcar Ingreso": 1,
                           "Marcar Salida": 2, "Cargar Inventario": 3}
    menuEmpleado = Menu("Menu del Empleado", dicOpcionesEmpleado)
    res = menuEmpleado.mostrarMenu()
    salirCreacionProducto = True
    while salirCreacionProducto:
        if(res == 3):
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
            lstProductos.append(producto.__init__)
            fileProducto.escribirArchivo(producto.nombreProducto)
            lstProductos.append(producto)
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
