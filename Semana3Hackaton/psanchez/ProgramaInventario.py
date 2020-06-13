#Programa de Inventario
#Alumno: Paola Sanchez

strMenuPrincipal="0"
dicInventario={}
lstInventario=[]

def AgregarProd():
    print("Agregar Producto")
    blApmenu=True
    while blApmenu:
        print("Agregando Producto a Inventario")
        blApmenu=input("S/N")
        if(blApmenu=="S"):
            print("Nombre del Producto")
            strNombreProudcto=input()
            print("Precio del Producto S/.")
            flPrecioProducto=float(input())
            print("Número de Existencias")
            intStockProducto=int(input())

            dicInventario={}
            dicInventario.update({"Nombre del Producto":strNombreProducto})
            dicInventario.update({"Precio del Producto":flPrecioProducto})
            dicInventario.update({"Número de Existencias":intStockProducto})

            lstInventario.append(dicInventario)
        else:
            print("Seguro")
            blApmenu=False
            if(blApmenu==False):
                print("Cerrando el programa. Hasta luego!")
                break

