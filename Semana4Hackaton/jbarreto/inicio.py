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
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente

    def dictCliente(self):
        d = {
            'dniCliente': self.dni,
            'nomCliente': self.nombre,
            'apeCliente': self.apellido,
            'edaCliente': self.edad,
            'codCliente': self.codCliente
            }
        return d


    def comprar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado

    def dicEmpleado(self):
        d = {
            'dniEmpleado': self.dni,
            'nomEmpleado': self.nombre,
            'apeEmpleado': self.apellido,
            'edaEmpleado': self.edad,
            'codEmpleado': self.codEmpleado
            }
        return d

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")



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

    def costearProducto(self):
        print("Costeando producto")
        print("Producto costeado")
        print("Cantidad de Productos:", len(lstProductos))


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
                  ":::::::::::::EMPRESA PACHAQTEC::::::::::::::"+'\033[0;m')
            print("\033[1;34m"+":::::::::::::" +
                  self.nombreMenu + "::::::::::::::"+'\033[0;m')
            for (key, value) in self.listaOpciones.items():
                print(key, " :: ", value)
            print("Salir :: 9")
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
lstProductos = []
lstProductosDic = []
flagValidacion = True

fileCliente = utils.fileManager("Clientes.txt")
lstClientes = []
lstclientesDic = []

fileEmpleado = utils.fileManager("Empleado.txt")
lstEmpleados = []
lstEmpleadosDic = []

def cargaInicial():
    try:
        res = fileProducto.leerArchivo()
        log.debug(res)
        lstProducto = json.loads(res)
        for dicProducto in lstProducto:
            objProducto = Producto(dicProducto["codProducto"], dicProducto["nombreProducto"],
                                dicProducto["cantidadProducto"], dicProducto["costoProducto"])
            lstProductos.append(objProducto)
            lstProductosDic.append(dicProducto)
        log.debug(lstProductosDic)
        log.debug(lstProductos)
    except Exception as erro:
        log.error(erro)

    try:
        res1=fileCliente.leerArchivo()
        lstCliente = json.loads(res1)
        for dicCliente in lstCliente:
            objcliente = Cliente(dicCliente["dniCliente"], dicCliente["nomCliente"], 
                                 dicCliente["apeCliente"], dicCliente["edaCliente"], 
                                 dicCliente["codCliente"])
            lstClientes.append(objcliente)
            lstclientesDic.append(dicCliente)                    
    except Exception as erro:
        log.error(erro)

    try:
        res2=fileEmpleado.leerArchivo()
        lstEmpleado = json.loads(res2)
        for dicEmpleado in lstEmpleado:
            objEmpleado = Empleado(dicEmpleado["dniEmpleado"], dicEmpleado["nomEmpleado"],
                                    dicEmpleado["apeEmpleado"], dicEmpleado["edaEmpleado"],
                                    dicEmpleado["codEmpleado"])
            lstEmpleados.append(objEmpleado)
            lstEmpleadosDic.append(dicEmpleado)
    except Exception as erro:        
        log.error(erro)


cargaInicial()



dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)

dicOpcionesCrearProducto = {"Crear otro": 1, "Mostrar todos": 2}
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)

