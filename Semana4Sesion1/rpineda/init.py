import os
class Persona:
    __estado = True
    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
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
    
class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni,nombre,apellido,edad)
        self.codCliente = codCliente 
    
    def compar(self):
        print("El Cliente esta comprando")
        print("El Cliente terminó de comprar")


class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni,nombre,apellido,edad)
        self.codEmpleado = codEmpleado

    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")

class Producto:
    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto

    def costearProducto(self):
        print("Costeando producto")
        print("Producto costeado")

class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        print("\033[1;34m"+":::::::::::::EMPRESA PACHAQTEC::::::::::::::"+'\033[0;m')
        print("\033[1;34m"+":::::::::::::"+ self.nombreMenu +"::::::::::::::"+'\033[0;m')
        #print(f"Empresa Roberto \n {self.nombreMenu}")
        for (key, value) in self.listaOpciones.items():
                    print(key , " :: ", value )
    
    def limpiarPantalla(self):
        clear = lambda: os.system('cls')
        #clear = lambda: os.system('clear')
        clear()

dicOpcionesMenuPrincipal = {"Cliente":1,"Empleado":2,"Salir":0}
menuPrincipal = Menu("Menu de Inicio", dicOpcionesMenuPrincipal)
menuPrincipal.mostrarMenu()

dicOpcionesCliente = {"Comprar": 1, "Devolver": 2, "Salir": "S"}
menuCliente = Menu("Menu de Cliente", dicOpcionesCliente)
menuCliente.mostrarMenu()

menuPrincipal.mostrarMenu()

# opcionMenuPrincipal = input("Seleccione una opcion \n")
# if(opcionMenuPrincipal == "1"):
#     print("bienvenido cliente")
# elif(opcionMenuPrincipal == "2"):
#     print("bienvenido Empleado")
# else:
#     print("Deseas Salir ?? ")



