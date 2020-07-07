import os
import conexion
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
# Definición de todos los menus:
menuPrincipal = Menu({1: "Crear Factura", 2: "Mantenimientos"},
                     "VENTAS GROUP S.A.", "Menú Principal")
menuFactura = Menu({1: "Facturar", 2: "", 3: "Validar existencia"},
                    "VENTAS GROUP S.A.", "Menú Factura")
menuMantenimiento = Menu({1: "Clientes",    2: "Productos"},
                   "VENTAS GROUP S.A.", "Menú Mantenimiento")
menuMantCliente = Menu({1: "Mostrar todos los clientes", 2: "Buscar cliente por DNI", 3: "Modificar cliente", 4: "Crear Cliente", 5: "Borrar Cliente"},
                    "VENTAS GROUP S.A.", "Menú Mantenimiento Clientes")
menuMantProductos = Menu({1: "Mostrar todos los productos", 2 : "Buscar producto por COD", 3 : "Modificar producto", 4 : "Crear Producto", 5 : "Borrar producto"},
                    "VENTAS GROUP S.A.", "Menu mantenimiento Productos")
# Menu de navegación

while True:
    intOptionSelect = menuPrincipal.show()
    if intOptionSelect == 1:  # Menu Factura
        pass
    elif intOptionSelect == 2:  # Menu Mantenimiento
        while True:
            intOptionSelect = menuMantenimiento.show()
            if intOptionSelect == 1:  # Mantenimiento Cliente
                while True:
                    intOptionSelect = menuMantCliente.show()
                    if intOptionSelect == 1:  # Mostrar todos los clientes
                        pass
                    elif intOptionSelect == 2:  # Buscar cliente por DNI
                        pass
                    elif intOptionSelect == 3:  # Modificar cliente
                        pass
                    elif intOptionSelect == 4:  # Crear Cliente
                        pass
                    elif intOptionSelect == 5:  # Borrar cliente
                        pass
                    else:
                        break
            elif intOptionSelect == 2:  # Mantenimiento Producto 
                while True:
                    intOptionSelect = menuMantProductos.show()
                    if intOptionSelect == 1:  # Mostrar todos los productos
                        conn = conexion.conexionBDD(1)
                        query = "select idProducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV from producto;"
                        resConn = conn.consultarBDD(query)
                        print("\tID\t\tNombre\t\t\tValor\t\t\tIGV")
                        for row in resConn:
                            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
                        input("continuar???")
                        print(resConn)
                    elif intOptionSelect == 2:  # Buscar cliente por COD
                        pass
                    elif intOptionSelect == 3:  # Modificar producto
                        pass
                    elif intOptionSelect == 4:  # Crear producto
                        pass
                    elif intOptionSelect == 5:  # Borrar producto
                        pass
                    else:
                        break
            else:
                break
    else:
        break
