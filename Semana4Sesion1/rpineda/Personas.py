class Personas:
    def __init__(self, nombre, apellido, nroIdentidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nroIdentidad = nroIdentidad

    def comprar(self):
        print("Estoy comprando")
    
    def consultar(self, producto):
        print(f"Estoy consultando por {producto}")
        print("Ya termine de consultar")
    
    def consultarPrecio(self, producto):
        print(f"Estpy viendo en el sistema el precio de {producto}")
        print(f"El precio de {producto} es de 200")

    def vender(self):
        print("Estoy vendiendo")
        print("Termine de vender")
    

vendedor = Personas("Roberto", "Pineda", "001575294")

comprador = Personas("David","Lopez","1716861993")

comprador.consultar("Zapatos")

vendedor.consultarPrecio("Zapatos")

comprador.comprar()

