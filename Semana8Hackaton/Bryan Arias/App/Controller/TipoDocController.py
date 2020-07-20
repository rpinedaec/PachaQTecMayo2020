from orator import Model, DatabaseManager
import Utils.utils as util
from Model.tipo_documento import TipoDocumento
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

def ListAllTipoDoc():
    __log = util.log("Tipo Documento")
    td = TipoDocumento()
    tipodoc = td.all()
    for row in tipodoc:
        print(row.idTipo_Documento, row.Descripcion, sep='\t')

def BuscarTipoDoc():
    __log = util.log("Buscar Tipo Documento")
    opcion = True
    while opcion:
        try:
            id_Tipo_Doc = int(input("Ingresar id del tipo de documento:\n"))
            TipoDoc = db.table('tipo_documento').where('idTipo_Documento', id_Tipo_Doc).first()
            if TipoDoc:
                return id_Tipo_Doc
            else:
                sleep(2)
                input('Ingrese un tipo de documento valido.\a')
                opcion = True
        except Exception as e:
            __log.info(f"{e} Dato ingresado es una letra")
            sleep(2)
            print("Debe ingresar un número de la lista.\n\a")
        except KeyboardInterrupt as k:
            __log.info(f"{k} Interrupcion por teclado")
            print("Interrupcion por teclado\n\a", k)
            util.Salir()

        
