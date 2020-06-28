# Prograna de inventario
# Acciones:
# 1: Agregar producto
#     1.1: Menu para agregar productos o salir
# 2: Quitar producto
#     2.1: Menu par quitar productos o salir
# 3: Inventario
#     3.1: Menu para ejecutar el inventario o salir

print("/**/**/**/**/**/**/**/**/**/**/")
print("Bienvenido, escoge una opción")
print("1 : Agregar producto")
print("2 : Quitar producto")
print("3 : Inventario")
print("0 : Salir")
strMenuPrincipal = input()
# Diccionario:
dicProductos={}
while strMenuPrincipal != "0":
    print("/**/**/**/**/**/**/**/**/**/**/")
    print("Bienvenido, escoge una opción")
    print("1 : Agregar producto")
    print("2 : Quitar producto")
    print("3 : Inventario")
    print("0 : Salir")
    strMenuPrincipal = input()
    if(strMenuPrincipal == "1"):
        print("Escogió Agregar Producto")
        strNombreProducto = input("Escribe el nombre del producto: ")
        flValorProducto =float(input(f"Escribe el valor de {strNombreProducto}: "))
        dicProductos.update({"NombreProducto": strNombreProducto})
        dicProductos.update({"ValorProducto": flValorProducto})
        print(dicProductos)
    elif (strMenuPrincipal == "2"):
        print("Escogió Quitar Producto")
    elif(strMenuPrincipal == "3"):
        print("Escogió Inventario")
    elif(strMenuPrincipal == "0"):
        break
    else:
        opcionSalir = input("No escogió las opciones indicadas, ¿desea salir? s/n --> ")
        if(opcionSalir == "s"):
            break

        
    