while True:
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

    if opcionMenuPrincipal == 1:    #Menú de Cliente
        #dicOpcionesCliente = {"Comprar": 1, "Devolver": 2, "Registrar Cliente": 3, "Mostrar Cliente": 4}
        dicOpcionesCliente = {"Registrar Cliente": 3, "Mostrar Cliente": 4}
        menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
        salirCreacionCliente = True
        while salirCreacionCliente:
            res = menuCliente.mostrarMenu()
            # if(res == 1):   #Comprar Producto(no está desarrollado)
            #     print("*****Comprar Productos*****")
            #     print("Digite su hora de ingreso")
            #     hingresoC = input()
            #     sleep(5)
            # elif(res == 2): #Devolver Productos(no está desarrollado)
            #     print("*****Devolver Productos*****")
            #     print("Digite su hora de salida")
            #     hSalidaC = input()
            #     sleep(5)
            if(res ==3):  #Registrar Cliente
                print("*****Ingrese los datos del Cliente*****")
                flagValidacion = True
                while flagValidacion:
                    print ("Digita el código del Cliente")
                    codCliente = input()
                    if not lstClientes:
                        flagValidacion = False
                    else:
                        for objCliente in lstClientes:
                            srtCodCliente = objCliente.codCliente
                            if(srtCodCliente == codCliente):
                                print(f"El codigo de cliente {objCliente.codCliente} ya existe")
                                flagValidacion = True
                                break
                            else:
                                flagValidacion = False 
                flagValidacion = True
                while flagValidacion:
                    try:                
                        print("Digita el DNI del Cliente")
                        dniCliente = int(input())
                        flagValidacion = False
                    except ValueError:
                         print("Error!: Ingrese un número entero para el DNI")
                flagValidacion = True   
                print("Digita el Nombre del Cliente")
                nomCliente = input()
                print("Digita los Apellidos del Cliente")
                apeCliente = input()
                flagValidacion = True
                while flagValidacion:
                    try:
                        print("Digita la edad del Cliente")
                        edaCliente = int(input())
                        flagValidacion = False
                    except ValueError:
                        print("Error!: Ingrese un número entero para la edad")
                flagValidacion = True
                #obteniendo los datos en el objeto cliente
                cliente = Cliente(dniCliente, nomCliente, 
                                    apeCliente, edaCliente, codCliente)
                print("Haz creado el cliente: ", cliente.nombre, " ", cliente.apellido)
                fileCliente.borrarArchivo()
                lstclientesDic.append(cliente.dictCliente())
                lstClientes.append(cliente)
                jsonStr1 = json.dumps(lstclientesDic)
                fileCliente.escribirArchivo(jsonStr1)

                sleep(10)
            elif(res == 4): #Mostrar datos de Cliente
                print("*****Mostrar datos de Cliente*****")
                if not lstClientes:
                    print("No existen Clientes")
                else:
                    for objCliente in lstClientes:
                        print(f"|{objCliente.dni} | {objCliente.nombre} | {objCliente.apellido} | {objCliente.edad} | {objCliente.codCliente} |") 
        
                sleep(10)
                #res = menuCliente.mostrarMenu()
            elif (res == 9):    #Mostrar menú principal
                salirCreacionCliente = False

    elif opcionMenuPrincipal == 2:  #Menú de Empleado/Cargar inventario
        dicOpcionesEmpleado = {"Marcar Ingreso": 1,"Marcar Salida": 2, 
                            "Cargar Inventario": 3, "Registrar Empleado": 4,
                            "Mostrar Empleado": 5}
        menuEmpleado = Menu("Menu del Empleado", dicOpcionesEmpleado)
        salirCreacionProducto = True
        while salirCreacionProducto:
            res = menuEmpleado.mostrarMenu()
            if(res == 1):   #Marcar ingreso de Empleado(no está desarrollado)
                print("*****Marcar Ingreso*****")
                print("Digite su hora de ingreso")
                hIngresoE = input()
                sleep(5)
            elif(res == 2): #Marcar salida de Empleado(no está desarrollado)
                print("*****Marcar Salida*****")
                print("Digite su hora de salida")
                hSalidaE = input()
                sleep(5)
            elif(res == 3): #Cargar menú de inventario
                flagValidacion = True
                while flagValidacion:
                    print("Digita el Codigo del Producto")
                    codProducto = input()
                    if not lstProductos:
                        flagValidacion = False
                    else:
                        for objProducto in lstProductos:
                            srtCodProducto = objProducto.codProducto
                            if(srtCodProducto == codProducto):
                                print(f"El codigo de producto {objProducto.codProducto} ya existe")
                                flagValidacion = True
                                break
                            else:
                                flagValidacion = False 
                print("Digita el Nombre del Producto")
                nomProducto = input()
                flagValidacion = True
                while flagValidacion:
                    try:
                        print("Digita la Cantidad del Producto")
                        cantProducto = int(input())
                        flagValidacion = False
                    except ValueError:
                        print("Error!: Ingrese entero para la cantidad")
                flagValidacion = True
                while flagValidacion:
                    try:
                        print("Digita costo del Producto")
                        costProducto = float(input())
                        flagValidacion = False
                    except ValueError:
                        print("Error!: Ingrese flotante para el precio")
                producto = Producto(codProducto, nomProducto,
                                    cantProducto, costProducto)
                print("Haz creado el producto: ", producto)
                fileProducto.borrarArchivo()
                lstProductosDic.append(producto.dictProducto())
                lstProductos.append(producto)
                jsonStr = json.dumps(lstProductosDic)
                fileProducto.escribirArchivo(jsonStr)

                sleep(10)
                resMenuProducto = menuProducto.mostrarMenu()
                if(resMenuProducto == 1):
                    log.debug("ingreso a la opcion 1 de menuProducto")
                elif(resMenuProducto == 2):
                    log.debug("ingreso a la opcion 2 de menuProducto")
                    #calcular valor de inventario
                    totalProducto = 0.0
                    if not lstProductos:
                        print("No existe inventario")
                    else:
                        for objProducto in lstProductos:
                            print(
                                f"|{objProducto.nombreProducto} | {objProducto.codProducto} | {objProducto.cantidadProducto} | {objProducto.costoProducto} |")
                            cantidad = objProducto.cantidadProducto
                            costo = objProducto.costoProducto
                            totalProducto += float(cantidad)*float(costo)
                        print("El Valor de Inventario es igual:", totalProducto)   
            
                    sleep(10)
                    res = menuEmpleado.mostrarMenu()
                    if(res == 1):
                        log.debug(f"ingreso a la opcion {res}")
                    elif(res == 9):
                        break        
                else:
                    log.debug(f"ingreso a la opcion {resMenuProducto} de menuProducto")
                    salirCreacionProducto = False
            elif(res == 4): #Registrar Empleado 
                print("*****Ingrese los datos del Empleado*****")
                flagValidacion = True
                while flagValidacion:
                    print ("Digita el código del Empleado")
                    codEmpleado = input()
                    if not lstEmpleados:
                        flagValidacion = False
                    else:
                        for objEmpleado in lstEmpleados:
                            srtCodEmpleado = objEmpleado.codEmpleado
                            if(srtCodEmpleado == codEmpleado):
                                print(f"El codigo de empleado {objEmpleado.codEmpleado} ya existe")
                                flagValidacion = True
                                break
                            else:
                                flagValidacion = False 
                print("Digita el DNI del Empleado")
                dniEmpleado = input()
                print("Digita el Nombre del Empleado")
                nomEmpleado = input()
                print("Digita los Apellidos del Empleado")
                apeEmpleado = input()
                print("Digita la edad del Empleado")
                edaEmpleado = input()  
                #obteniendo los datos en el objeto cliente
                empleado = Empleado(dniEmpleado, nomEmpleado, 
                                    apeEmpleado, edaEmpleado, codEmpleado)
                print("Haz creado el empleado: ", empleado.nombre," ", empleado.apellido)
                fileEmpleado.borrarArchivo()
                lstEmpleadosDic.append(empleado.dicEmpleado())
                lstEmpleados.append(empleado)
                jsonStr2 = json.dumps(lstEmpleadosDic)
                fileEmpleado.escribirArchivo(jsonStr2)

                sleep(10)
                res = menuEmpleado.mostrarMenu()
            elif(res == 5): #Mostrar datos de Empleado
                print("*****Mostrar datos de Empleado*****")
                if not lstEmpleados:
                    print("No existen Empleados")
                else:
                    for objEmpleado in lstEmpleados:
                        print(f"|{objEmpleado.dni} | {objEmpleado.nombre} | {objEmpleado.apellido} | {objEmpleado.edad} | {objEmpleado.codEmpleado} |")
            
                sleep(10)
                res = menuEmpleado.mostrarMenu()
            #Mostrar menu principal
            elif(res == 9):
                salirCreacionProducto = False

    else:
        break

