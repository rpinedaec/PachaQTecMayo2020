from io import open
import pickle
#funcion para buscar un objeto ya registrado segun atributo de clase y lista donde se almacena


def search(item, identify, lst):
    if len(lst) > 0:
        r = 0
        for i in lst:
            if getattr(i, identify) == item:
                r += 1
        if r > 0:
            return True
        else:
            return False
    else:
        return False
#funciones para añadir nuevos elementos


def addCliente(lst, classitem):
    while True:
        try:
            dni = int(input('Ingrese el dni  de la persona: '))
            break
        except:
            print('Erro!: Introdusca un numero entero')
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    while True:
        try:
            edad = int(input('Ingrese la edad de la persona: '))
            break
        except:
            print('Error: Introdusca un numero entero')
    sexo = input('Ingrese el sexo de la persona: ')
    while True:
        try:
            codcliente = int(input("Ingrese el codigo de cliente: "))
            break
        except:
            print('Error!: Ingrese un numero entero')
    newclient = classitem(dni, nombre, apellido, edad, sexo, codcliente)
    return newclient


def addEmpleado(lst, classitem):
    while True:
        try:
            dni = int(input('Ingrese el dni  del empleado: '))
            break
        except:
            print('Erro!: Introdusca un numero entero')
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    while True:
        try:
            edad = int(input('Ingrese la edad del empleado: '))
            break
        except:
            print('Error: Introdusca un numero entero')
    sexo = input('Ingrese el sexo del empleado: ')
    while True:
        try:
            codempleado = int(input("Ingrese el codigo de empleado: "))
            break
        except:
            print('Error!: Ingrese un numero entero')
    newempleado = classitem(dni, nombre, apellido, edad, sexo, codempleado)
    return newempleado


def addProducto(lst, classitem):
    while True:
        try:
            codigo = int(input('Ingrese el codigo del producto: '))
            break
        except:
            print('Erro!: Introdusca un numero entero')
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad del producto: '))
            break
        except:
            print('Error: Introdusca un numero entero')
    while True:
        try:
            costo = int(input("Ingrese el precio del producto: "))
            break
        except:
            print('Error!: Ingrese un numero entero')
    newproduct = classitem(codigo, nombre, cantidad, costo)
    return newproduct
#funciones para eliminar elementos


def showCliente(lst):
    while True:
        print(157*"-")
        print(
            f'|{"DNI":^25}|{"Nombre":^25}|{"Apellido":^25}|{"Edad":^25}|{"Sexo":^25}|{"CodCliente":^25}|')
        print(157*"-")
        for i in lst:
            dni = getattr(i, "dni")
            nombre = getattr(i, "nombre")
            apellido = getattr(i, "apellido")
            edad = getattr(i, "edad")
            sexo = getattr(i, "sexo")
            codCliente = getattr(i, "codCliente")
            print(
                f'|{dni:^25}|{nombre:^25}|{apellido:^25}|{edad:^25}|{sexo:^25}|{codCliente:^25}|')
        print(157*"-")
        c = input("Ingrese cualquier tecla para continuar: ")
        break


def showEmpleado(lst):
    while True:
        print(157*"-")
        print(
            f'|{"DNI":^25}|{"Nombre":^25}|{"Apellido":^25}|{"Edad":^25}|{"Sexo":^25}|{"CodEmpleado":^25}|')
        print(157*"-")
        for i in lst:
            dni = getattr(i, "dni")
            nombre = getattr(i, "nombre")
            apellido = getattr(i, "apellido")
            edad = getattr(i, "edad")
            sexo = getattr(i, "sexo")
            codEmpleado = getattr(i, "codEmpleado")
            print(
                f'|{dni:^25}|{nombre:^25}|{apellido:^25}|{edad:^25}|{sexo:^25}|{codEmpleado:^25}|')
        print(157*"-")
        c = input("Ingrese cualquier tecla para continuar: ")
        break


