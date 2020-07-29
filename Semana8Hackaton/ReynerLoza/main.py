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









