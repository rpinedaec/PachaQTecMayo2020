import getpass

global listaEmpleados
listaEmpleados = list()
global listaUsuarios
listaUsuarios = list()


class Empleado:
	idEmpleado = ""
	apellidoP = ""
	apellidoM = ""
	nombres = ""
	salario = ""


class Usuario:
	usuario = ""
	contraseña = ""


def registrarEmpleado():
	e = Empleado()

	cadena = "REGISTRAR NUEVO EMPLEADO"
	print("\n" + cadena.center(60, "═"))
	e.idEmpleado = input("Ingrese Numero de Id: ")
	e.nombres = input("Nombre(s): ")
	e.apellidoP = input("Apellido Paterno: ")
	e.apellidoM = input("Apellido Materno: ")
	e.salario = input("Salario Minimo: ")

	listaEmpleados.append(e)


def borrarEmpleado():

	cadena = "BORRAR EMPLEADO"
	print("\n" + cadena.center(60, "═"))
	i = 1
	for e in listaEmpleados:
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
	cadena = "ACTUALIZAR DATOS"
	print("\n" + cadena.center(60, "═"))
	i = 1
	for e in listaEmpleados:
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1

	opc = int(input("\n►►►►►Num de empleado a actualizar: "))

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
	cadena = "LISTA DE EMPLEADOS"
	print("\n" + cadena.center(60, "═"))
	i = 1
	for e in listaEmpleados:
		print(i, ".-  |ID:", e.idEmpleado, "-", e.apellidoP.upper(), " ",
		      e.apellidoM.upper(), ",", e.nombres.upper(), "-->$", e.salario)
		i += 1


def buscarEmpleado():
	cadena = "BUSCAR EMPLEADO"
	print("\n" + cadena.center(60, "═"))

	bandera = 0

	filtro = input("Ingrese Nombre o Apellido Paterno: ")

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
	cadena = "NOMINA"
	print("\n" + cadena.center(60, "═"))
	suma = 0

	for e in listaEmpleados:
		suma = float(e.salario)+suma

	print("El total de la nomina es: $", suma*12)


def salir():
	print("\nSaliendo del sistema►►►")


def menu():
	opcion = 0

	while opcion != 7:
		#Mostrar Menú
		cadena = "MENU"
		print("\n" + cadena.center(60, "═"))
		print("1.- Registrar empleado")
		print("2.- Eliminar empleado")
		print("3.- Actualizar datos de empleado")
		print("4.- Mostrar todos los empleados en la lista")
		print("5.- Buscar Empleado")
		print("6.- Calcular monto total de la nomina")
		print("7.- Salir")
		opcion = int(input("►►►►►Elija una opcion: "))

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
			salir()


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
	print("|        LOGIN      |")
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
