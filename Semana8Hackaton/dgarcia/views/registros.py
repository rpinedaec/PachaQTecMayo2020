from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.user import User
from models.tipo_documento import TipoDocumento
from models.estado_user import EstadoUser
from models.estado_libro import EstadoLibro
from models.biblioteca import Biblioteca 


class Registros:
    __log = log("Registros")
    def registroLibros(self):
        self.__log.info("Ingresando al Módulo de Registro")
        opcionesRegistroLibros = {"\t- Registrar Libros":1,"\t- Listar Libros":2, "\t- Registrar Usuarios":3, "\t- Listar Usuarios":4,"\t- Registrar Biblioteca":5, "\t- Listar Biblioteca":6}
        menuRegistroLibros = Menu("Módulo de Registro",opcionesRegistroLibros)
        resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistroLibros == 1:
                self.__log.info("Entrando al Registro de Libros")
                nuevoLibro = Libro()
                nombreLibro = input("Escriba el nombre del libro: \n")
                isbnLibro = input("Escriba el ISBN del libro: \n")

                autores = Autor()
                print(f"\t Codigo\t Nombre\t Tipo")
                for obj in autores.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.tipo}")
                print("Escriba el id del Autor de la siguiente lista:")
                autor_idLibro = input()
                estados = EstadoLibro()
                print(f"\t Codigo\t Estado")
                for obj in estados.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                print("Escriba el id del Estado del Libro de la siguiente lista:")
                estadoLibro = input()

                nuevoLibro.nombre = nombreLibro
                nuevoLibro.isbn = isbnLibro
                nuevoLibro.autor_id = autor_idLibro
                nuevoLibro.estado_libro_id = estadoLibro

                nuevoLibro.save()
                print("Registro Completo")
                stopMenu = False
            
            elif resmenuRegistroLibros == 2:
                self.__log.info("Entrando a la Lista de libros") 
                libros = Libro()  
                print("\t "+str("Codigo").ljust(10)+"\t\t\t "+str("Libro").ljust(10)+"\t\t\t "+str("ISBN").ljust(10)+"\t\t\t "+str("Autor").ljust(10))
                contador= 0
                for obj in libros.all():
                    contador+=1
                    print("\t"+str(obj.id).ljust(10)+"\t\t\t "+str(obj.nombre).ljust(10)+"\t\t\t "+str(obj.isbn).ljust(10)+"\t\t\t "+str(obj.autor_id).ljust(10))
                if contador>0:
                    print("Lista completa")
                else:
                    print("No hay registros")
                stopMenu = False
            
            elif resmenuRegistroLibros == 3:
                self.__log.info("Entrando al Registro de Usuario")
                nuevo = User()
                nombre = input("Nombre Completo: ")
                correo = input("Correo: ") 
                tipoDoc = TipoDocumento()
                print(f"\t Codigo\t TipoDocumento") 
                for obj in tipoDoc.all():
                    print(f"\t {obj.id}\t {obj.descripcion}") 
                tipoDoc_Id = input("Ingrese el Tipo de Documento: ")
                tipoDoc_Desc = input("Ingrese el número: ")                
                estados = EstadoUser()
                print(f"\t Codigo\t Estado")
                for obj in estados.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                estado_Id = input("Estado: ")
                nuevo.nombre = nombre
                nuevo.correo = correo
                nuevo.tipo_documento_id = tipoDoc_Id
                nuevo.documento = tipoDoc_Desc
                nuevo.estado_user_id = estado_Id
                nuevo.save()
                print("Registro completo")
                stopMenu = False
            
            elif resmenuRegistroLibros == 4:
                self.__log.info("Entrando a la Lista de Usuarios") 
                Usuario = User()  
                print("\t "+str("Codigo").ljust(10)+"\t\t\t "+str("Usuario").ljust(10)+"\t\t\t "+str("Correo").ljust(10))
                contador= 0
                for obj in Usuario.all():
                    contador+=1
                    print("\t"+str(obj.id).ljust(10)+"\t\t\t "+str(obj.nombre).ljust(10)+"\t\t\t "+str(obj.correo).ljust(10))
                if contador>0:
                    print("Lista Completa")
                else:
                    print("No hay nadie registrado")
                stopMenu = False
            
            elif resmenuRegistroLibros == 5:
                self.__log.info("Entrando al Registro de Bibliotecas")
                nuevo = Biblioteca()
                nombre = input("Escriba el nombre: ")
                direccion = input("Escriba la direccion: ") 
                         
                nuevo.nombre = nombre
                nuevo.direccion = direccion
                nuevo.save()
                print("Registro Completo")
                stopMenu = False
            
            elif resmenuRegistroLibros == 6:
                self.__log.info("Entrando a la Lista de Bibliotecas") 
                BibliotecaN = Biblioteca()  
                print("\t "+str("Codigo").ljust(10)+"\t\t\t "+str("Biblioteca").ljust(10)+"\t\t\t "+str("Direccion").ljust(10))
                contador= 0
                for obj in BibliotecaN.all():
                    contador+=1
                    print("\t"+str(obj.id).ljust(10)+"\t\t\t "+str(obj.nombre).ljust(10)+"\t\t\t "+str(obj.direccion).ljust(10))
                if contador>0:
                    print("Lista Completa")
                else:
                    print("No hay registros")
                stopMenu = False
            
            elif resmenuRegistroLibros == 9:
                self._log.info("Saliendo")
