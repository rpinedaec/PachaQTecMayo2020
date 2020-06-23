#Programa de inventario
#Acciones:
# 1.- Agregar Productos
#   1.1.- Menu para agregar productos o salir
# 2.- Quitar Producto
#   2.1.- Menu para quitar producto o salir
# 3.- Inventario
#   3.1.- Menu para ejecutar el inventario o salir

strMenuPrincipal = "1"
lstProductos=[]


def addProducto():
    print("Agregar Producto")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("Que deseas agregar=A / Salir=S : ")
        if(menuProducto == "A"):
            #print("Escogio Agregar Producto")
            strNombreProducto = input("Nombre: ")
            flValorProducto = float(input(f"Valor de {strNombreProducto}: "))
            flStockProducto = float(input(f"Stock de {strNombreProducto}: "))
            dicProducto={}
            dicProducto.update({"Nombre":strNombreProducto})
            dicProducto.update({"Valor":flValorProducto})
            dicProducto.update({"Stock":flStockProducto})
            flTotal = flValorProducto*flStockProducto
            dicProducto.update({"Total":flTotal})
            #print(dicProducto)
            lstProductos.append(dicProducto)
            #lstProductos.append(dicProducto)
            #print(lstProductos)
        else: 
            print("bye")
            blMenuProducto = False 


def listProducto():
    print("Listar Producto")
    print("----------------------------")
     
    for p in lstProductos:
        strTitulo = ""
        for(key, value) in p.items():
            strTitulo += str(key)+"\t"+"\t"
        print(strTitulo)
        break

    
    for p in lstProductos:
        strTexto = ""
        for (key, value) in p.items():
            strTexto += str(value)+"\t"+"\t"
            key
            #print(value)
        print(strTexto)
    print("---------------------------- \n\n")
    input("Enter para salir.")
    



def delProducto():
    print("Eliminar Producto")
    blMenuProductoEliminar = True
    while blMenuProductoEliminar:
        menuProducto = input("Que deseas Quitar=D / Salir=S : ")
        if(menuProducto == "D"):
            print("Busca en la lista el producto que deseas quitar")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key, " :: ", value)
            strNombreEliminar = input("Nombre del Producto: ")
            for p in lstProductos:
                for (key, value) in p.items():
                    if(value == strNombreEliminar):
                        if(input(f"borrar {value}???  s/n") == "s" ):
                            lstProductos.remove(p)
                        else:
                            break
        else: 
            #print("bye")
            blMenuProductoEliminar = False 





while strMenuPrincipal != "0":

    print("---------------------------------")
    print("Bienvenido escoje la opción:")
    print("1 : Agregar producto")
    print("2 : Quitar producto")
    print("3 : Inventario")
    print("0 : Salir")
    strMenuPrincipal=input("")

    if(strMenuPrincipal=="1"): 
        addProducto()
    elif(strMenuPrincipal=="2"):
        delProducto()
    elif(strMenuPrincipal=="3"):
        listProducto()
    elif(strMenuPrincipal=="0"):
        break
    else:
        opcionSalir = input("No escogio las opciones indicadas, desea salir s/n?")
        if(opcionSalir == "s"):
            break
    


