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
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.log.info("Se creo Cliente")

    def __str__(self):
        return """Codigo: {} \nNombre: {}""".format(self.codCliente, self.nombre)

    def dictCliente(self):
        dcli = {
            'codCliente': self.codCliente,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
        }
        return dcli

    def buscaCliente(self):
        print("Busca un Cliente")
        try:
            res = fileCliente.leerArchivo()
            log.debug(res)
            lstCliente = json.loads(res)
            for dictCliente in lstCliente:
                objCliente = Cliente(dictCliente["codCliente"], dictCliente["dni"],
                                    dictCliente["nombre"], dictCliente["apellido"], dictCliente["edad"])
                dictCliente.get(objCliente.nombre,0)
                print("El cliente encontrado es ", objCliente.nombre)
                #lstClientesDic.get(dictCliente)
                
            log.debug(lstClientesDic)
            log.debug(lstClientes)
        except Exception as erro:
            log.error(erro)
            print("Este Cliente no Existe")



    def comprar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    log = utils.log("Empleado")
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.log.info("Se creo Empleado")

    def __str__(self):
        return """Codigo: {} \nNombre: {}""".format(self.codEmpleado, self.nombre)

    def dictEmpleado(self):
        demple = {
            'codEmpleado': self.codEmpleado,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
        }
        return demple
        

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")



class Producto:
    log = utils.log("Producto")

    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.__codProducto = codProducto
        self.__nombreProducto = nombreProducto
        self.__cantidadProducto = cantidadProducto
        self.__costoProducto = costoProducto
        self.log.info("Se creo un producto")

    @property
    def codProducto(self):
        return self.__codProducto
    
    @codProducto.setter
    def codProducto(self, valor):
        self.__codProducto = valor
###############################################
    @property
    def nombreProducto(self):
        return self.__nombreProducto
    
    @nombreProducto.setter
    def nombreProducto(self, valor):
        self.__nombreProducto = valor
##############################################
    @property
    def cantidadProducto(self):
        return self.__cantidadProducto
    
    @cantidadProducto.setter
    def cantidadProducto(self, valor):
        self.__cantidadProducto = valor
 ############################################   
    @property
    def costoProducto(self):
        return self.__costoProducto
    
    @costoProducto.setter
    def costoProducto(self, valor):
        self.__costoProducto = valor
#############################################

    def __str__(self):
        return ' Codigo: ' + str(self.__codProducto) + ' Nombre  ' + self.__nombreProducto + ' Cantidad  ' + str(self.__cantidadProducto) + ' Costo  ' + str(self.__costoProducto)


    #def __str__(self):
    #    return """Codigo: {} \nNombre: {}""".format(self.__codProducto, self.__nombreProducto)

    def dictProducto(self):
        #d = dic()
        d = {
            'codProducto': self.__codProducto,
            'nombreProducto': self.__nombreProducto,
            'cantidadProducto': self.__cantidadProducto,
            'costoProducto': self.__costoProducto
        }
        return d
    
        
   # def eliminar_producto(self, producto):
     #   if producto in self.__productos:
       #     indice = self.__productos.index(producto)
       #     del self.__productos[indice]

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
                  ":::::::::::::EMPRESA PACHAQTEC::::::::::::::"+'\033[0;m')
            print("\033[1;34m"+":::::::::::::" +
                  self.nombreMenu + "::::::::::::::"+'\033[0;m')
            #print(f"Empresa Roberto \n {self.nombreMenu}")
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
#####################
fileCliente = utils.fileManager("Clientes.txt")
lstClientes = []
lstClientesDic = []
#####################
fileEmpleado = utils.fileManager("Empleados.txt")
lstEmpleados = []
lstEmpleadosDic = []

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
#########################################################

def cargaInicialCliente():
    try:
        res = fileCliente.leerArchivo()
        log.debug(res)
        lstCliente = json.loads(res)
        for dictCliente in lstCliente:
            objCliente = Cliente(dictCliente["codCliente"], dictCliente["dni"],
                                dictCliente["nombre"], dictCliente["apellido"], dictCliente["edad"])
            lstClientes.append(objCliente)
            lstClientesDic.append(dictCliente)
        log.debug(lstClientesDic)
        log.debug(lstClientes)
    except Exception as erro:
        log.error(erro)


cargaInicialCliente()

