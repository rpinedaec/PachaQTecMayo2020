def addproduct():
    while True:
        strMenu = input("Ingrese A para agregar producto y S para salir: ")
        if strMenu=="A":
            print("Menú agregar producto")
            dicNewProduct ={input("Ingrese el nombre del nuevo producto: "):float(input("Ingrese el precio del nuevo producto: "))} 
            lstInventario.append(dicNewProduct)
            print(lstInventario)
        elif strMenu=="S":
            break
        else:
            print("Error! = Opcción incorrecta, digite A o S")

def delproduct():
    while True:
        strMenu = input("Ingrese E para eliminar un producto y S para salir: ")
        if strMenu == "E":
            print("Item","Producto","Precio")
            for i in range(len(lstInventario)):
                print(i,lstInventario[i])
            intItemToDelete=int(input("Indique el item que desea eliminar: "))
            strConfirmation=(input("Esta seguro de eliminar el Item {} {} Y/N: ".format(intItemToDelete,lstInventario[intItemToDelete])))
            if strConfirmation == "Y":
                del lstInventario[intItemToDelete]
            elif strConfirmation == "N":
                break
            else:
                print("!Error = Opción incorrecta, digite Y o N")

        elif strMenu == "S":
            break
        else:
            print("opcción incorrecta")

def showproduct():
    while True:
        strMenu = input("Ingrese L para ver el listado de productos y S para salir: ")
        if strMenu == "L":
            print("Item","|","Producto","|","Precio")
            for i in range(len(lstInventario)):
                print(i,lstInventario[i])

        elif strMenu == "S":
            break
        else:
            print("!Error = Opción incorrecta, digite I o S")
def invproduct():
    while True:
        strMenu = input("Ingrese I para ver el listado de productos y S para salir: ")
        lstProd = []
        if strMenu == "I":
            for i in lstInventario:
                if "A" in i:
                    lstProd.append(i)
                    print(lstProd)
lstInventario=[]
dicNewProduct={}
strMenuPrincipal=""

while True:
    print("------------------------")
    print("Bienvenido escoge una opción: ")
    print("1 : Agregar producto")
    print("2 : Quitar producto")
    print("3 : Mostrar inventario")
    print("4 : Inventariar")
    print("0 : Salir")
    strMenuPrincipal = input()
    if strMenuPrincipal == "1":
        addproduct()
    elif strMenuPrincipal == "2":
        print("Menú quitar producto")
        delproduct()
    elif strMenuPrincipal == "3":
        print("Menú listar inventario")
        showproduct()
    elif strMenuPrincipal == "4":
        print("Menú inventario")
        invproduct()
    elif strMenuPrincipal == "0":
        break
    else:
        print("Opción incorrecta, intente de nuevo")

