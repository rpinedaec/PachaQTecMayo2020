class menu:
    def __init__(self,lstOpciones,strTitulo,strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def Choose(self):   
        print(self.strTitulo)
        print(self.strMenuDescr)
        for k,v in self.lstOpciones.items():
            print(k," : ", v)
        self.OptionSelect = input("Ingres su opción: ")
        return self.OptionSelect

MenuPrincipal= menu({1:"Vendedor",2:"Cliente",3:"Salir"},"EMPRESA PORRITAS","Seleccione cualquier opción")

MenuPrincipal.Choose()