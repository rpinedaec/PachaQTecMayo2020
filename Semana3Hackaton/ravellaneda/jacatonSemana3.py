# SISTEMA 1.0
# Ricardo Avellaneda
print('\x1b[6;30;42m' + "__________________________________________________" + '\x1b[0m')
print('\x1b[6;30;42m' + "  ____  _                           _     _       " + '\x1b[0m')
print('\x1b[6;30;42m' + " | __ )(_) ___ _ ____   _____ _ __ (_) __| | ___  " + '\x1b[0m')
print('\x1b[6;30;42m' + " |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \ " + '\x1b[0m')
print('\x1b[6;30;42m' + " | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |" + '\x1b[0m')
print('\x1b[6;30;42m' + " |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/ " + '\x1b[0m')
print('\x1b[6;30;42m' + "__________________________________________________" + '\x1b[0m')

# pmName = input('extras.py')
# pm = __import__(pmName)
# print(dir(pm))

strMenuPrincipal = "0"
tplNombre=("Producto: ", "Precio: ", "Cantidad: ")
lstProductos=[
    {tplNombre[0]: "Silla", tplNombre[1]: 50, tplNombre[2]: 10},
    {tplNombre[0]: "Mesa", tplNombre[1]: 22, tplNombre[2]: 3},
    {tplNombre[0]: "Cama", tplNombre[1]: 150, tplNombre[2]: 7}]

#FUNCION DE AÑADIR PRODUCTOS
def addProducto():
    print("|-|-| AGREGAR PRODUCTO: |-|-|")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("AGREGAR: A || SALIR: S  --> ")
        if(menuProducto == "A"):
            strNombreProducto = input("Ingresa el nombre del Producto: ")
            fltValorProducto = int(input(f"Ingresa el valor de {strNombreProducto}: "))
            fltCantidadProducto = int(input(f"Ingresa las existencias de {strNombreProducto}: "))
            dicProducto = {}
            dicProducto.update({tplNombre[0]:strNombreProducto})
            dicProducto.update({tplNombre[1]:fltValorProducto})
            dicProducto.update({tplNombre[2]:fltCantidadProducto})
            print(dicProducto)
            lstProductos.append(dicProducto)
            print(lstProductos)
        else:
            print("Hasta Pronto")
            blMenuProducto = False
    print("*************FIN**************")

#FUNCION DE ELIMINAR PRODUCTO
def delProducto():
    print("|-|-| ELIMINAR PRODUCTO: |-|-|")
    while True:
        menuProducto = input("ELIMINAR PRODUCTO : E / Salir : S --> ")
        if(menuProducto == "E"):
            print("Busca el producto que quieres quitar")
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
            print("Hasta Pronto")
            break
    print("*************FIN**************")
    
#FUNCION DE MOSTRAR EL INVENTARIO
def showInventario():
    print("|-|-| INVENTARIO: |-|-|")
    print(lstProductos, sep = "\n")
    print("*************FIN**************")

#FUNCION DE CONTAR PRODUCTOS DEL INVENTARIO
def countInventario():
    print("|-|-| CONTAR: |-|-|")
    print(f"Hay {len(lstProductos)} productos en la lista")
    print("*************FIN**************")

#FUNCION DE MULTIPLICAR PRECIO/EXISTENCIAS DEL INVENTARIO
def valueInventario():
    print("|-|-| VALORIZAR: |-|-|")
    totalSoles = 0.0
    for product in lstProductos:
        print(product)
        costoTotal = product['Precio: '] * product['Cantidad: ']
        print('\033[0;32m' + f"Hay {costoTotal} soles en {product['Producto: ']}s" + '\033[0m')
        totalSoles += costoTotal
        print('\033[1;31m' + "El total en Soles de todo el inventario es:" + '\033[0m')
        print(totalSoles)
    print("*************FIN**************")

# MENU PARA INTEACTUAR CON LAS FUNCIONES
while True:
    print("Escoge una opcion:")
    print("1 : Agregar Producto")
    print("2 : Quitar Producto")
    print("3 : Inventario")
    print("4 : Contar productos")
    print("5 : Valorizar")
    print("0 : Salir")
    strMenuPrincipal = input()
    if(strMenuPrincipal == "1"):
        addProducto()
    elif(strMenuPrincipal == "2"):
        delProducto()
    elif(strMenuPrincipal == "3"):
        showInventario()
    elif(strMenuPrincipal == "4"):
        countInventario()
    elif(strMenuPrincipal == "5"):
        valueInventario()
    elif(strMenuPrincipal == "0"):
        break
    else:
        opcionSalir = input("No escogió las opciones indicadas; ¿Desea salir? s/n --> ")
        if(opcionSalir == "s"):
            break
   