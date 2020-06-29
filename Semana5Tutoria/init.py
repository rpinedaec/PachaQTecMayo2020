# CINCO = 5
# NumeroCinco = "Cinco" #PascalCase
# numeroCinco = "Cinco" #CamelCase

# NUMERO_CINCO = 5 #ScreamerSnakeCase
# numero_cinco = 5 #SnakeCase
# numero-cinco = 5 #KebabCase
import json
import os
from time import sleep

class Persona:
    __estadoPersona = "Activo"
    def __init__(self, idPersona, nombrePersona, apellidoPersona, numeroIdPersona, edadPersona):
        self.idPersona = idPersona
        self.nombrePersona = nombrePersona
        self.apellidoPersona = apellidoPersona
        self.numeroIdPersona = numeroIdPersona
        self.edadPersona = edadPersona
        self.tipoDocumento = "DNI"

    def toDic(self):
        diccionarioPersona ={
            "idPersona":self.idPersona,
            "nombrePersona":self.nombrePersona,
            "apellidoPersona":self.apellidoPersona,
            "numeroIdPersona":self.numeroIdPersona,
            "edadPersona":self.edadPersona,
            "tipoDocumento":self.tipoDocumento,
            "estadoPersona":self.__estadoPersona
        } 
        return diccionarioPersona

class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        while(opSalir):
            self.limpiarPantalla()
            print(":::::::::::::EMPRESA PACHAQTEC::::::::::::::")
            print(":::::::::::::" +self.nombreMenu + "::::::::::::::")
            #print(f"Empresa Roberto \n {self.nombreMenu}")
            for (key, value) in self.listaOpciones.items():
                print(key, " :: ", value)
            print("Salir :: 9")
            opcion = 100
            try:
                print("Escoge tu opcion")
                opcion = int(input())
            except ValueError as error:
                print("Opcion invalida deben ser numeros de 0 - 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value) or opcion == 9):
                   contOpciones += 1
            if(contOpciones == 0):
                print("Escoge una opcion valida")
                sleep(5)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        #return os.system('cls')
        return os.system('clear')


dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.mostrarMenu()

print(f"La opcion que escogio el usuario es {opcionMenuPrincipal}")


miPersona = Persona(999,"Roberto","Pineda","001575294",36)
miAlterEgo = Persona(666,"David","Lopez","1716861991",36)

jsonStr = json.dumps(miPersona.toDic())
print(jsonStr)
print(miAlterEgo.toDic())

    