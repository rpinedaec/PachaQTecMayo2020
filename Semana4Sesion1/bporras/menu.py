import os
class menu:
    def __init__(self,lstOpciones,strTitulo,strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def show(self):   
        os.system("cls")
        print(f"\033[1;32;40m")
        print(20*":" + f"{self.strTitulo:^20}" + 20*":")
        print(20*":" + f"{self.strMenuDescr:^20}" + 20*":")
        for k,v in self.lstOpciones.items():
            print(k,"::", v)
        print("9 :: Salir")
        while True:
            try:
                self.OptionSelect = int(input("Ingres su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect<len(self.lstOpciones)+1:
                    return self.OptionSelect
                elif self.OptionSelect == 9:
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")
MenuPrincipal= menu({1:"Cliente",2:"Empleado"}, "VENTAS GROUP S.A.", "Menú Principal")
MenuEmpleado= menu({1:"Marcar Ingreso",2:"Marcar Salida",3:"Cargar Inventario"}, "VENTAS GROUP S.A.", "Menú Empleado")
MenuCliente= menu({1:"Comprar",2:"Devolver",3:"Registrar Cliente"}, "VENTAS GROUP S.A.", "Menú Cliente")
while True:
    intOptionSelect = MenuPrincipal.show()
    if intOptionSelect == 1:
        intOptionSelect = MenuCliente.show()
    elif intOptionSelect == 2:
        intOptionSelect = MenuEmpleado.show()
    else:
        break