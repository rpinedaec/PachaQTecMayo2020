from orator import Model, DatabaseManager
from time import sleep
import Utils.utils as util
from Model.prestamo import Prestamo


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

def SavePrestamo(idlector):
    __log = util.log("Guardar Prestamo")
    opcion = True
    while opcion:
        try:
            iddetlibro = int(input("Ingrese id del libro que desea un prestamo:\n"))
            libro = db.table('Detalle_Libro_Biblioteca')\
            .join('Libro', 'Libro.idLibro', '=', 'Detalle_Libro_Biblioteca.idLibro')\
            .join('Biblioteca', 'Biblioteca.idBiblioteca', '=', 'Detalle_Libro_Biblioteca.idBiblioteca')\
            .where('Detalle_Libro_Biblioteca.idDetalle_Libro_Biblioteca', iddetlibro).first()
            print('Id', 'Nombre Libro\t\t', 'Biblioteca', sep="\t")
            print(libro.idDetalle_Libro_Biblioteca, libro.Nombre_Libro, "", libro.Nombre_Biblioteca, sep="\t")
            if libro:
                prestamo = db.table('prestamo').insert({
                    'idLector' : idlector,
                    'idDetalle_Libro_Biblioteca' : iddetlibro
                    })
                libcant = libro.Cantidad - 1
                if libro.Cantidad > 0:
                    detalibrobiblio = db.table('Detalle_Libro_Biblioteca')\
                        .where('idDetalle_Libro_Biblioteca', iddetlibro)\
                        .update({
                            'Cantidad' : libcant
                        })
                    print('Se ah realizado el prestamo.')
                    sleep(2)
                    opcion = False
                else:
                    detalibrobiblio = db.table('Detalle_Libro_Biblioteca')\
                        .where('idDetalle_Libro_Biblioteca', iddetlibro)\
                        .update({
                            'Cantidad' : libcant,
                            'Estado' : '0'
                        })
                    print("No esta disponible el libro seleccionado.")
                    opcion = False
                opcion = False
            else:
                print('Seleccione un número de la lista.\a\a')
                opcion = True
        except Exception as e:
            __log.info(f"{e} Dato ingresado no es un numero")
            print("Debe ingresar un número de la lista.\a\a")
            sleep (2)
        except KeyboardInterrupt as k:
            __log.info(f"{k} Interrupcion por teclado.")
            print("Interrupcion por teclado")
            sleep (2)
            util.Salir()

def ListPrestamo(idlector):
    __log = util.log("Listar Prestamo")
    prestamo = db.table('Prestamo')\
    .join('Detalle_Libro_Biblioteca', 'Detalle_Libro_Biblioteca.idDetalle_Libro_Biblioteca', '=', 'Prestamo.idDetalle_Libro_Biblioteca')\
    .join('Libro', 'Libro.idLibro', '=', 'Detalle_Libro_Biblioteca.idLibro')\
    .where('Prestamo.idLector', idlector).where('Prestamo.Estado', '1').get()
    print('Id', 'Nombre Libro', sep="\t")
    for pres in prestamo:
        print(pres.idPrestamo, pres.Nombre_Libro, sep="\t")
    
def Devolucion():
    __log = util.log("Devolucion")
    opcion = True
    while opcion:
        try:
            idPrestamo = int(input("Ingrese id para devolucion:\n"))
            prestamo = db.table('Prestamo')\
                .join('Detalle_Libro_Biblioteca', 'Detalle_Libro_Biblioteca.idDetalle_Libro_Biblioteca', '=', 'Prestamo.idDetalle_Libro_Biblioteca')\
                .where('Prestamo.idPrestamo', idPrestamo)\
                .first()
            if prestamo:
                db.table('Prestamo').where('Prestamo.idPrestamo', idPrestamo).update({
                                'Estado' : '0'
                            })
                if prestamo.Cantidad == 0:
                    db.table('Detalle_Libro_Biblioteca')\
                        .where('idDetalle_Libro_Biblioteca', prestamo.idDetalle_Libro_Biblioteca)\
                        .update({
                            'Cantidad' : prestamo.Cantidad + 1,
                            'Estado' : '1'
                        })
                else:
                    db.table('Detalle_Libro_Biblioteca')\
                        .where('idDetalle_Libro_Biblioteca', prestamo.idDetalle_Libro_Biblioteca)\
                        .update({
                            'Cantidad' : prestamo.Cantidad + 1
                        })
                print("La devolucion se ah realizado.")
                sleep(2)
                opcion = False
            else:
                print("Ingrese un dato valido.\a\a")
                opcion = True
        except Exception as e:
            __log.info(f"{e} Dato ingresado no es un numero")
            print ("Ingrese un número de la lista.\a")
            sleep(2)
        except KeyboardInterrupt as k:
            __log.info(f"{k} Interrupcion por teclado.")
            print("Interrupcion por teclado")
            sleep (2)
            util.Salir()