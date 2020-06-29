#Importar el paquete estándar Json
import json
from colorama import init, Fore, Back, Style
init() 
#Definiendo la clase persona:
class persona ():

    #Iniciando el constructor de la clase
    def __init__ (self, nombre, apellidoPaterno ,apellidoMaterno):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno

#Definiendo la clase cliente:
class cliente (persona):
    
    #Iniciando el constructor de la clase, para el cliente nos interesa solo su DNI o bien RUC, ya que sera su distintivo
    def __init__(self,dni,nombre,apellidoPaterno,apellidoMaterno):
        #Relacionando con la clase padre
        super(). __init__ (nombre,apellidoPaterno,apellidoMaterno)
        self.dni = dni

    #Iniciando la función de guardar datos de cliente nuevo.
    def crearCliente (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\clientes.json','r') as f:
            #Descargando como Lista
            listaDescargada = json.load(f)
            #Asignando las entradas a la lista "datos"
            datos = {'Nombre':self.nombre,'Apellidos':self.apellidoPaterno+" "+self.apellidoMaterno,'DNI':self.dni}
            #Añadiendo la lista "datos" a la lista descargada
            listaDescargada.append(datos)
            #Abriendo el archivo Json en modo de escritura
            with open('Semana4Hackaton\jwilian\clientes.json','w') as f:
                #Agregando la cadena datos en forma de cadena Json en el archivo Json:
                json.dump(listaDescargada,f)
        
        print(Style.BRIGHT+"\nEl cliente ",self.nombre+" "+self.apellidoPaterno+" "+self.apellidoMaterno," fue creado con éxito")

    #Iniciando la función de borrar datos de cliente; en el caso se quiera usar mas adelante
    def eliminarCliente (self):
        
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\clientes.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            #Inicio del contador, para recorrer la lista con la sentencia while
            j = 0
            #Variable para determinar el final de la sentencia while
            i = False
            #Inicio de bucle while para eliminar el elemento
            while i == False:
                if self.nombre == ListaDescargada[j]["Nombre"]:
                    #Eliminacion del elemento j de la lista.
                    ListaDescargada.pop(j)
                    #Conversion de la variable "i", que indicara el final de la sentencia While
                    i=True
                    #Abriendo el archivo Json en modo de escritura
                    with open('Semana4Hackaton\jwilian\clientes.json','w') as f:
                    #Agregando la cadena datos en forma de cadena Json en el archivo Json:
                        json.dump(ListaDescargada,f)
                else:
                    #Aumento de la variable contador que recorre la lista
                    j+=1

    #Función para validar la existencia de un cliente
    def validarCliente (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\clientes.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para validar la existencia de algun producto
            while i == False:
                if self.nombre == ListaDescargada[j]["Nombre"]:
                    i=True
                    print("El cliente: ",ListaDescargada[j]["Nombre"]+" "+ListaDescargada[j]["Apellidos"]," ,se encuentra registrado en el sistema")
                else:
                    j+=1

    #Función para ver los datos de un cliente existente
    def verCliente (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\clientes.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while que busca el numero de DNI
            while i == False:
                if self.dni == ListaDescargada[j]["DNI"]:
                    print("""Los datos del cliente, son:\nNombre:    """, ListaDescargada[j]["Nombre"],"""\nApellidos: """, ListaDescargada[j]["Apellidos"],"""\nDNI:       """, ListaDescargada[j]["DNI"])
                    i=True
                else:
                    j+=1

#Definiendo la clase empleado
class empleado (persona):
    
    #Iniciando el constructor de la clase
    def __init__(self,codigo,nombre,apellidoPaterno,apellidoMaterno):
        super(). __init__ (nombre,apellidoPaterno,apellidoMaterno)
        self.codigo=codigo

    #Iniciando la función de guardar datos
    def crearEmpleado (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\empleados.json','r') as f:
            #Descargando como Lista
            listaDescargada = json.load(f)
            #Asignando las entradas a la lista "datos"
            datos = {'Nombre':self.nombre,'Apellidos':self.apellidoPaterno+" "+self.apellidoMaterno,'Codigo':self.codigo}
            #Añadiendo la lista "datos" a la lista descargada
            listaDescargada.append(datos)
            #Abriendo el archivo Json en modo de escritura
            with open('Semana4Hackaton\jwilian\empleados.json','w') as f:
                #Agregando la cadena datos en forma de cadena Json en el archivo Json:
                json.dump(listaDescargada,f)
    
    #Iniciando la función de borrar datos
    def eliminarEmpleado (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\empleados.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para eliminar el elemento
            while i == False:
                if self.nombre == ListaDescargada[j]["Nombre"]:
                    ListaDescargada.pop(j)
                    i=True
                    #Abriendo el archivo Json en modo de escritura
                    with open('Semana4Hackaton\jwilian\empleados.json','w') as f:
                    #Agregando la cadena datos en forma de cadena Json en el archivo Json:
                        json.dump(ListaDescargada,f)
                else:
                    j+=1

    #Función para validar la existencia de un empleado.
    def validarEmpleado (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\empleados.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para validar la existencia de algun producto
            while i == False:
                if self.codigo == ListaDescargada[j]["Codigo"]:
                    ListaDescargada.pop(j)
                    i=True
                    print("El empleado, se encuentra registrado en el sistema")
                else:
                    j+=1

    def verEmpleado (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\empleados.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while que busca el numero de DNI
            while i == False:
                if self.codigo == ListaDescargada[j]["Codigo"]:
                    print("""Los datos del empleado, son: \nNombre:    """, ListaDescargada[j]["Nombre"],"""\nApellidos: """, ListaDescargada[j]["Apellidos"])
                    i=True
                else:
                    j+=1

#Definiendo la clase producto
class producto ():
    
    #Iniciando el constructor de clase
    def __init__ (self, nombreMarca, presentacion, codigo, unidades , costoUnitario):
        self.nombreMarca = nombreMarca
        self.presentacion = presentacion
        self.codigo = codigo
        self.unidades = unidades
        self.costoUnitario = costoUnitario

    #Iniciando la función de guardar datos
    def addProduct (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\productos.json','r') as f:
            #Descargando como Lista
            listaDescargada = json.load(f)
            #Asignando las entradas a la lista "datos"
            datos = {'Nombre':self.nombreMarca,'Presentacion':self.presentacion,'Codigo':self.codigo, 'Unidades': self.unidades, 'CostoxUnidad':self.costoUnitario}
            #Añadiendo la lista "datos" a la lista descargada
            listaDescargada.append(datos)
            #Abriendo el archivo Json en modo de escritura
            with open('Semana4Hackaton\jwilian\productos.json','w') as f:
                #Agregando la cadena datos en forma de cadena Json en el archivo Json:
                json.dump(listaDescargada,f)

    #Iniciando la función para validar productos
    def validarProduct (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\productos.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para validar la existencia de algun producto
            while i == False:
                if self.nombreMarca == ListaDescargada[j]["Nombre"]:
                    ListaDescargada.pop(j)
                    i=True
                    print("El artículo, se encuentra registrado en el sistema")
                else:
                    j+=1

    #Iniciando la función para eliminar productos
    def delProduct (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\productos.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para eliminar el elemento
            while i == False:
                if self.nombreMarca == ListaDescargada[j]["Nombre"]:
                    ListaDescargada.pop(j)
                    i=True
                    #Abriendo el archivo Json en modo de escritura
                    with open('Semana4Hackaton\jwilian\productos.json','w') as f:
                    #Agregando la cadena datos en forma de cadena Json en el archivo Json:
                        json.dump(ListaDescargada,f)
                else:
                    j+=1

    #Iniciando la función para listar los productos
    def listProduct (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\productos.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            #Imprimiendo en pantalla la lista descargada
            print(ListaDescargada)

    #Iniciando la función para contar productos
    def countProduct (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\productos.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para buscar el elemento
            while i == False:
                if self.nombreMarca == ListaDescargada[j]["Nombre"]:
                    i=True
                    print("Se cuenta con: ",ListaDescargada[j]["Unidades"], "und. de ", self.nombreMarca)
                else:
                    j+=1

    #Iniciando la función para contar productos
    def valueProduct (self):
        #Abriendo el archivo Json en modo lectura
        with open('Semana4Hackaton\jwilian\productos.json','r') as f:
            #Descargando como Lista
            ListaDescargada = json.load(f)
            j = 0
            i = False
            #Inicio de bucle while para determinar los elementos
            while i == False:
                if self.nombreMarca == ListaDescargada[j]["Nombre"]:
                    i=True
                    value=(ListaDescargada[j]["Unidades"])*(ListaDescargada[j]["CostoxUnidad"])
                    print(value)
                else:
                    j+=1

#Definir la clase MENU

class menu ():
    
    def __init__ (self,opciones):
        self.opciones=opciones

    def selMenu (self):
        print(Fore.GREEN+"=================="+Fore.RESET)
        print(Style.BRIGHT+Fore.BLACK+" MENU DE OPCIONES "+Fore.RESET)
        print(Fore.GREEN+"==================\n"+Fore.RESET)

#INICIO DEL PROGRAMA

i = False
while i == False:
    opciones = """1. Clientes.\n2. Empleados.\n3. Productos\n"""
    miMenu = menu(opciones)
    miMenu.selMenu()
    #SE INTENTA DEFINIR LA ESTRUCTURA WHILE TRUE COMO UNA ACCION DEL MENU; SIN EMBARGO SE TIENE PROBLEMAS PARA CONTINUAR CON LA SENTENCIA "IF"
    while True:
        try:
            print(Fore.BLUE+opciones+Fore.RESET)
            opcion = int(input("INGRESE UNA DE LAS OPCIONES: "))
            break

        except ValueError:
            print("INTRODUJO UN VALOR ERRONEO, INTENTELO OTRA VEZ.\n")

    if opcion == 1:
        print(Fore.GREEN+"Usted, escogio el modulo CLIENTES: "+Fore.RESET)
        opciones1 = """1. Validar existencia del cliente.\n2. Crear cliente.\n3. Ver cliente\n"""
        miMenu = menu(opciones1)
        miMenu.selMenu()
        
        while True:
            try:
                print(Fore.BLUE+opciones1+Fore.RESET)
                opcion = int(input("INGRESE UNA DE LAS OPCIONES: "))
                break

            except ValueError:
                print("INTRODUJO UN VALOR ERRONEO, INTENTELO OTRA VEZ.\n")
        
        if opcion == 1:
            
            print(Fore.GREEN+'Usted escogio "VALIDAR LA EXISTENCIA DEL CLIENTE"\n'+Fore.RESET)
            i = True
            
            nombre1 = input("Ingrese el nombre a verificar: ")
            nombre = nombre1.capitalize()
            cliente1=cliente("dni",nombre,"apellidoPaterno","apellidoMaterno")
            cliente1.validarCliente()

        elif opcion == 2:
            print(Fore.GREEN+'Usted escogio "CREAR CLIENTE"\n'+Fore.RESET)
            i = True

            nombre1 = input("Ingrese el nombre a crear: ")
            nombre=nombre1.capitalize()
            apellidoPaterno = input("Ingrese el primer apellido: ")
            apellidoMaterno = input("Ingrese el segundo apellido: ")
            dni = input("Ingrese el numero de DNI: ")
            cliente1=cliente(dni,nombre,apellidoPaterno,apellidoMaterno)
            try:
                cliente1.validarCliente()
                print(Fore.RED+"No puede volver a agregar los mismos datos"+Fore.RESET)
            except:
                cliente1.crearCliente()

        elif opcion == 3:
            print('Usted escogio "VER CLIENTE"\n')
            i = True

            dni = input("Ingrese el numero de DNI: ")
            cliente1=cliente(dni,"nombre","apellidoPaterno","apellidoMaterno")
            cliente1.verCliente()
 
    elif opcion == 2:
        opciones2="""1. Validar existencia del empleado.\n2. Crear empleado.\n3. Ver empleado\n"""
        miMenu=menu(opciones2)
        miMenu.selMenu()
        
        while True:
            try:
                print(opciones2)
                opcion = int(input("INGRESE UNA DE LAS OPCIONES: \n"))
                break

            except ValueError:
                print(Fore.RED+"INTRODUJO UN VALOR ERRONEO, INTENTELO OTRA VEZ.\n"+Fore.RESET)

        if opcion == 1:
            print('Usted escogio "VALIDAR LA EXISTENCIA DEL EMPLEADO"\n')
            i = True

            codigo = input("Ingrese el codigo a verificar: ")
            empleado1=empleado(codigo,"nombre","apellidoPaterno","apellidoMaterno")
            empleado1.validarEmpleado()

        elif opcion == 2:
            print(Fore.GREEN+'Usted escogio "CREAR EMPLEADO"\n'+Fore.RESET)
            i = True
            nombre = input("Ingrese el nombre: ")
            apellidoPaterno = input("Ingrese el primer apellido: ")
            apellidoMaterno = input("Ingrese el segundo apellido: ")
            codigo = input("Ingrese el codigo: ")
            empleado1=empleado(codigo,nombre,apellidoPaterno,apellidoMaterno)
            try:
                empleado1.validarEmpleado()
                print(Fore.RED+"No puede volver a agregar los mismos datos"+Fore.RESET)
            except:
                empleado1.crearEmpleado()

        elif opcion == 3:
            print(Fore.GREEN+'Usted escogio "VER EMPLEADO"\n'+Fore.RESET)
            i = True

            codigo = input("Ingrese el codigo de empleado: ")
            empleado1=empleado(codigo,"nombre","apellidoPaterno","apellidoMaterno")
            empleado1.verEmpleado()

    elif opcion == 3:
        opciones="""1. Agregar Productos.\n2. Validar existencia del producto.\n3. Quitar Productos\n4. Listar productos.\n5. Inventariar productos.\n"""
        miMenu=menu(opciones)
        miMenu.selMenu()
        
        while True:
            try:
                print(opciones)
                opcion = int(input("Ingrese una de las opciones: \n"))
                break
            except ValueError:
                print("Introdujo un valor erroneo, intentelo de nuevo")
    
        if opcion == 1:
            print('Usted escogio "AGREGAR PRODUCTOS"\n')
            i = True
            
            nombreMarca = input("Escriba el nombre del producto a agregar: ")
            presentacion = input("Ingrese la presentacion: ")
            codigo = input("Ingrese el codigo del producto: ")

            while True:
                try:
                    unidades = int(input("Ingrese las unidades existentes del producto: "))
                    costoUnitario = float(input("Ingrese el costo unitario del producto: "))
                    break
                except ValueError:
                    print("Introdujo un valor erroneo, intentelo de nuevo")
            
            producto1=producto(nombreMarca,presentacion,codigo,unidades,costoUnitario)
            try:
                producto1.valueProduct()
                print("No puede volver a agregar el mismo producto")
            except:
                producto1.addProduct()

        elif opcion == 2:
            print('Usted escogio "VALIDAR LA EXISTENCIA DEL PRODUCTO"\n')
            i = True

            nombreMarca = input("Ingrese el nombre del producto a verificar: ")
            producto1=producto(nombreMarca,"presentacion","codigo","unidades","costoUnitario")
            producto1.validarProduct()
        
        elif opcion == 3:
            print('Usted escogio "QUITAR PRODUCTOS"\n')
            i = True
            nombreMarca = input("Ingrese el nombre del producto a eliminar: ")
            producto1=producto(nombreMarca,"presentacion","codigo","unidades","costoUnitario")
            try:
                producto1.delProduct()
            except:
                print("El producto no existe en el inventario")

        elif opcion == 4:
            print('Usted escogio "LISTAR PRODUCTOS"\n')
            i = True
            producto1=producto("nombreMarca","presentacion","codigo","unidades","costoUnitario")
            producto1.listProduct()
        
        elif opcion == 5:
            print('Usted escogio "INVENTARIAR PRODUCTOS"\n')
            opciones = """1. Contar los productos.\n2. Valorizar los productos.\n"""
            miMenu = menu(opciones)
            miMenu.selMenu()
        
            while True:
                try:
                    print(opciones)
                    opcion = int(input("INGRESE UNA DE LAS OPCIONES: \n"))
                    break

                except ValueError:
                    print("INTRODUJO UN VALOR ERRONEO, INTENTELO OTRA VEZ.\n")
                    
            if opcion == 1:
                print('Usted escogio "CONTAR LOS PRODUCTOS"\n')
                i = True
                
                nombreMarca = input("Ingrese el nombre del producto a contar: ")
                producto1=producto(nombreMarca,"presentacion","codigo","unidades","costoUnitario")
                try:
                    producto1.countProduct()
                except:
                    print("El producto elegido, no fue ingresado; intente ingresarlo primero")
            elif opcion == 2:
                print('Usted escogio "VALORIZAR LOS PRODUCTOS\n')
                i = True

                nombreMarca = input("Ingrese el nombre del producto a valorizar: ")
                producto1=producto(nombreMarca,"presentacion","codigo","unidades","costoUnitario")
                try:
                    producto1.valueProduct()
                except:
                    print("No hay disponibilidad del producto en inventario, no está registrado")

    else:
        i = False

#NOTAS: 
# - SE DEBE INDAGAR SOBRE LA MEJORA DE LA ARQUITECTURA DEL PROGRAMA.
# - MUCHA REPETITIVIDAD EN EL CODIGO, LO CUAL DA A LA IDEA DE QUE ESTOS PUEDEN ORIENTARSE A MAS OBJETOS Y ASI REDUCIR EL CODIGO.
