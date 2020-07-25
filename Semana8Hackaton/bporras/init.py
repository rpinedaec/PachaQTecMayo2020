from datetime import datetime
import os
from controllers.autores import *
from controllers.editoriales import *
from controllers.libros import *
from controllers.bibliotecas import *
from controllers.usuario import *
from controllers.prestamos import *

class Menu:
    def __init__(self, lstOpciones, strTitulo, strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def show(self):
        os.system("cls")
        print(f"\033[1;32;40m")
        print(20*":" + f"{self.strTitulo:^20}" + 20*":")
        print(20*":" + f"{self.strMenuDescr:^20}" + 20*":")
        for k, v in self.lstOpciones.items():
            print(k, "::", v)
        print("9 :: Salir")
        while True:
            try:
                self.OptionSelect = int(input("Ingrese su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect < len(self.lstOpciones)+1:
                    return self.OptionSelect
                elif self.OptionSelect == 9:
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")

menuPrincipal = Menu({1: "Módulo Registros", 2: "Módulo Prestamos"},
                     "Biblioteca Nacional", "Menú Principal")
menuRegistros = Menu({1: "Usuarios", 2: "Autores", 3: "Editoriales", 4: "Libros", 5: "Sucursales"},
                     "Biblioteca Nacional", "Modulo Registros")
menuPrestamos = Menu({1: "Reservar", 2: "Retirar", 3: "Devolver"},
                     "Biblioteca Nacional", "Modulo Prestamos")
menuAutores = Menu({1: "Crear", 2: "Editar", 3: "Eliminar"},
                     "Biblioteca Nacional", "Modulo Autores")
menuEditoriales = Menu({1: "Crear", 2: "Editar", 3: "Eliminar"},
                     "Biblioteca Nacional", "Modulo Editoriales")
menuLibros = Menu({1: "Crear", 2: "Editar", 3: "Eliminar"},
                     "Biblioteca Nacional", "Modulo Libros")
menuBibliotecas = Menu({1: "Crear", 2: "Editar", 3: "Eliminar"},
                     "Biblioteca Nacional", "Modulo bibliotecas")
menuUsuarios = Menu({1: "Crear", 2: "Editar", 3: "Eliminar"},
                     "Biblioteca Nacional", "Modulo Usuarios")

while True:
    intOptionSelect = menuPrincipal.show()
    if intOptionSelect == 1:  # Menu Registros
        while True:
            intOptionSelect = menuRegistros.show()
            if intOptionSelect == 1: # Usuarios
                while True:
                    intOptionSelect = menuUsuarios.show()
                    if intOptionSelect == 1 : # Crear usuario
                       insertarUsuario()
                    elif intOptionSelect == 2 : # Editar usuario
                        modificarUsuario()
                    elif intOptionSelect == 3 : # Eliminar usuario
                        eliminarUsuario()
                    else:
                        break
            elif intOptionSelect == 2: # Autores
                while True:
                    intOptionSelect = menuAutores.show()
                    if intOptionSelect == 1 : # Crear autor
                       insertarAutor()
                    elif intOptionSelect == 2 : # Editar autor
                        modificarAutor()
                    elif intOptionSelect == 3 : # Eliminar autor
                        eliminarAutor()
                    else:
                        break 
            elif intOptionSelect == 3: # Editoriales
                while True:
                    intOptionSelect = menuEditoriales.show()
                    if intOptionSelect == 1 : # Crear editorial
                       insertarEditorial()
                    elif intOptionSelect == 2 : # Editar editorial
                        modificarEditorial()
                    elif intOptionSelect == 3 : # Eliminar editorial
                        eliminarEditorial()
                    else:
                        break 
            elif intOptionSelect == 4: # Libros
                while True:
                    intOptionSelect = menuLibros.show()
                    if intOptionSelect == 1: # Ingresar libros
                        insertarLibro()
                    elif intOptionSelect == 2: # Modificar libros
                        modificarLibro()
                    elif intOptionSelect == 3: # Eliminar libros
                        eliminarLibro()
                    else:
                        break
            elif intOptionSelect == 5: #Sucursales
                while True:
                    intOptionSelect = menuBibliotecas.show()
                    if intOptionSelect == 1: # Ingresar biblioteca
                        insertarBiblioteca()
                    elif intOptionSelect == 2: # Modificar biblioteca
                        modificarBiblioteca()
                    elif intOptionSelect == 3: # Eliminar  biblioteca
                        eliminarBiblioteca()
                    else:
                        break
            else:
                break
    elif intOptionSelect == 2:  # Menu Prestamos
        while True:
            intOptionSelect = menuPrestamos.show()
            if intOptionSelect == 1: # Reservar
                reservarLibro()
            elif intOptionSelect == 2: # Retirar
                retirarLibro()
            elif intOptionSelect == 3: # Devolver
                devolverLibro()
            else:
                break
    else:
        break