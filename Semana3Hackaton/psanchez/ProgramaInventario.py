#Programa de Inventario
#Alumno: Paola Sanchez

strMenuPrincipal="0"
dicInventario={}
lstInventario=[]
# Agregar Productos
def AgregarProd():
    print("")
    print("---------------------------------------")
    print("AGREGAR PRODUCTOS AL INVENTARIO")
    print("---------------------------------------")
    print("")
    blApmenu=True
    while blApmenu:
        print("Ten a la mano el nombre, precio y stock del producto")
        Apmenu=input("Escriba S para comenzar : ")
        print("")
        if(Apmenu=="S"):
            print("Nombre del Producto:")
            strNombreProducto=input()
            print("")
            print("Precio del Producto S/:")
            flPrecioProducto=float(input())
            print("")
            print("Número de Existencias:")
            intStockProducto=int(input())

            dicInventario={}
            dicInventario.update({"NombreProducto":strNombreProducto})
            dicInventario.update({"PrecioProducto":flPrecioProducto})
            dicInventario.update({"Cantidad":intStockProducto})

            lstInventario.append(dicInventario)
            print("")
            print("***")
            print("ÉXITO!")
            print("Tu Producto ha sido agregado")
            print("***")
            print("")
            print("1: Ver Inventario")
            print("2: Agregar Producto")
            print("3: Menu Princiapl")
            print("")
            strMenuAgregar=input("Opción número : ")
            if(strMenuAgregar=="1"):
                ListInv()
            elif(strMenuAgregar=="2"):
                AgregarProd()
            elif(strMenuAgregar=="3"):
                MenuPrincipal()
    
        else:
            blApmenu=False
            if(blApmenu==False):
                break
#Quitar Productos
def QuitarPro():
        try:
            while True:
                print("")
                print("---------------------------------------")
                print("ELIMINAR PRODUCTOS DEL INVENTARIO")
                print("---------------------------------------")
                print("")
                strQtmenu = input("Escribe S para continuar : ")
                if(strQtmenu == "S"):
                    print("PRIMERO:")
                    print("Ubica el nombre del producto a eliminar")
                    print("")
                    for p in lstInventario:
                        for (key, value) in p.items():
                            print(key, " : ", value)
                    print("")
                    print("SEGUNDO:")
                    print("Escribe el nombre del producto a eliminar")
                    strProEliminado = input()
                    for p in lstInventario:
                        for (key, value) in p.items():
                            if(value == strProEliminado):
                                lstInventario.remove(p)
                                print("***")
                                print("PRODUCTO ELIMINADO")
                print("")
                print("1: Ver Inventario")
                print("2: Menu Principal")
                print("")
                strMenuQuitar=input("Opción número : ")
                if(strMenuQuitar=="1"):
                    ListInv()
                elif(strMenuQuitar=="2"):
                    MenuPrincipal()   
                else:
                    print("No ingreso una opción válida. Intente nuevamente")
                    QuitarPro()
        except Exception:
            print("No se pudo eliminar. Intente nuevamente")

#Ver Inventario
def ListInv():
    print("")
    print("---------------------------------------")
    print("INVENTARIO")
    print("---------------------------------------")
    print("")
    for p in lstInventario:
        for (key,value) in p.items():
            print(key,":",value)
    print("")
    print("1: Agregar Producto")
    print("2: Quitar Producto")
    print("3: Menu Principal")
    print("")
    strMenuInv=input("Opción número : ")
    if(strMenuInv=="1"):
        AgregarProd()
    elif(strMenuInv=="2"):
        QuitarPro()
    elif(strMenuInv=="3"):
        MenuPrincipal()

#Detalles del Inventario
def ValorInv():
    print("")
    print("---------------------------------------")
    print("DETALLE DEL INVENTARIO")
    print("---------------------------------------")
    print("")
    ValorTotal=0.0
    for p in lstInventario:
        Valor=p["PrecioProducto"]*p["Cantidad"]
        ValorTotal+=Valor
    print(f"Valor Total del Stock : S/", ValorTotal)
    print("")
    StockTotal=0
    for p in lstInventario:
        Stock=p["Cantidad"]
        StockTotal+=Stock
    print(f"Items Totales: ", StockTotal)
    print("")
    print("1: Agregar Producto")
    print("2: Quitar Producto")
    print("3: Menu Principal")
    print("")
    strMenuValor=input("Opción número : ")
    if(strMenuValor=="1"):
        AgregarProd()
    elif(strMenuValor=="2"):
        QuitarPro()
    elif(strMenuValor=="3"):
        MenuPrincipal()

#Calculadora
def Calculadora():
    while True:
        print("")
        print("---------------------------------------")
        print("CALCULADORA")
        print("---------------------------------------")
        print("")
        print("Escribe el nombre del producto a consultar: ")
        strConsulta = input()
        for p in lstInventario:
            for (key, value) in p.items():
                if(value == strConsulta):
                    lstInventario.index(p)
                    print(p)
        print("")
        print("Ahora calculemos: ")
        print("")
        precio=float(input("Ingresa el precio : "))
        descuento=float(input("Ingresa el descuento : "))
        preciocond=float(precio*(descuento/100.00))
        subtotal=float(precio-preciocond)
        print(f"El Subtotal es S/{subtotal}")
        IGV=subtotal*1.18
        print(f"El precio con IGV es S/{IGV}")
        print("")
        print("1: Ver Inventario")
        print("2: Menu Principal")
        print("")
        strMenuCalc=input("Opción número : ")
        if(strMenuCalc=="1"):
            ListInv()
        elif(strMenuCalc=="2"):
            MenuPrincipal()
        else:
            print("No ingreso una opción válida. Intente nuevamente")
#Menu Principal
def MenuPrincipal():
    while True:
        print("---------------------------------------")
        print("INVENTARION 3.0")
        print("---------------------------------------")
        nombre=input("Ingresa tu nombre : ", )
        print(f"¡Hola {nombre}! Qué vamos a hacer hoy?")
        print("Selecciona una opción:")
        print("")
        print("1 : Ver Inventario")
        print("2 : Agregar Producto")
        print("3 : Quitar un producto")
        print("4 : Salir del Programa")
        print("***")
        print("Otras opciones : ")
        print("8 : Calcular Precio + IGV")
        print("9 : Ver Detalle del Inventario")
        print("")
        strMenuPrincipal=input("Opción número : ")

        if(strMenuPrincipal=="1"):
            ListInv()
        elif(strMenuPrincipal=="2"):
            AgregarProd()
        elif(strMenuPrincipal=="3"):
            QuitarPro()
        elif(strMenuPrincipal=="4"):
            print("Saliendo del programa. Hasta luego!")
            exit()
        elif(strMenuPrincipal=="8"):
            Calculadora()
        elif(strMenuPrincipal=="9"):
            ValorInv()
        else:
            print("No ingreso una opción válida. Intente nuevamente")
            strMenuPrincipal=input()
MenuPrincipal()
