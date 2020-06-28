class Persona:
    __estado = True

    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def toDic(self):
        dicPersona = {
            "dni" : self.dni,
            "nombre" : self.nombre,
            "apellido" : self.apellido,
            "edad" : self.edad
        }
        return dicPersona

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevoEstado):
        __estado = nuevoEstado

    def registro(self):
        self.estado = True
        print("La Persona se ha registrado")

    def desresgistro(self):
        self.estado = False
