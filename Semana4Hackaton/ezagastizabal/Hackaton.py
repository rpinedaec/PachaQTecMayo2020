import sys
import os
from datetime import date
from datetime import datetime
import time
import os.path

#Defino la clase Personas, me servirá para Clientes y Trabajadores
class Personas:
    def __init__(self, NombrePersona, ApellidoPersona, EdadPersona):
        self.NombrePersona = NombrePersona
        self.ApellidoPersona = ApellidoPersona
        self.EdadPersona = EdadPersona

#Defino clase Clientes que hereda atributos de la clase Persona
class Cliente(Personas):
    def __init__(self,  NombrePersona, ApellidoPersona, EdadPersona, CodigoCliente):
        super().__init__(NombrePersona, ApellidoPersona, EdadPersona)
        self.NombrePersona = NombrePersona
        self.ApellidoPersona = ApellidoPersona
        self.EdadPersona = EdadPersona
        self.CodigoCliente = CodigoCliente

    
    # def RegistrarCliente(self):
    #     self.NombrePersona = input("Nombre: ")
    #     self.ApellidoPersona = input("Apellido: ")
    #     self.CodigoCliente = input("Código: ")

    
    

#Defino clase Trabajador que hereda atributos de la clase Persona
class Trabajador(Personas):
    def __init__(self,NombrePersona, ApellidoPersona, EdadPersona, CodigoTrabajador):
        super().__init__(NombrePersona, ApellidoPersona, EdadPersona)
        self.NombrePersona = NombrePersona
        self.ApellidoPersona = ApellidoPersona
        self.EdadPersona = EdadPersona
        self.CodigoTrabajador = CodigoTrabajador
    
    def MarcarSalida(self):
        CodTrabajSal = input("Ingresa tu código de trabajador: ")
        HoraSalida = datetime.now()
        formatHoraSalida = HoraSalida.strftime('Horas: %H, Minutos: %M, del %d/%m/%Y')
        print(f"El trabajador {self.CodigoTrabajador} marcó salida a las {formatHoraSalida}")
        time.sleep(2)
        os.system('clear')
        ExistArch = os.path.isfile("HorariosTB.txt")
        if(ExistArch == True):
                fileAdd = open("HorariosTB.txt","a")
                fileAdd.write(f"Trabajador: {CodTrabajSal} Salida: {formatHoraSalida} \n")
        else:
                open("HorariosTB.txt","w")
    
    def toDic(self):
        d={
            "NombrePersona":self.NombrePersona,
            "ApellidoPersona":self.ApellidoPersona,
            "EdadPersona":self.EdadPersona,
            "CodigoTrabajador":self.CodigoTrabajador 
        }
        return d
class Productos:
    def __init__(self, NombreProducto, CodigoProducto, PrecioProducto, CostoProducto):
        self.NombreProducto = NombreProducto
        self.CodigoProducto = CodigoProducto
        self.PrecioProducto = PrecioProducto
        self.CostoProducto = CostoProducto
    
    # def AgregarProducto(self)



#Defino el menú para utilizar en cada usuario (cliente,trabajador)
class Menu:
    def __init__(self, NombreMenu, MenuIndicaciones, MenuOpciones):
        self.NombreMenu = NombreMenu
        self.MenuIndicaciones = MenuIndicaciones
        self.MenuOpciones = MenuOpciones
    
    def MostrarMenu(self):
        print("--- Empresa Ferretera Edwin ---")
        print("      ---"+self.NombreMenu+"---")
        print(self.MenuIndicaciones)
        for (key,value) in self.MenuOpciones.items():
            print(key,":", value)
    
    def LimpiarPantalla(self):
        os.system('clear')
    




#1. Menú Principal
OpMenuPrincipal = {"Cliente":1, "Trabajador": 2, "Salir": 0}
MenuPIndicaciones = "Elige el tipo de usuario al que perteneces:"
MenuPrincipal = Menu("Menú Principal", MenuPIndicaciones, OpMenuPrincipal)
# MenuPrincipal.MostrarMenu()

#2. Menú del Cliente
OpMenuCliente = {"Comprar": 1, "Consultar Productos":2, "Devolver":3,"<-Regresar":0 }
MenuCIndicaciones = "Digite el número relacionado a la acción que desee ejecutar"
MenuCliente = Menu("Menú Cliente",MenuCIndicaciones, OpMenuCliente)
# MenuCliente.MostrarMenu()

