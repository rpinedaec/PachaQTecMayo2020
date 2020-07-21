from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.user import User
from models.tipo_documento import TipoDocumento
from models.estado_user import EstadoUser
from models.estado_libro import EstadoLibro
from models.biblioteca import Biblioteca
from models.prestamo import Prestamo
from orator import Model,DatabaseManager
from datetime import datetime

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'W8Y6N6G7',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


class Prestamos:
    __log = log("Prestamos")

    def registroPrestamos(self):
        self.__log.info("Ingresando al Módulo de Prestamos")
        stopMenu = True
        while stopMenu:
            opcionesPrestamoLibros = {"\t- Lista de Prestamos":1,"\t- Registrar Prestamos":2, "\t- Devolucion de Libros":3}
            menuPrestamoLibros = Menu("Módulo de Prestamos",opcionesPrestamoLibros)
            resmenuPrestamoLibros = menuPrestamoLibros.mostrarMenu()
            if resmenuPrestamoLibros == 1:
                self.__log.info("Entrando a la Lista de Prestamos") 
                PrestamoN = Prestamo()
                print(str("Codigo").ljust(5)
                        +"\t "+str("Fecha Prestamo").ljust(10)
                        +"\t "+str("Usuario").ljust(10)
                        +"\t"+str("Biblioteca").ljust(25)
                        +"\t "+str("Libro").ljust(7)
                        +"\t "+str("Estado").ljust(7)
                    )
                contador= 0
                for obj in PrestamoN.all():
                    ObjUserTemp = User.find(obj.user_id)
                    ObjLibrTemp = Libro.find(obj.libros_id)
                    ObjBiblioTemp = Biblioteca.find(obj.bibliotecas_id)
                    ObjEstaLibTempp = EstadoLibro.find(ObjLibrTemp.estado_libro_id)
                    contador+=1
                    print(str(obj.id).ljust(5)
                        +"\t "+str(obj.prestamo_on).ljust(10)
                        +"\t "+str(ObjUserTemp.nombre).ljust(10)
                        +"\t"+str(ObjBiblioTemp.nombre).ljust(25)
                        +"\t "+str(ObjLibrTemp.nombre).ljust(7)
                        +"\t "+str(ObjEstaLibTempp.descripcion).ljust(7)
                        )
                if contador>0:
                    print("Lista Completa")
                else:
                    print("No hay registros")
                stopMenu = False
                    
            elif resmenuRegistroLibros == 2:
                self.__log.info("Registrar Prestamos")
                nuevo = Prestamo()

                UserN = User()
                print(f"\t Codigo\t\t\t Nombre\t\t\t Estado")
                for obj in UserN.all():
                    print(f"\t {obj.id}\t\t\t {obj.nombre}\t\t\t {obj.estado_user_id}")
                print("Escriba el id del usuario: ")
                usuario_id = input()

                LibroN = Libro()
                print(f"\t Codigo\t Libro")
                for obj in LibroN.all():
                    print(f"\t {obj.id}\t {obj.nombre}")
                print("Escriba el id del libro: ")
                libroId = input()

                BibliotecaN = Biblioteca()
                print(f"\t Codigo\t Biblioteca")
                for obj in BibliotecaN.all():
                    print(f"\t {obj.id}\t {obj.nombre}")
                print("Escriba el id de la Biblioteca: ")
                bibliotecaId = input()
 
                nuevo.user_id = usuario_id
                nuevo.libros_Id = libroId
                nuevo.prestamo_on = datetime.now()
                nuevo.bibliotecas_id = bibliotecaId
                nuevo.save()
                         
                nuevoD = Libro.find(nuevo.libros_Id)
                nuevoD.estado_libro_id = 3
                nuevoD.save()

                print("Registro completo")
                stopMenu = False
                
            elif resmenuRegistroLibros == 3:
                self.__log.info("Devolución de Libros")
                librosTemporal = []
                libroNN = Libro.where('estado_libro_id', '=', '3').get()
                for libt in libroNN.all():
                    idlibTemp = libt.id 
                    PrestamoN = Prestamo.where('libros_id', '=', f"{idlibTemp}").get()
                    for presIn in PrestamoN.all():
                        temporalDato = {
                            "id" : str(presIn.id)
                            ,"user_id" : str(presIn.user_id)
                            ,"libros_id" : str(presIn.libros_id)
                            ,"prestamo_on" : str(presIn.prestamo_on)
                            ,"bibliotecas_id" : str(presIn.bibliotecas_id)
                        }
                        librosTemporal.append(temporalDato)
                contaDD = 0
                print(f"\t Codigo\t\t "+str("Libros").ljust(15)+"\t\t Fecha\t\t Bibliotecas")
                for obj in librosTemporal:
                    contaDD += 1
                    LibTempN = Libro.find(obj["libros_id"])
                    BibliTempN = Biblioteca.find(obj["bibliotecas_id"])
                    ididD = str(obj["id"])
                    prest = str(obj["prestamo_on"])
                    print(
                        f"\t{ididD}\t\t "
                        +str(LibTempN.nombre).ljust(15)+"\t\t"
                        +prest +"\t\t"+ BibliTempN.nombre)
                if contaDD>0:
                    print("Escriba el id del Préstamo")
                    Prestamo_NID = input()
                    nuevoPresD = Prestamo.find(Prestamo_NID)
                    nuevoD = Libro.find(nuevoPresD.libros_id)
                    nuevoD.estado_libro_id = 1
                    nuevoD.save()
                    print(f"Devolucion correcta")
                else:
                    print("No hay registros")
                stopMenu = False
                
            elif resmenuRegistroLibros == 9:
                stopMenu = False
                self.__log.info("Saliendo")