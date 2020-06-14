#Programa de inventario
# Acciones:
# 1.- Agregar Productos
#   1.1.-Menu para agregar productos o salir
# 2.- Eliminar Producto
#   2.1.-Menu para eliminar producto o salir
# 3.- Inventario
#   3.1.-Menu para Ejecutar el Inventario o salir

strMenuPrincipal = "0"
dicProducto = {}
lstProductos = []

#Agregar un nuevo producto
def addProducto():
    print("******AGREGAR PRODUCTO******")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("Deseas Agregar un producto : A / Salir : S ")
        if(menuProducto == "A"):
            strNombreProducto = input("Digita el nombre del Producto: ")
            #Excepción para cuando se ingresa otro valor que no sea un número
            try:
                flValorProducto = float(input(f"Digita el costo de {strNombreProducto}: "))
                intCantProducto = int(input(f"Digita la cantidad de {strNombreProducto}: "))
                dicProducto = {}
                #Actualizar la lista de productos
                dicProducto.update({"NombreProducto":strNombreProducto})
                dicProducto.update({"ValorProducto":flValorProducto})
                dicProducto.update({"CantidadProducto":intCantProducto})
                print(dicProducto)
                lstProductos.append(dicProducto)
                #Mostrar la lista actualizada de productos ingresados 
                print("***Lista de Productos actualizada***")
                for p in lstProductos:
                    for (key, value) in p.items():
                        print(key , " :: ", value )
            except ValueError:
                    print("Debes ingresar un número. Intente nuevamente")
       
        else:
            print("bye")
            blMenuProducto = False

#Eliminar un producto ingresado
def delProducto1():
    print("*****ELIMINAR PRODUCTOS*****")
    while True:
        menuProducto = input("Deseas eliminar un producto : E / Salir : S ")
        if(menuProducto == "E"):
            #Mostrar la lista de productos
            print("***Lista de Productos***")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
            print("Escribe el nombre del Producto que quieres Eliminar")
            strNombreEliminar = input()
            #Buscar el producto y eliminarlo
            for p in lstProductos:
                for (key, value) in p.items():
                    if(value == strNombreEliminar):
                        print(f"se elimino, {value}")
                        lstProductos.remove(p)               
            print("Lista de Productos actualizada")            
            #Mostrar la lista de productos actualizaza, luego de eliminar un producto
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )

        else:
            print("bye")
            break
#Mostrar el inventario de los productos ingresados

def showInventario():
    totalProducto = 0.0
    print("******INVENTARIO DE PRODUCTOS*******")
    print("Cantidad de Productos:", len(lstProductos))
    #Recorrer la lista de productos y calcular el total del inventario de productos
    for p in lstProductos:
          for (key, value) in p.items():
                    print(key , " :: ", value )
                    totalProducto = float(p['ValorProducto'] * p['CantidadProducto'])
                    totalProducto += totalProducto
    #Mostrar el inventario de productos
    print("El Valor de Invetario es igual:", totalProducto)

#Menú Principal de opciones para productos   
def MenuPrincipal():
    while True:
        print("--------------------------------")
        print("Bienvenido Escoge la opcion:")
        print("1 : AGREGAR PRODUCTO")
        print("2 : ELIMINAR PRODUCTO")
        print("3 : INVENTARIO DE PRODUCTOS")
        print("0 : SALIR")
        strMenuPrincipal = input()
        if(strMenuPrincipal == "1"):
            addProducto()
        elif(strMenuPrincipal == "2"):
            delProducto1()
        elif(strMenuPrincipal == "3"):
            showInventario()
        elif(strMenuPrincipal == "0"):
            break
        else:
            opcionSalir = input("No escogio las opciones indicadas; desea salir s/n")
            if(opcionSalir == "s"):
                break




MenuPrincipal()