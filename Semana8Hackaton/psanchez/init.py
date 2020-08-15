from orator import DatabaseManager, Model
import utils
import prestamo
import registros


config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'hackathons8',
        'user': 'root',
        'password': 'pachaqtec',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)


log = utils.utils.log("INIT")
log.info("Iniciando programa")


listaMenu = {"\t- Registro":1,"\t- Prestamos":2}
menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)
opcion_mp = input('Escribe la opción: ')

if opcion_mp == 1:
    registros.Registros()
else:
    prestamo.Prestamo()