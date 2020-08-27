from orator import DatabaseManager, Model
import utils.utils
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
resMenuInicial = menuInicial.mostrarMenu()
stopMenu = True
while stopMenu:
    if (resMenuInicial == 1):
        log.info("Entrando al Modulo de Registro")
        listaMenu = {"\t- Registro de Libros":1,"\t- Registro de Lectores":2}
        menuRegistro =  utils.utils.Menu("Menu de Registros",listaMenu)
        resmenuRegistro = menuRegistro.mostrarMenu()
        if (resmenuRegistro == 1):
            objRegistros = registros.Registros()
            objRegistros.registroLibros()
        elif (resmenuRegistro == 2):
            objRegistros = registros.Registros()
            objRegistros.registroLectores()
        else:
            log.info("Saliendo")
            stopMenu = False
    else:
        objPrestamo = prestamo.Prestamo()
        objPrestamo.prestamoLibros()
