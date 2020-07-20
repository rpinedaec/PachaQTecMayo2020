import Utils.utils as util
import Controller.LectorController as lector
import Controller.TipoDocController as tipodoc
import Controller.LibroController as libro
import Controller.PrestamoController as prestamo
import Controller.AutorController as autor
import Controller.EditorialController as editorial

def MenuPrincipal():
    __log = util.log("Principal")
    opcion = True
    tipodoc.ListAllTipoDoc()
    idtipodoc = tipodoc.BuscarTipoDoc()
    while opcion:
        idlector = lector.BuscarDni(idtipodoc)
        if idlector:
            tplmenu = ('1. Prestamo', '2. Devolucion', '3. Mantenimiento')
            menu = util.Menu("BIBLIOTECA", tplmenu)
            resmenu = menu.MostrarMenu()
            if resmenu == 1:
                libro.ListAllLibros()
                libro.BuscarLibros()
                prestamo.SavePrestamo(idlector)
            elif resmenu == 2:
                prestamo.ListPrestamo(idlector)
                prestamo.Devolucion()
            elif resmenu == 3:
                tplmant = ('1. Autor', '2. Editorial', '3. Libro', '4. Asignar Autor al Libro', '5. Asignar Libro a la Biblioteca')
                mant = util.Menu("MANTENIMIENTO", tplmant)
                resmant = mant.MostrarMenu()
                if resmant == 1:
                    opau = True
                    while opau:
                        tplautor = ('1. Listar Autor', '2. Agregar Autor', '3. Modificar Autor', '4. Regresar')
                        aut = util.Menu("AUTOR", tplautor)
                        resaut = aut.MostrarMenu()
                        if resaut == 1:
                            autor.ListAllAutor()
                            opau = True
                        elif resaut == 2:
                            autor.AddAutor()
                            opau = True
                        elif resaut == 3:
                            autor.UpdateAutor()
                            opau = True
                        elif resaut == 4:
                            opau = False
                        else:
                            util.Salir()
                elif resmant == 2:
                    oped = True
                    while oped:
                        tpledit = ('1. Listar Editorial', '2. Agregar Editorial', '3. Modificar Editorial', '4. Regresar')
                        edit = util.Menu("EDITORIAL", tpledit)
                        resedit = edit.MostrarMenu()
                        if resedit == 1:
                            editorial.ListAllEditorial()
                            oped = True
                        elif resedit == 2:
                            editorial.AddEditorial()
                            oped = True
                        elif resedit == 3:
                            editorial.UpdateEditorial()
                            oped = True
                        elif resedit == 4:
                            oped = False
                        else:
                            util.Salir()
                elif resmant == 3:
                    oplib = True
                    while oplib:
                        tpllib = ('1. Listar Libro', '2. Agregar Libro', '3. Modificar Libro', '4. Regresar')
                        lib = util.Menu("LIBRO", tpllib)
                        reslib = lib.MostrarMenu()
                        if reslib == 1:
                            libro.ListaLibro()
                            oplib = True
                        elif reslib == 2:
                            editorial.ListAllEditorial()
                            libro.AddLibro()
                            oplib = True
                        elif reslib == 3:
                            libro.UpdateLibro()
                            oplib = True
                        elif reslib == 4:
                            oplib = False
                        else:
                            util.Salir()
                elif resmant == 4:
                    oplibaut = True
                    while oplibaut:
                        tpllibaut = ('1. Listar Libro - Autor', '2. Agregar Libro - Autor', '3. Regresar')
                        libaut = util.Menu("LIBRO - AUTOR", tpllibaut)
                        reslibaut = libaut.MostrarMenu()
                        if reslibaut == 1:
                            libro.ListAllLibros()
                            oplibaut = True
                        elif reslibaut == 2:
                            autor.ListAllAutor()
                            libro.AddLibroAutor()
                            oplibaut = True
                        elif reslibaut == 3:
                            oplibaut = False
                        else:
                            util.Salir()
                elif resmant == 5:
                    oplibbib = True
                    while oplibbib:
                        tpllibbib = ('1. Listar Libro - Biblioteca', '2. Agregar Libro - Biblioteca', '3. Regresar')
                        libbib = util.Menu("LIBRO - BIBLIOTECA", tpllibbib)
                        reslibbib = libbib.MostrarMenu()
                        if reslibbib == 1:
                            libro.ListLibBib()
                            oplibbib = True
                        elif reslibbib == 2:
                            libro.AddLibBib()
                            oplibbib = True
                        elif reslibbib == 3:
                            oplibbib = False
                        else:
                            util.Salir()
                else:
                    util.Salir()
            else:
                util.Salir()
        else:
            opcion = True