import utils.utils
from views import registros
from views import prestamos 
from orator import Model,DatabaseManager
config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'uni20100420f',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

log = utils.utils.log("INIT")
log.info("Iniciando programa")


listaMenu = {"\t- Modulo de Registro":1,"\t- Modulo de Prestamos":2}
menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)

resMenuInical = menuInicial.mostrarMenu()
stopMenu = True
while stopMenu:
    if(resMenuInical == 1):
        log.info("Entrando al Modulo de Registro")
        objRegistros = registros.Registros()
        objRegistros.registroLibros()
        stopMenu = False
    if(resMenuInical == 2):
        log.info("Entrando al Modulo de Prestamos")
        objPrestamos = prestamos.Prestamos()
        objPrestamos.registroPrestamos()
        stopMenu = False
    elif(resMenuInical == 9):
        log.info("Saliendo")
        stopMenu = False
