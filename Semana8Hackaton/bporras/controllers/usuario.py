from models.usuario import Usuario
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
def insertarUsuario():
    usuario = Usuario()
    print(f"\t Codigo\t Nombre\t Correo\t Documento")
    for obj in usuario.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}")
    usuario.nombre = input("Escriba el nombre del usuario: ")
    usuario.correo = input("Escriba el correo del usuario: ")
    usuario.documento = input("Escriba el documento del usuario: ")
    usuario.save()
def modificarUsuario():
    usuario = Usuario()
    print(f"\t Codigo\t Nombre\t Correo\t Documento")
    for obj in usuario.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}")
    idtoUpdate = int(input("Escriba el id del usuario a editar: "))
    usuario = Usuario.find(idtoUpdate)
    usuario.nombre = input("Escriba el nombre del usuario: ")
    usuario.correo = input("Escriba el correo del usuario: ")
    usuario.documento = input("Escriba el documento del usuario: ")
    usuario.save()

def eliminarUsuario():
    usuario = Usuario()
    print(f"\t Codigo\t Nombre\t Correo\t Documento")
    for obj in usuario.all():
        print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.documento}")
    idToDelete = int(input("Ingrese el id del usuario a eliminar: "))
    usuario = Usuario.find(idToDelete)
    usuario.delete()
    