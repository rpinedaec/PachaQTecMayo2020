from utils.utils import log
from utils.utils import Menu
from models.libros import Libros
from models.autor import Autor
from models.estadolibro import Estado_libro



class Prestamo:
    __log = log("Prestamos")
    def prestamoLibros(self):
        self.__log.info("Entrando a prestamos de libros")
        opcionesPrestamoLibros = {"\t- Solicitar un libro":1,"\t- Devolver un Libro":2}
        menuPrestamoLibros = Menu("Registro de Libros",opcionesPrestamoLibros)
        resmenuPrestamoLibros = menuPrestamoLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuPrestamoLibros == 1:
                self.__log.info("Entrando a prestamos de libros")
                libros = Libros()
                for libro in libros.all():
                    print(f"\t {libro.libro_id}\t {libro.nombre}\t {libro.isbn}\t {libro.autor_id}")
                
                isbnLibro = input("Escriba en ISBN del libro \n")
                Libros.table('libros').where('isbn',isbnLibro).update(estado_libro_id = estado_libro_id,estado = 'P')
                stopMenu = False
            elif resmenuPrestamoLibros == 2:
                self.__log.info("Entrando a devolucion de libros")
                libros = Libros()
                print('Ingrese el isbn del libro a devolver')
                print('Podrá encontrar el número en la tapa del libro')
                isbnDev = input ('Ingrese el isbn aquí: ')
                Libros.table('libros').where('isbn',isbnDev).update(estado_libro_id = estado_libro_id,estado = 'D')
                stopMenu = False
            elif resmenuPrestamoLibros == 9:
                self._log.info("Saliendo")
