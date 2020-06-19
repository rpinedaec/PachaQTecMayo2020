import os
class menu:
    def __init__(self,lstOpciones,strTitulo,strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def show(self):   
        os.system("cls")
        print(f"\033[1;32;40m {self.strTitulo:^30} \n")
        print(f"{self.strMenuDescr}")
        for k,v in self.lstOpciones.items():
            print(k,"=>", v)
        while True:
            try:
                self.OptionSelect = int(input("Ingres su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect<len(self.lstOpciones)+1:
                    return self.OptionSelect
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")
MenuPrincipal= menu({1:"Vendedor",2:"Cliente",3:"Salir"},"EMPRESA PORRITAS","Seleccione cualquier opción")
MenuCliente= menu({1:"Ver Productos",2:"Comprar productos",3:"Darse de baja",4:"Salir"},"EMPRESA PORRITAS","Seleccione cualquier opción")
MenuCliente.show()