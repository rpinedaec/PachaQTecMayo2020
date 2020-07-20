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

def AddEditorial():
    Nombre = input("Ingresar Nombre de la Editorial:\n")
    res = db.table("Editorial").insert({
        'Nombre_Editorial' : Nombre
    })
    if res:
        print("Se ah insertado correctamente.")
        sleep(2)
    else:
        print("Hubo un problema al insertar el dato.\a")
        sleep(2)

def ListAllEditorial():
    res = db.table("Editorial").get()
    print("Id","Nombre Editorial", sep="\t")
    for row in res:
        print(row.idEditorial, row.Nombre_Editorial, sep="\t")
    sleep(2)
    
def UpdateEditorial():
    ListAllEditorial()
    idEditorial = input("Ingresar Id de la Editorial:\n")
    Nombre = input("Ingresar nuevo Nombre de la Editorial:\n")
    resup = db.table("Editorial").where("idEditorial", idEditorial).update({
        'Nombre_Editorial' : Nombre      
    })
    if resup:
        print("Se ah modificado la editorial")
        sleep(2)
    else:
        print("No fue posible modificar la editorial")
        sleep(2)
