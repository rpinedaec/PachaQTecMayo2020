import os
import random
from time import sleep

dictUsuario={}
dictTrabajador={}
lstUsuario=[]
lstTrabajador=[]

class Usuario:
    # log = utils.log("Usuario")

    def __init__(self, nombre, apellido, dni, usuario, password, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.usuario = usuario
        self.password = password
        self.email = email
        # self.log.info("Se creo un usuario")
    
    def dictUsuario(self):
        d = {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'usuario': self.usuario,
            'password': self.password,
            'email': self.email,
        }
        return d
    
    def __str__(self):
        return """Usuario: {} \nContrasena: {}""".format(self.usuario, self.password)

class Trabajador(Usuario):
    # log = utils.log("Trabajador")

    def __init__(self,nombre,apellido,dni,usuario,password,email,codTrabajador):
        super().__init__(nombre,apellido,dni,usuario,password,email)
        self.codTrabajador = codTrabajador
        # self.log.info("Se creo un nuevo trabajador")
    def dictTrabajador(self):    
        d = {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'usuario': self.usuario,
            'password': self.password,
            'email': self.email,
            'codTrabajador': self.codTrabajador,
        }
        return d
    
class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = "MENU"
        self.listaOpciones = listaOpciones

    def MostrarMenu(self):
        self.limpiarPantalla()
        salirMenu = True
        while(salirMenu):
            self.limpiarPantalla()
            print("-----------------------------------------")
            print("        TIENDA VIRTUAL PACHAQTEC         ")
            print("-----------------------------------------")
            print(" * "+ self.nombreMenu +" *     ")
            print("")
            for (key, value) in self.listaOpciones.items():
                print("• ",key," : [", value,"]")
            print("•  Salir : [ 0 ]")
            print("")
            print("Escribe tu opción abajo")
            opcion = 100
            try:
                opcion = int(input("Opción : "))
            except:
                contOpciones = 0
                for (key, value) in self.listaOpciones.items():
                    if(opcion == int(value)):
                        contOpciones += 1
                    if(contOpciones == 0):
                        print("Escoge una opcion valida. \n Ingresa numeros del 0 - 9.")
                        sleep(0.5)
            else:
                salirMenu = False
        return opcion
    
    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()

#Diccionario Menu Principal
dicOpcionesMenuPrincipal = {"Usuario Nuevo": 1, "Usuario Existente": 2}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
opcionMenuPrincipal = menuPrincipal.MostrarMenu()

#Opciones del Menu Principal
if (opcionMenuPrincipal == 1):
    dicOpcionesNuevoRegistro = {"Soy Cliente": 1, "Soy Trabajador":2, "Volver": 3}
    menuRegistro = Menu("Menu de Inicio", dicOpcionesNuevoRegistro)
    res = menuRegistro.MostrarMenu()
    salirNuevoRegistro = True
    while (salirNuevoRegistro):
        if(res == 1):
            print("")
            print("NUEVO REGISTRO")
            print("Ingresa los siguientes datos:")
            print("")
            nombre = input("Nombre :")
            apellido = input("Apellido :")
            dni = input("DNI :")
            usuario = input("Escribe tu usuario :")
            password = input("Escribe tu contrasena :")
            email = input("Ingresa tu email :")
            registro_nuevo = Usuario(nombre,apellido,dni,usuario,password,email)
            lstUsuario.append(registro_nuevo.dictUsuario())
            lstUsuario.append(registro_nuevo)
            sleep (2)
            print("************")
            print("ÉXITO!")
            print("Tu Usuario ha sido creado")
            print("")
            sleep(0.5)

        elif (opcionMenuPrincipal == 2):
            print("")
            print("NUEVO REGISTRO")
            print("Ingresa los siguientes datos:")
            print("")
            nombre = input("Nombre :")
            apellido = input("Apellido :")
            dni = input("DNI :")
            usuario = input("Escribe tu usuario :")
            password = input("Escribe tu contrasena :")
            email = input("Ingresa tu email :")
            codTrabajador = random.randint(1000,2000)
            trabajador_nuevo = Trabajador(nombre,apellido,dni,usuario,password,email,codTrabajador)
            lstTrabajador.append(trabajador_nuevo.dictTrabajador())
            lstTrabajador.append(trabajador_nuevo)
            sleep (2)
            print("************")
            print("ÉXITO!")
            print("Tu Usuario ha sido creado")
            print("Tu nuevo código de trabajador es:")
            print(codTrabajador)
            print("")

