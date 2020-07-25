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
        'password': 'SH4wnM3nd3s',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


log = utils.utils.log("INIT")
log.info("Inicando programa")



while True:
    listaMenu = {"\t- Modulo de Registo":1,"\t- Modulo de Prestamos":2}
    menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)
    resMenuInical = menuInicial.mostrarMenu()
    if(resMenuInical == 1):
        log.info("Entrando al Modulo de Resistro")
        while True:
            listaMenuR = {"\t- Libros":1,"\t- Lectores":2, "\t- Bibliotecas":3}
            menuR =  utils.utils.Menu("Menu Registro",listaMenuR)
            resMenuR = menuR.mostrarMenu()
            if(resMenuR == 1):
                objRegistrosLibros = registros.Registros()
                objRegistrosLibros.registroLibros()
            elif(resMenuR == 2):
                objRegistrosLectores = registros.Registros()
                objRegistrosLectores.registroLectores()
            elif(resMenuR == 3):
                objRegistrosBibliotecas = registros.Registros()
                objRegistrosBibliotecas.registroBibliotecas()
            elif(resMenuR == 9):
                log.info("Salir")
                break
    
    elif(resMenuInical == 2):
        objPrestamo = prestamos.Prestamos()
        objPrestamo.Prestamo()

    elif(resMenuInical == 9):
        log.info("Saliendo")
        break