#############################################################



 








dicOpcionesMenuPrincipal = {"Cliente": 1, "Administrador": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()


dicOpcionesCrearProducto = {"Agregar Otro": 1, "Mostrar todos": 2, "Eliminar Producto": 3}
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)



#Producto(codProducto, nomProducto, cantProducto, costProducto)

if(opcionMenuPrincipal == 9):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

elif(opcionMenuPrincipal == 1):
    dicOpcionesCliente = {"Comprar": 1, "Devolver": 2, "Registro Cliente": 3, "Ver Clientes": 4, "Buscar Clientes": 5}
    menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
    res = menuCliente.mostrarMenu()
    salirCreacionCliente = True
    while salirCreacionCliente:
        if(res == 3):
            print("Digita el Codigo del Cliente")
            codCliente = input()
            print("Digita el DNI del Cliente")
            dni = input()
            print("Digita el Nombre del Cliente")
            nombre = input()
            print("Digita el Apellido del Cliente")
            apellido = input()
            print("Digita la edad del Cliente")
            edad = input()
            cliente = Cliente(codCliente, dni,
                                    nombre, apellido, edad)

            print("Se agregó un Cliente Nuevo: ", cliente)
            fileCliente.borrarArchivo()
            lstClientesDic.append(cliente.dictCliente())
            lstClientes.append(cliente)
            jsonStr = json.dumps(lstClientesDic)
            fileCliente.escribirArchivo(jsonStr)  

        #rescli = menuCliente.mostrarMenu()
        if(res == 1):
            log.debug("ingreso a la opcion 1 de menuCliente")
                
        elif(res == 4):
                
            log.debug("ingreso a la opcion 4 de menuCliente")
            for objCliente in lstClientes:
                print(
                    f"|{objCliente.codCliente} | {objCliente.dni} | {objCliente.nombre} | {objCliente.apellido} | {objCliente.edad} |")
            sleep(10)
            res = menuCliente.mostrarMenu()
        elif(res == 5):
            log.debug("ingreso a la opcion 5 de menuCliente")
            for objCliente in lstClientes:
                print(
                    f"|{objCliente.codCliente} | {objCliente.dni} | {objCliente.nombre} | {objCliente.apellido} | {objCliente.edad} |")
        
            print("Digita el Nombre de Cliente a buscar")
            nombreCliente = input()
            if (nombreCliente == objCliente.nombre):
                    #dcli.get('Bugs', 'Esta clave no existe')
                    #'Esta clave no existe'
                    # Creates an instance of the class
                #cliente = Cliente(codCliente, dni,nombre, apellido, edad)
                    # Calls instance method
                #cliente.buscaCliente()
                try:
                    res = fileCliente.leerArchivo()
                    log.debug(res)
                    lstCliente = json.loads(res)
                    for dictCliente in lstCliente:
                        objCliente = Cliente(dictCliente["codCliente"], dictCliente["dni"],
                                            dictCliente["nombre"], dictCliente["apellido"], dictCliente["edad"])
                        dictCliente.get(nombreCliente,0)
                        print("El cliente encontrado es ", nombreCliente)
                        #lstClientesDic.get(dictCliente)
                
                    log.debug(lstClientesDic)
                    log.debug(lstClientes)
                except Exception as erro:
                    log.error(erro)
                    print("Este Cliente no Existe")
                    res = menuCliente.mostrarMenu()
        else:  
            salirCreacionCliente = False
            break
