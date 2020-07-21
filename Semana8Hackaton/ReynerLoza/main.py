from db import *
from models.libro import Libros
from models.prestamo import Prestamos
from models.lector import Lectores

db = DatabaseManager(config)
Model.set_connection_resolver(db)

def menuPrincipal():
    print("Ingrese opcion:")
    print("1. Mostrar Lectores")
    print("2. Mostrar Libros")
    print("3. Mostrar Prestamos")
    print("4. Registrar Prestamo por Usuario")
    print("5. Se entrego libro devuelta")
    value = input()
    if value == 2:
        libros = Libros()
        for libro in libros.all():
            print(f"\t {libro.libro_id}\t {libro.libro_nombre}\t {libro.libro_autor}\t {libro.estado} \t {libro.estado}")
    elif value == 1:
        lectores = Lectores()
        for lector in lectores.all():
            print(f"\t {lector.lector_id}\t {lector.lector_nombre}\t")
    elif value == 3:
        prestamos = Prestamos()
        for prestamo in prestamos.all():
            print(f"\t {prestamo.prestamo_id}\t {prestamo.lector_id}\t")
    elif value == 4:
        #Mostrar Libros
        libros = Libros()
        for libro in libros.all():
            print(f"\t {libro.libro_id}\t {libro.libro_nombre}\t {libro.libro_autor}\t {libro.estado}")

        idLibro = input()
        #Mostrar Lectores
        lectores = Lectores()
        for lector in lectores.all():
            print(f"\t {lector.lector_id}\t {lector.lector_nombre}\t")
        
        idLector = input()

        #Escoger el libro que escogera el Lector
        db.tables('prestamos').insert(lector_id = int(idLector) )

        #Actualizar estado del Libro
        #Mostramos el prestamo a escoger
        db.tables("prestamos"),get()

        idPrestamo = input()


        db.table('libros').where('id',idLibro).update(idPrestamo = idPrestamo,estado = 1)










        

from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.estado_libro import EstadoLibro



class Registros:
    __log = log("Registros")
    def registroLibros(self):
        self.__log.info("Ingresando al Registro de Libros")
        opcionesRegistroLibros = {"\t- Registrar Libros":1,"\t- Listar Libros":2}
        menuRegistroLibros = Menu("Registro de Libros",opcionesRegistroLibros)
        resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
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



                stopMenu = False
            
            elif resmenuRegistroLibros == 9:
                self._log.info("Saliendo")

    def registroLectores(self):
        pass

    