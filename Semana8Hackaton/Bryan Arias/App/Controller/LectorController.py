#from Model.lector import Lector
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

def BuscarDni(idtipodoc):
    DniLector = input("Ingrese el Dni del Usuario:\n")
    lector = db.table('lector').join('Tipo_Documento', 'lector.idTipo_Documento', '=', 'Tipo_Documento.idTipo_Documento').where('lector.Numero_Documento', DniLector).first()
    if lector:
        print ("Id Lector", "Tipo Documento", "Nombres\t", "Apellidos", "Numero Documeno", sep="\t")
        print (lector.idLector, lector.Descripcion, lector.Nombres, lector.Apellidos, lector.Numero_Documento, sep='\t\t')
        sleep(2)
        return lector.idLector
    else:
        Nombre = input("Ingrese el nombre del Usuario:\n")
        Apellido = input("Ingrese el apellido del Usuario:\n")
        lector = db.table('lector').insert({
            'idTipo_Documento': idtipodoc,
            'Nombres': Nombre,
            'Apellidos': Apellido,
            'Numero_Documento': DniLector
            })
        if lector:
            print("Los datos se insertaron")
            sleep(2)
        else:
            print("Error al insertar los datos")
            sleep(2)
    
