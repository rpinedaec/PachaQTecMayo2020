import utils
import conexion

log = utils.log("INIT")
log.info("inicio de programa")

lstClientes = []
lstProductos = []


def mantenimientoCliente():
    dicMenuCliente = {"Listar todos los cliente": 1, 
                    "Buscar Clientes por DocId":2, 
                    "Modificar Cliente por DocId":3,
                    "Crear Cliente":4,
                    "Borrar Cliente":5
                    }
    menuCliente = utils.Menu("Menu Cliente", dicMenuCliente)
    resMenuCliente = menuCliente.mostrarMenu()
    if resMenuCliente == 1:
        log.debug("Buscamos cliente")
        print("buscar cliente")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM cliente"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\t\tDNI")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t{row[2]}")
        input("continuar?")
    
    elif resMenuCliente == 2:
        log.debug("Busca Clientes")
        dni = input("Ingresa Doc. Ident. del Cliente: ")
        conn = conexion.ConexionBDD(1)
        query = f"SELECT idCliente, nombreCliente AS Nombre, nroIdentificacion AS ID from cliente where nroIdentificacion = '{dni}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\t\tDNI")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t{row[2]}")
        input("continuar?")
    
    elif resMenuCliente == 3:
        print("Escoja el idCliente que desea modificar: ")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM cliente"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\t\tDNI")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t{row[2]}")
        
        idCliente = input()
        nombre = input("Escriba el nuevo valor para Nombre: ")
    
        dni = input("Escriba el nuevo valor para DNI: ")

        query = f"UPDATE cliente SET nombreCliente = '{nombre}', nroIdentificacion = '{dni}' WHERE idCliente = '{idCliente}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se modificó con exito")
        else:
            print("Hubo un error")
    
    elif resMenuCliente == 4:
        print("-- Vas a crear un cliente --")
        nombre = input("Escribe Nombre del cliente: ")
        dni = input("Escribe el DNI del cliente: ")
        conn = conexion.ConexionBDD(1)
        query = f"INSERT INTO cliente (nombreCliente, nroIdentificacion) VALUES ('{nombre}','{dni}');"     
        resConn = conn.ejecutarBDD(query)
        if (resConn):
            print("Se ejecuto correctamente")
        else:
            print("hubo un error")
        input("desea continuar")
    
    elif resMenuCliente == 5:
        print("Escoja el idCliente que desea eliminar: ")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM cliente"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\t\tDNI")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t{row[2]}")


        idCliente = input("Escribe el idCliente:  ")
        query = f"DELETE FROM cliente WHERE idCliente = {idCliente};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se elimino con exito")
        else:
            print("Hubo un error")

def mantenimientoProducto():
    dicMenuProducto = {"Listar todos los productos": 1, 
                    "Buscar productos por codigo":2, 
                    "Modificar productos por codigo":3,
                    "Ingresar nuevo producto":4,
                    "Borrar Producto":5
                    }
    menuProducto = utils.Menu("Menu Mant. Producto", dicMenuProducto)
    resMenuProducto = menuProducto.mostrarMenu()
    if resMenuProducto == 1:
        log.debug("Listó todos los productos")
        print("Lista de productos:")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM productos"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t\t{row[2]}\t\t{row[3]}")
        input("continuar?")
    
    if resMenuProducto ==2:
        log.debug("Busca Productos por codigo")
        idprod = input("Ingresa codigo del producto: ")
        conn = conexion.ConexionBDD(1)
        query = f"SELECT idproductos, nombreProducto AS Nombre, valorProducto AS valor, igvProducto AS igv from productos where idproductos = '{idprod}';"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
        input("continuar?")

    if resMenuProducto == 3:
        print("Escoja el codigo(ID) del Producto que desea modificar: ")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM productos"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
        
        idProducto = input()
        nombre = input("Escriba el nuevo valor para Nombre del Producto: ")
    
        valor = input("Escriba el nuevo valor para el Producto: ")
        igv = input("Mofique el igv (No:0/Si:1): ")

        query = f"UPDATE productos SET nombreProducto = '{nombre}', valorProducto = '{valor}', igvProducto = '{igv}' WHERE idproductos = '{idProducto}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se modificó con exito")
        else:
            print("Hubo un error")
    
    if resMenuProducto == 4:
        print("-- Vas a ingresar un nuevo Producto --")
        nombre = input("Escribe Nombre del producto: ")
        valor = input("Escribe el valor del producto: ")
        igv = input("Elija si tiene igv (No:0/Si:1): ")
        conn = conexion.ConexionBDD(1)
        query = f"INSERT INTO productos (nombreProducto, valorProducto, igvProducto) VALUES ('{nombre}','{valor}','{igv}');"     
        resConn = conn.ejecutarBDD(query)
        if (resConn):
            print("Se ejecuto correctamente")
        else:
            print("hubo un error")
        input("desea continuar")
    
    if resMenuProducto == 5:
        print("Escoja el idProducto que desea eliminar: ")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM productos"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t\t{row[2]}\t\t{row[3]}")


        idProducto = input("Escribe el idProducto:  ")
        query = f"DELETE FROM productos WHERE idproductos = {idProducto};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se elimino con exito")
        else:
            print("Hubo un error")

