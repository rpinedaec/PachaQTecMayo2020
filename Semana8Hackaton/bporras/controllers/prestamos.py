from models.autor import Autor
from models.prestamo import Prestamo
from models.usuario import Usuario
from models.libro import Libro
from models.biblioteca import Biblioteca
from orator import Model,DatabaseManager
from datetime import date
config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': '1234',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)
def reservarLibro():
    usuario = Usuario()
    print(f"\t Codigo\t Nombre\t Correo\t Documento")
    for obj in usuario.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}")
    idUsuario = int(input("Escriba el id del usuario que realiza la reserva: "))
    libro = Libro()
    print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Editorial\tEstado")
    for obj in libro.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
    idLibro = int(input("Ingrese el id del libro a reservar: "))
    libro = Libro.find(idLibro)
    libro.estado_libro_id = 2
    libro.save()
    biblioteca = Biblioteca()
    print(f"\t Codigo\t Nombre\t Dirección\t Documento")
    for obj in biblioteca.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}\t {obj.documento}")
    idBiblioteca = int(input("Ingrese el id de la biblioteca donde se reservara: "))
    prestamo = Prestamo()
    prestamo.usuario_id = idUsuario
    prestamo.libros_id = idLibro
    prestamo.prestado_on = str(date.today())
    prestamo.bibliotecas_id = idBiblioteca
    prestamo.save()
def retirarLibro():
    usuario = Usuario()
    print(f"\t Codigo\t Nombre\t Correo\t Documento")
    for obj in usuario.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}")
    idUsuario = int(input("Escriba el id del usuario que realiza el retiro: "))
    libro = Libro()
    print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Editorial\tEstado")
    for obj in libro.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
    idLibro = int(input("Ingrese el id del libro a reservar: "))
    libro = Libro.find(idLibro)
    libro.estado_libro_id = 3
    libro.save()
    biblioteca = Biblioteca()
    print(f"\t Codigo\t Nombre\t Dirección\t Documento")
    for obj in biblioteca.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}\t {obj.documento}")
    idBiblioteca = int(input("Ingrese el id de la biblioteca donde se reservara: "))
    prestamo = Prestamo()
    prestamo.usuario_id = idUsuario
    prestamo.libros_id = idLibro
    prestamo.prestado_on = str(date.today())
    prestamo.bibliotecas_id = idBiblioteca
    prestamo.save()
def devolverLibro():
    usuario = Usuario()
    print(f"\t Codigo\t Nombre\t Correo\t Documento")
    for obj in usuario.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}")
    idUsuario = int(input("Escriba el id del usuario que realiza la reserva: "))
    libro = Libro()
    print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Editorial\tEstado")
    for obj in libro.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
    idLibro = int(input("Ingrese el id del libro a reservar: "))
    libro = Libro.find(idLibro)
    libro.estado_libro_id = 1
    libro.save()
    biblioteca = Biblioteca()
    print(f"\t Codigo\t Nombre\t Dirección\t Documento")
    for obj in biblioteca.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}\t {obj.documento}")
    idBiblioteca = int(input("Ingrese el id de la biblioteca donde se reservara: "))
    prestamo = Prestamo()
    prestamo.usuario_id = idUsuario
    prestamo.libros_id = idLibro
    prestamo.prestado_on = str(date.today())
    prestamo.bibliotecas_id = idBiblioteca
    prestamo.save()
