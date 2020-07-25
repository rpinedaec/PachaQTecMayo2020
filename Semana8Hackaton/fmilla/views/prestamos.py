from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.user import User
from models.autor import Autor
from models.biblioteca import Biblioteca
from models.estado_libro import EstadoLibro
from models.estado_user import EstadoUser
from models.tipo_documento import TipoDocumento
from models.prestamo import Prestamo
from orator import Model,DatabaseManager, SoftDeletes
import mysql.connector


class Prestamos:
    __log = log("Prestamos")
    def Prestamo(self):
        self.__log.info("Entrando al registro de prestamos")
        while True:
            opcionesPrestamo = {"\t- Hacer prestamo":1,"\t- Devolver prestamo":2, "\t- Ver prestamos":3}
            menuPrestamo = Menu("Prestamos",opcionesPrestamo)
            resmenuPrestamo = menuPrestamo.mostrarMenu()

            if(resmenuPrestamo == 1):
                nuevoPrestamo = Prestamo()
                libro = Libro()
                print(f"\t Codigo\t Nombre\t\t ISBN\t Autor\t Estado")
                x = libro.all().where('estado_libro_id',1)
                for obj in x:
                    print(f"\t {obj.id}\t {obj.nombre}\t\t {obj.isbn}\t {obj.autor_id}\t {obj.estado_libro_id}")
                idlibro = int(input("Escriba el id del libro de la siguiente lista\n "))
                #Cambiando el estado del prestamo
                libro = Libro()
                estado = libro.find(idlibro)
                estado.estado_libro_id = 3
                estado.save()
                
                lectores = User()
                print(f"\t Codigo\t Nombre\t\t Correo\t tipDoc\t NroDoc\t Estado")
                x = lectores.all().where('estado_user_id',1)
                for obj in x:
                    print(f"\t {obj.id}\t {obj.nombre}\t\t {obj.correo}\t {obj.tipo_documento_id}\t {obj.documento}\t {obj.estado_user_id}")
                print("Escriba el id del Lector de la siguiente lista")
                iduser = input()
                bibliotecas = Biblioteca()
                print(f"\t Codigo\t Nombre\t\t Direccion\t tipDoc\t NroDoc")
                for obj in bibliotecas.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t\t {obj.direccion}\t {obj.tipo_documento_id}\t {obj.documento}")
                print("Escriba el id de la biblioteca de la siguiente lista")
                idbiblioteca = input()
                print("Escriba la fecha del prestamo con este formato:")
                fecha = input("year-month-day(0000-00-00)\n")

                nuevoPrestamo.libros_id = idlibro
                nuevoPrestamo.user_id = iduser
                nuevoPrestamo.bibliotecas_id = idbiblioteca
                nuevoPrestamo.prestado_on = fecha

                nuevoPrestamo.save()
                input("Continuar?")
            
            if(resmenuPrestamo == 2):
                prestamo = Prestamo()
                print(f"\t Codigo\t User\t\t Libro\t Fecha\t Biblioteca")
                for obj in prestamo.all():
                    print(f"\t {obj.id}\t {obj.user_id}\t\t {obj.libros_id}\t {obj.prestado_on}\t {obj.bibliotecas_id}")
                print("Escriba el id del prestamo de la siguiente lista que desee devolver")
                idprestamo = int(input())
                #Cambiando el estado del libro
                x = prestamo.all().where('id',idprestamo)
                for obj in x:
                    y = obj.libros_id
                    libro = Libro()
                    estado = libro.find(y)
                    estado.estado_libro_id = 1
                    estado.save()
                #Borrando prestamo
                prestamoo = prestamo.find(idprestamo)
                prestamoo.delete()
                
                input("Continuar?")

            if(resmenuPrestamo == 3):
                prestamo = Prestamo()
                print(f"\t Codigo\t User\t\t Libro\t Fecha\t Biblioteca")
                for obj in prestamo.all():
                    print(f"\t {obj.id}\t {obj.user_id}\t\t {obj.libros_id}\t {obj.prestado_on}\t {obj.bibliotecas_id}")

                input("Continuar?")

            if(resmenuPrestamo ==9):
                break

