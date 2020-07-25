from models.editorial import Editorial 
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
def insertarEditorial():
    editorial = Editorial()
    print(f"\t Codigo\t Nombre\t Correo\t Dirección")
    for obj in editorial.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.dirección}")
    editorial.nombre = input("Escriba el nombre de la editorial: ")
    editorial.correo = input("Escriba el correo de la editorial: ")
    editorial.dirección = input("Escriba la dirección de la editorial: ")
    editorial.save()
def modificarEditorial():
    editorial = Editorial()
    print(f"\t Codigo\t Nombre\t Correo\t Dirección")
    for obj in editorial.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.dirección}")
    idToUpdate = int(input("Ingrese el id de la editorial a editar: "))
    editorial = Editorial.find(idToUpdate)
    editorial.nombre = input("Escriba el nuevo nombre de la editorial: ")
    editorial.correo = input("Escriba el nuevo correo de la editorial: ")
    editorial.dirección = input("Escriba la nueva dirección de la editorial: ")
    editorial.save()

def eliminarEditorial():
    editorial = Editorial()
    print(f"\t Codigo\t Nombre\t Correo\t Dirección")
    for obj in editorial.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.dirección}")
    idToDelete = int(input("Ingrese el id de la editorial a eliminar: "))
    editorial = Editorial.find(idToDelete)
    editorial.delete()
    