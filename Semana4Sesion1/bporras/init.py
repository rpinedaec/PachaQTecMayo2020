class Persona:
    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    __estado = True
@property
def estado(self):
    return __estado
@estado.setter
def estado(sel,nuevoEstado):
    __estado = nuevoEstado
def registro(self):
    self.__estado = True
    print("La Persona se ha registrado")
def desregistro(self):
    self.__estado = False

class Cliente:
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente
    def comprar(self):
        print("El cliente esta comprando")
        print("El cliente temrino de comprar")

class Empleado:
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado

class Producto:
    def __init__(self, codProducto, nombre, cantidad, costo):
        self.codProducto = condProducto
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
class Menu:
    def _init__(self, nombreMenu,lstOpciones):
        self.nombreMenu = nombreMenu
        self.lstOpciones = lstOpciones
