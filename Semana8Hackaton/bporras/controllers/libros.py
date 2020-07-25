from models.libro import Libro
from models.autor import Autor
from models.editorial import Editorial
from models.estado_libro import EstadoLibro
from orator import Model,DatabaseManager
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
def insertarLibro():
    libro = Libro()
    print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Editorial\tEstado")
    for obj in libro.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
    libro.nombre = input("Escriba el nombre del libro: ")
    libro.isbn = input("Ingrese el codigón ISBN del libro: ")
    autores = Autor()
    print(f"\t Codigo\t Nombre\t Tipo")
    for obj in autores.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")
    libro.autor_id = int(input("Ingrese el id del autor del libro: "))
    editorial = Editorial()
    print(f"\t Codigo\t Nombre\t Correo\t Dirección")
    for obj in editorial.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.dirección}")
    libro.editorial_id = int(input("Ingrese el id de la editorial del libro: "))
    libro.estado_libro_id = 1
    libro.save()
def modificarLibro():
    libro = Libro()
    print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Editorial\tEstado")
    for obj in libro.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
    idToUpdate = int(input("Ingrese el id del libro a editar: "))
    libro = libro.find(idToUpdate)
    libro.nombre = input("Escriba el nombre del libro: ")
    libro.isbn = input("Ingrese el codigón ISBN del libro: ")
    autores = Autor()
    print(f"\t Codigo\t Nombre\t Tipo")
    for obj in autores.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")
    libro.autor_id = int(input("Ingrese el id del autor del libro: "))
    editorial = Editorial()
    print(f"\t Codigo\t Nombre\t Correo\t Dirección")
    for obj in editorial.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.dirección}")
    libro.editorial_id = int(input("Ingrese el id de la editorial del libro: "))
    libro.estado_libro_id = 1
    libro.save()

def eliminarLibro():
    libro = Libro()
    print(f"\t Codigo\t Nombre\t ISBN\t Autor\t Editorial\tEstado")
    for obj in libro.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autor_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
    idToUpdate = int(input("Ingrese el id del libro a editar: "))
    libro = libro.find(idToUpdate)
    libro.delete()
    