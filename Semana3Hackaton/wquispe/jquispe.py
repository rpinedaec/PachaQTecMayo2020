#3ER HACKATHON - REALIZAR PROGRAMA DE INVENTARIOS

#Función para autoincrementar Id_Producto
def autoID():
    ID = 0
    for p in Listado:
        for (mmm, value) in p.items():
            if mmm == "Id_Producto":
                ID = value + 1
    return ID
#Función para agregar productos
def addProduct():
    #Bucle para regresar al menu y no salir del sistema 
    opcion = True
    while opcion:
       #Menú de opciones
        print (f"Eligió la opción {optmenu[0]} \n¿Que desea hacer?\nA Agregar", "S Salir", "R Regresar", sep=" / ")
        add = input ()
        #Variable para controlar la excepcion 
        error = True
        #Validar que operación eligió
        if add == "A" or add == "a":
            while error:
                #Control de excepcion para no salir de la operación.
                try:                    
                    #Solicitamos datos del producto
                    ID = autoID()
                    ProductName = input("Ingrese el nombre del producto:\n")                    
                    UnitPrice = float(input(f"Ingrese el precio del producto {ProductName}:\n"))
                    Stock = int(input(f"Ingrese stock disponible del producto {ProductName}:\n"))
                    TotalPrice = UnitPrice * Stock
                    #Declaramos una variable tipo diccionario para verificar que dato se esta ingresando
                    Productdic = {}
                    Productdic.update({"Id_Producto":ID})
                    Productdic.update({"Nombre Producto":ProductName})
                    Productdic.update({"Precio x Unidad":UnitPrice})
                    Productdic.update({"Stock":Stock})
                    Productdic.update({"Precio Total":TotalPrice})
                    #Mostramos el diccionario
                    print(Productdic)
                    #Agregamos el producto del diccionario a la lista
                    Listado.append(Productdic)
                    print(Listado)
                    print("\nSe registro correctamente.\n")
                    #Si se registra correctamente rompe el ciclo de solicitud (error) 
                    # pero sigue dentro del menu agregar
                    error = False
                    opcion = True
                except Exception:
                    #Si lanza la excepcion  vuelve a pedir datos del producto
                    print("\nDebe ingresar un valor entero o decimal.\n")
                    error = True
        elif add == "R" or add == "r":
            opcion = False
        #Si escoge la operacion (Salir), cierra el sistema
        elif add == "S" or add == "s":
            print("***FIN***")
            exit()
        #Si escribe una opcion distinta consulta si desea continuar o cerrar el sistema
        else:
            ErrorMessagge = input("\nIngresó una opcion invalida, ¿Desea (S) Salir o (R) Regresar?\n")
            if ErrorMessagge == "S" or ErrorMessagge == "s":
                print("***FIN***")
                exit()
            elif ErrorMessagge == "R" or ErrorMessagge == "r":
                break
            else:
                print("***FIN***")
                exit()
#Función para quitar productos
def delProduct():
    #Variable y bucle para mantenerse en las operaciones del menu Eliminar
    opcion = True
    while opcion:
        #Solicitamos que operacion va realizar
        print(f"Eligio {optmenu[1]}\n¿Que desea hacer?\n E Eliminar", "S Salir", "R Regresar", sep=" / ")
        dell = input()
        #Si la operacion es Eliminar
        if dell == "E" or dell == "e":
            #Mostramos la lista de los productos que se desea eliminar
            print("\nBusca en la lista el producto que desea eliminar\n")
            for p in Listado:
                for (mmm, value) in p.items():
                    if(mmm == "Id_Producto"):            
                        print(value, end="\t\t|\t")
                    if mmm == "Nombre Producto":
                        print(value, end="\t\t|\t")                        
                    if mmm == "Stock":
                        print(value, end="\t\t|\t\n")
            #Solicitamos que escoja que producto va eliminar
            NombreEliminar = input("\nEscribe el nombre del producto que desea eliminar\n")
            #Recorremos en busca del producto solicitado
            for p in Listado:
                for (mmm, value) in p.items():
                    #Confirmamos si desea eliminar el producto encontrado
                    if value == NombreEliminar:
                        print(f"¿Esta seguro de eliminar {value}? s/n")
                        o = input()
                        if o == "s" or o == "S":
                            Listado.remove(p)
                            print(f"El producto {value} fue eliminado\n")
                            opcion == False
                        elif o == "n" or o == "N":
                            print(f"El producto {value} no fue eliminado\n")
                            opcion == True
                        else:
                            print("***FIN***")
                            exit()
        elif dell == "R" or dell == "r":
            break
        #Si escoge Salir cierra el sistema
        elif dell == "S" or dell == "s":
            print("***FIN***")
            exit()
        else:
            ErrorMessagge = input("Ingresó una opcion invalida, ¿Desea (S) Salir o (R) Regresar?\n")
            if ErrorMessagge == "S" or ErrorMessagge == "s":
                print("***FIN***")
                exit()                    
            elif ErrorMessagge == "R" or ErrorMessagge == "r":
                opcion = True
            else:
                print("***FIN***")
                exit()
