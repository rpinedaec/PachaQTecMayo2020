from utils.utils import log
from utils.utils import Menu
from models.libros import Libros
from models.estadolibro import Estado_libro
from models.autor import Autor
from models.usuario import usuario

class Registros:
    __log = log("Registros")
    def registroLibros(self):
        self.__log.info("Ingresando al Registro de Libros")
        opcionesRegistroLibros = {"\t- Registrar Libros":1,"\t- Listar Libros":2}
        menuRegistroLibros = Menu("Registro de Libros",opcionesRegistroLibros)
        resmenuRegistroLibros = menuRegistroLibros.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if (resmenuRegistroLibros == 1):
                self.__log.info("Entrando al registro de libros")
                nuevoLibro = Libros()
                nombreLibro = input("escriba el nombre del Libro \n")
                isbnLibro = input("escriba en ISBN del libro \n")

                autores = Autor()
                print(f"\t Codigo\t Nombre\t Tipo")
                for obj in autores.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.tipo}")
                print("Escriba el id del Autor de la siguiente lista")
                print("*Importante : Si no lo ve ingrese NA*")
                autor_idLibro = input()
                if (autor_idLibro == 'NA'):
                    nuevoAutor = Autor()
                    nombrenuevoAutor = input('Ingrese el nombre del Autor: ')
                    correonuevoAutor = input('Ingrese el correo del Autor: ')
                    tiponuevoAutor = input('Ingrese si (01) si es Autor o (02) si es Editorial: ')
                    nuevoAutor.nombre = nombrenuevoAutor
                    nuevoAutor.correo = correonuevoAutor
                    nuevoAutor.tipo = tiponuevoAutor
                    nuevoAutor.save()
                    print('Inicializando menu de regsitro nuevamente')
                    Registros.registroLibros()
                else:
                    estados = Estado_libro()
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



                stopMenu = False
            
            elif resmenuRegistroLibros == 9:
                self._log.info("Saliendo")
                

    def registroLectores(self):
        self.__log.info("Ingresando al Registro de Lectores")
        opcionesRegistroLectores = {"\t- Registrar nuevo Lector":1,"\t- Listar Lectores":2}
        menuRegistroLectores = Menu("Registro de Lectores",opcionesRegistroLectores)
        resmenuRegistroLectores = menuRegistroLectores.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if (resmenuRegistroLectores == 1):
                self.__log.info("Entrando al opcion de nuevo registro")
                nuevoLector = usuario()
                nombreNusuario = input("Escriba el nombre del Lector \n")
                correoNusuario = input("Escriba el correo del lector \n")
                tipodedocumentoNusuario = input("Escriba DNI, CE o Carnet de Biblioteca \n")
                nodocumentoNusuario = input("Ingrese el no. de documento \n")
                estadousuarioNusuario = 2

                nuevoLector.nombre = nombreNusuario
                nuevoLector.correo = correoNusuario
                nuevoLector.tipo_documento_id = tipodedocumentoNusuario
                nuevoLector.documento= nodocumentoNusuario
                nuevoLector.estado_usuario_id= estadousuarioNusuario

                nuevoLector.save()
                print(f"\t El usuario '{nombreNusuario}'\t ha sido creado")
                stopMenu = False
            elif (resmenuRegistroLectores == 2):
                vistaUsuarios = usuario()
                print(f"\t ID\t Nombre\t Correo\t Tipo de Doc\t No. Doc\t Estado\t")
                stopMenu =False
                for obj in vistaUsuarios.all():
                    print(f"\t {obj.id}\t {obj.nombre}\t {obj.correo}\t {obj.tipo_documento_id}\t {obj.documento}\t {obj.estado_usuario_id}")
                    opcionlistarusuarios = input('Desea editar algun usuario? S/N: ')
                    if (opcionlistarusuarios == 'S'):
                        usuariocambio = usuario()
                        nombrecambio = input("Escriba el nombre del Lector \n")
                        correocambio = input("Escriba el correo del lector \n")
                        tipodedocumentocambio = input("Escriba (01) DNI, (02) CE o (03)Carnet de Biblioteca \n")
                        nodocumentocambio = input("Ingrese el no. de documento \n")
                        estadousuariocambio = input("Ingrese (01) para Activo y (03) para Pendiente \n")
                        usuariocambio.nombre = nombrecambio
                        usuariocambio.correo = correocambio
                        usuariocambio.tipo_documento_id = tipodedocumentocambio
                        usuariocambio.documento = nodocumentocambio
                        usuariocambio.estado_usuario_id = estadousuariocambio
                        usuariocambio.update()
                        
            elif resmenuRegistroLectores == 9:
                self._log.info("Saliendo")
                