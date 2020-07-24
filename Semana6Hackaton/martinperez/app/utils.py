import logging
import os
from time import sleep

class color:
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    UNDERLINE = ''
    CEND = ''
#    PURPLE = '\033[95m'
#    CYAN = '\033[96m'
#    DARKCYAN = '\033[36m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    RED = '\033[91m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    CEND = '\033[0m'
#-----------------


class log:
    def __init__(self, nombreLogger):
        # create logger
        self.logger = logging.getLogger(nombreLogger)
        self.logger.filename = 'app.log'
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler("app.log", mode='a')
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    def debug(self, mensaje):
        self.logger.debug(mensaje)

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)

    def critical(self, mensaje):
        self.logger.critical(mensaje)

class Menu:
    __log = log("Menu")
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        while(opSalir):
            self.limpiarPantalla()
            print(color.BLUE+":::::::::::::   BIENVENIDOS EMPRESA MARTIN PEREZ   ::::::::::::::"+color.CEND)
            print(color.BLUE+":::::::::::::::::::   " +self.nombreMenu + "   ::::::::::::::::::"+color.CEND)
            
            for (key, value) in self.listaOpciones.items():
                print(key, "\t:: ", value)
            opcion = 100
            print("\t- Salir \t\t::  9")
            try:
                print(color.CYAN+"Escoge tu opcion"+color.CEND)
                opcion = int(input())
            except ValueError as error:
                self.__log.error(error)
                print(color.RED+"Opcion invalida deben ser numeros del 0 al 2"+color.CEND)
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value) or opcion == 9):
                   contOpciones += 1
            if(contOpciones == 0):
                print(color.RED+"Escoge una opcion valida"+color.CEND)
                self.__log.debug("No escoje opion")
                sleep(3)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
            #return os.system('cls')
            return os.system('clear')
        clear()


