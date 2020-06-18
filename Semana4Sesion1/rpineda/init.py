import os
import utils
from time import sleep

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
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente

    def compar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")


class Producto:
    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto

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
            #print(f"Empresa Roberto \n {self.nombreMenu}")
            self.log.debug('Esto es un debug')
            for (key, value) in self.listaOpciones.items():
                print(key, " :: ", value)
                self.log.debug(f"{key}, {value}")
            print("Salir :: 9")
            opcion = 100 
            try:
                print("Escoge tu opcion")
                opcion = int(input())
            except ValueError:
                print("Opcion invalida deben ser numeros de 0 - 9")
            
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                    opSalir = False
                    break
                elif(opcion != int(value)):
                    if(opcion == 9):
                        opSalir = False
                        break
                    else:
                       print("Escoge una opcion valida")
                       sleep(5)  
                       break
        
        return opcion

    def limpiarPantalla(self):
        def clear(): return os.system('cls')
        #clear = lambda: os.system('clear')
        clear()


dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()
lstProductos = []


if(opcionMenuPrincipal == 9):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()    

elif(opcionMenuPrincipal == 1):
    dicOpcionesCliente = {"Comprar": 1, "Devolver": 2}
    menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
    res = menuCliente.mostrarMenu()
    print(res)
elif(opcionMenuPrincipal == 2):
    dicOpcionesEmpleado = {"Marcar Ingreso": 1, "Marcar Salida":2, "Cargar Inventario":3}
    menuEmpleado = Menu("Menu del Empleado", dicOpcionesEmpleado)
    res = menuEmpleado.mostrarMenu()
    print(res)
    if(res == 3):
        print("Digita el Codigo del Producto")
        codProducto = input()
        print("Digita el Nombre del Producto")
        nomProducto = input()
        print("Digita la Cantidad del Producto")
        cantProducto = input()
        print("Digita costo del Producto")
        costProducto = input()
        producto = Producto(codProducto,nomProducto,cantProducto,costProducto)
        lstProductos.append(producto)
        print(lstProductos)



# 
# 
# 

# menuPrincipal.mostrarMenu()

# # opcionMenuPrincipal = input("Seleccione una opcion \n")
# # if(opcionMenuPrincipal == "1"):
# #     print("bienvenido cliente")
# # elif(opcionMenuPrincipal == "2"):
# #     print("bienvenido Empleado")
# # else:
# #     print("Deseas Salir ?? ")
