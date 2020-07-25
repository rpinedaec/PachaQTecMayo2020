from models.autor import Autor
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
def insertarAutor():
    autor = Autor()
    print(f"\t Codigo\t Nombre\t Correo")
    for obj in autor.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")
    autor.nombre = input("Escriba el nombre del autor: ")
    autor.correo = input("Escriba el correo del autor: ")
    autor.save()
def modificarAutor():
    autor = Autor()
    print(f"\t Codigo\t Nombre\t Correo")
    for obj in autor.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")
    idToUpdate = int(input("Ingrese el id del autor a editar: "))
    autor = Autor.find(idToUpdate)
    autor.nombre = input("Escriba el nuevo nombre del autor: ")
    autor.correo = input("Escriba el nuevo correo del autor: ")
    autor.save()

def eliminarAutor():
    autor = Autor()
    print(f"\t Codigo\t Nombre\t Correo")
    for obj in autor.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")
    idToDelete = int(input("Ingrese el id del autor a eliminar: "))
    autor = Autor.find(idToDelete)
    autor.delete()
    