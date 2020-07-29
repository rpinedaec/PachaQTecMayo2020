#Importamos las clases ubicadas en la carpeta "models"
from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.estado_libro import EstadoLibro
from models.user import User
from models.estado_user import EstadoUser
from models.prestamo import Prestamo
from orator import Model,DatabaseManager
from datetime import datetime

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'uni20100420f',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

class Prestamos:
    __log = log("Prestamos")
    def registroPrestamos(self):
        self.__log.info("Ingresando al menu de Prestamos")
        opcionesPrestamo = {"\t- Registrar Prestamo":1,"\t- Registrar Devolucion":2}
        menuPrestamo = Menu("Prestamo de Libros",opcionesPrestamo)
        resmenuPrestamo = menuPrestamo.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuPrestamo == 1:
                self.__log.info("Entrando al prestamo de libros")
                usuario = User()
                numDocumento = input("Ingrese su numero de documento: ")
                try:
                    listaUser = []
                    for obj in usuario.all():
                        a = [obj.id, obj.nombre, obj.documento,obj.estado_user_id]
                        listaUser.append(a)
                    aaa = False                
                    i = 0
                    while aaa == False:
                        if listaUser[i][2] == numDocumento:
                            aaa = True
                            user_id = listaUser[i][0]
                            name = listaUser[i][1]
                            resultado = listaUser[i][3]
                            estadoUser = EstadoUser()
                            listaEstadoUser = []
                            for obj in estadoUser.all():
                                a = [obj.id, obj.descripcion]
                                listaEstadoUser.append(a)                       
                            bbb = False
                            j = 0
                            while bbb == False:
                                if listaEstadoUser[j][0] == resultado:
                                    est_User = listaEstadoUser[j][1]
                                    if est_User == "Inactivo" or est_User == "Pendiente Aprobacion":
                                        print("Su estado es: ", est_User, "no puede retirar libros")
                                        stopMenu = False         
                                    elif est_User == "Activo":
                                        print("Bienvenido ", name, "su estado de usuario es: ",est_User)

                                        libros = Libro()
                                        nombreLibro=input("Ingrese el nombre del libro: ")
                                        try:
                                            guiaLibros = []
                                            for obj in libros.all():
                                                a = [obj.id, obj.nombre, obj.estado_libro_id]
                                                guiaLibros.append(a)
                                            
                                            ccc = False
                                            i = 0
                                            while ccc == False:
                                                if guiaLibros[i][1] == nombreLibro:
                                                    libro_id = guiaLibros[i][0]
                                                    resultado1 = guiaLibros[i][2]
                                                    ccc = True
                                                    estadoLibro=EstadoLibro()
                                                    estadoLibros=[]
                                                    for obj in estadoLibro.all():
                                                        a=[obj.id, obj.descripcion]
                                                        estadoLibros.append(a)
                                                    
                                                    bbb = False
                                                    j=0
                                                    while bbb == False:
                                                        if estadoLibros[j][0] == resultado1:
                                                            est_Libros = estadoLibros[j][1]
                                                            
                                                            if est_Libros == "Disponible":
                                                                print("El libro, se encuentra ", est_Libros)
                                                                est_Libros="Prestado"
                                                                prestamo = Prestamo()                                                                
                                                                prestamo.user_id = user_id
                                                                prestamo.libros_id = libro_id
                                                                prestamo.prestado_on = datetime.now()
                                                                prestamo.bibliotecas_id = 1                          
                                                                prestamo.save()
                                                                stopMenu = False
                                                                print("El registro del prestamo, se realizo con exito")
                                                            elif est_Libros == "Reservado" or est_Libros == "Prestado":
                                                                print("El libro se encuentra: ", est_Libros)
                                                                stopMenu = False
                                                            else:
                                                                print("digito mal")
                                                                stopMenu = False
                                                            bbb = True
                                                        else:
                                                            j=j+1

                                                else:
                                                    i=i+1
                                        except:
                                            print("El libro no existe")
                                            stopMenu = False

                                    else:
                                        print("Digito mal")
                                        stopMenu = False
                                    bbb = True
                                else:
                                    j = j+1     
                        else:
                            i = i+1
                except:
                    print("ALGO FALLO EN EL PROGRAMA")
                stopMenu = False

            elif resmenuPrestamo == 2:
                libros = Libro()
                isbnLibro = input("Ingrese el ISBN del libro a devolver: ")
                try:
                    listaLibros=[]
                    for obj in libros.all():
                        a = [obj.id, obj.nombre,obj.isbn]
                        listaLibros.append(a)
                    aaa = False
                    i=0
                    while aaa == False:
                        if listaLibros[i][2] == isbnLibro:
                            idLibro = listaLibros[i][0]
                            prestamo = Prestamo()
                            listaPrestamos = []
                            for obj in libros.all():
                                a = [obj.id, obj.user_id, obj.libros_id, obj.prestado_on, obj.bibliotecas_id]
                                listaPrestamos.append(a)
                            bbb= False
                            j=0
                            while bbb == False:
                                if listaPrestamos[i][2] == idLibro:
                                    prestamo.user_id = listaPrestamos[i][1]
                                    prestamo.libros_id = listaPrestamos[i][2]
                                    prestamo.prestado_on = datetime.now()
                                    prestamo.bibliotecas_id= listaPrestamos[i][4]
                                    prestamo.save()
                                    stopMenu = False
                                    bbb = True
                                else:
                                    j = j+1
                            aaa = True
                        else:
                            i = i+1
                except:
                    print("El libro no existe o no está registrado en la biblioteca")
                stopMenu = False

            elif resmenuPrestamo == 9:
                self._log.info("Saliendo")
                stopMenu = False

    def registroLectores(self):
        pass