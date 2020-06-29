#GETPASS ES PARA CONTRASEÑAS
from time import sleep
import getpass
#OS ES DEL SISTEMA MISMO
import os
#GLOBAL declaración simple que permite modificar la variable fuera del alcance actual.
# Se utiliza para crear una variable global y realizar cambios en la variable en un contexto local.
global listaEmpleados
listaEmpleados = list()
global listaUsuarios
listaUsuarios = list()
global listaProductos
listaProductos = list()

class Persona:
    __estado = True
    def __init__(self, idPersona, dniPersona, nombrePersona, apellidoPersona, edadPersona):
        self.idPersona = idPersona
        self.dniPersona = dniPersona
        self.nombrePersona = nombrePersona
        self.apellidoPersona = apellidoPersona
        self.edadPersona = edadPersona

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

#CLASE EMPLEADO VACÍA PARA QUE SE LLENE DESPUÉS


class Empleado():
    # def __init__(self, dniPersona, nombrePersona, apellidoPersona, edadPersona, codEmpleado, sueldoEmpleado):
    #     super().__init__(dniPersona, nombrePersona, apellidoPersona, edadPersona)
    #     self.codEmpleado = codEmpleado
    #     self.sueldoEmpleado = sueldoEmpleado
    # def marcarIngreso(self):
    #     print("El empleado está marcando su hora de ingreso")
    #     print("El empleado ha marcado su hora de ingreso")

	idEmpleado = ""
	apellidoP = ""
	nombres = ""
	salario = ""

#CLASE USUARIO VACÍA PARA QUE SE LLENE DESPUÉS


class Usuario:
    # def __init__(self, dniPersona, nombrePersona, apellidoPersona, edadPersona, codCliente, usuarioCliente, contraseñaCliente):
    #     super().__init__(dniPersona, nombrePersona, apellidoPersona, edadPersona)
    #     self.codCliente = codCliente
    #     self.usuarioCliente = usuarioCliente
    #     self.contraseñaCliente = contraseñaCliente
    # def consumir(self):
    #     print("El cliente está consumiendo cosas que no necesita")
    #     print("El cliente es adicto al capitalismo salvaje")

	usuario = ""
	contraseña = ""

class Producto:
	# def __init__(self, codProducto, nombreProducto, cantidadProducto, costoProducto):
	# 	self.codProducto = codProducto
	# 	self.nombreProducto = nombreProducto
	# 	self.cantidadProducto = cantidadProducto
	# 	self.costoProducto = costoProducto
	# def __str__(self):
	# 	return """Codigo: {} \nNombre: {}""".format(self.codProducto, self.nombreProducto)
	# def costearProducto(self):
	# 	print("Calculando valor del producto")
	
	idProducto = ""
	nombreP = ""
	cantidad = ""

#FUNCIÓN DE REGISTRAR EMPLEADO


def registrarEmpleado():
	#SE LE DA "e" PORQUE SE LE PUEDE DAR CUALQUIER VARIABLE
	e = Empleado()
	#TÍTULO
	titulo = " \u2749 REGISTRAR NUEVO EMPLEADO \u2749 "
	print("\n" + titulo.center(30, "═"))

	e.idEmpleado = input("Ingrese Numero de Id:✎ ")
	e.nombres = input("Nombre:✎ ")
	e.apellidoP = input("Apellido Paterno:✎ ")
	e.salario = input("Salario Minimo:✎ ")

	listaEmpleados.append(e)


def borrarEmpleado():
	titulo = " \u2749 ELIMINAR EMPLEADO \u2749 "
	print("\n" + titulo.center(30, "═"))
	i = 1
	for e in listaEmpleados:
		#SE USA EL METODO .upper() PARA TRANSFORMAR EL string A MAYÚSCULAS
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1

	opc = int(input("\n►►►►►Num de empleado a borrar: "))
	del listaEmpleados[opc-1]
	print("\nLa nueva lista es:")
	i = 1
	for e in listaEmpleados:
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1