elif(opcionMenuPrincipal == 2):
    dicOpcionesEmpleado = {"Marcar Ingreso": 1,
                           "Marcar Salida": 2, "Agregar Producto": 3, "Eliminar Producto": 6, "Registrar Nuevo Empleado": 4, "Ver Empleados": 5}
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
            lstProductosDic.append(producto.dictProducto())
            lstProductos.append(producto)
            jsonStr = json.dumps(lstProductosDic)
            fileProducto.escribirArchivo(jsonStr)  
            #producto.showproducto()
            print("           *********INVENTARIO DE PRODUCTOS******")
            print("-----------------------------------------------------------------")
            fltotal=0.0
            print("ID\t|PRODUCTO\t|CANTIDAD\t|VALOR UNIT.\t|SUBTOTAL")
            print("-----------------------------------------------------------------")            
            for objProducto in lstProductos:
                print(
                f"|{objProducto.codProducto}\t| {objProducto.nombreProducto}\t|\t {objProducto.codProducto} \t|\t|{objProducto.cantidadProducto} \t|\t| {objProducto.costoProducto} |")
                valortotal= int(objProducto.cantidadProducto) * int(objProducto.costoProducto)
                fltotal += valortotal
                #print("El total de Productos es:",valortotal)
            print("-----------------------------------------------------------------")
            print(f"El Precio Total de todos los Productos es: S/.{fltotal}")
            sleep(8)
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
  #             if(res == 1):
   #                log.debug(f"ingreso a la opcion {res}")
            elif(resMenuProducto == 3):
                log.debug("ingreso a la opcion 3 de menuProducto")
                #print("Busca en la lista el producto que deseas quitar")
               
                
                try: 
                    res = fileProducto.leerArchivo()
                    log.debug(res)
                    lstProducto = json.loads(res)
                   
                            #fileProducto.borrarArchivo()
                    print("Digita el Codigo del producto que desea eliminar")
                    nomeProducto = input()
                    if (nomeProducto == Producto.nombreProducto):
                        for dicProducto in lstProducto:
                            objProducto = Producto(dicProducto["codProducto"], dicProducto["nombreProducto"],
                                            dicProducto["cantidadProducto"], dicProducto["costoProducto"])
                             #nom = dicProducto.get(nomeProducto)
                        
                            del [dicProducto]
                            #lstProductos.remove(objProducto)
                            #lstProductosDic.remove(objProducto)
                        #log.debug(lstProductosDic)
                        #log.debug(lstProductos)
                        #for deleprodu in d.values():
                         #   del d['deleprodu']
                         #   print(deleprodu)
                        print("Haz eliminado el producto: ", nomeProducto)
                                
                except ValueError:
                    print("no se encuentra en la lista")
                    sleep(10) 
        #res = menuEmpleado.mostrarMenu()
        if(res == 4):
            print("Digita el Codigo del Empleado")
            codEmpleado = input()
            print("Digita el DNI del Empleado")
            dni = input()
            print("Digita el Nombre del Empleado")
            nombre = input()
            print("Digita el Apellido del Empleado")
            apellido = input()
            print("Digita la edad del Empleado")
            edad = input()
            empleado = Empleado(codEmpleado, dni,
                                    nombre, apellido, edad)

            print("Se agregó un Empleado Nuevo: ", empleado)
            fileEmpleado.borrarArchivo()
            lstEmpleadosDic.append(empleado.dictEmpleado())
            lstEmpleados.append(empleado)
            jsonStr = json.dumps(lstEmpleadosDic)
            fileEmpleado.escribirArchivo(jsonStr) 
            sleep(5)
            res = menuEmpleado.mostrarMenu()
        if(res == 5):
            log.debug("ingreso a la opcion 5 de menuEmpleado")
            print("Lista de Empleados")
            for objEmpleado in lstEmpleados:
                print(
                    f"|{objEmpleado.codEmpleado} | {objEmpleado.dni} | {objEmpleado.nombre} | {objEmpleado.apellido} | {objEmpleado.edad} |")
            sleep(10)
            res = menuEmpleado.mostrarMenu()
        if(res == 6):
            log.debug("ingreso a la opcion 9 de menuEmpleado")
            try: 
                res = fileProducto.leerArchivo()
                log.debug(res)
                lstProducto = json.loads(res)
                    
                                #fileProducto.borrarArchivo()
                print("Digita el nombre del producto que desea eliminar")
                nomeProducto = input()
                        
                for dicProducto in lstProducto:
                    objProducto = Producto(dicProducto["codProducto"], dicProducto["nombreProducto"],
                                                dicProducto["cantidadProducto"], dicProducto["costoProducto"])
                                #nom = dicProducto.get(nomeProducto)
                    if (nomeProducto == Producto.nombreProducto):
                        del objProducto
                                #lstProductos.remove(objProducto)
                                #lstProductosDic.remove(objProducto)
                            #log.debug(lstProductosDic)
                            #log.debug(lstProductos)
                    print("Haz eliminado el producto: ", nomeProducto)
            except ValueError:
                    print("no se encuentra en la lista")
                    sleep(10) 
                                  

        else:  
            salirCreacionProducto = False
            break
