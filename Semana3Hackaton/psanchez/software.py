#Semana3 Hackathon    
#Agregar
def agregarpro():
    print("Agregemos un producto")
    blproducto = True
    while blproducto:
        print("Listo para comenzar? Escribe S para Si / Q para Salir")
        menuagregarpro = input()
        if(menuagregarpro == "S"):
            strNombreProducto = input("Escribe el nombre del producto: ")
            flValorProducto = float(input(f"Digita en valor de {strNombreProducto}: "))
            intCodigoProducto=int(input(f"Ingresa el código del {strNombreProducto}: "))
            intStockProducto= int(input("Ingresa el número de unidades disponibles: "))
            flValorStockP= float(input(f"Ingresa el valor total del Inventario: "))
            dicProducto = {}
            dicProducto.update({"NombreProducto":strNombreProducto})
            dicProducto.update({"ValorProducto":flValorProducto})
            dicProducto.update({"CodigoProducto":intCodigoProducto})
            dicProducto.update({"StockProducto":intStockProducto})
            dicProducto.update({"VTotalProducto":flValorStockP})
            print(dicProducto)
            lstProductos.append(dicProducto)
            print(lstProductos)
            print("Tu producto ha sido agregado")
        else:
            print(f"Saliendo del programa. Hasta luego")
            blproducto=False

#Quitar
def quitarpro():
    print("Eliminemos un producto")
    while True:
        menuquitarpro = input("Listo para comenzar? Escribe S para Si / Q para Salir")
        if(menuquitarpro == "S"):
            print("Busca en la lista el producto que deseas quitar")
            for p in lstProductos:
                for (key, value) in p.items():
                    print(key , " :: ", value )
            print("Escribe el nombre del Producto que quieres Eliminar")
            strNombreEliminar = input()
            for p in lstProductos:
                for (key, value) in p.items():
                    if(value == strNombreEliminar):
                        print(f"Borrar {value}???")
                        lstProductos.remove(p)
            print(lstProductos)
            print("Tu Producto ha sido eliminado")

        else:
            print("Saliendo del programa")
            break
#Inventario
def mostrarinv():
    print("Mostrando el Inventario")
strMenuP="0"
dicProducto={}
lstProductos=[]

# Menu Principal
def MenuP():
    while True:
        print("Bienvenido al Control de Inventario")
        print("Qué deseas hacer hoy?")
        print("Selecciona una de las opciones")
        print("1 : Revisar Inventario")
        print("2 : Agregar un producto")
        print("3 : Eliminar un producto")
        print("4 : Salir del programa")
        strMenuP=input()
        if(strMenuP=="1"):
            mostrarinv()
        elif(strMenuP=="2"):
            agregarpro()
        elif(strMenuP=="3"):
            quitarpro()
        else:
            print(f"Saliendo del programa. Hasta luego")
            break