#Programa de Inventario
# Acciones:
# 1. Agregar Productos
#   1.1. Menú para agregar productos o salir
# 2. Quitar Productos
#   2.1. Menú para quitar producto o salir
# 3. Inventario
#   3.1. Menú para ejecutar el inventario o salir
# 4. Lista de Productos
#   4.1. Listar productos1 

strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]
flttxttotprod= 0

#Agregar Producto
def addProducto():
    try:
        print("")
        print("--------------------------------")
        print("Agregar Producto")
        print("--------------------------------")
        blMenuProducto = True
        while blMenuProducto:
            menuProducto = input("¿Qué deseas hacer? Agregar : A / Salir : S - ")
            print("")
            if(menuProducto == "A"):
                strNombreProducto = input("Ingresa el nombre del producto: ")
                strMarcaProducto=input(f"Ingresa la marca de {strNombreProducto}: ")
                strModeloProducto=input(f"Ingresa el modelo de {strNombreProducto}: ")
                strColorProducto=input(f"Ingresa el color de {strNombreProducto}: ")
                strCategoriaProducto=input(f"Ingresa la categoría de {strNombreProducto}: ")
                strSubCategoriaProducto=input(f"Ingresa la subcategoría de {strNombreProducto}: ")
                ftlCantidadProducto=float(input(f"Ingresa la cantidad de {strNombreProducto}: "))
                flValorProducto = float(input(f"Ingresa el valor en soles de {strNombreProducto}: "))
                print("")    
                dicProducto = {}
                dicProducto.update({"Nombre del Producto":strNombreProducto})
                dicProducto.update({"Marca del Producto":strMarcaProducto})
                dicProducto.update({"Modelo del  Producto":strModeloProducto})
                dicProducto.update({"Color del Producto":strColorProducto})
                dicProducto.update({"Categoria del Producto":strCategoriaProducto})
                dicProducto.update({"Subcategoria del Producto":strSubCategoriaProducto})
                dicProducto.update({"Cantidad del Producto":ftlCantidadProducto})
                dicProducto.update({"Valor del Producto":flValorProducto})
                
                lstProductos.append(dicProducto)
            
            else:
                print("Finalizó")
                blMenuProducto = False
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("No se puede convertir letras en números")
    except:
        print("Unexpected error:")
        raise                 
        
#Quitar Producto
def delProducto():
    try:
        print("")
        print("--------------------------------")
        print("Entro a Quitar Producto")
        print("--------------------------------")
        while True:
            menuProducto = input("¿Qué deseas hacer? Quitar : Q / Salir : S - ")
            print("")
            if(menuProducto == "Q"):
                print("Busca en la lista el producto que deseas quitar: \n")
                for p in lstProductos:
                    for (key, value) in p.items():
                        print(key,":",value )
                print("")
                strNombreEliminar = input("Escribe el nombre del producto que quieres quitar: ")
                print("")
                for p in lstProductos:
                    for (key, value) in p.items():
                        if(value == strNombreEliminar):
                            print(f"Se ha quitado {value} del inventario")
                            print("")
                            lstProductos.remove(p)
                print(lstProductos)
                print("")

            else:
                print("Finalizó")
                break
    except:
        print("No se pudo eliminar")
        
#Mostrar Inventario
def showInventario():
    print("")
    print("--------------------------------")
    print("Entró a Inventario")
    print("--------------------------------")
    print(lstProductos)
    fltTotal=0.0
    for p in lstProductos:
        for (key, value) in p.items():
            fltTotal = p['Cantidad del Producto'] * p['Valor del Producto']
        fltTotal += flttxttotprod
    print("El valor total es: ", fltTotal)

#Lista de Productos
def listProducto():
    print("--------------------------------")
    print("Lista de productos")
    print("--------------------------------")
    print("")
    for p in lstProductos:
      for (key, value) in p.items():
         print(key,":",value) 
    
#Menú Principal
def MenuPrincipal():
    while True:
        print("--------------------------------")
        print("Bienvenid@, escoge una opción:")
        print("--------------------------------")
        print("1 : Agregar Producto")
        print("2 : Quitar Producto")
        print("3 : Inventario")
        print("4 : Lista de Productos")
        print("0 : Salir \n")
        
        strMenuPrincipal = input("Ingrese el número: ")
        if(strMenuPrincipal == "1"):
            addProducto()
        elif(strMenuPrincipal == "2"):
            delProducto()
        elif(strMenuPrincipal == "3"):
            showInventario()
        elif(strMenuPrincipal == "4"):
            listProducto()
        elif(strMenuPrincipal == "0"):
            break
        else:
            opcionSalir = input("No escogio las opciones indicadas; desea salir s/n")
            if(opcionSalir == "s"):
                break
            
MenuPrincipal()
