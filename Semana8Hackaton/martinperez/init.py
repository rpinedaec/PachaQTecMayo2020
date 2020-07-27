import utils.utils
from views import registros 
from views import prestamos 



log = utils.utils.log("INIT")
log.info("Inicando programa")

stopMenu = True
while stopMenu:    
    listaMenu = {"\t- Modulo de Registo":1,"\t- Modulo de Prestamos":2}
    menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)
    resMenuInical = menuInicial.mostrarMenu()
    if(resMenuInical == 1):
        log.info("Entrando al Modulo de Resistro")
        objRegistros = registros.Registros()
        objRegistros.registroLibros()
    elif(resMenuInical == 2):
        log.info("Entrando al Modulo de Prestamos")
        objRegistrosP = prestamos.Registros()
        objRegistrosP.registroPrestamos()
    elif(resMenuInical == 9):
        log.info("Saliendo")
        stopMenu = False
