from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.estado_libro import EstadoLibro
from models.user import User
from models.tipo_documento import TipoDocumento
from orator import Model,DatabaseManager
from time import sleep

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'mysql1',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


class Registros:
    __log = log("Registros")

    def registroLibros (self):
        self.__log.info("Ingresando al Registro de los ")
        opcionesRegistrolos  = {"\t- Registrar Libros ":1,"\t- Listar Libros ":2}
        menuRegistrolos  = Menu("Registro de Libros ",opcionesRegistrolos )
        resmenuRegistrolos  = menuRegistrolos .mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistrolos  == 1:
                self.__log.info("Entrando al registro de Libros ")
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

            elif resmenuRegistrolos  == 2:    
                self.__log.info("Entrando  a consultar los ")    
                listarLibro = Libro()
                print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Estado de Libro")
                for obj in listarLibro.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.estado_libro_id}")
                sleep(5)
                stopMenu = False

            elif resmenuRegistrolos  == 9:
                self._log.info("Saliendo")

    def registroLectores(self):
        self.__log.info("Ingresando al Registro de Lectores")
        opcionesRegistroLectores = {"\t- Registrar Lectores":1,"\t- Listar Lectores":2}
        menuRegistroLectores = Menu("Registro de Lectores",opcionesRegistroLectores)
        resmenuRegistroLectores = menuRegistroLectores.mostrarMenu()
        #menuRegistrolos .mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistroLectores == 1:
                self.__log.info("Entrando al registro de lectores")
                nuevoLector = User()
                nombreLector = input("Escriba el nombre del lector \n")
                correoLector = input("Escriba el correo del lector \n")
                
                tipodocumentos = TipoDocumento()
                print(f"\t Codigo\t Descripción")
                for obj in tipodocumentos.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del tipo de documento de la siguiente lista \n")
                tipodocumento_idLector = input()

                nroDocumentoLector = input("Escriba el numero de documento \n")
                estado_usuarioLector = 1

                nuevoLector.nombre = nombreLector
                nuevoLector.correo = correoLector
                nuevoLector.tipo_documento_id = tipodocumento_idLector
                nuevoLector.documento = nroDocumentoLector
                nuevoLector.estado_user_id = estado_usuarioLector

                nuevoLector.save()

                stopMenu = False

            elif resmenuRegistroLectores == 2:
                self.__log.info("Entrando  a consultar los lectores")    
                listarLectores = User()
                print(f"\t Codigo\t Nombre\t Correo\t Tipo de documento\t Documento\t Estado de Usuario")
                for obj in listarLectores.all():
                    #print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.tipodocumento_id}\t {obj.documento}\t {obj.estado_user_id}")
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.tipo_documento_id}\t {obj.documento}\t {obj.estado_user_id}")
                sleep(5)
                stopMenu = False    