import conexion



subtotal=0.00
igv=0.00

jjj = True
listDetalle=[]
while jjj == True:
    nombreProducto=input("Ingrese el producto a facturar: ")
    conn = conexion.conexionBDD(1)
    query = f"SELECT * FROM productos WHERE nombreProducto = '{nombreProducto}';"
    resConn = conn.consultarBDD(query)

    if resConn == []:
        print("Ingrese el valor del producto")
        valorProducto = input()
        print("¿El producto tiene IGV?")
        print("""1. El producto esta exonerado del IGV\n 2. El producto tributa el IGV""")
        nnn=int(input())
        if nnn == 1:
            igvProducto = 0
        elif nnn == 2:
            igvProducto = 1
        query = f"INSERT INTO productos (nombreProducto, valorProducto,igvProducto) VALUES('{nombreProducto}','{valorProducto}','{igvProducto}');"
        resConn =conn.ejecutarBDD(query)
        query = f"SELECT * FROM productos WHERE nombreProducto = '{nombreProducto}'"
        resConn = conn.consultarBDD(query)
        valorProducto=float(resConn[0][2])
        idProductos=resConn[0][0]
    else:
        print("El precio por unidad del producto seleccionado es: ",resConn[0][2])
        valorProducto=float(resConn[0][2])
        igvProducto=resConn[0][3]
        idProductos=resConn[0][0]
    
    cantFacDetalle=float(input("Ingrese la cantidad del producto a facturar: "))
    valorFacDetalle=cantFacDetalle*valorProducto
    
    #AGREGAMOS ELEMENTOS A LA LISTA
    listDetalle.append([cantFacDetalle,valorFacDetalle,"idFacturaCabecera",idProductos])
    
    
    if igvProducto == 0:
        igvProducto = 0
    elif igvProducto == 1:
        igvProducto = valorFacDetalle*0.18

    print("=========")

    subtotal=subtotal+valorFacDetalle
    igv = igv + igvProducto

    print("Seleccione una opción?\n1.-Agregar más productos\n2.-Finalizar")
    opcion=int(input("Ingrese su opción: "))
    if opcion == 1:
        jjj=True
    else:
        jjj=False
        print("Finalizamos la carga de productos")

#AQUI TENEMOS LA LISTA DE DETALLE#
print(listDetalle)
#AQUI ENTREGA LOS DATOS DE LA FACTURA
print("El subtotal de la factura es: ",subtotal)
print("El igv de la factura es: ",igv)
total=subtotal+igv
print("El total de la factura es: ",total)
#DEBEMOS CREAR LA FACTURA CABECERA

