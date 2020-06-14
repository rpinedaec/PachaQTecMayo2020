#Programa de Inventario
#Alumno: Paola Sanchez

strMenuPrincipal="0"
dicInventario={}
lstInventario=[]
# Agregar Productos
def AgregarProd():
    print("--------------------------")
    print("Agregar Producto")
    print("--------------------------")
    blApmenu=True
    while blApmenu:
        print("Escriba S para continuar o N para salir")
        Apmenu=input()
        if(Apmenu=="S"):
            print("Nombre del Producto")
            strNombreProducto=input()
            print("Precio del Producto S/.")
            flPrecioProducto=float(input())
            print("Número de Existencias")
            intStockProducto=int(input())

            dicInventario={}
            dicInventario.update({"NombreProducto":strNombreProducto})
            dicInventario.update({"PrecioProducto":flPrecioProducto})
            dicInventario.update({"Cantidad":intStockProducto})

            lstInventario.append(dicInventario)
            print("******************************")
            print("El producto ha sido agregado")
            print("******************************")
            print("Te gustaría ver el inventario?")
            print("Escribe S para Si y N para No")
            strOpcionInv=input()
            if(strOpcionInv=="S"):
                ListInv()
            elif(strOpcionInv=="N"):
                print("Volviendo al menú principal")
                MenuPrincipal()
        else:
            blApmenu=False
            if(blApmenu==False):
                print("******************************")
                print("Volviendo al menú principal")
                print("******************************")
                MenuPrincipal()
#Quitar Productos
def QuitarPro():
    while True:
        print("--------------------------")
        print("Quitar Producto")
        print("--------------------------")
        print("Te gustaría eliminar un producto?")
        print("Escribe S para Si y N para No")
        Apmenu=input()
        if(Apmenu=="S"):
            print("Ubica el nombre del producto a eliminar")
            for p in lstInventario:
                for (key,value) in p.items():
                    print (key, ":", value)
            print("Escribe el nombre del producto a eliminar")
            try:
                strProEliminado=input()
                for p in lstInventario:
                    for (key, value) in p.items():
                        if(value==strProEliminado):
                            print(f"El producto {value} ha sido eliminado")
                            lstInventario.remove(p)
            except ValueError:
                print("Lo siento, el producto no está en la lista")
        else:
            print("******************************")
            print("Volviendo al Menu Principal")
            print("******************************")
            break
#Ver Inventario
def ListInv():
    print("--------------------------")
    print("Inventario")
    print("--------------------------")
    for p in lstInventario:
        for (key,value) in p.items():
            print(key,":",value)
    print("--------------------------")
#Detalles del Inventario
def ValorInv():
    print("***************************")
    print("DETALLE DEL INVENTARIO")
    print("***************************")
    print("Valor Total del Stock")
    ValorTotal=0.0
    for p in lstInventario:
        Valor=p["PrecioProducto"]*p["Cantidad"]
        ValorTotal+=Valor
    print(f"Valor Total: ", ValorTotal)
    print("Número de items totales en Stock")
    StockTotal=0
    for p in lstInventario:
        Stock=p["Cantidad"]
        StockTotal+=Stock
    print(f"Items Totales: ", StockTotal)
#Menu Principal
def MenuPrincipal():
    while True:
        print("Programa de Inventario")
        print("Selecciona una opción")
        print("1 : Ver Inventario")
        print("2 : Agregar Producto")
        print("3 : Quitar un producto")
        print("4 : Salir del Programa")
        print("9 : Ver Detalle del Inventario")
        strMenuPrincipal=input()

        if(strMenuPrincipal=="1"):
            ListInv()
        elif(strMenuPrincipal=="2"):
            AgregarProd()
        elif(strMenuPrincipal=="3"):
            QuitarPro()
        elif(strMenuPrincipal=="4"):
            print("Saliendo del programa. Hasta luego!")
            break
        elif(strMenuPrincipal=="9"):
            ValorInv()
        else:
            print("Intente nuevamente")
            strMenuPrincipal=input()
MenuPrincipal()
