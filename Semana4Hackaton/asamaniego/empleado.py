from persona import Persona

class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")
