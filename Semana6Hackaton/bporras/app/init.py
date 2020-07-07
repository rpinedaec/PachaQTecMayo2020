from datetime import datetime
import os
import conexion
# Definicion de clases
class Menu:
    def __init__(self, lstOpciones, strTitulo, strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def show(self):
        os.system("cls")
        print(f"\033[1;32;40m")
        print(20*":" + f"{self.strTitulo:^20}" + 20*":")
        print(20*":" + f"{self.strMenuDescr:^20}" + 20*":")
        for k, v in self.lstOpciones.items():
            print(k, "::", v)
        print("9 :: Salir")
        while True:
            try:
                self.OptionSelect = int(input("Ingrese su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect < len(self.lstOpciones)+1:
                    return self.OptionSelect
                elif self.OptionSelect == 9:
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")
class Factura:
    Fecha=""
    ID=""
    IGV=""
    IDFAC=""
    def create():
        conn = conexion.conexionBDD(1)
        query = "select * from cliente;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDNI\t\tNombre\t\tApellido\t\tCorreo")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        Factura.ID = input("Escriba el ID del cliente a facturar: ")
        Factura.IGV = input("Ingrese el porcentaje de IGV a aplicar: ")
        Factura.Fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = f"insert into faccabecera (idCliente,igvFacCabecera,subtotalFacCabecera,totalFacCabecera,fechaFacCabecera,estadoFacCabecera) values ('{Factura.ID}', '{Factura.IGV}','0','0','{Factura.Fecha}','0');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
    def agregarProd():
        conn = conexion.conexionBDD(1)
        query = "select idProducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from producto;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        query = f"SELECT idFacCabecera from faccabecera where fechaFacCabecera='{Factura.Fecha}'and idCliente='{Factura.ID}';"
        resConn = conn.consultarBDD(query)
        Factura.IDFAC= resConn[0][0]
        idProducto= input("Ingrese el ID del producto a facturar: ")
        Cant = input("Ingresa la cantidad del producto a facturar: ")
        query = f"select valorProducto from producto where idProducto= {idProducto};"
        resConn = conn.consultarBDD(query)
        Precio = resConn[0][0]
        print(Precio)
        query = f"insert into facdetalle(idFacCabecera,idProducto,cantFacDetalle,valorFacDetalle) values ('{Factura.IDFAC}','{idProducto}','{Cant}','{Precio}')"
        resConn = conn.ejecutarBDD(query)                    
    def show():
        conn = conexion.conexionBDD(1)
        query = f"select idFacCabecera,fechaFacCabecera,subtotalFacCabecera,igvFacCabecera,totalFacCabecera from faccabecera where idFacCabecera='{Factura.IDFAC}'"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tFecha\t\t\t\tSubtotal\t\tIGV\t\tTotal")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        query= f"select nombreProducto, cantFacDetalle,valorFacDetalle from facdetalle t1  inner join producto t2 on t1.idProducto = t2.idProducto where idFacCabecera={Factura.IDFAC}"
        print("")
        print("\t\t\tProducto\t\tCantidad\t\tDetalle")
        resConn = conn.consultarBDD(query)
        for row in resConn:
            print(f"\t\t\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}")      
        input("continuar???")
    def showall():
        conn = conexion.conexionBDD(1)
        query = f"select idFacCabecera,fechaFacCabecera,subtotalFacCabecera,igvFacCabecera,totalFacCabecera from faccabecera"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tFecha\t\t\t\tSubtotal\t\tIGV\t\tTotal")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        input("continuar???")
class Cliente:
    def show():
        conn = conexion.conexionBDD(1)
        query = "select * from cliente;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDNI\t\tNombre\t\tApellido\t\tCorreo")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        input("continuar???")
    def search():
        dni = int(input("Ingrese el DNI del cliente: "))
        conn = conexion.conexionBDD(1)
        query = f"select * from cliente where dniCliente = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDNI\t\tNombre\t\tApellido\t\tCorreo")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        input("continuar???")
    def modify():
        conn = conexion.conexionBDD(1)
        query = "select * from cliente;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDNI\t\tNombre\t\tApellido\t\tCorreo")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        id = input("Ingrese el id del cliente a modificar: ")
        dni = input("Ingrese el nuevo DNI: ")
        nombre = input("Escriba el nuevo nombre: ")
        apellido = input("Escriba el nuevo apellido: ")
        correo = input("Escriba el nuevo correo: ")
        query = f"update cliente set dniCliente = '{dni}', nombreCliente = '{nombre}', apellidoCliente = '{apellido}', correoCliente = '{correo}' where idCliente = {id};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")
    def create():
        conn = conexion.conexionBDD(1)
        dni = input("Ingrese el DNI del nuevo cliente: ")
        nombre = input("Escriba el nombre del nuevo cliente: ")
        apellido = input("Escriba el apellido del nuevo cliente: ")
        correo = input("Escriba el correo del nuevo cliente: ")
        query = f"insert into cliente (dniCliente,nombreCliente,apellidoCliente,correoCliente) values ('{dni}','{nombre}','{apellido}','{correo}')"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")
    def delete():
        conn = conexion.conexionBDD(1)
        query = "select * from cliente;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tDNI\t\tNombre\t\tApellido\t\tCorreo")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}")
        idCliente = input("Ingrese el ID del cliente a eliminar: ")
        query = f"delete from cliente where idCliente = {idCliente};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")