def actualizarDatos():
	titulo = " \u2749 ACTUALIZAR DATOS \u2749 "
	print("\n" + titulo.center(30, "═"))
	i = 1
	for e in listaEmpleados:
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1

	opc = int(input("\n✎✎✎✎Num de empleado a actualizar: "))

	print("")
	listaEmpleados[opc-1].idEmpleado = input("Ingrese Nuevo Numero de Id: ")
	listaEmpleados[opc-1].nombres = input("Nuevo Nombre(s): ")
	listaEmpleados[opc-1].apellidoP = input("Nuevo Apellido Paterno: ")
	listaEmpleados[opc-1].apellidoM = input("Nuevo Apellido Materno: ")
	listaEmpleados[opc-1].salario = input("Nuevo Salario Minimo: ")

	print("\nLa nueva lista es:")
	i = 1
	for e in listaEmpleados:
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1


def listarEmpleado():
	titulo = " \u2749 LISTA DE EMPLEADOS \u2749 "
	print("\n" + titulo.center(30, "═"))
	i = 1
	for e in listaEmpleados:
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1


def buscarEmpleado():
	titulo = " \u2749 BUSCAR EMPLEADO \u2749 "
	print("\n" + titulo.center(30, "═"))

	bandera = 0

	filtro = input("✎✎✎✎ Ingrese Nombre o Apellido Paterno: ")

	for e in listaEmpleados:
		if e.apellidoP == filtro or e.nombres == filtro:
			print("\nResultado de Busqueda: ")
			print("1.-|", e.idEmpleado, "-", e.apellidoP.upper(),
			      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
			bandera = 1
		elif e.apellidoP == filtro.upper() or e.nombres == filtro.upper():
			print("\nResultado de Busqueda: ")
			print("1.-|", e.idEmpleado, "-", e.apellidoP.upper(),
			      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
			bandera = 1
		elif e.apellidoP == filtro.lower() or e.nombres == filtro.lower():
			print("\nResultado de Busqueda: ")
			print("1.-|", e.idEmpleado, "-", e.apellidoP.upper(),
			      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
			bandera = 1
		elif e.apellidoP == filtro.capitalize() or e.nombres == filtro.capitalize():
			print("\nResultado de Busqueda: ")
			print("1.-|", e.idEmpleado, "-", e.apellidoP.upper(),
			      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
			bandera = 1

	if bandera == 0:
		print("Usuario no encontrado...")


def totalNomina():
	titulo = " \u2749 NOMINA \u2749 "
	print("\n" + titulo.center(30, "═"))
	suma = 0

	for e in listaEmpleados:
		suma = float(e.salario)+suma

	print("El total de la nomina es: $", suma*12)


def registrarCompra():
	p = Producto()
	titulo = " \u2749 COMPRAR \u2749 "
	print("\n" + titulo.center(30, "═"))

	p.idProducto = input("Ingrese Numero de Id:✎ ")
	p.nombreP = input("Nombre:✎ ")
	p.cantidad = input("Cuántos vas a comprar?:✎ ")

	listaProductos.append(p)
	#QUERÍA QUE SE MUESTRE LOS DATOS INGRESADOS COMO RESUMEN:
	# i = 1
	# for p in listaProductos:
	# 	print(i, ".-  |ID:", p.idProducto, "-", p.nombreP.upper(), " ", p.cantidad.upper())
	# 	i += 1


def eliminarCompra():
	titulo = " \u2749 ELIMINAR COMPRA \u2749 "
	print("\n" + titulo.center(30, "═"))
	i = 1
	for p in listaProductos:
		#SE USA EL METODO .upper() PARA TRANSFORMAR EL string A MAYÚSCULAS
		print(i, ".-  |ID:", p.idProducto, "-",
		      p.nombreP.upper(), " ", p.cantidad.upper())
		i += 1

	opc = int(input("\nID de producto a borrar: "))
	del listaProductos[opc-1]
	print("\nResultado:")
	i = 1
	for p in listaProductos:
		print(i, ".-  |ID:", p.idProducto, "-",
		      p.nombreP.upper(), " ", p.cantidad.upper())
		i += 1


def buscarProducto():
	titulo = " \u2749 BUSCAR PRODUCTO \u2749 "
	print("\n" + titulo.center(30, "═"))

	bandera = 0

	filtro = input("✎✎✎✎ Ingrese Nombre del Producto: ")

	for p in listaProductos:
		if p.idProducto == filtro or p.nombreP == filtro:
			print("\nResultado de Busqueda: ")
			print(".-  |ID:", p.idProducto, "-",
			      p.nombreP.upper(), " ", p.cantidad.upper())
			bandera = 1
		elif p.idProducto == filtro.upper() or p.nombreP == filtro.upper():
			print("\nResultado de Busqueda: ")
			print(".-  |ID:", p.idProducto, "-",
			      p.nombreP.upper(), " ", p.cantidad.upper())
			bandera = 1
		elif p.idProducto == filtro.lower() or p.nombreP == filtro.lower():
			print("\nResultado de Busqueda: ")
			print(".-  |ID:", p.idProducto, "-",
			      p.nombreP.upper(), " ", p.cantidad.upper())
			bandera = 1
		elif p.idProducto == filtro.capitalize() or p.nombreP == filtro.capitalize():
			print("\nResultado de Busqueda: ")
			print(".-  |ID:", p.idProducto, "-",
			      p.nombreP.upper(), " ", p.cantidad.upper())
			bandera = 1

	if bandera == 0:
		print("Producto no encontrado...")


def salir():
	print("\nSaliendo del sistema 🍕 🍕 🍕")


def menu():
	limpiarPantalla()
	opcion = {}

	while opcion != 0:
		#MOSTRAR EL MENU
		titulo = " \u2749 MENU \u2749 "
		print("\n" + titulo.center(60, "═"))
		print(":::::PARA EMPLEADOS:::::")
		print("	1.- Registrar empleado")
		print("	2.- Eliminar empleado")
		print("	3.- Actualizar datos de empleado")
		print("	4.- Mostrar todos los empleados en la lista")
		print("	5.- Buscar Empleado")
		print("	6.- Calcular monto total de la nomina")
		print(":::::PARA CLIENTES:::::")
		print("	7.- Comprar")
		print("	8.- Eliminar compra")
		print("	9.- Buscar producto")
		print("	0.- Salir")
		opcion = int(input("✎✎✎✎ Elija una opcion: "))

		if opcion == 1:
			registrarEmpleado()
		elif opcion == 2:
			borrarEmpleado()
		elif opcion == 3:
			actualizarDatos()
		elif opcion == 4:
			listarEmpleado()
		elif opcion == 5:
			buscarEmpleado()
		elif opcion == 6:
			totalNomina()
		elif opcion == 7:
			registrarCompra()
		elif opcion == 8:
			eliminarCompra()
		elif opcion == 9:
			buscarProducto()
		elif opcion == 0:
			salir()


def limpiarPantalla():
    def clear():
    	return os.system('clear')
    clear()


def archivoUsuarios():

	with open('usuarios.txt') as arch:
		users = arch.readlines()

	dicUsuarios = {}

	j = 0
	for u in users:
		aux = u.strip()
		dicUsuarios[j] = aux.split('|')
		h = Usuario()
		h.usuario = dicUsuarios[j][0]
		h.contraseña = dicUsuarios[j][1]
		listaUsuarios.append(h)
		j += 1


def archivoEmpleados():

	with open('empleados.txt') as arch:
		emple = arch.readlines()

	dicEmpleados = {}

	j = 0
	for emp in emple:
		aux = emp.strip()
		dicEmpleados[j] = aux.split('|')
		o = Empleado()
		o.idEmpleado = dicEmpleados[j][0]
		o.apellidoP = dicEmpleados[j][1]
		o.apellidoM = dicEmpleados[j][2]
		o.nombres = dicEmpleados[j][3]
		o.salario = dicEmpleados[j][4]
		listaEmpleados.append(o)
		j += 1


def main():
	archivoUsuarios()
	archivoEmpleados()
	print("---------------------")
	print("|       ACCESO      |")
	print("---------------------")

	contador = 0
	i = 3

	while contador != 3:
		usuario = input("►Usuario: ")
		contraseña = getpass.getpass("►Contraseña: ")
		contador += 1

		valido = False

		for u in listaUsuarios:
			if u.usuario == usuario and u.contraseña == contraseña:
				valido = True
				break

		if valido == True:
			contador = 3
			print("")
			print("╔═════════════════════════════════════════╗")
			print("║        BIENVENIDOS A CIUDAD 17 ®        ║")
			print("╚═════════════════════════════════════════╝")
			menu()
		else:
			i -= 1
			if i == 0:
				print("\n\nQuedan", i, "intentos")
				print("▼CERRANDO SISTEMA▼")
			else:
				print("\n▬▬Usuario Invalido▬▬")
				print("Quedan", i, "de 3 intento(s)...")


menu()
