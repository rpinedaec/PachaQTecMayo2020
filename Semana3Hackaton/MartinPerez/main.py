# Administrador de Productos | Interaccion con Usuario

#Programa de inventario
#Acciones:
# 1.- Agregar Productos
#   1.1.- Menu para agregar productos o salir
# 2.- Quitar Producto
#   2.1.- Menu para quitar producto o salir
# 3.- Inventario
#   3.1.- Menu para ejecutar el inventario o salir

import admProducto
#listUnidadMedida = ["UND"="UN","UND":"KG","UND":"LT","UND":"TON","UND":"MG","UND":"ML"]
listUnidadMedida = ["UN","KG","LT","TON","MG","ML"]
strMenuPrincipal = 1
lstProductos=[]

while strMenuPrincipal != 0:
    print("\n\n")
    print("********************************* MENU ADMINISTRACION DE INVENTARIOS (Soles/Dolares) ***************************************")
    print("Bienvenido escoje la opción:")
    print("1 : Agregar producto")
    print("2 : Quitar producto")
    print("3 : Inventario")
    print("0 : Salir")
    strMenuPrincipal=admProducto.validarEntero("Seleccion: ")

    if(strMenuPrincipal==1): 
        lstProductos = admProducto.addProducto(lstProductos,listUnidadMedida)
    elif(strMenuPrincipal==2):
        lstProductos = admProducto.delProducto(lstProductos)
    elif(strMenuPrincipal==3):
        lstProductos = admProducto.listProducto(lstProductos)
    elif(strMenuPrincipal==0):
        break
    else:
        opcionSalir = input("No escogio las opciones indicadas, desea salir s/n?")
        if(opcionSalir == "s" or opcionSalir == "S"):
            break