class fileManager:
    logD = log("fileManager")

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
        self.logD.debug(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                self.logD.debug("removiendo archivo")

            except Exception as error:
                self.logD.error(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            self.logD.debug(path)
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    self.logD.error(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            self.logD.error(error)






def validarEntero(mensaje):
    booleanCampo = True
    entrada=0
    while booleanCampo:
        entrada = input(mensaje)
        try:
            entrada = int(entrada)
            booleanCampo=False
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")
    return entrada


def validarFloat(mensaje):
    booleanCampo = True
    entrada=0.0
    while booleanCampo:
        entrada = input(mensaje)
        try:
            entrada = float(entrada)
            booleanCampo=False
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero o con decimal")
    return entrada






def validarNombreEnLista(ListaGeneral, mensaje):
    strRetornar = "" 
    boolValor = True
    while boolValor:
        strNombreIngresado=input(mensaje)
        if(strNombreIngresado=="0"):
            boolValor = False
            break
        else:
            ValorTemporal = 0
            for p in ListaGeneral:
                if(p.nombre==strNombreIngresado):
                    ValorTemporal+=1
                    print("Valor existente.")
            if(ValorTemporal==0):
                strRetornar=strNombreIngresado
                boolValor=False
    return strRetornar


def validarDniEnLista(ListaGeneral, mensaje):
    strRetornar = "" 
    boolValor = True
    while boolValor:
        strNombreIngresado=validarEntero(mensaje)
        if(strNombreIngresado==9999):
            boolValor = False
            break
        else:
            ValorTemporal = 0
            for p in ListaGeneral:
                if(p.nroIdentidicacionCliente==strNombreIngresado):
                    ValorTemporal+=1
                    print("Valor existente.")
            if(ValorTemporal==0):
                strRetornar=strNombreIngresado
                boolValor=False
    return strRetornar




def validarIDEnLista(ListaGeneral, mensaje, tipo):
    strRetornar = "" 
    boolValor = True
    while boolValor:
        strNombreIngresado=validarEntero(mensaje)
        if(strNombreIngresado==9999):
            boolValor = False
            break
        else: 
            ValorTemporal = 0
            for p in ListaGeneral:
                # 1 cliente, 2 productos, 3 empresas, 4 tipoPago
                if tipo == 1:
                    if(p.idCliente==strNombreIngresado):
                        ValorTemporal+=1
                elif tipo == 2:
                    if(p.idProducto==strNombreIngresado):
                        ValorTemporal+=1
                elif tipo == 3:
                    if(p.idempresa==strNombreIngresado):
                        ValorTemporal+=1
                elif tipo == 4:
                    if(p.idtipopago==strNombreIngresado):
                        ValorTemporal+=1

            if(ValorTemporal==1):
                strRetornar=strNombreIngresado
                boolValor=False
            else:
                print("Ingrese valor existente.")
    return strRetornar







#select idCliente, "nombreCliente" as Nombre, "nroIdentidicacionCliente" as ID, "direccionCliente" as Direccion from clientes;
def listaSimple(lstObjeto, opcionMenuPrincipal, alertaDetener): 
    strTitulo = "  "
    strTituloGuion = "  "
    intContador = 0
    strTexto = ""
    # Opcion 1 Clientes
    if opcionMenuPrincipal==1: 
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            strTexto += str(p.idCliente).ljust(10)+"\t\t" 
            strTexto += str(p.nombreCliente).ljust(10)+"\t\t" 
            strTexto += str(p.nroIdentidicacionCliente).ljust(10)+"\t\t" 
            strTexto += str(p.direccionCliente).ljust(10)+"\n" 
        if intContador>0:
            strTitulo += str("CODIGO").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("ID").ljust(10)+"\t\t"
            strTitulo += str("DIRECCION").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..."
    # Opcion 2 Productos        idProducto,nombreProducto,valorProducto,igvProducto
    elif opcionMenuPrincipal==2:
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            strTexto += str(p.idProducto).ljust(10)+"\t\t" 
            strTexto += str(p.nombreProducto).ljust(10)+"\t\t" 
            strTexto += str(p.valorProducto).ljust(10)+"\t\t"
            if p.igvProducto == 1:
                strTexto += str("Si").ljust(10)+"\n" 
            else:
                strTexto += str("No").ljust(10)+"\n" 
        if intContador>0:
            strTitulo += str("CODIGO").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("VALOR").ljust(10)+"\t\t"
            strTitulo += str("AFECTO IGV").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..." 
    # Opcion 3 empresas        idempresa,rucEmpresa,nombreEmpresa
    elif opcionMenuPrincipal==3:
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            strTexto += str(p.idempresa).ljust(10)+"\t\t" 
            strTexto += str(p.rucEmpresa).ljust(10)+"\t\t" 
            strTexto += str(p.nombreEmpresa).ljust(10)+"\n"
        if intContador>0:
            strTitulo += str("ID").ljust(10)+"\t\t" 
            strTitulo += str("RUC").ljust(10)+"\t\t"
            strTitulo += str("RAZON SOCIAL").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..." 
    # Opcion 4 tipo de pago         --idtipoPago,descTipoPago   
    elif opcionMenuPrincipal==4:
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            strTexto += str(p.idtipopago).ljust(10)+"\t\t"  
            strTexto += str(p.desctipopago).ljust(10)+"\n"
        if intContador>0:
            strTitulo += str("ID").ljust(10)+"\t\t"  
            strTitulo += str("TIPO DE PAGO").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..." 
    # Opcion 5 Cabecera de Factura   --c.idfacCabecera, empresa,cliente, tipoPago
    #   ,c.fechaFacCabecera,c.igvFacCabecera,c.subtotalFacCabecera,c.totalFacCabecera,c.estadoFactura
    elif opcionMenuPrincipal==5:
        for p in lstObjeto:
            intContador+=1
            strTexto += " "  
            strTexto += str(p.idfacCabecera).ljust(10)+"\t\t"  
            strTexto += str(p.empresa).ljust(10)+"\t\t"  
            strTexto += str(p.cliente).ljust(10)+"\t\t"  
            strTexto += str(p.tipoPago).ljust(10)+"\t\t"  
            strTexto += str(p.fechaFacCabecera).ljust(10)+"\t\t"  
            strTexto += str(p.igvFacCabecera).ljust(10)+"\t\t"  
            strTexto += str(p.subtotalFacCabecera).ljust(10)+"\t\t"  
            strTexto += str(p.totalFacCabecera).ljust(10)+"\n"
            #strTexto += str(p.estadoFactura).ljust(10)+"\n"
        if intContador>0:
            strTitulo += str("ID").ljust(10)+"\t\t"  
            strTitulo += str("Empresa").ljust(10)+"\t\t"
            strTitulo += str("Cliente").ljust(10)+"\t\t"
            strTitulo += str("TipoPago").ljust(10)+"\t\t"
            strTitulo += str("Fecha").ljust(10)+"\t\t"
            strTitulo += str("IGV").ljust(10)+"\t\t"
            strTitulo += str("SubTotal").ljust(10)+"\t\t"
            strTitulo += str("Total").ljust(10)+"\t\t"
            #strTitulo += str("Estado").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..." 
    # Opcion 5 Cabecera de Factura   --idfacDetalle, idfacCabecera, p.nombreProducto producto
    #   ,d.cantFacDetalle cantidad,d.valorFacDetalle valor, p.igvProducto afecto
    #   idFacDetalle, facCabecera, producto, cantidad, valor, afecto
    elif opcionMenuPrincipal==6:
        for p in lstObjeto:
            intContador+=1
            strTexto += " "  
            strTexto += str(p.idFacDetalle).ljust(10)+"\t\t"  
            strTexto += str(p.facCabecera).ljust(10)+"\t\t"  
            strTexto += str(p.producto).ljust(10)+"\t\t"  
            strTexto += str(p.cantidad).ljust(10)+"\t\t"  
            strTexto += str(p.valor).ljust(10)+"\t\t"
            if p.afecto==1:
                strTexto += str("Si").ljust(10)+"\n"
            else:
                strTexto += str("No").ljust(10)+"\n"
        if intContador>0:
            strTitulo += str("ID").ljust(10)+"\t\t"  
            strTitulo += str("Factura").ljust(10)+"\t\t"
            strTitulo += str("Producto").ljust(10)+"\t\t"
            strTitulo += str("Cantidad").ljust(10)+"\t\t"
            strTitulo += str("SubTotal").ljust(10)+"\t\t" 
            strTitulo += str("AfectoIGV").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..." 
    print(strTitulo)
    print(strTituloGuion)
    print(strTexto)
    if alertaDetener ==1:
        input("Enter para continuar...")
    else:
        pass




