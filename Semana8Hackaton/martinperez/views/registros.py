from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.user import User
from models.tipo_documento import TipoDocumento
from models.estado_user import EstadoUser
from models.estado_libro import EstadoLibro
from models.biblioteca import Biblioteca 
from orator import Model,DatabaseManager

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'passmysqlmartin',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


class Registros:
    __log = log("Registros")

    def registroLibros(self):
        self.__log.info("Ingresando al Registro de Libros")
        stopMenu = True
        while stopMenu:
            opcionesRegistroLibros = {"\t- Listar Libros":1, "\t- Listar Usuarios":2,"\t- Listar Biblioteca":3
                                    ,"\t- Registrar Libros":4, "\t- Registrar Usuarios":5,"\t- Registrar Biblioteca":6}
            menuRegistroLibros = Menu("Registro de Libros",opcionesRegistroLibros)
            resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
            if resmenuRegistroLibros == 1:
                self.__log.info("Entrando al listar de libros") 
                libros = Libro()  
                print("\t "+str("Codigo").ljust(10)+"\t\t\t "+str("Libro").ljust(10)+"\t\t\t "+str("ISBN").ljust(10)+"\t\t\t "+str("Autor").ljust(10))
                contador= 0
                for obj in libros.all():
                    contador+=1
                    print("\t"+str(obj.id).ljust(10)+"\t\t\t "+str(obj.nombre).ljust(10)+"\t\t\t "+str(obj.isbn).ljust(10)+"\t\t\t "+str(obj.autor_id).ljust(10))
                if contador>0:
                    input("Listado completo, enter para continuar..")
                else:
                    input("Sin datos...")
            elif resmenuRegistroLibros == 2:
                self.__log.info("Entrando al listar de Usuarios") 
                Usuario = User()  
                print("\t "+str("Codigo").ljust(10)+"\t\t\t "+str("Usuario").ljust(10)+"\t\t\t "+str("Correo").ljust(10))
                contador= 0
                for obj in Usuario.all():
                    contador+=1
                    print("\t"+str(obj.id).ljust(10)+"\t\t\t "+str(obj.nombre).ljust(10)+"\t\t\t "+str(obj.correo).ljust(10))
                if contador>0:
                    input("Listado completo, enter para continuar..")
                else:
                    input("Sin datos...")
            elif resmenuRegistroLibros == 3:
                self.__log.info("Entrando al listar de Bibliotecas") 
                BibliotecaN = Biblioteca()  
                print("\t "+str("Codigo").ljust(10)+"\t\t\t "+str("Biblioteca").ljust(10)+"\t\t\t "+str("Direccion").ljust(10))
                contador= 0
                for obj in BibliotecaN.all():
                    contador+=1
                    print("\t"+str(obj.id).ljust(10)+"\t\t\t "+str(obj.nombre).ljust(10)+"\t\t\t "+str(obj.direccion).ljust(10))
                if contador>0:
                    input("Listado completo, enter para continuar..")
                else:
                    input("Sin datos...")
            elif resmenuRegistroLibros == 4:
                self.__log.info("Entrando al registro de libros")
                nuevoLibro = Libro()
                nombreLibro = input("escriba el nombre del Libro \n")
                isbnLibro = input("escriba en ISBN del libro \n")

                autores = Autor()
                print(f"\t Codigo\t Nombre\t Tipo")
                for obj in autores.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.tipo}")
                print("Escriba el id del Autor de la siguiente lista")
                autor_idLibro = input()
                estados = EstadoLibro()
                print(f"\t Codigo\t Estado")
                for obj in estados.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del Estado del Libro de la siguiente lista")
                estadoLibro = input()

                nuevoLibro.nombre = nombreLibro
                nuevoLibro.isbn = isbnLibro
                nuevoLibro.autor_id = autor_idLibro
                nuevoLibro.estado_libro_id = estadoLibro

                nuevoLibro.save()
                input("Registro completo, enter para continuar..")
            elif resmenuRegistroLibros == 5:
                self.__log.info("Entrando al registro de Usuario")
                nuevo = User()
                nombre = input("escriba el nombre: ")
                correo = input("escriba el correo: ") 
                tipoDoc = TipoDocumento()
                print(f"\t Codigo\t TipoDocumento") 
                for obj in tipoDoc.all():
                    print(f"\t {obj.id}\t {obj.descripcion}") 
                tipoDoc_Id = input("Escriba el id de la siguiente lista: ")
                tipoDoc_Desc = input("Documento: ")                
                estados = EstadoUser()
                print(f"\t Codigo\t Estado")
                for obj in estados.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                estado_Id = input("Escriba el id del Estado del Libro de la siguiente lista: ")
                nuevo.nombre = nombre
                nuevo.correo = correo
                nuevo.tipo_documento_id = tipoDoc_Id
                nuevo.documento = tipoDoc_Desc
                nuevo.estado_user_id = estado_Id
                nuevo.save()
                input("Registro completo, enter para continuar..")
            elif resmenuRegistroLibros == 6:
                self.__log.info("Entrando al registro de Bibliotecas")
                nuevo = Biblioteca()
                nombre = input("escriba el nombre: ")
                direccion = input("escriba el direccion: ") 
                tipoDoc = TipoDocumento()
                print(f"\t Codigo\t TipoDocumento")
                #listaTipoDoc = []
                for obj in tipoDoc.all():
                #    objt = { "codigo" : obj.id, "descripcion" : obj.descripcion }
                #    listaTipoDoc.append(objt)
                    print(f"\t {obj.id}\t {obj.descripcion}")
                tipoDoc_Id = input("Escriba el id de la siguiente lista: ")
                tipoDoc_Desc = input("Documento: ")
                 
                nuevo.nombre = nombre
                nuevo.direccion = direccion
                nuevo.tipo_documento_id = tipoDoc_Id
                nuevo.documento = tipoDoc_Desc 
                nuevo.save()
                input("Registro completo, enter para continuar..")
            elif resmenuRegistroLibros == 9:
                stopMenu = False
                self.__log.info("Saliendo")

    def registroLectores(self):
        pass


