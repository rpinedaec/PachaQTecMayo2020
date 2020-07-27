import program.utils
import db
from program.utils import log
from program.utils import Menu
from models.libro import Libro 
from models.user import User
from models.autor import Autor
from models.editorial import Editorial
from models.tipo_documento import TipoDocumento
from models.estado_user import EstadoUser
import models.estado_libro 
from orator import Model,DatabaseManager

class Registros:
    __log = log("Registros")
    def RegistroLibros(self):
        self.__log.info("Ingresando al Registro de Libros")
        opcionesRegisLibros = {"\t- Registrar Libro":1, "\t- Listar Libros":2, "\t- Eliminar Libros":3}
        MenuRegisLibros = Menu("Menu Modulo Libros", opcionesRegisLibros)
        regisLibros = MenuRegisLibros.mostrarMenu()
        menuRegisLib = True
        while menuRegisLib:
            if(regisLibros == 1):
                nuevoLibro = Libro()
                nombreLibro = input("escriba el nombre del Libro \n")
                isbnLibro = input("escriba el ISBN del libro \n")

                autores = Autor()
                print(f"\t ID\t Nombre\t Correo")
                for obj in autores.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")
                print("Escriba el id del Autor")
                autor_idLibro = input()

                editoriales = Editorial()
                print(f"\t ID\t Nombre")
                for obj in editoriales.all():
                    print(f"\t {obj.id}\t {obj.nombre}")
                print("Escriba el id de la editorial")
                editorialLibro = input()

                nuevoLibro.nombre = nombreLibro
                nuevoLibro.isbn = isbnLibro
                nuevoLibro.autor_id = autor_idLibro
                nuevoLibro.estado_libro_id = editorialLibro

                nuevoLibro.save()
                menuRegisLib = False

            elif(regisLibros == 2):
                libros = Libro()
                print(f"ID\t NOMBRE\t ISBN\t AUTOR\t EDITORIAL\t ESTADO")
                for obj in libros.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.ISBN}\t {obj.autors_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")
                print("Escriba el id de la editorial")
                editorialLibro = input()

                input("Regresar???")
                menuRegisLib = False
                program.utils.Menu("Menu Modulo Libros", regisLibros)

            elif(regisLibros == 3):
                libros = Libro()
                print(f"ID\t NOMBRE\t ISBN\t AUTOR\t EDITORIAL\t ESTADO")
                for obj in libros.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.autors_id}\t {obj.editorial_id}\t {obj.estado_libro_id}")

                print("Escriba el id del libro que se desea eliminar: \n") 
                id = input()   

                DatabaseManager.table('libros').get()
                DatabaseManager.table('libros').where('id', '=', f'{id}').delete()
                menuRegisLib = False

            elif(regisLibros == 9):
                __log = log("Saliendo")
            break

    def RegistroClientes(self):
        self.__log.info("Ingresando al Registro de Clientes")
        opcionesRegisClientes = {"Registrar Cliente":1, "Listar Cientes":2}
        MenuRegisClientes = Menu("Menu Modulo Libros", opcionesRegisClientes)
        regisClientes = MenuRegisClientes.mostrarMenu()
        menuRegisCli = True
        while menuRegisCli:
            if(regisClientes == 1):
                nuevoCliente = User()
                nombreCliente = input("escriba el nombre del cliente \n")
                correoCliente = input("escriba el correo del cliente \n")

                tipoDoc = TipoDocumento()
                print(f"\t ID\t Descripcion")
                for obj in tipoDoc.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                tipoDocCliente = input("escriba el tipo de documento del cliente \n")

                estadoCli = EstadoUser()
                print(f"\t ID\t Descripcion")
                for obj in estadoCli.all():
                    print(f"\t {obj.id}\t {obj.descripcion}")
                estadoCliente = input("escriba el tipo de documento del cliente \n")

                nuevoCliente.nombre = nombreCliente
                nuevoCliente.correo = correoCliente
                nuevoCliente.tipo_documento_id = tipoDocCliente
                nuevoCliente.estado_user_id = estadoCliente

                nuevoCliente.save()
                menuRegisCli = False

            elif(regisClientes == 2):
                clientes = User()        
                print(f"ID\t NOMBRE\t CORREO\t DOCUMENTO\t ESTADO")
                for obj in clientes.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.isbn}\t {obj.correo}\t {obj.documento}\t {obj.estado_user_id}")

                input("Regresar???")
                program.utils.Menu("Menu Modulo Clientes", regisClientes)

            elif(regisClientes == 9):
                __log = log("Saliendo")
            break

    def RegistroEditorial(self):
        menuRegisEdit = True
        __log = log("Ingresando al Registro de las editoriales")

        self.__log.info("Ingresando al Registro de las editoriales")
        opcionesRegisEditorial = {"Registrar Editorial":1, "Listar Editoriales":2, "Eliminar Editoriales":3}
        MenuRegisEditorial = Menu("Menu Modulo Libros", opcionesRegisEditorial)
        regisEditoriales = MenuRegisEditorial.mostrarMenu()
        menuRegisEdit = True
        while menuRegisEdit:
            if(regisEditoriales == 1):
                nuevaEditorial = Editorial()
                nombreEditorial = input("escriba el nombre de la editorial \n")

                nuevaEditorial.nombre = nombreEditorial

                nuevaEditorial.save()
                menuRegisEdit = False

            elif(regisEditoriales == 2):
                editorial = Editorial()
                print(f"\t ID\t NOMBRE")
                for obj in editorial.all():
                    print(f"\t {obj.id}\t {obj.nombre}")

                input("Regresar???")
                program.utils.Menu("Menu Modulo Editoriales", regisEditoriales)

            elif(regisEditoriales == 3):
                editorial = Editorial()
                print(f"\t ID\t NOMBRE")
                for obj in editorial.all():
                    print(f"\t {obj.id}\t {obj.nombre}")

                print("Escriba el id de la editorial que se desea eliminar: \n") 
                id = input()   

                DatabaseManager.table('editorial').get()
                DatabaseManager.table('editorial').where('id', '=', f'{id}').delete()

            elif(regisEditoriales == 9):
                __log = log("Saliendo")
            break

    def RegistroAutor(self):
        self.__log.info("Ingresando al Registro de los autores")
        opcionesRegisAutor = {"\t- Agregar Autor":1, "\t- Listar Autores":2, "\t- Eliminar Autor":3}
        MenuRegisAutor = Menu("Menu Modulo Autor", opcionesRegisAutor)
        regisAutor = MenuRegisAutor.mostrarMenu()
        resMenuRegisAutor = True
        if(resMenuRegisAutor == 1):
            nuevoAutor = Autor()
            nombreAutor = input("escriba el nombre del autor \n")
            correoAutor = input("escriba el correo del autor \n")

            nuevoAutor.nombre = nombreAutor
            nuevoAutor.correo = correoAutor

            nuevoAutor.save()
            resMenuRegisAutor = False
        if(resMenuRegisAutor == 2):
            autor = Autor()
            print(f"\t ID\t NOMBRE\t CORREO")
            for obj in autor.all():
                print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}")

                input("Regresar???")
                program.utils.Menu("Menu Modulo Autor", regisAutor)
        if(resMenuRegisAutor == 3):
            pass


