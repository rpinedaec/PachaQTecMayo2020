#Alumno: Paola Sanchez
#Variables globales
lstPersonas = []
lstClientes = []
lstTrabajadores = []
lstProductos = []

#Clase Padre
class Personas:
    def __init__(self, nombre,apellido, dni, tipo, fdn):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.fdn = fdn

    def RegistroCliente(self):
        print("Ingresa los siguientes datos:")

    def ComprarCliente(self):
        print("Que producto deseas comprar hoy:")

    def ComprobanteCliente(self):
        print("Ingresa tu numero de compra:")

#Clientes
class Clientes(Personas):
    def __init__(self, nombre, apellido, dni, fdn, email, usuario, password):
        super().__init__(self, nombre, apellido, dni, fdn)
        self.email = email
        self.usuario = usuario
        self.__password = self.MostrarPassword(password)
    
    def Catalogo(self):
    
    def Registro(self):

    def Comprobante(self):
    
    @property
    def gPassword(self):
        return self.__password
        #print(usuario.password)
    @password.setter
    def gPassword(self, valor):
    self.__password = self.MostrarPassword(valor)    

#Trabajadores
class Trabajadores(Personas):
    def __init__(self, nombre, apellido, dni, fdn, cdgtrabajador):
        super().__init__(self, nombre, apellido, dni, fdn)
        self.cdgtrabajador = cdgtrabajador

    def VenderTrabajador(self):
        print("Ingresa tu numero de trabajador:")

    def RegistroTrabajador(self):
        print("Registra un nuevo usuario:")

    def InventarioTrabajador(self):
        print("Consulta el inventario:")

#Producto
class Producto:
    @staticmethod
    def IGV():
        return 1.18

    def __init__(self, codprod, modelo, marca, color, descripcion, precio, stock):
        self.codprod = codprod
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def EditarInventario(self):
        print("Ingresa el producto que deseas eliminar:")

    def AgregarInventario(self):
       print("Ingresa los siguientes datos:")

    def ConsultarInventario(self):
        print("Ingresa los siguientes datos:")

    def Calculadora(self):
        print("Calculadora")

#Menu Principal
class MenuCliente:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def MostrarMenu(self):
        IngresandoOpcion = True
        while (IngresandoOpcion):
            print("-----------------------------------------")
            print("        TIENDA VIRTUAL PACHAQTEC         ")
            print("-----------------------------------------")
            print("      * "+ self.nombreMenu +" *          ")
            print("")
            nombre=input("Ingresa tu nombre : ", )
            print(f"¡Hola {nombre}! Qué vamos a hacer hoy?")
            for (key, value) in self.listaOpciones.items():
                print(key,"",value)
            print("***")
            print("Otras opciones : ")
            print("9 :Ingresar a Worktarion 3.0")
            opcion = 1
            try:
                opcion = int(input("Opción : "))
            except ValueError:
                #self.__log.error(error)
                print("Opcion inválida. Debes ingresar números del 0 - 9")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                   contOpciones += 1
            if(contOpciones == 0):
                print("Escoge una opcion valida")
                # self.__log.debug("No escoje opion")
                # sleep(5)
            else:
                IngresandoOpcion = False

        return opcion

#Diccionarios
dicMenuCliente ={"Ver el catálogo":1,"Registrate en el club de ofertas":2,"Solicita tu comprobante de compra":3, "Salir del Programa":4 }
menuPrincipal = Menu("Menu de Inicio", dicMenuCliente)

dicMenuTrabajador = {"Registra Venta": 1, "Registrar Nuevo Usuario":2, "Consulta el Inventario":3}
menuTrabajador = Menu("Menu de Inicio", dicMenuTrabajador)

dicMenuInventario = {"Editar Inventario":1, "Agregar Producto":2, "Ver Inventario":3}
menuInventario = Menu("Menu de Inicio", dicMenuInventario)

#Mostrando Menu Principal
opcionMenuPrincipal = menuPrincipal.MostrarMenu()
if (opcionMenuPrincipal == 1):
    print("Catalogo Cliente")
elif (opcionMenuPrincipal == 2):
    print("Registro Cliente")
    print("Ingresa tu nombre")
    nombre = input()
    print("Ingresa tu apellido")
    apellido = input()
    print("Ingresa tu dni")
    dni = input()
    print("Tienes una empresa?")
    print("Para Personas ingresa 'SE'")
    print("Para Empresas ingresa 'CE'")
    tipo = input()
    print("Ingresa tu fecha de nacimiento")
    fdn = input()
    clientenuevo = Personas(nombre, apellido, dni, tipo, fdn)
    print("Gracias por registrarte")
    lstPersonas.append(clientenuevo.dicClientes())
    lstPersonas.append(clientenuevo)
    resMenuPersonas = menuCliente.mostrarMenu()
elif (opcionMenuPrincipal == 3):
    print("Comprobante")
elif (opcionMenuPrincipal == 4):
    print("Salir")
elif (opcionMenuPrincipal == 9):
    print("Bienvenidos al Worktarion 3.0")
    print("Para ingresar, ingresa tu codigo de trabajador.")
    opcionworktario = input("Mi código es: ")
    