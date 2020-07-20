# SISTEMA 1.0

print("  ____  _                           _     _       ")
print(" | __ )(_) ___ _ ____   _____ _ __ (_) __| | ___  ")
print(" |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \ ")
print(" | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |")
print(" |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/ ")
print("--------------------------------------------------")

strNombre01 = "Producto: "
strNombre02 = "Precio: "
strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]

def addProducto():
    print("Agregar Producto")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("AGREGAR: A || SALIR: S  --> ")
        if(menuProducto == "A"):
            strNombreProducto = input("Ingresa el nombre del Producto: ")
            flValorProducto = float(input(f"Ingresa el valor de {strNombreProducto}: "))
            dicProducto = {}
            dicProducto.update({strNombre01:strNombreProducto})
            dicProducto.update({strNombre02:flValorProducto})
            print(dicProducto)
            lstProductos.append(dicProducto)
            print(lstProductos)
        else:
            print("bye")
            blMenuProducto = False

def delProducto():
    print("entro a delProducto")
    while True:
        menuProducto = input("BORRAR PRODUCTO : R / Salir : S ")
        if(menuProducto == "R"):
            print("Busca el producto que deseas quitar")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
            print("Escribe el Producto que quieres Eliminar")
            strNombreEliminar = input()
            for p in lstProductos:
                for (key, value) in p.items():
                    if(value == strNombreEliminar):
                        print(f"{value} Eliminada, mira abajo, ya no está!")
                        lstProductos.remove(p)
            print(lstProductos)
        else:
            print("bye")
            break

def showInventario():
    print("|-|-| INVENTARIO: |-|-|")
    print(lstProductos)


while True:
    print("Escoge una opcion:")
    print("1 : Agregar Producto")
    print("2 : Quitar Producto")
    print("3 : Inventario")
    print("0 : Salir")
    strMenuPrincipal = input()
    if(strMenuPrincipal == "1"):
        addProducto()
    elif(strMenuPrincipal == "2"):
        delProducto()
    elif(strMenuPrincipal == "3"):
        showInventario()
    elif(strMenuPrincipal == "0"):
        break
    else:
        opcionSalir = input("No escogio las opciones indicadas; desea salir s/n --> ")
        if(opcionSalir == "s"):
            break

