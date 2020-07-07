import logging
import os.path
import os
from time import sleep

class Color():
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    CEND      = '\033[0;m'


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
            print(Color.BLUE+"::::::::::::: EMPRESA EL BACAN ::::::::::::::"+Color.CEND)
            print(Color.BLUE+":::::::::::::::::::" +self.nombreMenu + "::::::::::::::::::"+Color.CEND)
            
            for (key, value) in self.listaOpciones.items():
                print(key, "\t: ", value)       
            opcion = 100
            print("\t- Salir \t\t:  9")
            try:
                print(Color.CYAN+"Escoge tu opcion"+Color.CEND)
                opcion = int(input())
            except ValueError as error:
                self.__log.error(error)
                print(Color.RED+"Solo usar los numeros de la lista"+Color.CEND)
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                #EN ESTA LINEA POR PONER EL NUMERO NUEVE SE RESUELVE UNA SOLA VEZ QUE SIEMPRE LA OPCIÓN 9 SERÁ SALIR SIN TENER QUE PONERLA EN CADA OBJETO
                if(opcion == int(value) or opcion == 9):
                   contOpciones += 1
            if(contOpciones == 0):
                print(Color.RED+"Escoge una opcion valida"+Color.CEND)
                self.__log.debug("No escogió ninguna opción")
                sleep(2)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
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