#Función para Listar Productos
def listProduct():
    #Editamos la cabecera
    print("Id Producto", "Producto", "Precio x Unidad", "Cantidad", "Precio Total", sep="\t|\t", end="\n\t")
    for p in Listado:
        for (mmm, value) in p.items():
            #Mostramos todos los productos de la lista
            if(mmm == "Id_Producto"):            
                print(value, end="\t|\t")
            if(mmm == "Nombre Producto"):            
                print(value, end="\t\t|\t")
            if mmm == "Precio x Unidad":
                print(value, end="\t\t|\t")
            if mmm == "Stock":
                print(value, end="\t\t|\t")
            if mmm == "Precio Total":
                print(value, end="\n\t")
    print("\nSon todos los productos disponibles en stock, Gracias\n") 
#Función para Inventariar Productos
def invProduct():
    #Editamos la cabecera
    print("Id Producto", "Producto", "Precio x Unidad", "Cantidad", "Precio Total", sep="\t|\t", end="\n\t")
    #Declaramos contadores
    x = 0  
    y = 0  
    for p in Listado:
        for (mmm, value) in p.items():
            #Mostramos todos los productos de la lista
            if(mmm == "Id_Producto"):            
                print(value, end="\t|\t")                
            if(mmm == "Nombre Producto"):            
                print(value, end="\t\t|\t")
            if mmm == "Precio Total":
                print(value, end="\n\t")
                #Sumamos el contador para tener la suma del precio de todos los productos
                y += value
            if mmm == "Precio x Unidad":
                print(value, end="\t\t|\t")
            if mmm == "Stock":
                print(value, end="\t\t|\t")
                #Sumamos el contador para tener la suma de todos los productos
                x += value        
    print("\nExisten un total de",x , "Productos en Inventario, con un Precio Total de", y, sep=" \" ", end="\"\n") 
#INICIO DEL PROGRAMA
print ("Bienvenido. ¿Qué desea realizar?")
#Productos por defecto
Listado=[{"Id_Producto": 1, "Nombre Producto": "Corrector", "Precio x Unidad": 3.20, 
                "Stock": 100 ,"Precio Total": 320.0},{"Id_Producto": 2, 
                "Nombre Producto": "Cuaderno", "Precio x Unidad": 4.5, "Stock": 80 ,"Precio Total": 360.0} ]
#Tupla del menú
optmenu = ("1. Agregar producto.", "2. Quitar producto.", "3. Listar producto.", 
        "4. Inventariar producto.", "0. Salir del programa.")
#Bucle para mantener el menú abierto.
while True:
    #Bucle para imprimir todas las opciones del optmenu
    for i in optmenu:
        print(i)
    try:
        #Solicitamos que se ingrese la opcion ha ejecutar
        op = int(input("Ingrese la operacion que desee: \n"))  
        if op == 1:
            #Se llama a la función addProduct
            addProduct()
        elif op == 2:
            #Se llama a la función delProduct
            delProduct()
        elif op == 3:
            #Se llama a la función listProduct
            listProduct()
        elif op == 4:
            #Se llama a la función invProduct
            invProduct()
        elif op == 0:
            print("***FIN***")
            break
        else:
            print("Ingresó una opción invalida, seleccione una opción válida")
    except Exception:
        print("Usted es un robot, no merece ingresar.")
        print("***FIN***")
        exit()