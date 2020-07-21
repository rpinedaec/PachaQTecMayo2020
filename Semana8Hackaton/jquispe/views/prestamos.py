from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.estado_libro import EstadoLibro
from models.user import User
from orator import Model,DatabaseManager

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'uni20100420f',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


class Prestamos:
    __log = log("Prestamos")
    def registroPrestamos(self):
        self.__log.info("Ingresando al menu de Prestamos")
        opcionesPrestamoLibros = {"\t- Registrar Prestamo":1,"\t- Registrar Devolucion":2}
        menuPrestamoLibros = Menu("Prestamo de Libros",opcionesPrestamoLibros)
        resmenuPrestamoLibros = menuPrestamoLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuPrestamoLibros == 1:
                self.__log.info("Entrando al prestamo de libros")
                Libro = Libro()
                #nombreLibro = input("escriba el nombre del Libro \n")
                #isbnLibro = input("escriba en ISBN del libro \n")

                #autores = Autor()
                #print(f"\t Codigo\t Nombre\t Tipo")
                #for obj in autores.all():
                #    print(f"\t {obj.id}\t {obj.nombre}\t {obj.tipo}")
                #print("Escriba el id del Autor de la siguiente lista")
                #autor_idLibro = input()
                #estados = EstadoLibro()
                #print(f"\t Codigo\t Estado")
                #for obj in estados.all():
                #    print(f"\t {obj.id}\t {obj.descripcion}")
                #print("Escriba el id del Estado del Libro de la siguiente lista")
                #estadoLibro = input()

                #nuevoLibro.nombre = nombreLibro
                #nuevoLibro.isbn = isbnLibro
                #nuevoLibro.autor_id = autor_idLibro
                #nuevoLibro.estado_libro_id = estadoLibro

                #nuevoLibro.save()



                stopMenu = False
            
            elif resmenuRegistroLibros == 9:
                self._log.info("Saliendo")

    def registroLectores(self):
        pass