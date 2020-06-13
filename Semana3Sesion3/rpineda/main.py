#Programa de inventario
# Acciones:
# 1.- Agregar Productos
#   1.1.-Menu para agregar productos o salir
# 2.- Quitar Producto
#   2.1.-Menu para quitar producto o salir
# 3.- Inventario
#   3.1.-Menu para Ejecutar el Inventario o salir

def addProducto():
    print("Agregar Producto")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("que deseas hacer Agregar : A / Salir : S")
        if(menuProducto == "A"):
            strNombreProducto = input("Digita el nombre del Producto: ")
            flValorProducto = float(input(f"Digita en valor de {strNombreProducto}: "))
            dicProducto = {}
            dicProducto.update({"NombreProducto":strNombreProducto})
            dicProducto.update({"ValorProducto":flValorProducto})
            print(dicProducto)
            lstProductos.append(dicProducto)
            print(lstProductos)
        else:
            print("bye")
            blMenuProducto = False

def delProducto():
    print("entro a delProducto")
    while True:
        menuProducto = input("que deseas hacer Quitar : Q / Salir : S ")
        if(menuProducto == "Q"):
            print("Busca en la lista el producto que deseas quitar")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
            print("Escribe el nombre del Producto que quieres Eliminar")
            strNombreEliminar = input()
            for p in lstProductos:
                for (key, value) in p.items():
                    if(value == strNombreEliminar):
                        print(f"Borrar {value}???")
                        lstProductos.remove(p)
            print(lstProductos)

        else:
            print("bye")
            break


def showInventario():
    print("Entro a showInventario")

strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]

while True:
    print("--------------------------------")
    print("Bienvenido Escoge la opcion:")
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
        opcionSalir = input("No escogio las opciones indicadas; desea salir s/n")
        if(opcionSalir == "s"):
            break

