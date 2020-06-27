import os
import utils
from time import sleep
import json

def buscarobjeto(nombreobjeto,lstbuscar,strnombrebuscar):
    for objbuscar in lstbuscar:  
        if objbuscar[nombreobjeto] == strnombrebuscar:
           return objbuscar
        else:
           return  False
       
def validarobjeto(nombreobjeto,lstvalidar,strnombrevalidar):
    for objvalidar in lstvalidar:
        if objvalidar[nombreobjeto] == strnombrevalidar:
           return True
        else:
           return  False
    
class Persona:
    __estado = True

    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
       

class Cliente(Persona):
    def __init__(self, codCliente, nombre, apellido, edad,  dni):
        super().__init__(nombre, apellido, edad,  dni)
        self.codCliente = codCliente


    def dictCliente(self):
        d = {
            'codCliente': self.codCliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'dni': self.dni
        }
        return d

class Empleado(Persona):
    def __init__(self,  nombre, apellido, edad, dni, codEmpleado):
        super().__init__(nombre, apellido, edad,  dni)
        self.codEmpleado = codEmpleado

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")
        
    def dictEmpleado(self):
        d = {
            'codEmpleado': self.codEmpleado,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'dni': self.dni
        }
        return d


class Producto:
    log = utils.log("Producto")

    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto,TotalXProducto, TotalProductos):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto
        self.TotalXProducto = TotalXProducto
        self.TotalProductos = TotalProductos
        self.log.info("Se creo un producto")

    def __str__(self):
        return """Codigo: {} \nNombre: {}""".format(self.codProducto, self.nombreProducto)

    def dictProducto(self):
        d = {
            'codProducto': self.codProducto,
            'nombreProducto': self.nombreProducto,
            'cantidadProducto': self.cantidadProducto,
            'costoProducto': self.costoProducto,
            'TotalXProducto': self.TotalXProducto,
            'TotalProductos': self.TotalProductos
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
fileCliente = utils.fileManager("Clientes.txt")
fileEmpleado = utils.fileManager("Empleados.txt")
lstCliente = []
lstClienteDic = []
lstEmpleado = []
lstEmpleadoDic = []
lstProductos = []
lstProductosDic = []


def cargaInicial():
    try:
        try:
            res = fileProducto.leerArchivo()
            log.debug(res)
            lstProducto = json.loads(res)
            for dicProducto in lstProducto:
                #codProducto, nombreProducto, cantidadProducto, costoProducto 
                objProducto = Producto(dicProducto["codProducto"], dicProducto["nombreProducto"],
                                    dicProducto["cantidadProducto"], dicProducto["costoProducto"], 
                                    dicProducto["TotalXProducto"], dicProducto["TotalProductos"])
                lstProductos.append(objProducto)
                lstProductosDic.append(dicProducto)
            log.debug(lstProductosDic)
            log.debug(lstProductos)
        except Exception as error:
            log.error(error)
        
        try:
        
            res=""
            res = fileCliente.leerArchivo()
            log.debug(res)
            lstClientetmp = json.loads(res)
            for dicCliente in lstClientetmp:
                #dni, nombre, apellido, edad, codCliente
                objCliente = Cliente(dicCliente["codCliente"], dicCliente["nombre"],
                                    dicCliente["apellido"],
                                    dicCliente["edad"], dicCliente["dni"])
                lstCliente.append(objCliente)
                lstClienteDic.append(dicCliente)
            log.debug(lstClienteDic)
            log.debug(lstCliente)
        except Exception as error:
            log.error(error)
        
        
        res = ""
        res = fileEmpleado.leerArchivo()
        log.debug(res)
        lstEmpleado = json.loads(res)
        for dicEmpleado in lstEmpleado:
            #dni, nombre, apellido, edad, codEmpleado
            objEmpleado = Empleado(dicEmpleado["codEmpleado"], dicEmpleado["nombre"],
                                   dicEmpleado["apellido"], dicEmpleado["dni"],
                                   dicEmpleado["edad"])
            lstEmpleado.append(objEmpleado)
            lstEmpleadoDic.append(dicEmpleado)
        log.debug(lstEmpleadoDic)
        log.debug(lstEmpleado)
    except Exception as erro:
        log.error(erro)


cargaInicial()

dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()


dicOpcionesCrearProducto = {"Crear otro": 1, "Mostrar todos": 2, "Eliminar Producto" : 3}
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)

dicOpcionesCrearCliente = {"Crear otro": 1, "Mostrar todos": 2}
menuClientesub = Menu("Menu Cliente", dicOpcionesCrearCliente)

