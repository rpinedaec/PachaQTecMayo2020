#Funcion para autoincrementar Id_Producto
def autoID():
    ID = 0
    for p in lstProductos:
        for (key, value) in p.items():
            if key == 'Id_Producto':
                ID = value + 1
    return ID

#Funcion para agregar producto
def addProducto():
    #Bucle para regresar al menu y no salir del sistema 
    opcion = True
    while opcion:
        #Solicitamos la operacion que se desea realizar
        print (f'Eligió la opción {tpmenu[0]} \n¿Que desea hacer?\nA Agregar', 'S Salir', 'R Regresar', sep=' / ')
        add = input ()
        #Variable para controlar la excepcion 
        error = True
        #Validar que operacion eligió
        if add == 'A' or add == 'a':
            while error:
                #Control de excepcion para no salir de la operacion, si se agrega un String cambio de Float o Int
                try:                    
                    #Solicitamos datos del producto
                    ID = autoID()
                    NombreProducto = input("Ingrese el nombre del producto:\n")                    
                    PrecioUnidad = float(input(f"Ingrese el precio del producto {NombreProducto}:\n"))
                    Stock = int(input(f"Ingrese el stock disponible del producto {NombreProducto}:\n"))
                    PrecioTotal = PrecioUnidad * Stock
                    #Declaramos una variable tipo diccionario para verificar que dato se esta ingresando
                    dicProducto = {}
                    dicProducto.update({"Id_Producto":ID})
                    dicProducto.update({"Nombre Producto":NombreProducto})
                    dicProducto.update({"Precio x Unidad":PrecioUnidad})
                    dicProducto.update({"Stock":Stock})
                    dicProducto.update({"Precio Total":PrecioTotal})
                    #Mostramos el diccionario
                    print(dicProducto)
                    #Agregamos el producto del diccionario a la lista
                    lstProductos.append(dicProducto)
                    print(lstProductos)
                    print("\nSe registro correctamente.\n")
                    #Si se registra correctamente rompe el ciclo de solicitud (error) 
                    # pero sigue dentro del menu agregar
                    error = False
                    opcion = True
                except Exception:
                    #Si lanza la excepcion  vuelve a pedir datos del producto
                    print('\nDebe ingresar un valor entero o decimal.\n')
                    error = True
        #Si escoge la operacion (Regresar), rompe el ciclo de operaciones y vuelve al menu
        elif add == 'R' or add == 'r':
            opcion = False
        #Si escoge la operacion (Salir), cierra el sistema
        elif add == 'S' or add == 's':
            print ('Eligió salir del programa, Gracias.')
            print('******************FIN******************')
            exit()
        #Si escribe una opcion distinta consulta si desea continuar o cerrar el sistema
        else:
            opin = input('\nIngresó una opcion invalida, ¿Desea (S) Salir o (R) Regresar?\n')
            if opin == 'S' or opin == 's':
                print ('Eligió salir del programa, Gracias.')
                print('******************FIN******************')
                exit()
            elif opin == 'R' or opin == 'r':
                break
            else:
                print('******************FIN******************')
                exit()
def delProducto():
    #Variable y bucle para mantenerse en las operaciones del menu Eliminar
    opcion = True
    while opcion:
        #Solicitamos que operacion va realizar
        print(f'Eligio {tpmenu[1]}\n¿Que desea hacer?\n E Eliminar', 'S Salir', 'R Regresar', sep=' / ')
        dell = input()
        #Si la operacion es Eliminar
        if dell == "E" or dell == "e":
            #Mostramos la lista de los productos que se desea eliminar
            print("\nBusca en la lista el producto que desea eliminar\n")
            for p in lstProductos:
                for (key, value) in p.items():
                    if(key == 'Id_Producto'):            
                        print(value, end='\t\t|\t')
                    if key == 'Nombre Producto':
                        print(value, end='\t\t|\t')                        
                    if key == 'Stock':
                        print(value, end='\t\t|\t\n')
            #Solicitamos que escoja que producto va eliminar
            NombreEliminar = input('\nEscribe el nombre del producto que desea eliminar\n')
            #Recorremos en busca del producto solicitado
            for p in lstProductos:
                for (key, value) in p.items():
                    #Confirmamos si desea eliminar el producto encontrado
                    if value == NombreEliminar:
                        print(f"¿Esta seguro de eliminar {value}? s/n")
                        o = input()
                        if o == 's' or o == 'S':
                            lstProductos.remove(p)
                            print(f'El producto {value} fue eliminado\n')
                            opcion == False
                        elif o == 'n' or o == 'N':
                            print(f'El producto {value} no fue eliminado\n')
                            opcion == True
                        else:
                            print('******************FIN******************')
                            exit()
        #Si escoge la opcion Regresar rompe el ciclo y vuelve al menu
        elif dell == "R" or dell == "r":
            break
        #Si escoge Salir cierra el sistema
        elif dell == 'S' or dell == 's':
            print ('Eligió salir del programa, Gracias.')
            print('******************FIN******************')
            exit()
        #Si ingresa una opcion no valida Solicita continuar o salir
        else:
            opin = input('Ingresó una opcion invalida, ¿Desea (S) Salir o (R) Regresar?\n')
            if opin == 'S' or opin == 's':
                print ('Eligió salir del programa, Gracias.')
                print('******************FIN******************')
                exit()                    
            elif opin == 'R' or opin == 'r':
                opcion = True
            else:
                print('******************FIN******************')
                exit()