def showProducto(lst):
    while True:
        print(105*"-")
        print(f"Se tiene registrado '{len(lst)}'' productos")
        print(105*"-")
        print(f'|{"codProducto":^25}|{"Nombre":^25}|{"Cantidad":^25}|{"Costo":^25}|')
        print(105*"-")
        for i in lst:
            cod = getattr(i, "codProducto")
            nombre = getattr(i, "nombreProducto")
            cantidad = getattr(i, "cantProducto")
            costo = getattr(i, "costoProducto")
            print(f'|{cod:^25}|{nombre:^25}|{cantidad:^25}|{costo:^25}|')
        print(105*"-")
        c = input("Ingrese cualquier tecla para continuar: ")
        break
#Funcion para eliminar un producto


def delProducto(lst):
    while True:
        try:
            if len(lst) > 0:
                #Muestra todos los producto
                print(105*"-")
                print(
                    f'|{"codProducto":^25}|{"Nombre":^25}|{"Cantidad":^25}|{"Costo":^25}|')
                print(105*"-")
                for i in lst:
                    cod = getattr(i, "codProducto")
                    nombre = getattr(i, "nombreProducto")
                    cantidad = getattr(i, "cantProducto")
                    costo = getattr(i, "costoProducto")
                    print(f'|{cod:^25}|{nombre:^25}|{cantidad:^25}|{costo:^25}|')
                print(105*"-")
                #Elimar
                codProducto = int(
                    input("Ingrese el codigo del Producto a eliminar: "))
                if search(codProducto, "codProducto", lst):
                    strConfirmation = input(
                        f"Esta seguro de eliminar el item {codProducto} S/N: ")
                    if strConfirmation == "S":
                        for i, x in enumerate(lst):
                            if getattr(x, "codProducto") == codProducto:
                                del lst[i]
                        print("Item eliminado correctamente")
                        c = input(
                            "Producto eliminado, ingrese cualquier tecla para continuar: ")
                        break
                    elif strConfirmation == "N":
                        c = input(
                            "No se eliminara ningun producto, ingrese cualquier tecla para continuar: ")
                        break
                    else:
                        print("Ingrese S o N")
                else:
                    c = input(
                        "El producto no existe, ingrese cualquier tecla para continuar")
            else:
                c = input(
                    "Aún no se ah registrado ningun producto, ingrese cualquier tecla para continuar")
                break
        except:
            print("Error!: Ingrese un codigo de producto valido")
#Funcion para valorizar todos los productos


def valProducto(lst):
    fltValTot = 0.0
    if len(lst) > 0:
        print(131*"-")
        print(
            f'|{"codProducto":^25}|{"Nombre":^25}|{"Cantidad":^25}|{"Costo":^25}|{"Valor producto":^25}|')
        print(131*"-")
        for i in lst:
            cod = getattr(i, "codProducto")
            nombre = getattr(i, "nombreProducto")
            cantidad = getattr(i, "cantProducto")
            costo = getattr(i, "costoProducto")
            valor = costo*cantidad
            fltValTot += costo*cantidad
            print(f'|{cod:^25}|{nombre:^25}|{cantidad:^25}|{costo:^25}|{valor:^25}|')
        print(131*"-")
        print(f'Valorización total del inventario: S/.{fltValTot}')
        print(131*"-")
        c = input("Ingrese cualquier tecla para continuar: ")
    else:
        c = input(
            "Aun no se han agregado productos,ingrese cualquier tecla para continuar: ")
#Función de recuperación de datos


def recovery(archivo):
    lst = []
    fichero = open(f"{archivo}.pckl", "ab+")
    fichero.seek(0)
    try:
        lst = pickle.load(fichero)
        return lst
    except:
        print(f"El fichero {archivo} esta vació")
        return lst
    finally:
        fichero.close()
        print(f"Se han cargado {len(lst)} {archivo}")
#Función de guardado de datos


def save(archivo, lst):
    fichero = open(f'{archivo}.pckl', 'wb')
    pickle.dump(lst, fichero)
    fichero.close()
