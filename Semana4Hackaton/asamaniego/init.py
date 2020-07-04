import os
import utils
from time import sleep
import json
from producto import Producto

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
                 opcion = int(input("Escoge tu opcion: "))
            except ValueError as error:
                 self.__log.error(error)
                 print("Opcion invalida deben ser numeros de 0 - 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value) or opcion == 9):
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
           # print(f"tipo1 : {lstProductosDic}")
            #print(f"existe: {lstProductosDic}")
        
        #prods = Productos(lstProductosDic)
        log.debug(lstProductosDic)
        log.debug(lstProductos)

    except Exception as erro:
        log.error(erro)


def buscarProducto(listDic, codPro):
    
    
    pos = 0
    existe1 = -1
    for x in listDic:
        if x['codProducto'] == codPro:
            existe1 = pos
            break
        pos= pos + 1
    

    return existe1 

def costearProducto(listDic):
    
    
    parcial = 0
    monto  = 0
    for x in listDic:
        parcial = int(x['cantidadProducto']) * int(x['costoProducto'])
        monto = monto + parcial
    
    return monto 

cargaInicial()

dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()


dicOpcionesCrearProducto = {"Crear otro": 1, "Mostrar todos": 2, "Eliminar producto": 3, "Costear productos": 4 }
menuProducto = Menu("Menu Producto", dicOpcionesCrearProducto)


if(opcionMenuPrincipal == 90):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()

elif(opcionMenuPrincipal == 1):
    dicOpcionesCliente = {"Comprar": 1, "Devolver": 2}
    menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
    res = menuCliente.mostrarMenu()
elif(opcionMenuPrincipal == 2):
    dicOpcionesEmpleado = {"Marcar Ingreso": 1,
                           "Marcar Salida": 2, "Cargar Inventario": 3}
    menuEmpleado = Menu("Menu del Empleado", dicOpcionesEmpleado)
    res = menuEmpleado.mostrarMenu()
    salirCreacionProducto = True
    existe = -1
    while salirCreacionProducto:
        if(res == 3):
            try:
                codProducto = int(input("Digita el Codigo del Producto: "))
                codProducto = str(codProducto)
                existe = buscarProducto(lstProductosDic, codProducto)
                if existe == -1:
                    nomProducto = input("Digita Nombre del Producto: ")
                    try:
                        cantProducto = int(input("Digita la Cantidad del Producto: "))
                        cantProducto = str(cantProducto)
                        try:
                            costProducto = int(input("Digita costo del Producto: "))
                            costProducto = str(costProducto)
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
                                elif(res == 9):
                                    log.debug(f"ingreso a la opcion {res}")
                                    salirCreacionProducto = False
                            elif(resMenuProducto == 3):
                                log.debug("ingreso a la opcion 3 de menuProducto")
                                try:
                                    codProducto = int(input("Digita el Codigo del Producto a eliminar: "))
                                    codProducto = str(codProducto)
                                    existe = buscarProducto(lstProductosDic, codProducto)
                                    if existe >  -1:
                                        lstProductosDic.pop(existe)
                                        jsonStr = json.dumps(lstProductosDic)
                                        fileProducto.escribirArchivo(jsonStr)
                                        #print(f"borro la posicion {lstProductosDic}")
                                        
                                except ValueError:
                                    print("El código es numerico")

                            elif (resMenuProducto == 4):
                                log.debug("ingreso a la opcion 4 de menuProducto")
                                monto = costearProducto(lstProductosDic)
                                print(f"el monto del inventario es: {monto}")
                                    
                            else:
                                log.debug(
                                    f"ingreso a la opcion {resMenuProducto} de menuProducto")
                                salirCreacionProducto = False
                                break
                        except ValueError:
                            print("el costo es númerico")

                    except ValueError:
                        print("La cantidad es numerico")    
                else:
                    print("este código ya existe")

            except ValueError:
                print("El código es numerico")
                #verificaProducto(codProducto)
            #existe = lstProductosDic.index(codProducto)
            

