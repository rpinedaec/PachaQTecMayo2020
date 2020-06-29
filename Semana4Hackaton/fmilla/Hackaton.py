import os
import json
from time import sleep

#Definiendo Clases
class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, codCliente):
        super().__init__(dni, nombre, apellido)
        self.dniCliente = dni
        self.nombreCliente = nombre
        self.apellidoCliente = apellido
        self.codCliente = codCliente

    def dictCliente(self):
        c = {
            'dniCliente': self.dniCliente,
            'nombreCliente': self.nombreCliente,
            'apellidoCliente': self.apellidoCliente,
            'codCliente': self.codCliente
        }
        return c

class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, codEmpleado):
        super().__init__(dni, nombre, apellido)
        self.dniEmpleado = dni
        self.nombreEmpleado = nombre
        self.apellidoEmpleado = apellido
        self.codEmpleado = codEmpleado

    def dictEmpleado(self):
        e = {
            'dniEmpleado': self.dniEmpleado,
            'nombreEmpleado': self.nombreEmpleado,
            'apellidoEmpleado': self.apellidoEmpleado,
            'codEmpleado': self.codEmpleado
        }
        return e

class Producto:
    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto

    def dictProducto(self):
        d = {
            'codProducto': self.codProducto,
            'nombreProducto': self.nombreProducto,
            'cantidadProducto': self.cantidadProducto,
            'costoProducto': self.costoProducto
        }
        return d

class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()

    def printMenu(self):
        self.limpiarPantalla()
        print("Menu " + self.nombreMenu)
        print(" ")
        for (key, value) in self.listaOpciones.items():
                print(key, " :: ", value)

    def inputMenu(self):
        print("Elige una opcion")
        try:
            opcion = int(input())
            
            for value in self.listaOpciones.values():
                if(opcion == int(value)):
                    return opcion
        except:
            print("Elige una opcion valida")

class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            return file.read()
        except Exception as e:
            return e

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual+"\\"+self.nombreArchivo
        if(os.path.isfile(path)):
            os.remove(path)
            print("Archivo removido")
        else:
            print("No existe el archivo")

    def escribirArchivo(self, texto):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(texto + "\n")
                except:
                    print("error")
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(texto + "\n")
        except:
            print("error") 
    

#Variables globales
lstCliente = []
lstEmpleado = []
lstProducto = []
archivoproduct = Archivo("Productos.txt")
archivocliente = Archivo("Clientes.txt")
archivoemplead = Archivo("Empleados.txt")

