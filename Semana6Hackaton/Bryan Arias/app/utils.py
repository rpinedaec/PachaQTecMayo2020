#import conexion
import logging
import os.path
from time import sleep

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

#Objeto menu
class Menu:
    __log = log("Menu")

    #Constructor
    def __init__(self, NombreMenu, TuplaMenu):
        self.NombreMenu = NombreMenu
        self.TuplaMenu = TuplaMenu

    #Limpiar la pantall
    def LimpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()
    #Metodo para mostrar el menu que se quiera
    def MostrarMenu(self):
        #variable para mantener abierto el menu
        menu = True
        while menu:
            self.LimpiarPantalla()
            print("....::::::::.... BIENVENIDO AL SISTEMA\t....::::::::....")
            print(f"....::::::::.... {self.NombreMenu}....::::::::....")
            #Recorremos la tupla donde se encuentran las opciones
            for i in self.TuplaMenu:
                print (i)
            print("0. SALIR", end="\n\n")
            print("Elija una opcion:")
            #Calculamos tamaño de la tupla (un valor sera el 9. Regresar)
            TamañoTupla = len(self.TuplaMenu)
            #Manejo de error al momento de ingresar un valor
            try:
                opcion = int(input())
                #Validar que exista la opcion con el tamaño de la tupla
                if opcion > TamañoTupla or opcion < 0:
                    self.__log.info(f"La opcion {opcion} no es valida del menu {self.NombreMenu}")
                    print(f"\nEscoja una opcion valida entre 0 y {TamañoTupla}\n\a")
                    sleep(2)
                else:
                    self.__log.debug(f"La opcion {opcion} es valida del menu {self.NombreMenu}")
                    menu = False
            except Exception as e:
                self.__log.error(e)
                print("\nDigite un número entre 0 - 9\n\a")
                sleep(2)
        return opcion

def Salir():
    print("►►►►►► Gracias por usar el Sistema ◄◄◄◄◄◄")
    exit()
        