class Producto:
    def show():
        conn = conexion.conexionBDD(1)
        query = "select * from producto;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
    def search():
        id = int(input("Ingrese el ID del producto: "))
        conn = conexion.conexionBDD(1)
        query = f"select idProducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from producto where idProducto = '{id}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        input("continuar???")
    def modify():
        conn = conexion.conexionBDD(1)
        query = "select idProducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from producto;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        idProducto = input("Ingrese el ID del producto a modificar: ")
        nombre = input("Escriba el nuevo nombre: ")
        valor = input("Escriba el nuevo valor: ")
        igv = input("Escriba si aplica IGV(1) o no aplica IGV(0) : ")
        query = f"update producto set nombreProducto = '{nombre}', valorProducto = '{valor}',igvProducto = '{igv}' where idProducto = {idProducto};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")
    def create():
        conn = conexion.conexionBDD(1)
        nombre = input("Escriba el nombre del nuevo producto: ")
        valor = input("Escriba el valor del nuevo producto: ")
        igv = input("Escriba si aplica IGV(1) o no aplica IGV(0) al nuevo producto: ")
        query = f"insert into producto (nombreProducto, valorProducto, igvProducto) values ('{nombre}','{valor}','{igv}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")
    def delete():
        conn = conexion.conexionBDD(1)
        query = "select idProducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from producto;"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
        idProducto = input("Ingrese el ID del producto a eliminar: ")
        query = f"delete from producto where idProducto = {idProducto};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        input("desea continuar???")
# Definición de todos los menus:
menuPrincipal = Menu({1: "Crear Factura", 2: "Mantenimientos"},
                     "VENTAS GROUP S.A.", "Menú Principal")
menuFactura = Menu({1: "Crear Factura", 2: "Ver todas las facturas"},
                    "VENTAS GROUP S.A.", "Menú Factura")
menuMantenimiento = Menu({1: "Clientes",    2: "Productos"},
                   "VENTAS GROUP S.A.", "Menú Mantenimiento")
menuMantCliente = Menu({1: "Mostrar todos los clientes", 2: "Buscar cliente por DNI", 3: "Modificar cliente", 4: "Crear Cliente", 5: "Borrar Cliente"},
                    "VENTAS GROUP S.A.", "Menú Mantenimiento Clientes")
menuMantProductos = Menu({1: "Mostrar todos los productos", 2 : "Buscar producto por ID", 3 : "Modificar producto", 4 : "Crear Producto", 5 : "Borrar producto"},
                    "VENTAS GROUP S.A.", "Menu mantenimiento Productos")
# Menu de navegación
while True:
    intOptionSelect = menuPrincipal.show()
    if intOptionSelect == 1:  # Menu Factura
        while True:
            intOptionSelect = menuFactura.show()
            if intOptionSelect == 1: # Crear factura
                Factura.create()
                Factura.agregarProd()
                while True:
                    more = input("¿Desea agregar mas productos S/N: ?")
                    if more=="S":
                        Factura.agregarProd()
                    elif more =="N":
                        conn = conexion.conexionBDD(1)
                        query = f"select nombreProducto, cantFacDetalle,valorFacDetalle from facdetalle t1  inner join producto t2 on t1.idProducto = t2.idProducto where idFacCabecera='{Factura.IDFAC}'; "
                        resConn = conn.consultarBDD(query)
                        acumulado = 0
                        for i in resConn:
                            acumulado += int(i[1])*int(i[2])
                        acumuladototal = (acumulado+acumulado*int(Factura.IGV)/100)
                        query = f"update faccabecera set subtotalFacCabecera={acumulado}, totalFacCabecera={acumuladototal} where idFacCabecera='{Factura.IDFAC}'"
                        resConn = conn.ejecutarBDD(query)
                        break
                    else: 
                        print("Ingrese S o N")
                Factura.show()
            elif intOptionSelect == 2: # Ver todas las Facturas
                Factura.showall()
            else:
                break
    elif intOptionSelect == 2:  # Menu Mantenimiento
        while True:
            intOptionSelect = menuMantenimiento.show()
            if intOptionSelect == 1:  # Mantenimiento Cliente
                while True:
                    intOptionSelect = menuMantCliente.show()
                    if intOptionSelect == 1:  # Mostrar todos los clientes
                        Cliente.show()
                    elif intOptionSelect == 2:  # Buscar cliente por DNI
                        Cliente.show()
                    elif intOptionSelect == 3:  # Modificar cliente
                        Cliente.modify()
                    elif intOptionSelect == 4:  # Crear Cliente
                        Cliente.create()
                    elif intOptionSelect == 5:  # Borrar cliente
                        Cliente.delete()
                    else:
                        break
            elif intOptionSelect == 2:  # Mantenimiento Producto 
                while True:
                    intOptionSelect = menuMantProductos.show()
                    if intOptionSelect == 1:  # Mostrar todos los productos
                        Producto.show()
                    elif intOptionSelect == 2:  # Buscar producto por ID
                        Producto.search()
                    elif intOptionSelect == 3:  # Modificar producto
                        Producto.modify()
                    elif intOptionSelect == 4:  # Crear producto
                        Producto.create()
                    elif intOptionSelect == 5:  # Borrar producto
                        Producto.delete()
                    else:
                        break
            else:
                break
    else:
        break
