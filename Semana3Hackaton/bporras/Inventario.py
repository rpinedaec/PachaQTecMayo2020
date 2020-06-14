#Desarrollado pro Bruce Porras - Hackaton Semana 3


#Funcion que devuelve True si el producto ya existe en la lista
def searchproduct(a):
    strNewProduct = a
    for i in lstInventario:
        if i["Producto"] == strNewProduct:
            return True
        else:
            return False
#Función para agregar un nuevo producto
def addproduct():
    while True:
        strMenu = input("Ingrese A para agregar producto y S para salir: ")
        if strMenu=="A":
            print("Menú agregar producto")
            try:
                strNewProduct = input("Ingrese el nombre del nuevo producto: ")
                if searchproduct(strNewProduct):
                        strExiste = input ("El producto ya existe, ¿Desea reemplazarlo? S/N: ")
                        if strExiste == "S":
                            strNewPrice = float(input("Ingrese el precio del nuevo producto: "))
                            strNewCant = float(input("Ingrese la cantidad del producto: ")) 
                            for i,x in enumerate(lstInventario):
                                if x["Producto"] == strNewProduct:
                                    lstInventario[i] = {"Producto" : strNewProduct,"Precio":strNewPrice,"Cantidad":strNewCant}                                  
                            print(94*"-")
                            print(f"|{'Producto':^30}|{'Precio':^30}|{'Cantidad':^30}|")
                            print(94*"-")
                        elif strExiste == "N":
                            break
                        else:
                            print("Error!: Ingrese S o N")
                else:
                    dicNewProduct ={"Producto" : strNewProduct, 
                                "Precio": float(input("Ingrese el precio del nuevo producto: ")), 
                                "Cantidad": float(input("Ingrese la cantidad del producto: "))} 
                    lstInventario.append(dicNewProduct)
                    print(94*"-")
                    print(f"|{'Producto':^30}|{'Precio':^30}|{'Cantidad':^30}|")
                    print(94*"-")
                for i in lstInventario:
                    print(f"|{i['Producto']:^30}|{i['Precio']:^30}|{i['Cantidad']:^30}|")
                print(94*"-")
            except ValueError:
                print("Error!: Ingrese enteros o flotantes para el precio y cantidad")              
            else:
                print(f'Producto agregado correctamente')
        elif strMenu=="S":
            break
        else:
            print("Error!: Opcción incorrecta, digite A o S")
#Función para eliminar un producto existente
def delproduct():
    while True:
        strMenu = input("Ingrese E para eliminar un producto y S para salir: ")
        intIndex = 0
        if strMenu == "E":
            try:
                print(125*"-")
                print(F'|{"Item":^30}|{"Producto":^30}|{"Precio":^30}|{"Cantidad":^30}|')
                print(125*"-")
                for i in lstInventario:
                    intIndex += 1
                    print(f'|{intIndex:^30}|{i["Producto"]:^30}|{i["Precio"]:^30}|{i["Cantidad"]:^30}')
                print(125*"-")
                intItemToDelete=int(input("Indique el item que desea eliminar: "))-1
                strConfirmation=(input(F'Esta seguro de eliminar el Item {intItemToDelete+1} {lstInventario[intItemToDelete]} S/N: '))
                if strConfirmation == "S":
                    del lstInventario[intItemToDelete]
                    print("Item eliminado correctamente")
                elif strConfirmation == "N":
                    break
                else:
                    print("Error!: Opción incorrecta, digite S o N")
            except IndexError:
                print("Error!: Item no encontrado, intente de nuevo")
            except ValueError:
                print("Error!: Introdusca un número entero")
        elif strMenu == "S":
            break
        else:
            print("Opcción incorrecta, intente de nuevo")
#Función para visualizar el inventario total ó el valor de la emrcancia
def invproduct():
    while True:
        strMenu = input("Ingrese I para ver el listado de productos, V para valorizar los productos y S para salir: ")
        fltValTot = 0.0
        intIndex = 0
        if strMenu == "I":
            print(125*"-")
            print("Se tiene registrado {} productos".format(len(lstInventario)))
            print(125*"-")
            print(f"|{'Item':^30}|{'Producto':^30}|{'Precio':^30}|{'Cantidad':^30}|")
            print(125*"-")
            for i in lstInventario:
                intIndex += 1
                print(f"|{intIndex:^30}|{i['Producto']:^30}|{i['Precio']:^30}|{i['Cantidad']:^30}|")
            print(125*"-")
        elif strMenu == "V":
            print (156*"-")
            print (f'|{"Item":^30}|{"Producto":^30}|{"Precio":^30}|{"Cantidad":^30}|{"Valorización":^30}|')
            print (156*"-")
            for i in lstInventario:
                intIndex +=1
                fltValTot += i["Precio"]*i["Cantidad"]
                print(f'|{intIndex:^30}|{i["Producto"]:^30}|{i["Precio"]:^30}|{i["Cantidad"]:^30})|{i["Precio"]*i["Cantidad"]:^30}|')
            print (156*"-") 
            print (f'Valorización total del inventario: S/.{fltValTot}')
            print (156*"-")
        elif strMenu == "S":
            break
        else:
            print("Opcción incorrecta, intente de nuevo")
#Variable a usar en el programa
lstInventario=[]
dicNewProduct={}
strMenuPrincipal=""
#Programa del inventario.
while True:
    print("------------------------")
    print("Bienvenido escoge una opción: ")
    print("1 : Agregar producto")
    print("2 : Quitar producto")
    print("3 : Mostrar inventario")
    print("0 : Salir")
    strMenuPrincipal = input()
    if strMenuPrincipal == "1":
        addproduct()
    elif strMenuPrincipal == "2":
        print("Menú quitar producto")
        delproduct()
    elif strMenuPrincipal == "3":
        print("Menú inventario")
        invproduct()
    elif strMenuPrincipal == "0":
        break
    else:
        print("Opción incorrecta, intente de nuevo")

