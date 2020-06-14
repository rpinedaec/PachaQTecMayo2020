def addProducto():
    print("Agregar Producto")
    blMenuProducto = True
    while blMenuProducto:
        print ("Para agregar pulse : A / para Salir : S ")
        menuProducto = input("seleccione una opcion ")
        if(menuProducto == "A"):
            strNombreProducto = input("Digita el nombre del Producto: ")
            flValorProducto = float(input(f"Digita en valor de {strNombreProducto}: "))
            intCantProducto = int(input(f"Digita la cantidad de {strNombreProducto}: "))
            dicProducto = {}
            dicProducto.update({"NombreProducto":strNombreProducto})
            dicProducto.update({"ValorProducto":flValorProducto})
            dicProducto.update({"CantidadProducto":intCantProducto})
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


def listProductos():
    LIST=True
    while LIST:
        print(lstProductos)
        menuProducto = input("Para retornar prisionar R: ")
        LIST=False

def invProducto():
    while True:
        print("--------------------------------")
        print("Escoge la opcion:")
        print("1 : Contar los productos")
        print("2 : Valorizar los productos")
        print("3 : Retornar")
        strMenuSecundario = input()
        if(strMenuSecundario == "1"):
            for produc in lstProductos:
                for (key, value) in produc.items():
                    if(value == "NombreProducto"):
                        print(value)
            print("Hay "+str(len(lstProductos))+ " productos")



strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]

while True:
    print("--------------------------------")
    print("Bienvenido Escoge la opcion:")
    print("1 : Agregar Producto")
    print("2 : Quitar Producto")
    print("3 : Listar Producto")
    print("4 : Inventariar Producto")
    print("0 : Salir")
    strMenuPrincipal = input()
    if(strMenuPrincipal == "1"):
        addProducto()
    elif(strMenuPrincipal == "2"):
        delProducto()
    elif(strMenuPrincipal == "3"):
        listProductos()
    elif(strMenuPrincipal == "4"):
        invProducto()
    elif(strMenuPrincipal == "0"):
        break
    else:
        opcionSalir = input("No escogio las opciones indicadas; desea salir s/n")
        if(opcionSalir == "s"):
            break
