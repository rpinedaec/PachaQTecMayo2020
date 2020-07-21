from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.user import User
from models.tipo_documento import TipoDocumento
from models.estado_user import EstadoUser
from models.estado_libro import EstadoLibro



class Registros:
    __log = log("Registros")
    def registroLibros(self):
        self.__log.info("Ingresando al Registro de Libros")
        opcionesRegistroLibros = {"\t- Registrar Libros":1,"\t- Listar Libros":2,"\t- Registrar Lector":3,"\t- Listar Lectores":4}
        menuRegistroLibros = Menu("Registro de Libros",opcionesRegistroLibros)
        resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistroLibros == 1:
                self.__log.info("Entrando al registro de libros")
                print("Registrar Libros")
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
                stopMenu = False
            if resmenuRegistroLibros == 2:
                self.__log.info("Entrando a listar libros")
                print("Listar libros")
                libros=Libro()
                print(f"\t Codigo\t Nombre\t ISBN")
                for obj in libros.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}")

                stopMenu = False

            if resmenuRegistroLibros == 3:
                self.__log.info("Entrando al registro de lectores")
                print("Registrar Lectores")
                nuevoUser = User()
                nombreUser = input("escriba el nombre del nuevo Usuario \n")
                correoUser = input("escriba el correo \n")
                
                tipodocumento = TipoDocumento()
                print(f"\t id\t Descripcion")
                for obj in tipodocumento.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del tipo de documento de la anterior lista")
                documento_idTipodocumento = input()
                documentoUser = input("escriba el numero del documento \n")

                estadoUser = EstadoUser()
                print(f"\t id\t descripcion")
                for obj in estadoUser.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del Estado del Usuario de la anterior lista")
                estado_User = input()

                nuevoUser.nombre = nombreUser
                nuevoUser.correo = correoUser
                nuevoUser.tipo_documento_id = documento_idTipodocumento
                nuevoUser.documento = documentoUser
                nuevoUser.estado_user_id = estado_User

                nuevoUser.save()
                stopMenu = False

            if resmenuRegistroLibros == 4:
                self.__log.info("Entrando a listar lector")
                print("Listar lectores")
                Usuarios=User()
                print(f"\t Codigo\t Nombre\t correo")
                for obj in Usuarios.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")

                stopMenu = False

            elif resmenuRegistroLibros == 9:
                self._log.info("Saliendo")

    def registroLectores(self):
        self.__log.info("Ingresando al Registro de Libros")
        opcionesRegistroLibros = {"\t- Registrar Libros":1,"\t- Listar Libros":2}
        menuRegistroLibros = Menu("Registro de Libros",opcionesRegistroLibros)
        resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistroLibros == 1:
                self.__log.info("Entrando al registro de libros")
                print("Registrar Libros")
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
                stopMenu = False
            if resmenuRegistroLibros == 2:
                self.__log.info("Entrando a listar libros")
                print("Listar libros")
                libros=Libro()
                print(f"\t Codigo\t Nombre\t ISBN")
                for obj in libros.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}")

                stopMenu = False    
            elif resmenuRegistroLibros == 9:
                self._log.info("Saliendo")
