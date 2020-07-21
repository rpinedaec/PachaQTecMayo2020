from models.biblioteca import Biblioteca
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
def insertarBiblioteca():
    biblioteca = Biblioteca()
    print(f"\t Codigo\t Nombre\t Dirección\t Documento")
    for obj in biblioteca.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}\t {obj.documento}")
    biblioteca.nombre = input("Escriba el nombre de la biblioteca: ")
    biblioteca.direccion = input("Escriba la dirección de la biblioteca: ")
    biblioteca.documento = input("Ingrese el documento para la biblioteca: ")
    biblioteca.save()
def modificarBiblioteca():
    biblioteca = Biblioteca()
    print(f"\t Codigo\t Nombre\t Dirección\t Documento")
    for obj in biblioteca.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}\t {obj.documento}")
    idToUpdate = int(input("Ingrese el id de la biblioteca a editar: "))
    biblioteca = Biblioteca.find(idToUpdate)
    biblioteca.nombre = input("Escriba el nombre de la biblioteca: ")
    biblioteca.direccion = input("Escriba la dirección de la biblioteca: ")
    biblioteca.documento = input("Ingrese el documento para la biblioteca: ")
    biblioteca.save()

def eliminarBiblioteca():
    biblioteca = Biblioteca()
    print(f"\t Codigo\t Nombre\t Dirección\t Documento")
    for obj in biblioteca.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.direccion}\t {obj.documento}")
    idToDelete = int(input("Ingrese el id de la biblioteca a eliminar: "))
    biblioteca = Biblioteca.find(idToDelete)
    biblioteca.delete()
    