dicOpcionesCrearEmpleado = {"Crear otro": 1, "Mostrar todos": 2}
menuEmpleadosub = Menu("Menu Cliente", dicOpcionesCrearCliente)

if(opcionMenuPrincipal == 9):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

elif(opcionMenuPrincipal == 1):
    dicOpcionesCliente = {"Registrar Cliente": 1, "Buscar Cliente": 2}
    menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
    resmenucliente = menuCliente.mostrarMenu()
    salirCreacionCliente = True
    try: 
        while salirCreacionCliente:
            if(resmenucliente == 1):
                
                print("Digita el Codigo del Cliente")
                codCliente = input()
                print("Digita el Nombre del Cliente")
                nomCliente = input()
                print("Digita el apellido del Cliente")
                apeCliente = input()
                print("Digita el D.N.I del Cliente")
                dniCliente = input()
                print("Digita la edad del Cliente")
                edadCliente = input()
                if validarobjeto("dni", lstClienteDic, dniCliente):
                    print("El Cliente ya existe")
                    sleep(10)
                    resretornarmenucliente = menuCliente.mostrarMenu()
                else:    
                    cliente = Cliente(codCliente, nomCliente,
                                    apeCliente, dniCliente,edadCliente)
                print("Haz creado el cliente: ", cliente)
                fileCliente.borrarArchivo()
                lstClienteDic.append(cliente.dictCliente())
                lstCliente.append(cliente)
                jsonStr = json.dumps(lstClienteDic)
                fileCliente.escribirArchivo(jsonStr)
                resMenuClientesub = menuClientesub.mostrarMenu()
                if(resMenuClientesub == 1):
                    log.debug("ingreso a la opcion 1 del menuCliente")
                elif(resMenuClientesub == 2):
                    log.debug("ingreso a la opcion 2 del menuCliente")
                    for objCliente in lstCliente:
                        print(
                            f"|{objCliente.codCliente} | {objCliente.nombre} | {objCliente.apellido} | {objCliente.edad} | {objCliente.dni} |")
                    sleep(10)
                    resretornarmenucliente = menuCliente.mostrarMenu()
                    if(resretornarmenucliente == 1):
                        log.debug(f"ingreso a la opcion {res}")
                else:
                    
                    log.debug(
                        f"ingreso a la opcion {resMenuClientesub} de menuCliente")
                    salirCreacionCliente = False
                    break
            elif(resmenucliente == 2):
                print("Digita el DNI del Cliente")
                strDniCliente = input()
                objetoencontrado = buscarobjeto(
                    "dni", lstClienteDic, strDniCliente)
                if objetoencontrado["codCliente"]!="":
                    print(
                        f"|{objetoencontrado ['codCliente']} | {objetoencontrado['nombre']} | {objetoencontrado['apellido']} | {objetoencontrado['edad']} | {objetoencontrado['dni']} |")
                    sleep(10)   
                    res = menuCliente.mostrarMenu()
                else:
                   print("No se encuentra el cliente a buscar")
                #break
            else:
                pass
    except Exception as error:
        log.error(error)
            
            
        
