from orator import Model, DatabaseManager
from time import sleep
config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'admin',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)

def AddAutor():
    Nombre = input("Ingresar Nombre del Autor:\n")
    Correo = input("Ingresar Correo del Autor:\n")
    res = db.table("Autor").insert({
        'Nombre_Autor' : Nombre,
        'Correo' : Correo
    })
    if res:
        print("Se ah insertado correctamente.")
        sleep(2)
    else:
        print("Hubo un problema al insertar el dato.\a")
        sleep(2)

def ListAllAutor():
    res = db.table("Autor").get()
    print("Id","Nombre Autor", "Correo", sep="\t")
    for row in res:
        print(row.idAutor, row.Nombre_Autor, row.Correo, sep="\t")
    sleep(2)
    
def UpdateAutor():
    ListAllAutor()
    idAutor = input("Ingresar Id del Autor:\n")
    Nombre = input("Ingresar nuevo Nombre del Autor:\n")
    Correo = input("Ingresar nuevo Correo del Autor:\n")
    resup = db.table("Autor").where("idAutor", idAutor).update({
        'Nombre_Autor' : Nombre,
        'Correo' : Correo          
    })
    if resup:
        print("Se ah modificado al autor")
        sleep(2)
    else:
        print("No fue posible modificar al autor")
        sleep(2)
