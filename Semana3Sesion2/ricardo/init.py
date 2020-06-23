# Este programa va a ser un carrito de compras
# Vamos a pedir el nombre bodeguero
print("Hola ¿Cuál es tu nombre?")
strBodeguero = input()
print(f"{strBodeguero} Ingresa el nombre del producto")
lstProductos = []
lstProductoUnitario = []
strNombreProducto = input()
print("Ingresa el valor del producto")
fltValorProducto = float(input())
lstProductoUnitario.append(strNombreProducto)
lstProductoUnitario.append(fltValorProducto)
lstProductos.append(lstProductoUnitario)
print(lstProductoUnitario)
print(lstProductos)
print(f"{strBodeguero} Deseas agregar otro producto, Y/N")
strOpcion = input()
if (strOpcion == "Y"):
    print(f"{strBodeguero} Ingresa el nombre del producto")
    strNombreProducto = input()
    print("Ingresa el valor del pruducto")
    fltValorProducto = float(input())
    lstProductoUnitario = []
    lstProductoUnitario.extend([strNombreProducto, fltValorProducto])
    lstProductos.append(lstProductoUnitario)
    print(lstProductoUnitario)
    print(lstProductos)
else:
    print("Gracias por usar nuestros servicio")
    