
from persona import Persona


class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente

    def comprar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")

