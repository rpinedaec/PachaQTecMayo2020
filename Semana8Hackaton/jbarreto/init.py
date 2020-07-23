import utils.utils
from views import registros 
from views import prestamos



log = utils.utils.log("INIT")
log.info("Iniciando programa")

def menumantenimientos():
    stopMenumantenimientos = True
    while stopMenumantenimientos:
        listaMenu = {"\t- Registrar Libros":1,"\t- Registrar Lectores":2}
        menumantenimientos = utils.utils.Menu("Menu Principal",listaMenu)
        resmenumantenimientos = menumantenimientos.mostrarMenu()
        if(resmenumantenimientos == 1):
            log.info("Ingresamos al mantenimiento de Libros")
            objRegistros = registros.Registros()
            objRegistros.registroLibros()
            stopMenumantenimientos = False

        elif(resmenumantenimientos == 2):
            log.info("Ingresamos al mantenimiento de Lectores")
            objRegistros = registros.Registros()
            objRegistros.registroLectores()
            stopMenumantenimientos = False

        elif(resmenumantenimientos == 9):
            log.info("Saliendo")
            stopMenumantenimientos = False

def menuPrestamos():
    stopMenuPrestamos = True
    while stopMenuPrestamos:
        listaMenu = {"\t- Registrar Prestamo":1,}
        menuprestamos = utils.utils.Menu("Menu Principal",listaMenu)
        menuprestamos = menuprestamos.mostrarMenu()
        log.info("Ingresamos al menu de prestamos")
        objprestamo = prestamos.Prestamos()
        objprestamo.registroPrestamos()
        stopMenuPrestamos = False

#def menuInicial():
stopMenuInicial = True
while stopMenuInicial:
    listaMenu = {"\t- Modulo de Registros":1,"\t- Modulo de Prestamos":2}
    menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)

    resMenuInicial = menuInicial.mostrarMenu()
    if(resMenuInicial == 1):
            log.info("Ingresamos al modulo de registros")
            menumantenimientos()
    elif(resMenuInicial == 2):
            log.info("Ingresamos al modulo de Prestamos")
            menuPrestamos()
else:
    log.debug("volvemos a mostrar menu")
    stopMenuInicial = False


# stopMenu = True
# while stopMenu:
#     if(resMenuInical == 1):
#         log.info("Entrando al Modulo de Registro")# mant de libros
#         objRegistros = registros.Registros()
#         objRegistros.registroLibros()
#         stopMenu = False
#     elif(resMenuInical == 9):
#         log.info("Saliendo")
#         stopMenu = False
