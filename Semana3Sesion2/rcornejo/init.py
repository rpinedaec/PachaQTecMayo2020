#Este programa va hacer un carrito de compras
#Vamos a pedir el nombre del bodeguero.
print ("Hola ¿Cuál es tu nombre?")

strbodeguero = input()
print (f"{strbodeguero} ingresa tu primer producto")
lstproductos = []
lstproductounitario = []
strnombredelproducto = input()
print("Ingresa el valor del producto")
fltvalorproducto = float(input())
lstproductounitario.append(strnombredelproducto)
lstproductounitario.append(fltvalorproducto)
lstproductos.append(lstproductounitario)
print (lstproductounitario)
print (lstproductos)
print(f"{strbodeguero} Deseas agregar otro producto Y/N")
stropcion = input ()
if (stropcion == "Y"):
    print (f"{strbodeguero} ingresa tu primer producto")
    strnombredelproducto = input()
    print("Ingresa el valor del producto")
    fltvalorproducto = float(input())
    lstproductounitario = []
    lstproductounitario.extend([strnombredelproducto, fltvalorproducto])
    lstproductos.append(lstproductounitario)
    print (lstproductounitario)
    print (lstproductos)
else:
    print("Gracias por usar nuestro sistema")