#3. Menú del Trabajador
OpMenuTrabajador = {"Marcar Ingreso": 1, "Marcar Salida":2, "Cargar Inventario":3, "<-Regresar":0}
MenuTIndicaciones = "Digite el número relacionado a la acción que desee ejecutar"
MenuTrabajador = Menu("Menú Trabajador",MenuTIndicaciones, OpMenuTrabajador)
# MenuTrabajador.MostrarMenu()

#4. Menú de Registro
OpMenuRegCliente = {"Sign Up":1, "Log In":2, "<-Regresar":0}
MenuRCIndicaciones = "Registrese o Ingrese a su cuenta"
MenuRegCliente = Menu("Menu de Ingreso/Registro", MenuRCIndicaciones, OpMenuRegCliente)

#3.1 Trabajador Elige Marcar Ingreso. Creo al archivo para almacenar entradas y salidas 
def MarcarIngreso():
    CodTrabajIng = input("Ingresa tu código de trabajador: ")
    HoraEntrada = datetime.now()
    formatHoraEntrada = HoraEntrada.strftime('Horas: %H, Minutos: %M, del %d/%m/%Y')
    print(f"El trabajador {CodTrabajIng} ingresó a las {formatHoraEntrada}")
    time.sleep(2)
    os.system('clear')
    #Crear el archivo si es que no existe, sino escribe en la siguiente línea, el ingreso
    ExistArch = os.path.isfile("HorariosTB.txt")
    if(ExistArch == True):
        fileAdd = open("HorariosTB.txt","a")
        fileAdd.write(f"Trabajador: {CodTrabajIng} Ingreso: {formatHoraEntrada} \n")
    else:
        open("HorariosTB.txt","w")
    
    # fileAlmac = open("HorariosTB.txt","a")
    # fileAlmac.write(f"Trabajador: {CodTrabajIng}, Hora Ingerso: {formatHoraEntrada}\n")
   
#3.2 Trabajador Elige Marcar Salida
def MarcarSalida():
    CodTrabajSal = input("Ingresa tu código de trabajador: ")
    HoraSalida = datetime.now()
    formatHoraSalida = HoraSalida.strftime('Horas: %H, Minutos: %M, del %d/%m/%Y')
    print(f"El trabajador {CodTrabajSal} marcó salida a las {formatHoraSalida}")
    time.sleep(2)
    os.system('clear')
    ExistArch = os.path.isfile("HorariosTB.txt")
    if(ExistArch == True):
            fileAdd = open("HorariosTB.txt","a")
            fileAdd.write(f"Trabajador: {CodTrabajSal} Salida: {formatHoraSalida} \n")
    else:
            open("HorariosTB.txt","w")

def AddProducto():
    blAddProd = True
    while blAddProd:
        OpAoS = input("Que deseas hacer Agregar: A / Salir : S ").title()
        if(OpAoS == "A"):
            strNomNuevProd = input("Qué producto quieres agregar: ")
            flValorNuevProd = float(input("Cuál es su valor: "))
            strCantNuevProd = int(input("Cantidad de productos: "))
            DicAddProd = {}
            print(strNomNuevProd)
            print(flValorNuevProd)
            DicAddProd.update({"NombProd": strNomNuevProd})
            DicAddProd.update({"ValorProd": flValorNuevProd})
            DicAddProd.update({"CantProd": strCantNuevProd})
            lstProd.append(DicAddProd)
            #Comando para agregar archivo
            ExistArchInv = os.path.isfile("InventarioProd.txt")
            if(ExistArchInv == True):
                fileAddInv = open("InventarioProd.txt","a")
                fileAddInv.write(f"{DicAddProd}\n")
            else:
                fileAddNuevoInv = open("InventarioProd.txt","w")
                fileAddNuevoInv.write(f"{DicAddProd}\n")
            print(lstProd)
        elif(OpAoS == "S"):
            print("Saliste")
            time.sleep(2)
            os.system('clear')
            blAddProd = False
        else:
            print("Digita una opción válida: A/S")