def listProducto():
    #Editamos la cabecera
    print('Id Producto', 'Producto', 'Precio x Unidad', 'Cantidad', 'Precio Total', sep='\t|\t', end='\n\t')
    for p in lstProductos:
        for (key, value) in p.items():
            #Mostramos todos los productos de la lista
            if(key == 'Id_Producto'):            
                print(value, end='\t|\t')
            if(key == 'Nombre Producto'):            
                print(value, end='\t\t|\t')
            if key == 'Precio x Unidad':
                print(value, end='\t\t|\t')
            if key == 'Stock':
                print(value, end='\t\t|\t')
            if key == 'Precio Total':
                print(value, end='\n\t')
    print('\nSon todos los productos disponibles en stock, Gracias\n') 

def invProducto():
    #Editamos la cabecera
    print('Id Producto', 'Producto', 'Precio x Unidad', 'Cantidad', 'Precio Total', sep='\t|\t', end='\n\t')
    #Declaramos contadores
    x = 0  
    y = 0  
    for p in lstProductos:
        for (key, value) in p.items():
            #Mostramos todos los productos de la lista
            if(key == 'Id_Producto'):            
                print(value, end='\t|\t')                
            if(key == 'Nombre Producto'):            
                print(value, end='\t\t|\t')
            if key == 'Precio Total':
                print(value, end='\n\t')
                #Sumamos el contador para tener la suma del precio de todos los productos
                y += value
            if key == 'Precio x Unidad':
                print(value, end='\t\t|\t')
            if key == 'Stock':
                print(value, end='\t\t|\t')
                #Sumamos el contador para tener la suma de todos los productos
                x += value        
    print('\nExisten un total de',x , 'Productos en Inventario, con un Precio Total de', y, sep=' \' ', end='\'\n') 

#Inicia el Sistema
print("""
'######:'####'######'##::: ##'##:::'##'######'##::: ##'####'######::'#####::
 ##.. ##. ##::##...::###:: ##:##::: ##:##...::###:: ##. ##::##.. ##'##.. ##:
 ##:: ##: ##::##:::::####: ##:##::: ##:##:::::####: ##: ##::##:: ##:##:: ##:
 ######:: ##::####:::## ## ##:##::: ##:####:::## ## ##: ##::##:: ##:##:: ##:
 ##.. ##: ##::##.::::##. ####. ##: ##::##.::::##. ####: ##::##:: ##:##:: ##:
 ##:: ##: ##::##:::::##:. ###:. ####:::##:::::##:. ###: ##::##:: ##:##:: ##:
 ######:'####:######:##::. ##::. ##::::######:##::. ##'####:######:. #####::
........::....:........:..::::..::::...::::........:..::::..:....:........:: 
'########::'########::'##:::'##::::'###::::'##::: ##:
 ##.... ##: ##.... ##:. ##:'##::::'## ##::: ###:: ##:
 ##:::: ##: ##:::: ##::. ####::::'##:. ##:: ####: ##:
 ########:: ########::::. ##::::'##:::. ##: ## ## ##:
 ##.... ##: ##.. ##:::::: ##:::: #########: ##. ####:
 ##:::: ##: ##::. ##::::: ##:::: ##.... ##: ##:. ###:
 ########:: ##:::. ##:::: ##:::: ##:::: ##: ##::. ##:
........:::..:::::..:::::..:::::..:::::..::..::::..:: """)
print ('Bienvenidos al sistema. ¿Que desea realizar?')
#Productos por defecto
lstProductos=[{'Id_Producto': 1, 'Nombre Producto': 'Lapiz', 'Precio x Unidad': 3.50, 
                'Stock': 100 ,'Precio Total': 350.0},{'Id_Producto': 2, 
                'Nombre Producto': 'Libro', 'Precio x Unidad': 5.0, 'Stock': 75 ,'Precio Total': 375.0} ]
#Tupla para el menu (No se modifica)
tpmenu = ('1. Agregar producto.', '2. Quitar producto.', '3. Listar producto.', 
        '4. Inventariar producto.', '0. Salir del programa.')
#Para mantener abierto el menu
while True:
    #Recorremos y listamos el menu
    for i in tpmenu:
        print(i)
    #Control de error en caso de que ingrese un String
    try:
        #Solicitamos la opcion que se va ejecutar
        op = int(input('Ingrese la operacion que desea hacer: \n'))  
        #opcion 1 Agregar Producto
        if op == 1:
            #Llamamos a la funcion Agregar Producto
            addProducto()
        #opcion 2 Eliminar Producto
        elif op == 2:
            #Llamamos a la funcion Eliminar Producto
            delProducto()
        elif op == 3:
            #Llamamos a la funcion Listar Producto
            listProducto()
        elif op == 4:
            #Llamamos a la funcion Inventario Producto
            invProducto()
        elif op ==  0:
            print ('Eligió salir del programa, Gracias.')
            print('******************FIN******************')
            break
        elif op > 4 or op < 0:
            opin = input ('Eligió una operacion invalida, ¿Desea (S) Salir o (R) Regresar?\n')
            if opin == 'S' or opin == 's':
                break
            elif opin == 'R' or opin == 'r':
                pass
            else:
                print('******************FIN******************')
                exit()
        else:
            print('Ingreso')
    except Exception:
        print('Ingreso una opcion no valida.\nSe cerrara el programa, Adios')
        print('******************FIN******************')
        exit()
    
