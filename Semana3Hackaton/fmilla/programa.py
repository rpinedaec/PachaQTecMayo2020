#Programa de inventario

def menu():
    print("---------------------------------")
    print("Bienvenido Escoge la opcion:")
    print("1 : Agregar Producto")
    print("2 : Quitar Producto")
    print("3 : Inventario")
    print("0 : Salir")

def addProducto():
    print("Agregar Producto")
    blMenuProducto = True
    while blMenuProducto:
        menuProducto = input("¿Que desea hacer? Agregar un producto : A / Salir : S -> ")
        if(menuProducto == "A"):
            try:
                strNombreProducto = input("Digita el nombre del Producto: ")
                flValorProducto = float(input(f"Digita el valor de {strNombreProducto}: "))
                intCantidadProducto = int(input(f"Digita la cantidad de {strNombreProducto}: "))
                dicProducto = {}
                dicProducto.update({"NombreProducto":strNombreProducto})
                dicProducto.update({"ValorProducto":flValorProducto})
                dicProducto.update({"CantidadProducto":intCantidadProducto})
                print("Usted agregó este producto:")
                print(dicProducto)
                lstProductos.append(dicProducto)
                print("Ahora tiene estos productos:")
                print(lstProductos)
            except:
                print("Hay un error: Digite bien")
        else:
            print("Salió de Añadir Producto") 
            blMenuProducto = False

def delProducto():
    print("Entró a Quitar Producto")
    while True:
        menuProducto = input("¿Que desea hacer? Quitar : Q / Salir : S -> ")
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
                        print(f"{value} eliminado")
                        lstProductos.remove(p)
            print("Tiene estos productos aún:")
            print(lstProductos)

        else:
            print("Salió de Quitar Producto") 
            break

def showInventario():
    print("Entró al Inventario")
    while True:
        menuProducto = input("¿Que desea hacer? Ver Inventario : V / Salir : S -> ")
        if(menuProducto == "V"):
            #Cantidad total de productos
            cantproducto = 0
            for i in range(len(lstProductos)):
                Elemento = lstProductos[i]
                valor = Elemento["CantidadProducto"]
                cantproducto = cantproducto + valor
            print(f"Usted tiene {cantproducto} productos")
                
            #Valorización de cada producto
            for i in range(len(lstProductos)):
                Elemento = lstProductos[i]
                Cantidad = Elemento['CantidadProducto']
                Precio = Elemento['ValorProducto']
                valortotal = Cantidad * Precio
                Elemento.update({'MontoTotal':valortotal})
                
                #Sacando values del diccionario Elemento
                producto=Elemento.get('NombreProducto')
                precio=Elemento.get('ValorProducto')
                cantidad=Elemento.get('CantidadProducto')
                total=Elemento.get('MontoTotal')

                #Declarando las variables de los valores del diccionario Elemento
                producto=str(producto)
                precio=float(precio)
                cantidad=int(cantidad)
                total=float(total)

                #Agregando valores a sus listas respectivas
                listaProducto.append(producto)
                listaPrecio.append(precio)
                listaCantidad.append(cantidad)
                listaTotal.append(total)
                
                #Imprimiento listas con un formato tabla
                sep = '|{}|{}|{}|{}|'.format('-'*16,  '-'*10,  '-'*10,  '-'*16)
                print('{0}\n|      Producto  |   Precio | Cantidad |     MontoTotal |\n{0}'.format(sep))
                for producto, precio, cantidad, total in zip(listaProducto, listaPrecio, listaCantidad, listaTotal):
                    print('| {:>14.5} | {:>8} | {:>8} | {:>14.5} |\n{}'.format(producto, precio, cantidad, total,  sep))

            #Monto total del inventario
            s = 0
            for i in range(len(lstProductos)):
                Elemento = lstProductos[i]
                valor = Elemento["MontoTotal"]
                s = s + valor
                print(f"El monto total es de {s} soles")
        else:
            print("Salió del Inventario")
            break

strMenuPrincipal = "0"
dicProducto={}
lstProductos=[]
#Listas para showInventario
listaProducto=[]
listaPrecio=[]
listaCantidad=[]
listaTotal=[]

try:
    while True:
        menu()
        strMenuPrincipal = input()
        if(strMenuPrincipal == "1"):
            addProducto()
        elif(strMenuPrincipal == "2"):
            delProducto()
        elif(strMenuPrincipal == "3"):
            showInventario()
        elif(strMenuPrincipal == "0"):
            break
        else:
            opcionSalir = input("No escogio las opciones indicadas; desea salir s/n -> ")
            if(opcionSalir == "s"):
                break
except:
    print("Error")
finally:
    print("Hasta su próxima visita")