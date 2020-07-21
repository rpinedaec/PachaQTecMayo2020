from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.user import User
from models.autor import Autor
from models.biblioteca import Biblioteca
from models.estado_libro import EstadoLibro
from models.estado_user import EstadoUser
from models.tipo_documento import TipoDocumento



class Registros:
    __log = log("Registros")
    def registroLibros(self):
        self.__log.info("Ingresando al Registro de Libros")

        while True:
            opcionesRegistroLibros = {"\t- Registrar Libros":1,"\t- Listar Libros":2}
            menuRegistroLibros = Menu("Registro de Libros",opcionesRegistroLibros)
            resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
            if resmenuRegistroLibros == 1:
                self.__log.info("Entrando al registro de libros")
                nuevoLibro = Libro()
                nombreLibro = input("escriba el nombre del Libro \n")
                isbnLibro = input("escriba en ISBN del libro \n")

                autores = Autor()
                print(f"\t Codigo\t Nombre\t Tipo")
                for obj in autores.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.tipo}")
                print("Escriba el id del Autor de la siguiente lista")
                autor_idLibro = input()
                estados = EstadoLibro()
                print(f"\t Codigo\t Estado")
                for obj in estados.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del Estado del Libro de la siguiente lista")
                estadoLibro = input()

                nuevoLibro.nombre = nombreLibro
                nuevoLibro.isbn = isbnLibro
                nuevoLibro.autor_id = autor_idLibro
                nuevoLibro.estado_libro_id = estadoLibro

                nuevoLibro.save()



                input("Continuar?")

            elif resmenuRegistroLibros == 2:
                self.__log.info("Ingresando a listar libros")
                libros = Libro()
                print(f"\t Codigo\t Nombre\t\t ISBN\t Autor\t Estado")
                for obj in libros.all():
                    y = obj.estado_libro_id
                    if(y == 1):
                        estado = "Disponible"
                    elif(y == 2):
                        estado = "Reservado"
                    elif(y == 3):
                        estado = "Prestado"
                    print(f"\t {obj.id}\t {obj.nombre}\t\t {obj.isbn}\t {obj.autor_id}\t {estado}")


                input("Continuar?")

            
            elif resmenuRegistroLibros == 9:
                self.__log.info("Saliendo")
                break

    def registroLectores(self):
        self.__log.info("Ingresando al Registro de Lectores")
        while True:
            opcionesRegistroLectores = {"\t- Registrar Lectores":1,"\t- Listar Lectores":2}
            menuRegistroLectores = Menu("Registro de Lectores",opcionesRegistroLectores)
            resmenuRegistroLectores = menuRegistroLectores.mostrarMenu()
            if(resmenuRegistroLectores == 1):
                self.__log.info("Entrando al registro de Lectores")
                nuevoLector = User()
                nombreLector = input("escriba el nombre del Lector \n")
                correoLector = input("escriba el correo del Lector \n")

                tipo_documento = TipoDocumento()
                print(f"\t Codigo\t Descripcion")
                for obj in tipo_documento.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del tipo de documento de la siguiente lista")
                tipo_documento_idLector = input()
                documentoLector = input("escriba el nro de documento del Lector \n")
                estados = EstadoUser()
                print(f"\t Codigo\t Estado")
                for obj in estados.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del Estado del Lector de la siguiente lista")
                estadoLector = input()

                nuevoLector.nombre = nombreLector
                nuevoLector.correo = correoLector
                nuevoLector.tipo_documento_id = tipo_documento_idLector
                nuevoLector.documento = documentoLector
                nuevoLector.estado_user_id = estadoLector

                nuevoLector.save()



                input("Continuar?")
            
            elif(resmenuRegistroLectores == 2):
                self.__log.info("Ingresando a listar lectores")
                lectores = User()
                print(f"\t Codigo\t Nombre\t\t Correo\t tipDoc\t NroDoc\t Estado")
                for obj in lectores.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t\t {obj.correo}\t {obj.tipo_documento_id}\t {obj.documento}\t {obj.estado_user_id}")

                input("Continuar?")
            
            elif(resmenuRegistroLectores == 9):
                self.__log.info("Saliendo")
                break

    def registroBibliotecas(self):
        self.__log.info("Ingresando al Registro de Bibliotecas")
        while True:
            opcionesRegistroBibliotecas = {"\t- Registrar Bibliotecas":1,"\t- Listar Bibliotecas":2}
            menuRegistroBibliotecas = Menu("Registro de Bibliotecas",opcionesRegistroBibliotecas)
            resmenuRegistroBibliotecas = menuRegistroBibliotecas.mostrarMenu()

            if(resmenuRegistroBibliotecas == 1):
                self.__log.info("Entrando al registro de Bibliotecas")
                nuevaBiblioteca = Biblioteca()
                nombreBiblioteca = input("escriba el nombre de la Biblioteca \n")
                direccionBiblioteca = input("escriba la direccion de la Biblioteca \n")

                tipo_documento = TipoDocumento()
                print(f"\t Codigo\t Descripcion")
                for obj in tipo_documento.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del tipo de documento de la siguiente lista")
                tipo_documento_idBiblioteca = input()
                documentoBiblioteca = input("escriba el nro de documento de la Biblioteca \n")

                nuevaBiblioteca.nombre = nombreBiblioteca
                nuevaBiblioteca.direccion = direccionBiblioteca
                nuevaBiblioteca.tipo_documento_id = tipo_documento_idBiblioteca
                nuevaBiblioteca.documento = documentoBiblioteca

                nuevaBiblioteca.save()



                input("Continuar?")
            
            elif(resmenuRegistroBibliotecas == 2):
                self.__log.info("Ingresando a listar Bibliotecas")
                bibliotecas = Biblioteca()
                print(f"\t Codigo\t Nombre\t\t Direccion\t tipDoc\t NroDoc")
                for obj in bibliotecas.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t\t {obj.direccion}\t {obj.tipo_documento_id}\t {obj.documento}")

                input("Continuar?")
            
            elif(resmenuRegistroBibliotecas == 9):
                self.__log.info("Saliendo")
                break
