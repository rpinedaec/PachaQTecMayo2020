import program.utils
import moduloregis
from moduloregis import Registros
import modulopres
from modulopres import Prestamos

log = program.utils.log("INIT")
log.info("Inicando programa")

class Inicio:
    MenuInicio = True
    while MenuInicio:
        def MenuInicioMenu(self):
            dictMenuInicio = {"\t- Modulo Registro":1, "\t- Modulo Prestamo":2}
            MenuInicio = program.utils.Menu("Menu Inicio", dictMenuInicio)
            resMenuInicio = MenuInicio.mostrarMenu()
            if(resMenuInicio == 1):
                log.debug("Entro a Modulo Registro")
                dictMenuRegistro = {"\t- Libro\t\t":1, "\t- Cliente\t":2, "\t- Editorial\t":3, "\t- Autor\t\t":4}
                menuRegistro = program.utils.Menu(
                    "Menu Modulo Registro", dictMenuRegistro)
                resMenuRegistro = menuRegistro.mostrarMenu()
                if(resMenuRegistro == 1):
                    objRegistros = moduloregis.Registros()
                    objRegistros.RegistroLibros()
                elif(resMenuRegistro == 2):
                    objRegistros = moduloregis.Registros()
                    objRegistros.RegistroClientes()
                elif(resMenuRegistro == 3):
                    objRegistros = moduloregis.Registros()
                    objRegistros.RegistroEditorial()
                elif(resMenuRegistro == 4):
                    objRegistros = moduloregis.Registros()
                    objRegistros.RegistroAutor()

            elif(resMenuInicio == 2):
                log.info("Entro a Modulo Prestamo")
                dictMenuPrestamo = {"\t- Alquilar Libro\t":1, "\t- Devolver Libro\t":2}
                menuPrestamo = program.utils.Menu(
                    "Menu Modulo Prestamo", dictMenuPrestamo)
                resMenuPrestamo = menuPrestamo.mostrarMenu()
                if(resMenuPrestamo == 1):
                    objPrestamos = modulopres.Prestamos()
                    objPrestamos.Alquilar()
            
            else:
                pass
    MenuInicio = False
    


