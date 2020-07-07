import os
from time import sleep

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CEND = '\033[0m'

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
        print(color.GREEN + "Menu " + self.nombreMenu + color.GREEN)
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
            print(color.RED+"Escoge una opcion valida"+color.RED)
            sleep(3)



