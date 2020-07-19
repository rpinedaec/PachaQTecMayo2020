import utils.utils
from views import registros 



log = utils.utils.log("INIT")
log.info("Inicando programa")


listaMenu = {"\t- Modulo de Registo":1,"\t- Modulo de Prestamos":2}
menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)

resMenuInical = menuInicial.mostrarMenu()
stopMenu = True
while stopMenu:
    if(resMenuInical == 1):
        log.info("Entrando al Modulo de Resistro")
        objRegistros = registros.Registros()
        objRegistros.registroLibros()
        stopMenu = False
    elif(resMenuInical == 9):
        log.info("Saliendo")
        stopMenu = False
