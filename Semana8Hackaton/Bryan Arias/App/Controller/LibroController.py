from orator import Model, DatabaseManager
from time import sleep
import Utils.utils as util

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'admin',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)

def ListAllLibros():
    __log = util.log("Listar libros")
    try:
        detallelibro = db.table('Detalle_Libro_Autor')\
            .join('Autor', 'Detalle_Libro_Autor.idAutor', '=', 'Autor.idAutor')\
            .join('Libro', 'Detalle_Libro_Autor.idLibro', '=', 'Libro.idLibro')\
            .join('Editorial', 'Editorial.idEditorial', '=', 'Libro.idEditorial').get()
        print('Id', 'Nombre Libro\t\t', 'ISBN\t\t', 'Nombre Autor', 'Nombre Editorial', sep="\t")
        for dl in detallelibro:
            print(dl.idLibro, dl.Nombre_Libro+'\t', dl.ISBN, dl.Nombre_Autor, dl.Nombre_Editorial, sep="\t")    
        sleep(2)   
    except KeyError as k:
        __loginfo(f"{k} Error")
        input("Hubo un error")
    except KeyboardInterrupt as kb:
        __log.info(f"{kb} Interrupcion por teclado")
        print("Interrupcion por teclado\a")
        sleep(2)
        util.Salir()

def BuscarLibros():
    __log = util.log("Buscar Libro")
    opcion = True
    while opcion:
        try:
            idlibro = int(input("Ingrese id del libro que desea:\n"))
            detallelibro = db.table('Detalle_Libro_Autor')\
                .join('Autor', 'Detalle_Libro_Autor.idAutor', '=', 'Autor.idAutor')\
                .join('Libro', 'Detalle_Libro_Autor.idLibro', '=', 'Libro.idLibro')\
                .join('Editorial', 'Editorial.idEditorial', '=', 'Libro.idEditorial')\
                .join('Detalle_Libro_Biblioteca', 'Detalle_Libro_Biblioteca.idLibro', '=', 'Libro.idLibro')\
                .join('Biblioteca', 'Biblioteca.idBiblioteca', '=', 'Detalle_Libro_Biblioteca.idBiblioteca')\
                .where('Detalle_Libro_Biblioteca.idLibro',idlibro).where('Estado', '1').get()
            print('Id', 'Nombre Libro\t\t', 'Nombre Autor\t', 'Nombre Editorial', 'Cantidad', 'Estado', 'Biblioteca', sep="\t")
            if detallelibro:
                for row in detallelibro:
                    print(row.idDetalle_Libro_Biblioteca, row.Nombre_Libro, "", row.Nombre_Autor, "", row.Nombre_Editorial, "", row.Cantidad, row.Estado, row.Nombre_Biblioteca,sep="\t")                
                opcion = False
            else:
                print('Ingrese el id de un libro valido.\a')
                sleep(2)
                opcion = True
        except Exception as e:
            __log.info(f"{e} El dato no es un numero.")
            print("Escoja un número de la lista.\a")
        except KeyboardInterrupt as k:
            __log.info(f"{k} Interrupcion por teclado")
            print("Interrupcion por teclado\a")
            sleep(2)
            util.Salir()

def AddLibro():
    idedit = input("Ingrese id del editorial:\n")
    Nombre = input("Ingrese Nombre del Libro:\n")
    ISBN = input("Ingrese ISBN del Libro:\n")
    res = db.table("Libro").insert({
        "idEditorial" : idedit,
        "Nombre_Libro" : Nombre,
        "ISBN" : ISBN
    })
    if res:
        print("Se agrego correctamente.")
        sleep(2)
    else:
        print("No fue posible agregar el libro.")
        sleep(2)

def ListaLibro():
    res = db.table("Libro").join('Editorial', 'Editorial.idEditorial', '=', 'Libro.idEditorial').get()
    print("Id","Nombre Editorial", "Nombre Libro", "ISBN\t\t", sep="\t")
    for row in res:
        print(row.idLibro, row.Nombre_Editorial, row.Nombre_Libro, row.ISBN, sep="\t")
    sleep(2)

def UpdateLibro():
    ListaLibro()
    idlibro = input("Ingrese id del libro:\n")
    idedit = input("Ingrese nuevo id del editorial:\n")
    Nombre = input("Ingrese nuevo Nombre del libro:\n")
    ISBN = input("Ingrese nuevo ISBN del libro:\n")
    res = db.table("Libro").where("idLibro", idlibro).update({
        "idEditorial" : idedit,
        "Nombre_Libro" : Nombre,
        "ISBN" : ISBN
    })

def AddLibroAutor():
    idautor = input("Ingrese id del autor:\n")
    ListaLibro()
    idlibro = input("Ingrese id del libro:\n")
    res = db.table("Detalle_Libro_Autor").insert({
        "idAutor" : idautor,
        "idLibro" : idlibro
    })
    if res:
        print("Se ah insertado correctamente.")
        sleep(2)
    else:
        print("No fue posible insertar el dato.")
        sleep(2)

def ListLibBib():
    res = db.table("Libro")\
            .join('Detalle_Libro_Biblioteca', 'Detalle_Libro_Biblioteca.idLibro', '=', 'Libro.idLibro')\
            .join('Biblioteca', 'Biblioteca.idBiblioteca', '=', 'Detalle_Libro_Biblioteca.idBiblioteca')\
            .get()
    print("Id","Nombre Biblioteca", "Nombre Libro", "Cantidad", sep="\t")
    for row in res:
        print(row.idDetalle_Libro_Biblioteca, row.Nombre_Biblioteca, row.Nombre_Libro, row.Cantidad, sep="\t")
    sleep(2)

def ListBiblioteca():
    res = db.table("Biblioteca").get()
    print("Id", "Nombre Biblioteca", sep="\t")
    for row in res:
        print(row.idBiblioteca, row.Nombre_Biblioteca, sep="\t")
    sleep(2)

def AddLibBib():
    ListBiblioteca()
    idbib = input("Ingrese id de la biblioteca:\n")
    ListaLibro()
    idlib = input("Ingresa id del libro:\n")
    cantidad = input("Ingrese Cantidad de libros:\n")
    res = db.table("Detalle_Libro_Biblioteca").insert({
        "idLibro" : idlib,
        "idBiblioteca" : idbib,
        "Cantidad" : cantidad
    })
    if res:
        print("Se guardó correctamente")
        sleep(2)
    else:
        print("No se pudo guardar")
        sleep(2)