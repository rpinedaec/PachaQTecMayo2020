import Connection
from datetime import date

def insert_factura(fecha_factura,sub_total_factura,\
    IGV_factura,total_factura,cliente_id_cliente,\
        metodo_pago_id_metodo_pago,estado_factura):
    query="INSERT INTO factura (fecha_factura,sub_total_factura,"+\
        "IGV_factura,total_factura,cliente_id_cliente,"+\
            "metodo_pago_id_metodo_pago,estado_factura) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    reg=(fecha_factura,sub_total_factura,\
    IGV_factura,total_factura,cliente_id_cliente,\
        metodo_pago_id_metodo_pago,estado_factura)
    Connection.mycursor.execute(query,reg)
    Connection.mydb.commit()

def insert_detalle_factura(factura_id_factura,cantidad_detalle_factura,\
    total_detalle_factura,producto_id_producto):
    query="INSERT INTO detalle_factura (factura_id_factura,cantidad_detalle_factura,\
    total_detalle_factura,producto_id_producto) VALUES (%s,%s,%s,%s)"
    reg=(factura_id_factura,cantidad_detalle_factura,\
        total_detalle_factura,producto_id_producto)
    Connection.mycursor.execute(query,reg)
    Connection.mydb.commit()
    
def create_factura_detalle():
    query="SELECT id_producto, nombre_producto FROM producto"
    Connection.mycursor.execute(query)
    reg=Connection.mycursor.fetchall()
    a=""
    for x in reg:
        a=a+x[1]+" →["+str(x[0])+"]"+"   "
    print(a)
    print("")
    print("Ingrese el codigo del producto y la cantidad,\n0 para dejar de agregar")
    product_list=[]
    price_list=[]
    quantity_list=[]
    code_list=[]
    add=True
    while add:
        code=input("Codigo: ")
        if (code=='0'):
            break
        code_list.append(code)
        quantity=input("Cantidad: ")
        query="SELECT nombre_producto, precio_unitario_producto FROM producto WHERE id_producto="+code
        Connection.mycursor.execute(query)
        reg=Connection.mycursor.fetchall()
        for x in reg:
            product_list.append(x[0])
            price_list.append(x[1])
            quantity_list.append(quantity)
    n=len(product_list)  
    Sub_total_factura=0  
    for x in range(n):    
        Total_product=price_list[x-1]*int(quantity_list[x-1])
        print(product_list[x-1]+": "+str(price_list[x-1])+" x "+str(quantity_list[x-1])+"    ="+str(Total_product))
        Sub_total_factura=Sub_total_factura+Total_product
    print("------------")
    print("Sub-total ="+str(Sub_total_factura))
    IGV_factura=float(Sub_total_factura)*0.18
    print("IGV = "+str(round(IGV_factura,2)))
    Total_factura=float(Sub_total_factura)+IGV_factura
    print("Total = "+str(Total_factura))
    Cliente_id=input("Ingrese el cliente id: ")
    Metodo_pago=input("Ingrese el metodo de pago: ")

    insert_factura(date.today(),Sub_total_factura,IGV_factura,Total_factura,Cliente_id,Metodo_pago,1)

    query="SELECT max(id_factura) from factura"
    Connection.mycursor.execute(query)
    reg=Connection.mycursor.fetchone()
    factura_id=reg[0]
    for x in range(n):
        insert_detalle_factura(factura_id,int(quantity_list[x-1]),int(price_list[x-1]),int(code_list[x-1]))