#Programa Principal
while True:

    dictMenuPrincipal = {"Cliente":1, "Empleado":2, "Salir":9}
    MenuPrincipal = Menu("Principal",dictMenuPrincipal)
    MenuPrincipal.printMenu()
    opcionMenuPrincipal = MenuPrincipal.inputMenu()

    #Modulo Clientes
    if(opcionMenuPrincipal == 1):
        while True:
            dictMenuClientes = {"Añadir":1,"Ver":2, "Validar":3, "Salir":9}
            MenuClientes = Menu("Clientes",dictMenuClientes)
            MenuClientes.printMenu()
            opcionMenuClientes = MenuClientes.inputMenu()

            if(opcionMenuClientes == 1):
                #Añadir Clientes
                print("Digita el dni del Cliente")
                dniCliente = input()
                print("Digita el nombre del Cliente")
                nombreCliente = input()
                print("Digita el apellido del Cliente")
                apellidoCliente = input()
                print("Digita el codigo del Cliente")
                codCliente = input()
                cliente = Cliente(dniCliente,nombreCliente,apellidoCliente,codCliente)
                print("Has creado al cliente: ", nombreCliente)
                lstCliente.append(cliente.dictCliente())
                linea = cliente.dictCliente()
                linea = str(linea)
                archivocliente.escribirArchivo(linea + ",")
                sleep(5)

            elif(opcionMenuClientes == 2):
                #Ver Clientes añadidos
                print(lstCliente)
                sleep(5)

            elif(opcionMenuClientes == 3):
                #Valida clientes
                print("Ingrese el nombre del cliente que desee validar")
                nomClienteValid = input()
                for i in range(len(lstCliente)):
                    Elemento = lstCliente[i]
                    nom = Elemento["nombreCliente"]
                    if(nomClienteValid == nom):
                        print(f"El cliente con el nombre {nomClienteValid} esta validado")
                sleep(5)

            elif(opcionMenuClientes == 9):
                break
            
            else:
                print("Elige la opcion correcta")

    elif(opcionMenuPrincipal == 2):
        while True:
            dictMenuEmpleado = {"Añadir":1,"Ver":2, "Validar":3, "Inventariar":4, "Salir":9}
            MenuEmpleados = Menu("Empleado",dictMenuEmpleado)
            MenuEmpleados.printMenu()
            opcionMenuEmpleados = MenuEmpleados.inputMenu()

            if(opcionMenuEmpleados == 1):
                #Añadir Empleados
                print("Digita el dni del Empleado")
                dniEmpleado = input()
                print("Digita el nombre del Empleado")
                nombreEmpleado = input()
                print("Digita el apellido del Empleado")
                apellidoEmpleado = input()
                print("Digita el codigo del Empleado")
                codEmpleado = input()
                empleado = Empleado(dniEmpleado,nombreEmpleado,apellidoEmpleado,codEmpleado)
                print("Has creado al Empleado: ", nombreEmpleado)
                lstEmpleado.append(empleado.dictEmpleado())
                linea = empleado.dictEmpleado()
                linea = str(linea)
                archivoemplead.escribirArchivo(linea + ",")
                sleep(5)

            elif(opcionMenuEmpleados == 2):
                #Ver Empleados añadidos
                print(lstEmpleado)
                sleep(5)

            elif(opcionMenuEmpleados == 3):
                #Valida Empleados
                print("Ingrese el nombre del Empleado que desee validar")
                nomEmpleadoValid = input()
                for i in range(len(lstEmpleado)):
                    Elemento = lstEmpleado[i]
                    nom = Elemento["nombreEmpleado"]
                    if(nomEmpleadoValid == nom):
                        print(f"El Empleado con el nombre {nomEmpleadoValid} esta validado")
                sleep(5)

            elif(opcionMenuEmpleados == 4):
                while True:
                    dictMenuProducto = {"Añadir":1,"Quitar":2, "Ver":3, "Salir":9}
                    MenuProductos = Menu("Producto",dictMenuProducto)
                    MenuProductos.printMenu()
                    opcionMenuProductos = MenuProductos.inputMenu()
                    if(opcionMenuProductos == 1):
                        #Añadir Productos
                        print("Digita el codigo del Producto")
                        codProducto = input()
                        print("Digita el nombre del Producto")
                        nombreProducto = input()
                        print("Digita el cantidad del Producto")
                        cantProducto = input()
                        print("Digita el costo del Producto")
                        costProducto = input()
                        producto = Producto(codProducto,nombreProducto,cantProducto,costProducto)
                        print("Has creado al Producto: ", nombreProducto)
                        lstProducto.append(producto.dictProducto())
                        linea = producto.dictProducto()
                        linea = str(linea)
                        archivoproduct.escribirArchivo(linea + ",")
                        sleep(5)

                    elif(opcionMenuProductos == 2):
                        #Quitar Productos
                        print("Busca en la lista el producto que deseas quitar")
                        for p in lstProducto:
                            for (key, value) in p.items():
                                print(key , " :: ", value )
                        print("Escribe el nombre del Producto que quieres Eliminar")
                        strNombreEliminar = input()
                        for p in lstProducto:
                            for (key, value) in p.items():
                                if(value == strNombreEliminar):
                                    print(f"{value} eliminado")
                                    lstProducto.remove(p)
                        print("Tiene estos productos aún:")
                        print(lstProducto)
                        sleep(5)

                    elif(opcionMenuProductos == 3):
                        #Ver Productos añadidos
                        print(lstProducto)
                        sleep(5)

                    elif(opcionMenuProductos == 9):
                        break

                    else:
                        print("Elige la opcion correcta")

            elif(opcionMenuEmpleados == 9):
                break
            
            else:
                print("Elige la opcion correcta")

    elif(opcionMenuPrincipal == 9):
        break