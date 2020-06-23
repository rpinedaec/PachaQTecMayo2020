import os

print('\033[1;91m' + "   (                                        (         " + '\033[0m')
print('\033[1;91m' + " ( )\ (     (          )      (        (    )\ )      " + '\033[0m')
print('\033[1;91m' + " )((_))\   ))\  (     /((    ))\  (    )\  (()/(  (   " + '\033[0m')
print('\033[1;91m' + "((_)_((_) /((_) )\ ) (_))\  /((_) )\ )((_)  ((_)) )\  " + '\033[0m')
print('\033[1;91m' + " | _ )(_)(_))  _(_/( _)((_)(_))  _(_/( (_)  _| | ((_) " + '\033[0m')
print('\033[1;91m' + " | _ \| |/ -_)| ' \))\ V / / -_)| ' \))| |/ _` |/ _ \ " + '\033[0m')
print('\033[1;91m' + " |___/|_|\___||_||_|  \_/  \___||_||_| |_|\__,_|\___/ " + '\033[0m')
print('\033[1;96m' + "******************************************************" + '\033[0m')

#CONTRUCTOR DE CLASE
class Persona:
    __estado =  True
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
        print("La persona se ha registrado")
    def desregistro(self):
        self.estado = False
        print("La personas se ha desregistrado")


#CONTRUCTOR DE LA CLASE CLIENTE
class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, edad, codCliente):
        super().__init__(dni, nombre, apellido, edad)
        self.codCliente = codCliente
    #FUNCION PROPIA DEL CLIENTE    
    def comprar(self):
        print("El cliente está comprando")
        print("El cliente terminó de comprar")
    
#CONTRUCTOR DE LA CLASE EMPLEADO
class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, codEmpleado):
        super().__init__(dni, nombre, apellido, edad)
        self.codEmpleado = codEmpleado
    #FUNCION PROPIA DEL EMPLEADO
    def marcarIngreso(self):
        print("El empleado esta marcando su ingreso")
        print("El empleado marcó su ingreso")

#CONTRUCTOR DE LA CLASE PRODUCTO
class Producto:
    def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
        self.codProducto = codProducto
        self.nombreProducto = nombreProducto
        self.cantidadProducto = cantidadProducto
        self.costoProducto = costoProducto
    #FUNCION PROPIA DEL PRODUCTO
    def costearProducto(self):
        print("Costeando producto")
        print("Producto costeado")
    
#CONTRUCTOR DE LA CLASE MENU
#UNA SOLA ESTRUCTURA DE MENU PARA DIVERSAS OPCIONES

class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones
    #FUNCION PROPIA DEL MENU
    
    def mostrarMenu(self):
        print(f"EMPRESAS CAPITALISTAS LES SALUDA \n {self.nombreMenu}")
        acceder = input("(e) Para empleado || (c) Para Cliente --> ")
        if(acceder == "e"):
            for (key, value) in self.listaOpciones.items():
                        print(key, ":", value)
        elif(acceder == "c"):
            for (key, value) in self.listaOpciones.items():
                        print(key, ":", value)
        else:
            print("Gracias por nada")
            print("*************FIN**************")

            
    #FUNCION PARA LIMPIAR LA PANTALLA (OPCIONAL E IMPORTANDO DESDE ARRIBA)
    # def limpiarPantalla(self):
    #     clear = lambda: os.system('clear')
    #     clear()

#DIVERSOS TIPOS DE MENU
#OPCION DE MENU PARA MENÚ PRINCIPAL
dicOpcionesMenuPrincipal = {"Cliente":1,"Empleado":2, "Salir":0}
menuPrincipal = Menu("Menu de inicio", dicOpcionesMenuPrincipal)
menuPrincipal.mostrarMenu()

#OPCION MENU PARA MENU DE EMPLEADOS
dicOpcionesEmpleado = {"Marcar Entrada": 1, "Marcar Refrigerio": 2, "Marcar Salida":3}
menuEmpleado = Menu("Menu del empleado", dicOpcionesEmpleado)
menuEmpleado.mostrarMenu()

#OPCION MENU PARA MENU DE CLIENTES
dicOpcionesCliente = {"Comprar":1, "Devolver":2, "Salir":0}
menuCliente = Menu("Menu de cliente", dicOpcionesCliente)
menuCliente.mostrarMenu()

#INTERACCION CON EL USUARIO Y QUE PUEDA ELEGIR
opcionMenuPrincipal = input("Seleccione una opcion \n")
if(opcionMenuPrincipal == "1"):
    print("Bienvenido cliente")
elif(opcionMenuPrincipal == "2"):
    print("Bienvenido empleado")
else:
    print("Deseas salir?")