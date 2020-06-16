# :::::Programa de inventario::::::::
# :::::ERIN MADRID::::::BACKEND::::::
# :::::13/06/2020:::::::Ver.1.0::::::
# Acciones:
# 1.- Agregar Productos
#   1.1.-Menu para agregar productos o salir
# 2.- Quitar Producto
#   2.1.-Menu para quitar producto o salir
# 3.- Listar Producto
#   3.1.-Menu para Listar Producto o salir
# 4.- Inventario
#   4.1.-Menu para Ejecutar el Inventario o salir

# Modulo con control de excepciones 
# para validar el ingreso correcto a las Opciones
def ingresarOpcion():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Ingresa una Opcion: "))
            correcto=True
        except ValueError:
            print("\033[1;31m"+'Error, introduce un numero entero'+'\033[0;m')
     
    return num

# Modulo para Agregar Productos a Nuestro Inventario.
def addProducto():
    print("\033[1;34m"+":::::::::::::SUB MENU AGREGAR PRODUCTO::::::::::::::"+'\033[0;m')
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("Que deseas hacer Agregar (A) / Salir (S) : ")
        if(menuProducto == "A"):
            strNombreProducto = input("Digita el nombre del Producto: ")

            costoCorrecto = False
            while(not costoCorrecto):
                try:
                    flValorProducto = float(input(f"Digita en valor de {strNombreProducto}: "))
                    costoCorrecto = True
                except ValueError:
                    print("\033[1;31m"+'Error, Ingrese un numero entero o decimal'+'\033[0;m')

            cantidadCorrecto = False
            while(not cantidadCorrecto):
                try:
                    intCantidad = int(input(f"Digita la Cantidad de {strNombreProducto}: "))
                    cantidadCorrecto = True
                except ValueError:
                    print("\033[1;31m"+'Error, Ingrese un numero entero '+'\033[0;m')
                    
            dicProducto = {}
            dicProducto.update({"nombreProducto":strNombreProducto})
            dicProducto.update({"valorProducto":flValorProducto})
            dicProducto.update({"cantProducto":intCantidad})
            print(dicProducto)
            lstProductos.append(dicProducto)
            print(lstProductos)
        else:
            print("\033[1;31m"+"Gracias, Salio con exito del Sub Menu Agregar Producto"+'\033[0;m')
            blMenuProducto = False

# Modulo para Eliminar Productos de Nuestro Inventario.
def delProducto():
    print("\033[1;34m"+":::::::::::::SUB MENU ELIMINAR PRODUCTO::::::::::::::"+'\033[0;m')
    while True:
        menuProducto = input("Que deseas hacer ELIMINAR (E) / SALIR (S) : ")
        if(menuProducto == "E"):
            print("Busca en la lista el producto que deseas quitar")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
            print("Escribe el nombre del Producto que quieres Eliminar")
            strNombreEliminar = input()
            for p in lstProductos:
                for (key, value) in p.items():
                    if(value == strNombreEliminar):
                        print(f"Borrar {value}?")
                        lstProductos.remove(p)
            print(lstProductos)

        else:
            print("\033[1;31m"+"Gracias, Salio con exito del Sub Menu Elimiar Producto"+'\033[0;m')
            break

# Modulo para Listar Productos.
def listarProductos():
    print("Entro a Sub Menu Listar Producto")
    while True:
        menuProducto = input("Que deseas hacer Listar (L) / Salir (S) : ")
        if(menuProducto == "L"):
            print("Su lista de productos Son:")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
        else:
            print("\033[1;31m"+"Gracias, Salio con exito del Sub Menu Lista de Productos"+'\033[0;m')
            break

# Modulo para Valorizar Inventario Productos.
def inventario():     

    print("Sub Menu Inventario de Productos")
    while True:
        menuProducto = input("Que deseas hacer Inventariar (I) / Salir (S) : ")
        if(menuProducto == "I"):
            fltTotal = 0.0
            print("\033[1;34m"+":::::::::::::VALORIZACION DE INVENTARIO::::::::::::::"+'\033[0;m')
            for p in lstProductos:
                fltSP = p['cantProducto'] * p['valorProducto']
                print(f"\033[1;33m"+"La Valorizacion de "+'\033[0;m',"\033[1;33m"+p['nombreProducto']+'\033[0;m',"\033[1;33m"+" es: \t\t\t"+'\033[0;m',"S/.",float(fltSP))
                fltTotal += fltSP
            print("\033[1;33m"+"----------------------------------------------------- "+'\033[0;m')    
            print("\033[1;33m"+"La Valorizacion Total es: \t\t\t"+'\033[0;m',"S/.",float(fltTotal))
            
        else:
            print("\033[1;34m"+"Gracias, Salio con exito del Sub Menu Inventario"+'\033[0;m')
            break
    

strMenuPrincipal = 0
dicProducto={}
lstProductos=[{"nombreProducto":"Silla","valorProducto":50,"cantProducto":10},{"nombreProducto":"Mesa","valorProducto":22,"cantProducto":3}]

while True:
    print("\033[1;34m"+"--------------------------------"+'\033[0;m')
    print("\033[1;34m"+"Bienvenido Sistema de Inventario:"+'\033[0;m')
    print("\033[1;34m"+"--------------------------------"+'\033[0;m')
    print("\033[1;33m"+"1 : Agregar Producto"+'\033[0;m')
    print("\033[1;33m"+"2 : Quitar Producto"+'\033[0;m')
    print("\033[1;33m"+"3 : Listar"+'\033[0;m')
    print("\033[1;33m"+"4 : Inventario"+'\033[0;m')
    print("\033[1;33m"+"0 : Salir"+'\033[0;m')
    
    strMenuPrincipal = ingresarOpcion()
    if(strMenuPrincipal == 1):
        addProducto()
    elif(strMenuPrincipal == 2):
        delProducto()
    elif(strMenuPrincipal == 3):
        listarProductos()
    elif(strMenuPrincipal == 4):
        inventario()
    elif(strMenuPrincipal == 0):
        break
    else:
        opcionSalir = input("\033[1;31m"+"Introduce un numero entre 0 y 4 o si Desea Salir (S)" +'\033[0;m')
        if(opcionSalir == "S"):
            break