elif(opcionMenuPrincipal == 2):
    dicOpcionesEmpleado = {"Registrar Empleado": 1,
                           "Buscar Empleado": 2, "Cargar Inventario": 3}
    menuEmpleado = Menu("Menu del Empleado", dicOpcionesEmpleado)
    resmenuempprod = menuEmpleado.mostrarMenu()
    
    salirCreacionEmpleado = True
    while salirCreacionEmpleado:
        if(resmenuempprod == 1):
            print("Digita el Codigo del Empleado")
            codEmpleado = input()
            print("Digita el Nombre del Empleado")
            nomEmpleado = input()
            print("Digita el apellido del Empleado")
            apeEmpleado = input()
            print("Digita el D.N.I del Empleado")
            dniEmpleado = input()
            print("Digita la edad del Empleado")
            edadEmpleado = input()
            if validarobjeto("dni", lstEmpleadoDic, dniEmpleado):
                print("El Empleado ya existe")
                sleep(10)
                resretornarmenuempleado = menuEmpleado.mostrarMenu()
            else:
                empleado = Empleado(codEmpleado, nomEmpleado,
                                apeEmpleado, dniEmpleado, edadEmpleado)
            print("Haz creado el empleado: ", empleado)
            fileEmpleado.borrarArchivo()
            lstEmpleadoDic.append(empleado.dictEmpleado())
            lstEmpleado.append(empleado)
            jsonStr = json.dumps(lstEmpleadoDic)
            fileEmpleado.escribirArchivo(jsonStr)
            resMenuEmpleadosub = menuEmpleadosub.mostrarMenu()
        elif (resmenuempprod == 2):
                print("Digita el DNI del Empleado:")
                strDniEmpleado = input()
                objetoencontrado = buscarobjeto(
                    "dni", lstEmpleadoDic, strDniEmpleado)
                if objetoencontrado["codEmpleado"] != "":
                    print(
                    #codEmpleado, nomEmpleado,
                    #apeEmpleado, dniEmpleado, edadEmpleado
                        f"|{objetoencontrado ['codEmpleado']} | {objetoencontrado['nombre']} | {objetoencontrado['apellido']} | {objetoencontrado['edad']} | {objetoencontrado['dni']} |")
                    sleep(10)
                    res = resmenuempprod.mostrarMenu()
                else:
                   print("No se encuentra el Empleado a buscar")
                if(resMenuEmpleadosub == 1):
                    log.debug("ingreso a la opcion 1 del menuEmpleado")
                elif(resMenuEmpleadosub == 2):
                    log.debug("ingreso a la opcion 2 del menuEmpleado")
                    for objEmpleado in lstEmpleado:
                        print(
                            f"|{objEmpleado.codEmpleado} | {objEmpleado.nombre} | {objEmpleado.apellido} | {objEmpleado.edad} | {objEmpleado.dni} |")
                    sleep(10)
                    resretornarmenuempleado = menuEmpleado.mostrarMenu()
                if(resmenuempprod == 1):
                    log.debug(f"ingreso a la opcion {resmenuempprod}")
                else:

                    log.debug(
                    f"ingreso a la opcion {resMenuEmpleadosub} de menuCliente")
                    salirCreacionCliente = False
                break
        elif(resmenuempprod == 3):
            try: 
                salirCreacionProducto = True
                while salirCreacionProducto:
                
                    print("Digita el Codigo del Producto")
                    codProducto = input()
                    print("Digita el Nombre del Producto")
                    nomProducto = input()
                    print("Digita la Cantidad del Producto")
                    cantProducto = input()
                    print("Digita costo del Producto")
                    costProducto = input()
                    
                    totalxproducto=float(cantProducto) * float(costProducto)                 
                    
                    if validarobjeto("codProducto", lstProductosDic, codProducto):
                        print("El Empleado ya existe")
                        sleep(10)
                        resmenuempprod = menuEmpleado.mostrarMenu()
                   
                          
                    producto = Producto(codProducto, nomProducto,
                                        cantProducto, costProducto, totalxproducto,0.0)

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
                        fltTotal=0.0
                        for objProducto in lstProductos:
                            totalx = float(objProducto.costoProducto) * float(objProducto.cantidadProducto)
                            fltTotal += totalx
                            print(
                                f"|{objProducto.nombreProducto} | {objProducto.codProducto} | {objProducto.cantidadProducto} | {objProducto.costoProducto} | {objProducto.TotalXProducto} | {fltTotal} |")
                        sleep(10)
                        resmenuempprod = menuEmpleado.mostrarMenu()
                        if(res == 1):
                            log.debug(f"ingreso a la opcion {res}")
                    elif(resMenuProducto==3):
                        try:
                            print("entro a delProducto")
                            while True:
                                menuProducto = input("que deseas hacer Quitar : Q / Salir : S ")
                                if(menuProducto == "Q"):
                                    print("Busca en la lista el producto que deseas quitar")
                                    for p in lstProductos:
                                        for (key, value) in p.items():
                                            print(key, " :: ", value)
                                    print("Escribe el nombre del Producto que quieres Eliminar")
                                    strNombreEliminar = input()
                                    for p in lstProductos:
                                        for (key, value) in p.items():
                                            if(value == strNombreEliminar):
                                                print(f"Borrar {value}???")
                                                lstProductos.remove(p)
                                    fileProducto.borrarArchivo()
                                    lstProductosDic.append(producto.dictProducto())
                                    lstProductos.append(producto)
                                    jsonStr = json.dumps(lstProductosDic)
                                    fileProducto.escribirArchivo(jsonStr)
                                    resMenuProducto = menuProducto.mostrarMenu()
                                else:
                                    print("bye")
                                    break
                        except:
                            print("No se pudo eliminar")

                    else:
                        log.debug(
                            f"ingreso a la opcion {resMenuProducto} de menuProducto")
                        salirCreacionProducto = False
                        break
            except Exception as error:
                log.error(error)
                
