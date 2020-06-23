class Persona:
    def __init__(self, nombre, apellido, nroIdentidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nroIdentidad = nroIdentidad

    # @property
    # def cargo(self):
    #     return self.__cargo

    # @cargo.setter
    # def cargo(self, nuevoCargo):
    #     self.__cargo = nuevoCargo

    # def getCargo(self):
    #     return f"Mi nuevo cargo: {self.__cargo}"

    # def setCargo(self, nuevoCargo):
    #     self.__cargo = nuevoCargo

    def comprar(self):
        print("Estoy comprando")

    def consultar(self, producto):
        print(f"Estoy consultando por {producto}")
        print("Ya termine de consultar")

    def consultarPrecio(self, producto):
        print(f"Estoy viendo en el sistema el precio de {producto}")
        print(f"El precio de {producto} es de 200")

    def vender(self):
        print("Estoy vendiendo")
        print("Termine de vender")


class Trabajador(Personas):
    def __init__(self, nombre, apellido, nroIdentidad, cargo, sueldo):
        super().__init__(nombre, apellido, nroIdentidad)
        self.cargo = cargo
        self.sueldo = sueldo

    def marcarEntrada(self, hora):
        print(f"Estoy entrando a trabajar a las {hora}")




Vendedor = Persona("Martin","Perez", "41414122")
Comprador = Persona("Abigail","Zam","25896534")

trabajador_1 = Trabajador("Juan","Perez","12345678","Bodeguero",1000)


print(trabajador_1.nombre, trabajador_1.cargo)

trabajador_1.marcarEntrada("08:00")
trabajador_1.vender()



