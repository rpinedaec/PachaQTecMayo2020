#Programa de inventario
# Acciones:
# 1.- Agregar Productos
#   1.1.-Menu para agregar productos o salir
# 2.- Quitar Producto
#   2.1.-Menu para quitar producto o salir
# 3.- Inventario
#   3.1.-Menu para Ejecutar el Inventario o salir
strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]
flttxttotprod= 0

#Función para adicionar productos
def addProducto():
    try:    

         print("Agregar Producto")
         blMenuProducto = True
         while blMenuProducto:
            menuProducto = input("que deseas hacer Agregar : A / Salir : S")
            if(menuProducto == "A"):
                strNombreProducto =input("Digita el nombre del Producto: ")
                strMarcaProducto=input(f"Digita la marca de {strNombreProducto}: ")
                strModeloProducto=input(f"Digita el modelo de {strNombreProducto}: ")
                strFamiliaProducto=input(f"Digita la familia de {strNombreProducto}: ")
                strSubFamiliaProducto=input(f"Digita la sub familia de {strNombreProducto}: ")
                strUniMedProducto=input(f"Digita la unidad de medida de {strNombreProducto}: ")
                ftlCantidadProducto=float(input(f"Digita la cantidad de {strNombreProducto}: "))
                flValorProducto = float(input(f"Digita el precio en soles de {strNombreProducto}: "))
            
                dicProducto = {}
                dicProducto.update({"NombreProducto":strNombreProducto})
                dicProducto.update({"MarcaProdcuto":strMarcaProducto})
                dicProducto.update({"ModeloProducto":strModeloProducto})
                dicProducto.update({"UniMedProducto":strFamiliaProducto})
                dicProducto.update({"FamiliaProducto":strSubFamiliaProducto})
                dicProducto.update({"SubFamiliaProducto":strUniMedProducto})
                dicProducto.update({"CantidadProducto":ftlCantidadProducto})
                dicProducto.update({"ValorProducto":flValorProducto})
                # print(dicProducto)
                lstProductos.append(dicProducto)
                #print(lstProductos)
            else:
                print("bye")
                blMenuProducto = False
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("no se puede convertir letras en numeros")
    except:
        print("Unexpected error:")
        raise
        
        
#Función para eliminar productos
def delProducto():
    try:
        print("entro a delProducto")
        while True:
            menuProducto = input("que deseas hacer Quitar : Q / Salir : S ")
            if(menuProducto == "Q"):
                print("Busca en la lista el producto que deseas quitar")
                for p in lstProductos:
                    for (key, value) in p.items():
                        print(key, " :: ", value)
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
    except:
        print("No se pudo eliminar")

#Función para listar productos
def listProducto():
    print("------------------------------------------------------------ \n")
    print("Listado Del Prodcuto \n")
    print("------------------------------------------------------------ \n")
    
    for p in lstProductos:
      for (key, value) in p.items():
         print(key, " :: ", value) 
            

#funcion para mostra el inventario
def showInventario():
    print("Entro a showInventario")
    print(lstProductos)
    fltTotal=0.0
    for p in lstProductos:
        for (key, value) in p.items():
            # print(p['CantidadProducto'])
            flttxttotprod = p['CantidadProducto'] * p['ValorProducto']
        fltTotal += flttxttotprod
    print(fltTotal)

#Función para definir el menu principal
def MenuPrincipal():
 while True:
    print("--------------------------------")
    print("Bienvenido Escoge la opcion:")
    print("1 : Agregar Producto")
    print("2 : Quitar Producto")
    print("3 : Inventario")
    print("4 : Listar Producto")
    
    print("0 : Salir")
    
    strMenuPrincipal = input()
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