def mantenimientoTipoPago():
    dicMenuTipoPago = {"Mostrar tipo de pago": 1, 
                    "Buscar tipos de pago por codigo":2, 
                    "Modificar tipo de pago por codigo":3,
                    "Ingresar nuevo tipo de pago":4,
                    "Borrar un tipo de pago":5
                    }
    menuTipoPago = utils.Menu("Menu Mant. Tipo de Pago", dicMenuTipoPago)
    resMenuTipoPago= menuTipoPago.mostrarMenu()
    if resMenuTipoPago == 1:
        log.debug("Muestra lista de formas de pagos")
        print("Lista de Tipos de pagos:")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM tipopago"
        resConn = conn.consultarBDD(query)
        print("\tID\tDescripcion")
        for row in resConn:
            print(f"\t{row[0]}\t{row[1]}")
        input("continuar?")
    
    if resMenuTipoPago == 2:
        log.debug("Busca tipos de pago por codigo")
        idtipopago = input("Ingresa codigo del tipo de pago: ")
        conn = conexion.ConexionBDD(1)
        query = f"SELECT idtipoPago, descTipoPago AS tipoPago from tipopago where idtipopago = '{idtipopago}';"
        resConn = conn.consultarBDD(query)
        print("\tID\tDescripcion")
        for row in resConn:
            print(f"\t{row[0]}\t{row[1]}")
        input("continuar?")

    if resMenuTipoPago == 3:
        print("Escoja el codigo(ID) del tipo de pago que desea modificar: ")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM tipopago"
        resConn = conn.consultarBDD(query)
        print("\tID\tDescripcion")
        for row in resConn:
            print(f"\t{row[0]}\t{row[1]}")
        
        idtipopago = input()
        desc = input("Escriba la nueva descripción: ")

        query = f"UPDATE tipopago SET descTipoPago = '{desc}' WHERE idtipoPago = '{idtipopago}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se modificó con exito")
        else:
            print("Hubo un error")

    if resMenuTipoPago == 4:
        print("-- Vas a ingresar un tipo de Pago --")
        desc = input("Escribe la descripción del tipo de pago: ")
        conn = conexion.ConexionBDD(1)
        query = f"INSERT INTO tipopago (descTipoPago) VALUES ('{desc}');"     
        resConn = conn.ejecutarBDD(query)
        if (resConn):
            print("Se ejecuto correctamente")
        else:
            print("hubo un error")
        input("desea continuar")
    
    
    if resMenuTipoPago == 5:
        print("Escoja el id del tipo de pago que desea eliminar: ")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM tipopago"
        resConn = conn.consultarBDD(query)
        print("\tID\tDescripcion")
        for row in resConn:
            print(f"\t{row[0]}\t{row[1]}")

        idtipopago = input("Escribe el id del tipo de pago:  ")
        query = f"DELETE FROM tipopago WHERE idtipoPago = {idtipopago};"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se elimino con exito")
        else:
            print("Hubo un error")
    
def MostrarProductos():
        log.debug("Listó todos los productos")
        print("Lista de productos:")
        conn = conexion.ConexionBDD(1)
        query = "SELECT * FROM productos"
        resConn = conn.consultarBDD(query)
        print("\tID\t\tNombre\t\t\t\tValor\t\tIGV")
        for row in resConn:
            print(f"\t{row[0]}\t\t{row[1]}\t\t\t{row[2]}\t\t{row[3]}")
        idprod = input("elige el id de producto: ")

    
    

def mantenimiento (resMenu):
    if resMenu == 1:
        log.debug("escogio 1")
        mantenimientoCliente()
    elif resMenu ==2:
        log.debug("escogio 2")
        mantenimientoProducto()
    elif resMenu ==3:
        log.debug("escogio 3")
        mantenimientoTipoPago()
    else:
        pass

def CreacionFactura(resfact):
    if resfact == 1:
        print("vas a agregar producto a factura")
        MostrarProductos()
    elif resfact == 2:
        print("vas a agregar cantidad de productos")
    elif resfact == 3:
        print("elminar productos")
    else:
        pass


stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"Crear Factura": 1, "Mantenimientos":2}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if (resMenuInicio == 1):
        log.debug("Mostramos el Menu crear Factura")
        
        dicMenuFactura = {"Agregar Prod.": 1, "Agregar Cantidad":2, "Eliminar Prod":3}
        menuFactura = utils.Menu("Menu Creación Factura", dicMenuFactura)
        resMenuFactura = menuFactura.mostrarMenu()
        CreacionFactura(resMenuFactura)

    elif (resMenuInicio == 2):
        log.debug("Mostramos el Menu Mantenimiento")
        dicMenuMantenimiento = {"Mant. Cliente": 1, "Mant. Productos":2, "Mant. Tipo de Pago":3}
        menuMantenimiento = utils.Menu("Menu Mantenimiento", dicMenuMantenimiento)
        resMenuMantenimiento = menuMantenimiento.mostrarMenu()
        mantenimiento(resMenuMantenimiento)
    elif (resMenuInicio == 9):
        print("Finalizar programa")
        stopMenuInicio = False
    else:
        pass
