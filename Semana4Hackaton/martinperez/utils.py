import logging
import os.path
from os import remove 

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

 
def listaSimple(lstObjeto, opcionMenuPrincipal): 
    strTitulo = "  "
    strTituloGuion = "  "
    intContador = 0
    totalValorizado = 0.00
    strTexto = ""
    if opcionMenuPrincipal==3: 
        for p in lstObjeto:
            intContador+=1
            strTexto += str(intContador)+") "  
            strTexto += str(p.codigo).ljust(10)+"\t\t" 
            strTexto += str(p.nombre).ljust(10)+"\t\t" 
            strTexto += str(p.cantidadProducto).ljust(10)+"\t\t" 
            strTexto += str(p.unidad).ljust(10)+"\t\t" 
            strTexto += str(p.costoProducto).ljust(10)+"\t\t"
            strTexto += str(round(p.total,2)).ljust(10)+"\t\t\n"
            totalValorizado +=p.total
        if intContador>0:
            strTitulo += str("CODIGO").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("CANTIDAD").ljust(10)+"\t\t"
            strTitulo += str("UNIDAD").ljust(10)+"\t\t"
            strTitulo += str("COSTO").ljust(10)+"\t\t"
            strTitulo += str("TOTAL").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
            strTexto += "\n\t"+str(intContador)+" PRODUCTOS, TOTAL VALORIZADO: "+str(round(totalValorizado,2))
        else:
            strTitulo +="Sin datos..."
    elif opcionMenuPrincipal==2: # para empleados
        for p in lstObjeto:
            intContador+=1
            strTexto += "   "  
            strTexto += str(p.codigo).ljust(10)+"\t\t"  
            strTexto += str(p.dni).ljust(10)+"\t\t" 
            strTexto += str(p.nombre).ljust(10)+"\t\t" 
            strTexto += str(p.apellido).ljust(10)+"\t\t"
            strTexto += str(p.edad).ljust(10)+"\t\t\n" 
        if intContador>0:
            strTitulo += str("CODIGO").ljust(10)+"\t\t"
            strTitulo += str("DNI").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("APELLIDO").ljust(10)+"\t\t"
            strTitulo += str("EDAD").ljust(10)+"\t\t" 
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------\t\t----------"
        else:
            strTitulo +="Sin datos..."
    elif opcionMenuPrincipal==1:
        for p in lstObjeto:
            intContador+=1
            strTexto += "   "  
            strTexto += str(p.codigo).ljust(10)+"\t\t"  
            strTexto += str(p.dni).ljust(10)+"\t\t" 
            strTexto += str(p.nombre).ljust(10)+"\t\t" 
            strTexto += str(p.apellido).ljust(10)+"\t\t"
            strTexto += str(p.edad).ljust(10)+"\t\t\n" 
        if intContador>0:
            strTitulo += str("CODIGO").ljust(10)+"\t\t"
            strTitulo += str("DNI").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("APELLIDO").ljust(10)+"\t\t"
            strTitulo += str("EDAD").ljust(10)+"\t\t" 
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------\t\t----------"
        else:
            strTitulo +="Sin datos..."
    elif opcionMenuPrincipal==111:
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            strTexto += str(p.codigo).ljust(10)+"\t\t" 
            strTexto += str(p.nombre).ljust(10)+"\t\t" 
            strTexto += str(p.cantidadProducto).ljust(10)+"\t\t" 
            strTexto += str(p.unidad).ljust(10)+"\t\t" 
            strTexto += str(p.costoProducto).ljust(10)+"\t\t"
            strTexto += str(round(p.total,2)).ljust(10)+"\t\t\n"
            totalValorizado +=p.total
        if intContador>0:
            strTitulo += str("CODIGO").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("CANTIDAD").ljust(10)+"\t\t"
            strTitulo += str("UNIDAD").ljust(10)+"\t\t"
            strTitulo += str("COSTO").ljust(10)+"\t\t"
            strTitulo += str("TOTAL").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t----------\t\t----------\t\t----------\t\t" 
        else:
            strTitulo +="Sin datos..."

    print(strTitulo)
    print(strTituloGuion)
    print(strTexto)
    if opcionMenuPrincipal!=111 and opcionMenuPrincipal!=2 and opcionMenuPrincipal!=1:
        input("Enter para continuar...")


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
        if(strNombreIngresado=="0"):
            boolValor = False
            break
        else:
            ValorTemporal = 0
            for p in ListaGeneral:
                if(p.dni==strNombreIngresado):
                    ValorTemporal+=1
                    print("Valor existente.")
            if(ValorTemporal==0):
                strRetornar=strNombreIngresado
                boolValor=False
    return strRetornar


 
def AutogenerarMayorMasUno(lstProductos):
    strRetornar = 0
    for p in lstProductos:
        if(p.codigo>strRetornar):
            strRetornar = p.codigo
    return strRetornar+1



def listarUnidadMedida(listUnidadMedida):
    strTexto = "Unidad de Medida: "
    Contador = 0
    for p in listUnidadMedida:
        Contador+=1
        strTexto += str(Contador)+")"+ p.nombre +"\t"
    print(strTexto)

