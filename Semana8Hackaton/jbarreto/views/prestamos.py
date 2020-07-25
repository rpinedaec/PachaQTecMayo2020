from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.estado_libro import EstadoLibro
from models.user import User
from models.tipo_documento import TipoDocumento
from models.prestamo import Prestamo
from orator import Model,DatabaseManager
from time import sleep
from datetime import datetime

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

class Prestamos:
    __log = log("Prestamos")

    def registroPrestamos (self):
        self.__log.info("Ingresando al Registro de los ")
        opcionesRegistrolos  = {"\t- Registrar Prestamos ":1,"\t- Registrar devolucion de prestamo ":2}
        menuRegistrolos  = Menu("Registro de Prestamos ",opcionesRegistrolos )
        resmenuRegistrolos  = menuRegistrolos .mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistrolos  == 1:
                self.__log.info("Entrando al registro de Prestamos ")
                nuevoPrestamo = Prestamo()
                codigoLibro = input("escriba el codigo del Libro \n")
                codigoUsuario = input("escriba el codigo del usuario \n")
                fechaPrestamo = datetime.today().strftime('%Y-%m-%d')
                bibliotecaId = 1
                flagUpdate = False

                nuevoPrestamo.user_id = codigoUsuario
                nuevoPrestamo.libros_id = codigoLibro
                nuevoPrestamo.prestado_on = fechaPrestamo
                nuevoPrestamo.bibliotecas_id = bibliotecaId

                listaLibros = Libro.where('id', '=', f'{codigoLibro}').get()
                for row in listaLibros:
                    libro = row

                if libro.estado_libro_id == 1:
                    listaAutor = Autor.where('id', '=', f'{libro.autor_id}').get()
                    for row in listaAutor:
                        autor = row

                    print("\tCodigo Usuario\t\tLibro\t\tISBN\t\tAutor\t\tBiblioteca")
                    print(f"\t{str(codigoUsuario)}\t\t{str(libro.nombre)}\t\t{str(libro.isbn)}\t\t{str(autor.nombre)}\t\t{str(bibliotecaId)}")
                    
                    registro = input("Desea registrar el prestamo Si(1)/No(0)?: ")
                    if str(registro) == '1':
                        if nuevoPrestamo.save():
                            print("Registro de prestamo satisfactorio")
                            sleep(5)
                            flagUpdate = Libro.where('id', '=', f'{codigoLibro}').update(estado_libro_id=3)

                            if flagUpdate:
                                print("Actualización de libro satisfactorio")
                                sleep(5)
                            else:
                                print("No se pudo actualizar el libro") 
                else:
                    print("No se puede prestar el libro.\nLibro ha sido prestado.")
                    sleep(5)
    
                stopMenu = False

            elif resmenuRegistrolos  == 2:    
                self.__log.info("Entrando a la devolución de libro Prestado ")
                codigoUsuario = input("escriba el codigo del usuario \n")
                fechaDevolucion = '9999-12-31'  #Constante para identificar devolucion
                flagUpdate = False

                listaDev = Prestamo.where('user_id', '=', f'{codigoUsuario}').get()
                if listaDev:
                    print("\tID Prestamo\tLibro\t\tISBN\t\tAutor\t\tBiblioteca")
                    for rowDev in listaDev:
                        if str(rowDev.prestado_on) != fechaDevolucion:  #No mostrar devoluciones
                            listaLibros = Libro.where('id', '=', f'{rowDev.libros_id}').get()
                            for rowLibro in listaLibros:
                                libro = rowLibro
                                listaAutor = Autor.where('id', '=', f'{libro.autor_id}').get()
                                for rowAutor in listaAutor:
                                    autor = rowAutor
                                print(f"\t{str(rowDev.id)}\t\t{str(libro.nombre)}\t\t{str(libro.isbn)}\t\t{str(autor.nombre)}\t\t{str(rowDev.bibliotecas_id)}")

                    idDev = input("Escriba el Id de Prestamo: ")

                    if idDev:
                        flagUpdate = Prestamo.where('id', '=', f'{idDev}').update(prestado_on=fechaDevolucion)
                        if flagUpdate:
                            print("Actualización de Devolución satisfactoria")
                            sleep(5)
                            flagUpdate = Libro.where('id', '=', f'{rowDev.libros_id}').update(estado_libro_id=1)
                            if flagUpdate:
                                print("Actualización de libro satisfactorio")
                                sleep(5)
                            else:
                                print("No se pudo actualizar el libro") 
                        else:
                            print("No se pudo actualizar Devolución") 
    
                stopMenu = False

            elif resmenuRegistrolos  == 9:
                self._log.info("Saliendo")
                stopMenu = False