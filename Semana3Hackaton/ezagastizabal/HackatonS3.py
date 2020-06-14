#Pantalla Menú

lstProd = []

def AddProducto():
    blAddProd = True
    while blAddProd:
        OpAoS = input("Que deseas hacer Agregar: A / Salir : S ").title()
        if(OpAoS == "A"):
            strNomNuevProd = input("Qué producto quieres agregar: ")
            flValorNuevProd = float(input("Cuál es su valor: "))
            strCantNuevProd = int(input("Cantidad de productos: "))
            DicAddProd = {}
            print(strNomNuevProd)
            print(flValorNuevProd)
            DicAddProd.update({"NombProd": strNomNuevProd})
            DicAddProd.update({"ValorProd": flValorNuevProd})
            DicAddProd.update({"CantProd": strCantNuevProd})
            lstProd.append(DicAddProd)
            print(lstProd)
        elif(OpAoS == "S"):
            print("Saliste")
            blAddProd = False
        else:
            print("Digita una opción válida: A/S")

def DelProducto():
    while True:
        OpQoS = input("Deseas quitar un producto: Q / Salir: S ").title()
        if(OpQoS == "Q" and len(lstProd) != 0):
            print("Los siguientes poductos puedes retirar del inventario: ")
            for p in lstProd:
                for (key, value) in p.items():
                    print(key , " :: ", value )
            ProdRet = input("Escribe el producto que vas a retirar:")
            for p in lstProd:
                for (key, value) in p.items():
                    if(value == ProdRet):
                        print(f"Has retirado: {value}")
                        lstProd.remove(p)
            print("Productos y precios actuales en inventario:")
            # print(lstProd)
            for p in lstProd:
                for (key, value) in p.items():
                    print(key , " :: ", value )
        elif (OpQoS == "Q" and len(lstProd) == 0):
            print("No hay productos en el inventario para retirar")
        elif (OpQoS == "S"):
            print("Elegiste Salir")
            break
        else:
            PresSalir = input("No seleccionaste opción valida, deseas salir: S/N: ")
            if(PresSalir == "S"):
                break
            
def VerInventario():
    while True:
        OpInv = input("Deseas ver el inventario: V / Salir: S ").title()
        if(OpInv == "V" and len(lstProd) == 0 ):
            print("No hay productos agregados al inventario")
        elif(OpInv == "V" and len(lstProd) != 0):
            print(lstProd)
            flValTotal = 0
            for v in range(0,len(lstProd)):
                # print(lstProd[v]['NombProd'])
                # print(lstProd[v]['ValorProd'])
                # print(lstProd[v]['CantProd'])
                flValInvPro = int(lstProd[v]['CantProd']) * int(lstProd[v]['ValorProd'])
                # print(flValInvPro)
                print(f"Valor del inventario {lstProd[v]['NombProd']} es {flValInvPro}")
                flValTotal += flValInvPro
            print(f"El valor total del inventario es {flValTotal}")
        else:
            break



while True:
    try:
        print("-------------------------")
        print("Pantalla Menu de Opciones")
        print("1. Agregar productos al inventario")
        print("2. Retirar productos del inventario")
        print("3. Ver Inventario")
        print("0. Salir del Menú")
        OpcionMenu = int(input("Digita opción:"))

    
        if(OpcionMenu == 1):
            AddProducto()
        elif(OpcionMenu ==2):
            DelProducto()
        elif(OpcionMenu ==3):
            VerInventario()
        elif(OpcionMenu == 0):
            print("Saliste del Menú")
            break
        else:
            PresSalir = input("No seleccionaste opción valida, deseas salir: S/N: ")
            if(PresSalir == "S"):
                break
    except ValueError:
        PresStr = input("Has ingresado una letra donde debería ir un número, deseas salir: S/N: ")
        if(PresStr == "S"):
            break





        
