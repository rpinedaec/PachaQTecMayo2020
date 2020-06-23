import os
import utils
from time import sleep

class Persona:
    __estado = True
    def __init__(self, codigo, dni, nombre, apellido, edad):
        self.codigo = codigo
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
    def __init__(self, codigo, dni, nombre, apellido, edad, codCliente):
        super().__init__(codigo, dni, nombre, apellido, edad)
        self.codCliente = codCliente

    def dictCliente(self):
        d = {
            'codigo': self.codigo,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'codCliente': self.codCliente
        }
        return d
        
    def comprar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    def __init__(self, codigo, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(codigo, dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado

    def dictEmpleado(self):
        d = {
            'codigo': self.codigo,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'codEmpleado': self.codEmpleado
        }
        return d

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")

class UnidadMedidad:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    
    def dictUnidadMedida(self):
        d = {
            'codigo': self.codigo,
            'nombre': self.nombre
        }
        return d

class Producto:
    log = utils.log("Producto")

    def __init__(self, codigo, nombre, cantidadProducto, unidad, costoProducto, total):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidadProducto = cantidadProducto
        self.unidad = unidad
        self.costoProducto = costoProducto
        self.total = total
        self.log.info("Se creo un producto")

    def __str__(self):
        return """Codigo: {} \nNombre: {}""".format(self.codigo, self.nombre)

    def dictProducto(self):
        d = {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'cantidadProducto': self.cantidadProducto,
            'unidad': self.unidad,
            'costoProducto': self.costoProducto,
            'total': self.total
        }
        return d

    def costearProducto(self):
        print("Costeando producto")
        print("Producto costeado")


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
                  ":::::::::::::MARTIN PEREZ::::::::::::::"+'\033[0;m')
            print("\033[1;34m"+":::::::::::::" +
                  self.nombreMenu + "::::::::::::::"+'\033[0;m')
            #print(f"Empresa Roberto \n {self.nombreMenu}")
            for (key, value) in self.listaOpciones.items():
                print(key, " : ", value)
            print("Salir : 9")
            opcion = 100
            try:
                opcion = int(input("Escoge tu opcion: "))
            except ValueError as error:
                self.__log.error(error)
                print("Opcion invalida deben ser numeros de 0 - 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                   contOpciones += 1
            if(opcion==9):
                contOpciones +=1
            if(contOpciones == 0):
                print("Escoge una opcion valida")
                self.__log.debug("No escoje opion")
                #sleep(5)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
            #return os.system('cls')
            return os.system('clear')
        clear()






