            if intOptionSelect == 1: # Crear factura
                        conn = conexion.conexionBDD(1)
                        query = "select * from cliente;"
                        resConn = conn.consultarBDD(query)
                        print("\tID\t\tDNI\t\tNombre\t\tApellido\t\tCorreo")
                        for row in resConn:
                            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
                        ID = input("Escriba el ID del cliente a facturar: ")
                        IGV = input("Ingrese el porcentaje de IGV a aplicar: ")
                        Fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        query = f"insert into faccabecera (idCliente,igvFacCabecera,subtotalFacCabecera,totalFacCabecera,fechaFacCabecera,estadoFacCabecera) values ('{ID}', '{IGV}','0','0','{Fecha}','0');"
                        resConn = conn.ejecutarBDD(query)
                        if(resConn):
                            print("Se ejecuto correctamente")
                        else:
                            print("Hubo un error")
                        input("Agregue los productos y cantidades???")
                        query = "select idProducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from producto;"
                        resConn = conn.consultarBDD(query)
                        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
                        for row in resConn:
                            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
                        query = f"SELECT idFacCabecera from faccabecera where fechaFacCabecera='{Fecha}';"
                        resConn = conn.consultarBDD(query)
                        idFacCabecera = resConn[0][0]
                        print(idFacCabecera)
                        idProducto= input("Ingrese el ID del producto a facturar")
                        Cant = input("Ingresa la cantidad del producto a facturar")
                        query = f"select valorProducto from producto where idProducto= {idProducto};"
                        resConn = conn.consultarBDD(query)
                        Precio = resConn[0][0]
                        print(Precio)
                        query = f"insert into facdetalle(idFacCabecera,idProducto,cantFacDetalle,valorFacDetalle) values ('{idFacCabecera}','{idProducto}','{Cant}','{Precio}')"
                        resConn = conn.ejecutarBDD(query)                  