import Connection

# Read: select por id
def select_factura(id_fact):
    query="SELECT factura.fecha_factura,factura.sub_total_factura,\
        factura.IGV_factura,factura.total_factura,factura.id_factura,\
            detalle_factura.cantidad_detalle_factura,producto.nombre_producto,detalle_factura.\
                total_detalle_factura FROM detalle_factura INNER JOIN producto ON detalle_factura.\
                    producto_id_producto = id_producto INNER JOIN factura ON detalle_factura.factura_id_factura= \
                        factura.id_factura WHERE factura.id_factura="+str(id_fact)
    Connection.mycursor.execute(query)
    reg=Connection.mycursor.fetchall()
    print("--------------------------------------------------")
    print(":::::::::::::::::::::FACTURA:"+str(id_fact)+"::::::::::::::::::::")
    print("fecha de emisión: "+str(reg[0][0]))
    print("--------------------------------------------------")
    a=len(reg)
    print("Producto              Cantidad              Monto          ")
    for n in range(a):
        b=26-len(reg[n][6])
        c=19-len(str(reg[n][5]))
        print(reg[n][6]+" "*b+str(reg[n][5])+" "*c+str(reg[n][7]))
    print("--------------------------------------------------")
    print("Sub total: "+str(reg[0][1]))
    print("IGV: "+str(reg[0][2]))
    print("Total facturado: "+str(reg[0][3]))


 
