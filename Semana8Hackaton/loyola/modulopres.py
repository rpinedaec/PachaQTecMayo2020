import program.utils
import db
import init
from init import Inicio
from program.utils import log
from program.utils import Menu
from models.libro import Libro 
from models.user import User
from models.autor import Autor
from models.editorial import Editorial
from models.prestamo import Prestamo
from models.biblioteca import Biblioteca
from models.tipo_documento import TipoDocumento
from models.estado_user import EstadoUser
from models.estado_libro import EstadoLibro
from orator import Model,DatabaseManager

class Prestamos:
    __log = log("Ingresando a Modulo Prestamos")

    def Alquilar(self):
        self.__log.info("Alquilar un libro")

        estadolibro = EstadoLibro()
        print(f"\t ID\t Descripcion")
        for obj in estadolibro.all():
            print(f"\t {obj.id}\t {obj.descripcion}")

            if obj.descripcion == 1:

                libroporalquilar = Prestamo()

                cliente = User()
                print(f"\t ID\t Nombre\t CORREO\t DOCUMENTO\t ESTADO")
                for obj in cliente.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}\t {obj.estado_user_id}")
                print("Escriba el id del cliente")
                cliente = input()

                libro = Libro()
                print(f"\t ID\t Nombre\t ISBN\t Autor\t Editorial\t Estado")
                for obj in libro.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autors_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
                print("Escriba el id del libro")
                libro = input()

                DatabaseManager.table('libro').where('nombre', f'{obj.nombre}').update({'obj.estado_libro_id': 3})

                biblioteca = Biblioteca()
                print(f"\t ID\t Nombre\t DIRECCION")
                for obj in biblioteca.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}")
                print("Escriba el id de la biblioteca")
                biblioteca = input()

                libroporalquilar.users_id = cliente
                libroporalquilar.libros_id = libro
                libroporalquilar.bibliotecas_id = biblioteca

                libroporalquilar.save()

                objMenus = init.Inicio()
                objMenus.MenuInicioMenu()
               
            elif obj.descripcion == 2:
                print("Lo sentimos el libro que busca esta reservado")
                objMenus = init.Inicio()
                objMenus.MenuInicioMenu()

            elif obj.descripcion == 2:
                print("Lo sentimos el libro que busca no se encuentra disponible")
                objMenus = init.Inicio()
                objMenus.MenuInicioMenu()
        
    def Devolver(self):
        self.__log.info("Devolver un libro")

        libro = Libro()
        print(f"\t ID\t Nombre\t ISBN\t Autor\t Editorial\t Estado")
        for obj in libro.all():
            print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autors_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
        print("Escriba el id del libro")
        idlibro = input()

        DatabaseManager.table('libro').where('nombre', f'{obj.nombre}').update({'obj.estado_libro_id': 1})
        libro.libros_id = idlibro
        libro.save()

        objMenus = init.Inicio()
        objMenus.MenuInicioMenu()