def UsuarioNuevo():
    NombreCl = input("Nombre: ")
    ApellidoCl = input("Apellido: ")
    UsuarioCod = input("Crea Codigo: ")
    PasswCl = input("Crea una constraseña:")
    dicNuevoCl = {}
    dicNuevoCl.update({"NomCliente": NombreCl})
    dicNuevoCl.update({"ApellidoCliente": ApellidoCl})
    dicNuevoCl.update({"UsuarioCod": UsuarioCod})
    dicNuevoCl.update({"PasswordCliente": PasswCl})
    Usuarios.append(dicNuevoCl)
    print(Usuarios)
    ExistArchUsuarios = os.path.isfile("RegUsuariosEZ.txt")
    if(ExistArchUsuarios == True):
        fileAddUsu = open("RegUsuariosEZ.txt","a")
        fileAddUsu.write(f"{dicNuevoCl}\n")
        print(f"Se registró el usuario {dicNuevoCl}")
        time.sleep(2)
        os.system('clear')
    else:
        fileAddUsu = open("RegUsuariosEZ.txt","w")
        fileAddUsu.write(f"{dicNuevoCl}\n")
        print(f"Se registró el usuario {dicNuevoCl}")
        time.sleep(2)
        os.system('clear')

def UsuarioAntiguo():
    UsuarioCodA = input("Ingresa tu código de Usuario: ")
    PasswUsuA = input("Ingresa tu Clave: ")
    print(f"Se ingresó {UsuarioCodA} con clave {PasswUsuA}")
    time.sleep(2)
    os.system('clear')
    
lstTrabajadorDic = []
lstTrabajador = []
Usuarios = []
lstProd = []
bucle = True
while(bucle == True):
    MenuPrincipal.MostrarMenu()
    OpElegir = input("Elegir Opcion: ")
    if(OpElegir == "1"):#Eligio que es cliente
        MenuCliente.LimpiarPantalla()
        bucleCliente = True
        while(bucleCliente == True):
            MenuRegCliente.MostrarMenu()
            bucleCliente == False
            # MenuCliente.MostrarMenu()
            OpElegirIngreso = input("Cliente, elige Opción: ")
            if (OpElegirIngreso == "1"):
                UsuarioNuevo()
            elif(OpElegirIngreso == "2"):
                UsuarioAntiguo()
            elif(OpElegirIngreso == "0"):
                os.system('clear')
                break
            else:
                print("Digita una opción válida")
                time.sleep(3)
                os.system('clear')
                bucleCliente == False
    elif(OpElegir == "2"):#Eligio que es trabajador
        MenuTrabajador.LimpiarPantalla()
        bucleTrabajador = True
        while(bucleTrabajador == True):
            MenuTrabajador.MostrarMenu()
            OpElegirTrabajador = input("Trabajador, elije Opción: ")
            if(OpElegirTrabajador == "1"):
                print("no se encontro trabajador")
                print("desea crearlo?")
                print("Ingrese el codigo")
                CodigoTrabajador = input()
                print("Ingrese el Nombre Persona")
                NombrePersona = input()
                print("Ingrese el Apellido Persona")
                ApellidoPersona = input()
                print("Ingrese la edad ")
                EdadPersona = input()
                trabajador = Trabajador(NombrePersona, ApellidoPersona, EdadPersona, CodigoTrabajador)
                lstTrabajador.append(trabajador)
                lstTrabajadorDic.append(trabajador.toDic())
                codTrabajador = input()
                for dicTrabajador in lstTrabajadorDic:
                    if dicTrabajador["CodigoTrabajador"] == codTrabajador:
                        print("Trabajador encontrado")
                        break;
                    else:
                        pass
                        #NombrePersona, ApellidoPersona, EdadPersona, CodigoTrabajador
                #MarcarIngreso()
            elif(OpElegirTrabajador == "2"):
                MarcarSalida()
            elif(OpElegirTrabajador =="3"):
                AddProducto()
            elif(OpElegirTrabajador == "0"):
                os.system('clear')
                break
            else:
                print("Digita una opción válida")
                time.sleep(3)
                os.system('clear')
                bucleTrabajador == False
    elif(OpElegir == "0"):
        sys.exit()
    else:
        print("Digita una opción válida")
        time.sleep(3)
        os.system('clear')
        bucle == False


