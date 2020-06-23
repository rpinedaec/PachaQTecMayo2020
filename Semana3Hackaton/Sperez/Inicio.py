#Trabajo de la Hackaton de Sergio Perez Tafur
#El metodo addProducto va agregar los productos solicitando al usuario el nombre del producto, el valor unitario del producto y la cantidad que va a ingresar al inventario.
def addProducto():
    
        print("Agregar Producto")
        blMenuProducto = True
        while blMenuProducto:
            print ("Para agregar pulse : A / para Salir : S ")
            menuProducto = str(input("seleccione una opcion "))
            menuProducto = menuProducto.upper()
            try:
                if(menuProducto == "A"):
                    strNombreProducto = str(input("Digita el nombre del Producto: "))
                    flValorProducto = float(input(f"Digita en valor de {strNombreProducto} en soles: "))
                    intCantProducto = int(input(f"Digita la cantidad de {strNombreProducto}: "))
                    dicProducto = {}
                    dicProducto.update({"NombreProducto":strNombreProducto})
                    dicProducto.update({"ValorProducto (S/.)":flValorProducto})
                    dicProducto.update({"CantidadProducto (Unid.)":intCantProducto})
                    lstProductos.append(dicProducto)
                    for p in lstProductos:
                        for (key, value) in p.items():
                            print(key , " :: ", value )
                else:
                    break
            except ValueError:
                print ("Digite el opcion de manera correcta")                
#El metodo delProducto va a retirar los productos que el usuario desee, solicitandole solamente el nombre del producto a retirar.
def delProducto():
    print("entro a delProducto")
    while True:
        menuProducto = input("que deseas hacer Quitar : Q / Salir : S ")
        menuProducto = menuProducto.upper()
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
                        menuProducto = input(f"Borrar {value}? Y/N: ")
                        menuProducto = menuProducto.upper()
                        if(menuProducto == "Y"):
                            lstProductos.remove(p)                  
                        elif(menuProducto == "N"):
                            break
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
        else:
            print("bye")
            break
#El metodo listProductos va a mostrar al usuario los productos, cantidades y precios unitarios que existen en el inventario.
def listProductos():
    LIST=True
    while LIST:
        try:
            print("En el Inventario encontramos lo siguiente:")
            for p in lstProductos:
                for (key, value) in p.items():
                    print (key , " :: ", value)
            menuProducto = str(input("Para retornar prisionar R: "))
            menuProducto = menuProducto.upper()
            if (menuProducto == "R"):
                LIST=False
            else:
                print ("Digite la letra solicitada")
        except Exception as e:
            print ("Digite la letra solicitada")    
#El metodo invProducto le mostrara al usurio que funcion desea realizar al inventario, contar los tipos de productos que hay en el inventario y mostrar la valorizacion total del inventario.
def invProducto():
    while True:
        print("--------------------------------")
        print("Escoge la opcion:")
        print("1 : Contar los productos")
        print("2 : Valorizar los productos")
        print("3 : Retornar")
        strMenuSecundario = input()
        if(strMenuSecundario == "1"):
            for p in lstProductos:
                print(p['NombreProducto'])
            print("Hay "+str(len(lstProductos))+ " productos")       
        elif(strMenuSecundario == "2"):
            fltTotal=0.0
            for p in lstProductos:
                fltProd=p['ValorProducto (S/.)']*p['CantidadProducto (Unid.)']
                fltTotal+=fltProd
            print("S/."+str(fltTotal)+ " Soles")        
        elif(strMenuSecundario == "3"):
            break

strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]
#Pantalla principal donde se mostrara las opciones que desee realizar el usuario.
while True:
    try:
        print("--------------------------------")
        print("Bienvenido Escoge la opcion:")
        print("1 : Agregar Producto")
        print("2 : Quitar Producto")
        print("3 : Listar Producto")
        print("4 : Inventariar Producto")
        print("5 : Salir")
        strMenuPrincipal = input()
        if(strMenuPrincipal == "1"):
            addProducto()
        elif(strMenuPrincipal == "2"):
            delProducto()
        elif(strMenuPrincipal == "3"):
            listProductos()
        elif(strMenuPrincipal == "4"):
            invProducto()
        elif(strMenuPrincipal == "5"):
            break
        else:
            opcionSalir = input("No escogio las opciones indicadas; desea salir S/N")
            opcionSalir = opcionSalir.upper()
            if(opcionSalir == "S"):
                break
    except Exception as e:
        print ("Digite un numero del 1 al 5")