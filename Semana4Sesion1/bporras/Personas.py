class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    def vender(self):
        print("Estoy vendiendo")
    def consultar(self,producto):
        print(f"Estoy consultando {producto}")
        print(f"El precio del {producto} es 100 soles")
    def comprar(self):
        print("Estoy comprando")

comprador= Persona("Bruce","Porras","71206364")
vendedor = Persona("Kevin","Miliano","2114801")

comprador.consultar("zapato")
vendedor.vender()
comprador.comprar()
