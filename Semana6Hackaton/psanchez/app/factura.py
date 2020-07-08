import connect

def seleccionar():
    conn = conexion.conexionBDD(1)
    query = "select idproductos, nombreproducto as Nombre, valorproducto as Precio, igvproducto as IGV from productos;"
    resconn = conn.consultarBDD(query)
    for row in resconn:
        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        print("Escoja el ID de producto que desea comprar")
        idfactdetalle = 1
        idproducto = input()
        print("Escriba la cantidad que desea comprar")
        cantidad = input()
        print("Elija y escriba el tipo de pago de acuerdo al número en la lista")
        print("Para Transferencia: 1001")
        print("Para Efectivo: 1002")
        print("Para Credito: 1003")
        tipodepago = input()
        query = f"update facdetalle set idproducto = '{idproducto}', cantfacdetalle = '{cantidad}'where idfactdetalle = {idfactdetalle};"
        resConn = conn.ejecutarBDD(query)

cliente
    id_cliente = clientes.nombreCliente
    nombre_cliente = clientes.nombreCliente
no_factura = print('E001-01')
fecha_factura = print ('06/07/2020')

ruc
 id_empresa = empresa.idempresa
 ruc_empresa = empresa.rucEmpresa

detalle
    Fila 1:
    d_cantidad = print('ingresar cantidad')
    d_idproducto = productos.idProducto
    d_descripcion = productos.nombreProducto
    d_valor_unitario = productos.valorProducto
    d_valor_total = d_cantidad * d_valor_unitario

subtotal = sum(d_valor_total)
igv = subtotal * 0.18
total = igv + subtotal
