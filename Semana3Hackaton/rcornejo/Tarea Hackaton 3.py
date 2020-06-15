#Programa de inventario - Hackaton 3
#Alumno : Ricardo Cornejo

dicProducto={}
lstProductos=[{"Producto":"Silla","Precio S/":50,"Stock":10},
              {"Producto":"Mesa","Precio S/":22,"Stock":3}]

#Agregar productos
def addProducto():
    print("-------------------------------------")
    print("\033[;36m"+"Escogiste: Agregar producto")
    print("-------------------------------------")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("¿Qué deseas hacer? *a* para agregar producto | *s* para salir : ")
        if(menuProducto == "a"):
            print("-------------------------------------")
            strNombreProducto = input("Digita el nombre del producto: ")
            print("-------------------------------------")
            flValorProducto = float(input(f"Digita el precio(und.) de {strNombreProducto}: S/ "))
            print("-------------------------------------")
            intCantProducto = int(input(f"Digita el stock del producto: "))
            print("-------------------------------------")
            dicProducto = {}
            dicProducto.update({"Producto":strNombreProducto})
            dicProducto.update({"Precio":flValorProducto})
            dicProducto.update({"Stock":intCantProducto})
            lstProductos.append(dicProducto)
            #print(lstProductos)
            for p in lstProductos:
             for (key, value) in p.items():  
                   print(key , "  \t:  ", value )
                   
        else:
            print("-------------------------------------")
            print("\033[;36m"+"*******¡GRACIAS, HASTA LUEGO!********")
            blMenuProducto = False
        

#Eliminar productos
def delProducto():
    print("-------------------------------------")
    print("\033[;35m""Escogiste: Quitar producto")
    print("-------------------------------------")
    while True:
        menuProducto = input("¿Qué deseas hacer? q = Quitar producto | s = Salir :")
        if(menuProducto == "q"):
            print("-------------------------------------------------")
            print("Busca en la lista el producto que deseas quitar")
            print("-------------------------------------------------")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , "  \t:  ", value )
            print("-------------------------------------------------")
            print("Escribe debajo el nombre del producto que quieres quitar:")
            print("-------------------------------------------------")
            strNombreEliminar = input()
            print("-------------------------------------------------")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , "  \t:  ", value )
                    if(value == strNombreEliminar):
                        lstProductos.remove(p)
                        print("-------------------------------------")
                        print(f"Acabas de borrar {value}")
                        opcionSalir = input("¿Desea regresar al menú? s = SI | n = NO ")
                        if(opcionSalir == "s"):
                            break            

        else:
            print("-------------------------------------")
            print("*******¡GRACIAS, HASTA LUEGO!********")
            break

#Mostrar Inventario
def showInventario():
    print("-------------------------------------")
    print("\033[;34m"+"Aquí te muestro el inventario")
    print("-------------------------------------")
    for p in lstProductos:
         for (key, value) in p.items():  
                   print(key , "  \t:  ", value )
    print("-------------------------------------")
    while True:
            menuProducto = input("Para salir digita la letra s :")
            if (menuProducto == "s"):
                print("-------------------------------------")
                print("*******¡GRACIAS, HASTA LUEGO!********")
                break
    
#Lista de productos
def listProductos():
    print("-------------------------------------")
    print("\033[;37m"+"Aquí tienes la lista de productos:")
    print("-------------------------------------")
    for p in lstProductos:
          for (key, value) in p.items():
                   print(key , "  \t:  ", value)
     
    print("-------------------------------------")
    while True:
            menuProducto = input("Digita la letra *s* para salir :")
            if (menuProducto == "s"):
                print("-------------------------------------")
                print("*******¡GRACIAS, HASTA LUEGO!********")
                break
    
#Valorización de inventario

def valueinventario():
    
    print("-------------------------------------")
    print("\033[;31m"+"Escogió Valorización de inventario")
    print("-------------------------------------")
    totalsoles = 0.0 #le decimos al programa que el valor es un float
    for producto in lstProductos:
            print(producto) 
            costototal = producto["Precio S/"] * producto ["Stock (uds.)"] #le decimos al programa que pase por todas la llaves y valores.
            print("S/",costototal)
            totalsoles += costototal 
    print("-------------------------------------")        
    print("----AQUÍ TIENES EL VALOR TOTAL DEL INVENTARIO----")    
    print("\x1b[1;33m"+"S/",totalsoles) #Resultado en float  
    print("\033[;31m"+"-------------------------------------") 
            
    while True:
            menuProducto = input("Digita la letra *s* para salir :")
            if (menuProducto == "s"):
                print("-------------------------------------")
                print("*******¡GRACIAS, HASTA LUEGO!********")
                break
  
#Conteo total de productos        
def contProductos():

    print("-------------------------------------")
    print("\033[;36m"+"Escogió: Conteo total del productos")
    print("-------------------------------------")
    
    totalproductos = 0 #Le decimos al programa que el valor es un entero
    for producto in lstProductos:
        print(producto) 
        intCantProducto = producto ["Stock (uds.)"] + producto ["Stock (uds.)"]#Que pase por cada llave Stock.
        print(intCantProducto, "unidades")
        totalproductos += intCantProducto
    print("----AQUÍ TIENES EL TOTAL DE PRODUCTOS----")    
    print("\x1b[1;33m"+"TOTAL: ",totalproductos)  #resultado integer
    print("\033[;36m"+"-------------------------------------")   
            
    while True:
            menuProducto = input("Digita la letra *s* para salir :")
            if (menuProducto == "s"):
                print("-------------------------------------")
                print("*******¡GRACIAS, HASTA LUEGO!********")
                break
 
    
#Menú principal

strMenuPrincipal = "0"

dicProducto={}
lstProductos=[{"Producto":"Silla","Precio S/":50,"Stock (uds.)":10},
              {"Producto":"Mesa","Precio S/":22,"Stock (uds.)":3}]

while True:
    print("____________________________________")
    print ("\x1b[1;33m"+"---------- MENÚ PRINCIPAL ----------")
    
    print("---¡Bienvenido, escoge la opción!---")
    print("------------------------------------")
    print("\033[;33m"+"0 : Salir del programa")
    print("\033[;36m"+"1 : Agregar producto")
    print("\033[;35m"+"2 : Quitar producto")
    print("\033[;37m"+"3 : Lista de productos")
    print("\033[;34m"+"4 : Inventario")
    print("\033[;31m"+"5 : Valorización de productos")
    print("\033[;36m"+"6 : Conteo total de stock")
    print("\x1b[1;33m"+"-----------------------------------")
    print("Digita aquí debajo el número:")
    strMenuPrincipal = input()
    if(strMenuPrincipal == "1"):
        addProducto()
    elif(strMenuPrincipal == "2"):
        delProducto()
    elif(strMenuPrincipal == "3"):
        listProductos()
    elif(strMenuPrincipal == "4"):
        showInventario()
    elif(strMenuPrincipal == "5"):
        valueinventario()
    elif(strMenuPrincipal == "6"):
        contProductos()
    elif(strMenuPrincipal == "0"):
        break
    else:
        opcionSalir = input("No escogió las opciones indicadas. ¿Desea salir del programa? s/n : ")
        if(opcionSalir == "s"):
            break
