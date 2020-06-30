import os
import time
import pickle
from funciones import *
from io import open

<<<<<<< HEAD
# Definición de Clases:
=======
#Definición de Clases:
>>>>>>> upstream/develop


class Menu:
    def __init__(self, lstOpciones, strTitulo, strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0

    def show(self):
        os.system("cls")
        print(f"\033[1;32;40m")
        print(20*":" + f"{self.strTitulo:^20}" + 20*":")
        print(20*":" + f"{self.strMenuDescr:^20}" + 20*":")
        for k, v in self.lstOpciones.items():
            print(k, "::", v)
        print("9 :: Salir")
        while True:
            try:
                self.OptionSelect = int(input("Ingrese su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect < len(self.lstOpciones)+1:
                    return self.OptionSelect
                elif self.OptionSelect == 9:
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")


class Persona:
    def __init__(self, dni=0, nombre=None, apellido=None, edad=None, sexo=None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo


class Cliente(Persona):
    def __init__(self, dni: int = 0, nombre: str = None, apellido: str = None, edad: int = 0, sexo: str = None, codCliente: int = 0):
        super().__init__(dni, nombre, apellido, edad, sexo)
        self.codCliente = codCliente

    def name(self):
        return "Cliente"

    def __str__(self):
        return (f'El cliente "{self.nombre} {self.apellido}" con  codigo "{self.codCliente}" se ha registrado')


class Empleado(Persona):
    def __init__(self, dni=None, nombre=None, apellido=None, edad=None, sexo=None, codEmpleado=None):
        super().__init__(dni, nombre, apellido, edad, sexo)
        self.codEmpleado = codEmpleado

    def name(self):
        return "Empleado"

    def __str__(self):
        return (f'El empleado "{self.nombre} {self.apellido}" con codigo "{self.codEmpleado}" se ha registrado')


class Producto:
    def __init__(self, codProducto: int = None, nombreProducto: str = None, cantProducto: int = None, costoProducto: int = None):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantProducto = cantProducto
        self.costoProducto = costoProducto

    def name(self):
        return "Producto"

    def __str__(self):
        return (f'El producto "{self.nombreProducto}", código "{self.codProducto}" se ha registrado')


<<<<<<< HEAD
# Almacen de datos en ejecución
=======
#Almacen de datos en ejecución
>>>>>>> upstream/develop
lstProductos = []
lstClientes = []
lstEmpleados = []

<<<<<<< HEAD
# Definición de todos los menus:
=======
#Definición de todos los menus:
>>>>>>> upstream/develop
MenuPrincipal = Menu({1: "Cliente",            2: "Empleado",           3: "Producto"},
                     "VENTAS GROUP S.A.", "Menú Principal")
MenuEmpleado = Menu({1: "Crear empleado",     2: "Ver empleado",       3: "Validar existencia"},
                    "VENTAS GROUP S.A.", "Menú Empleado")
MenuCliente = Menu({1: "Crear cliente",      2: "Ver cliente",        3: "Validar existencia"},
                   "VENTAS GROUP S.A.", "Menú Cliente")
MenuProducto = Menu({1: "Agregar producto",   2: "Quitar Producto",    3: "Listar/Contar Producto",
                     4: "Valorizar productos"},   "VENTAS GROUP S.A.", "Menú Producto")
<<<<<<< HEAD
# Inicio del programa(recupera datos):
=======
#Inicio del programa(recupera datos):
>>>>>>> upstream/develop
while True:
    os.system("cls")
    lstClientes = recovery("cliente")
    print("Cargando.....33%")
    time.sleep(2)
    os.system("cls")
    lstEmpleados = recovery("empleado")
    print("Cargando.....66%")
    time.sleep(2)
    os.system("cls")
    lstProductos = recovery("producto")
    print("Cargando.....99%")
    time.sleep(2)
    break
# Ejecución del programa
while True:
    intOptionSelect = MenuPrincipal.show()
    if intOptionSelect == 1:  # Menu cliente
        while True:
            intOptionSelect = MenuCliente.show()
            if intOptionSelect == 1:  # Crear Cliente
                newclient = addCliente(lstClientes, Cliente)
                if search(getattr(newclient, "dni"), "dni", lstClientes):
                    strExiste = input(
                        "El cliente ya existe, ¿Desea reemplazarlo? S/N: ")
                    if strExiste == "S":
                        for i, x in enumerate(lstClientes):
                            if getattr(x, "dni") == getattr(newclient, "dni"):
                                lstClientes[i] = newclient
                                print(newclient)
                                save("cliente", lstClientes)
                    elif strExiste == "N":
                        c = input(
                            "El registro del cliente se ah descartado, ingrese cualquier tecla para continuar: ")
                        break
                    else:
                        print("Error!: El registro del cliente se ah descartado")
                else:
                    lstClientes.append(newclient)
                    print(newclient)
                    save("cliente", lstClientes)
                c = input("Pulse cualquier tecla para continuar: ")
            elif intOptionSelect == 2:  # Ver Cliente
                showCliente(lstClientes)
            elif intOptionSelect == 3:  # Validad Existencia
                while True:
                    try:
                        if search(int(input("Ingrese el numero de dni: ")), "dni", lstClientes):
                            print("El cliente ya existe")
                            c = input(
                                "Ingrese cualquier valor para continua: ")
                            break
                        else:
                            print("El cliente aun no se ah registrado")
                            c = input(
                                "Ingrese cualquier valor para continua: ")
                            break
                    except:
                        print("Erro!: Ingrese numeros enteros")
            else:
                break
    elif intOptionSelect == 2:  # Menu Empleado
        while True:
            intOptionSelect = MenuEmpleado.show()
            if intOptionSelect == 1:  # Crear Empleado
                newempleado = addEmpleado(lstEmpleados, Empleado)
                if search(getattr(newempleado, "dni"), "dni", lstEmpleados):
                    strExiste = input(
                        "El empleado ya existe, ¿Desea reemplazarlo? S/N: ")
                    if strExiste == "S":
                        for i, x in enumerate(lstEmpleados):
                            if getattr(x, "dni") == getattr(newempleado, "dni"):
                                lstEmpleados[i] = newempleado
                                print(newempleado)
                                save("empleado", lstEmpleados)
                    elif strExiste == "N":
                        c = input(
                            "El registro del emplado se ha descartado, pulse cualquier tecla para continuar: ")
                        break
                    else:
                        print("Error!: El registro del cliente se ah descartado")
                else:
                    lstEmpleados.append(newempleado)
                    save("empleado", lstEmpleados)
                    print(newempleado)
                c = input("Pulse cualquier tecla para continuar: ")
            elif intOptionSelect == 2:  # Ver empleado
                showEmpleado(lstEmpleados)
            elif intOptionSelect == 3:  # Validar existencia
                while True:
                    try:
                        if search(int(input("Ingrese el numero de dni: ")), "dni", lstEmpleados):
                            print("El empleado ya existe")
                            c = input(
                                "Ingrese cualquier valor para continuar: ")
                            break
                        else:
                            print("El empleado aun no se ah registrado")
                            c = input(
                                "Ingrese cualquier valor para continuar: ")
                            break
                    except:
                        print("Erro!: Ingrese numeros enteros")
            else:
                break
    elif intOptionSelect == 3:  # Menu Producto
        while True:
            intOptionSelect = MenuProducto.show()
            if intOptionSelect == 1:  # Menu Agregar producto
                newproduct = addProducto(lstProductos, Producto)
                if search(getattr(newproduct, "codProducto"), "codProducto", lstProductos):
                    strExiste = input(
                        "El producto ya existe, ¿Desea reemplazarlo? S/N: ")
                    if strExiste == "S":
                        for i, x in enumerate(lstProductos):
                            if getattr(x, "codProducto") == getattr(newproduct, "codProducto"):
                                lstProductos[i] = newproduct
                                print(newproduct)
                                save("producto", lstProductos)
                    elif strExiste == "N":
                        c = input(
                            "El registro del producto se ha descartado, pulse cualquier tecla para continuar: ")
                        break
                    else:
                        print("Error!: El registro del producto se ha descartado")
                else:
                    lstProductos.append(newproduct)
                    print(newproduct)
                    save("producto", lstProductos)
                c = input("Pulse cualquier tecla para continuar: ")
            elif intOptionSelect == 2:  # Menu Quitar producto
                delProducto(lstProductos)
            elif intOptionSelect == 3:  # Menu Listar/Contar producto
                showProducto(lstProductos)
            elif intOptionSelect == 4:  # Menu Valorizar productos
                valProducto(lstProductos)
            else:
                break
    else:
        break
