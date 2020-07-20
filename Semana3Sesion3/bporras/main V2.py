###VERSION SIN LISTA

def addproduct():
    while True:
        strMenu = input("Ingrese A para agregar producto y S para salir: ")
        strProduct =""
        fltPrice =""
        if strMenu=="A":
            print("Menú agregar producto")
            strProduct=input("Ingrese el nombre del nuevo producto: ")
            fltPrice=float(input("Ingrese el precio del nuevo producto: "))
            dicInventario[strProduct] = fltPrice
            print("------Producto agregado------")
            print("Producto","=>","Precio")
            print(strProduct,"=> S/.",dicInventario[strProduct])
        elif strMenu=="S":
            break
        else:
            print("Error! = Opcción incorrecta, digite A o S")

def delproduct():
    while True:
        strMenu = input("ingrese E para eliminar un producto y S para salir: ")
        if strMenu == "E":
            print("Item","Producto","Precio")
            for i in range(len(lstInventario)):
                print(i,lstInventario[i])
            intItemToDelete=int(input("Indique el item que desea eliminar: "))
            strConfirmation=(input("Esta seguro de eliminar el Item {} {} Y/N: ".format(intItemToDelete,lstInventario[intItemToDelete])))
            if strConfirmation == "Y":
                del lstInventario[intItemToDelete]
                for i in range(len(lstInventario)):
                    print(i,lstInventario[i])

            elif strConfirmation == "N":
                break
            else:
                print("!Error = Opción incorrecta, digite Y o N")

        elif strMenu == "S":
            break
        else:
            print("!Error = Opción incorrecta, digite E o S")

def showproduct():
    while True:
        strMenu = input("Ingrese I para ver el inventario de productos y S para salir: ")
        dicShowItem ={}
        if strMenu == "I":
            print("Item","Producto","Precio")
            for i,x in dicInventario.items():
                print(i,"=> S/.",x)
        elif strMenu == "S":
            break
        else:
            print("!Error = Opción incorrecta, digite I o S")

dicInventario={}
strMenuPrincipal=""

while True:
    print(
    """
    Bienvenido al Almacén escoja una opción: 
    1 : Agregar producto
    2 : Quitar producto
    3 : Mostrar inventario
    0 : Salir""")
    strMenuPrincipal = input()
    if strMenuPrincipal == "1":
        addproduct()
    elif strMenuPrincipal == "2":
        print("Menú quitar producto")
        delproduct()
    elif strMenuPrincipal == "3":
        print("Menú mostrar inventario")
        showproduct()
    elif strMenuPrincipal == "0":
        break
    else:
        print("Opción incorrecta, intente de nuevo")
        break

