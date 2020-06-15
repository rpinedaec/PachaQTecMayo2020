#Modulo_1: Menu
#Módulo_2: Agregar Producto
#Módulo_3: Realizar Consulta
    #3.1 Buscar producto
    #3.2 Calcular inventario
#Módulo_4: Modificar Inventario
    #3.1 Remover produto
    #3.2 Cambiar inforamción

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#Modulo_1: Menu
def M1_menu():
    Keep=True
    while Keep:
        try:
            print(" ")
            print(color.BLUE+"::::::::::BIENVENIDO. CÚAL ACCIÓN DESEA REALIZAR?::::::::::"+color.END)
            print(" ")
            print("Agregar producto    : ingrese A")
            print("Realizar consulta   : ingrese C")
            print("Modificar Inventario: ingrese M")
            print("Salir del sistema   : ingrese S")
            print("-----------------------------------------------------------")
            respuesta=input(color.YELLOW+"Respuesta:"+color.END)
            print("    ")
            if (respuesta.upper()=="A"):
                M2_agregarproducto()
            elif (respuesta.upper()=="C"):
                print(color.BLUE+"::::::::::::::::::::MÓDULO DE CONSULTA:::::::::::::::::::::"+color.END)
                print(" ")
                print("Cúal consulta desea realizar?:")
                print(" ")
                print("Buscar producto    : ingrese B")
                print("Calcular inventario: ingrese I")
                print("-----------------------------------------------------------")
                respuesta=input(color.YELLOW+"Respuesta:"+color.END)
                print(" ")
                if(respuesta.upper()=="B"):
                    M3_buscprodct()
                elif(respuesta.upper()=="I"):
                    M3_calinvent()
                else:
                    print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
                    M1_menu()
            elif (respuesta.upper()=="M"):
                print(color.BLUE+":::::::::::::::::MÓDULO PARA MODIFICACIPNES::::::::::::::::"+color.END)
                print(" ")
                print("Cúal modificación desea realizar? Elija una opción:")
                print(" ")
                print("Remover información: ingrese R")
                print("Cambiar información: ingrese K")
                print("-----------------------------------------------------------")
                respuesta=input(color.YELLOW+"Respuesta:"+color.END)
                if (respuesta.upper()=="K"):
                    M4_modf()
                elif(respuesta.upper()=="R"):
                    M4_remv()
                else:
                    print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
                    M1_menu()
            elif (respuesta.upper()=="S"):
                quit()
        except ValueError:
            print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
            M1_menu()   

#Módulo_2: Agregar Producto
Lista_producto=[]
def M2_agregarproducto():
    print(color.BLUE+":::::::::::::::MÓDULO PARA AGREGAR PRODUCTOS:::::::::::::::"+color.END)
    print("Ingrese los siguientes datos:")
    Nombre_producto=input(color.GREEN+"→"+color.END+"Nombre del producto         : ")
    FechIng_producto=input(color.GREEN+"→"+color.END+"Fecha de ingreso            : ")
    PrecioUni_producto=input(color.GREEN+"→"+color.END+"Precio unitario del producto: ")
    FechVen_producto=input(color.GREEN+"→"+color.END+"Fecha de vencimiento        : ")
    Ubica_producto=input(color.GREEN+"→"+color.END+"Ubicación del producto      : ")
    print("-----------------------------------------------------------")
    print("Esta seguro que dese agregar la siguiente información? si/no:")
    respuesta=input(color.YELLOW+"Respuesta:"+color.END)
    
    if (respuesta.upper()=="SI"):
        Dic_producto={
        "Nombre de producto": Nombre_producto,
        "Fecha de ingreso": FechIng_producto,
        "Precio unitario": PrecioUni_producto,
        "Fecha de vencimiento": FechVen_producto,
        "Ubicación": Ubica_producto,
        }
        Lista_producto.append(Dic_producto)
        print(color.GREEN+"Producto agregado (✓)"+color.END)
        print(" ")
        print("Deseas agregar otro producto? si/no: ")
        respuesta=input(color.YELLOW+"Respuesta:"+color.END)
        print(" ")
    if (respuesta.upper()=="SI"):
        M2_agregarproducto()
    if(respuesta.upper()=="NO"):
        M1_menu()
    else:
        print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
        M1_menu()
  
#Módulo_3: Realizar Consulta
def M3_buscprodct():
    print(color.BLUE+"::::::::::::::::::::MÓDULO DE CONSULTA:::::::::::::::::::::"+color.END)
    print(" ")
    print("Ingrese el numero del que desea consultar")
    print(" ")
    n=0
    for x in Lista_producto:
         nomb_product=x["Nombre de producto"]
         n=n+1
         print(f"Para, {nomb_product} ingrese: {n}")
    print("-----------------------------------------------------------")
    respuesta=int(input(color.YELLOW+"Respuesta: "+color.END))
    print(" ")
    print(color.GREEN+"Esta es la información que se enocntró (✓):"+color.END)
    print(Lista_producto[respuesta-1]["Nombre de producto"])
    print(Lista_producto[respuesta-1]["Fecha de ingreso"])
    print(Lista_producto[respuesta-1]["Precio unitario"])
    print(Lista_producto[respuesta-1]["Fecha de vencimiento"])
    print(Lista_producto[respuesta-1]["Ubicación"])
    print(" ")
    print("Deseas realizar otra busquedad? si/no:")
    print("-----------------------------------------------------------")
    respuesta=input(color.YELLOW+"Respuesta:"+color.END)
    if (respuesta.upper()=="SI"):
        M3_buscprodct()
    if (respuesta.upper()=="NO"):
        M1_menu()
    else:
        print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
        M1_menu()

def M3_calinvent():
    print(color.BLUE+"::::::::::::::::::::MÓDULO DE CONSULTA:::::::::::::::::::::"+color.END)
    print(" ")
    Total_val_inv=0
    Total_cant_inv=0
    for x in Lista_producto:
        Total_val_inv=Total_val_inv+float(x["Precio unitario"])
        Total_cant_inv=Total_cant_inv+1
    print(color.GREEN+f"El total del valor del inventario es de {Total_val_inv}"+color.END)
    print(color.GREEN+f"La cantidad total de productos es de {Total_cant_inv}"+color.END)

    print("Deseas calcular otra vez? si/no: ")
    print("-----------------------------------------------------------")
    respuesta=input(color.YELLOW+"Respuesta:"+color.END)
    if (respuesta.upper()=="SI"):
        M3_calinvent()
    if (respuesta.upper()=="NO"):
        M1_menu()
    else:
        print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
        M1_menu()

#Módulo_4: Modificar inventario     
def M4_modf():
    print(color.BLUE+":::::::::::::::::MÓDULO PARA MODIFICACIPNES::::::::::::::::"+color.END)
    print(" ")
    print("Esta es la base de datos")
    print(" ")
    n=0
    for x in Lista_producto:
        n=n+1
        Nom=x["Nombre de producto"]
        FechIng=x["Fecha de ingreso"]
        PrecUni=x["Precio unitario"]
        FechVen=x["Fecha de vencimiento"]
        Ubica=x["Ubicación"]
        print(f"|  {Nom}  |  {FechIng}  |  {PrecUni}  |  {FechVen}  |  {Ubica}  |"+color.GREEN+f"→{n}"+color.END)
    print(" ")
    print("Ingrese el numero del producto que desea modificar:")
    print("-----------------------------------------------------------")
    respuesta_1=int(input(color.YELLOW+"Respuesta: "+color.END))
    print(" ")
    print("Ingrese el campo que desea modificar:")
    print(color.GREEN+"→"+color.END+"Nombre de producto")
    print(color.GREEN+"→"+color.END+"Fecha de ingreso")
    print(color.GREEN+"→"+color.END+"Precio unitario")
    print(color.GREEN+"→"+color.END+"Fecha de vencimiento")
    print(color.GREEN+"→"+color.END+"Ubicación")
    print("-----------------------------------------------------------")
    respuesta_2=input(color.YELLOW+"Respuesta: "+color.END)
    print(" ")
    print("Ingrese el nuevo valor")
    print("-----------------------------------------------------------")
    respuesta_3=input(color.YELLOW+"Respuesta: "+color.END)
    print(" ")
    Lista_producto[respuesta_1-1][respuesta_2]=respuesta_3
    print(color.GREEN+"Se realizo la modificación(✓)"+color.END)
    print("Deseas realizar otra modificación? si/no")
    respuesta=input(color.YELLOW+"Respuesta:"+color.END)
    if (respuesta.upper()=="SI"):
        M4_modf()
    if (respuesta.upper()=="NO"):
        M1_menu()
    else:
        print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
        M1_menu()

def M4_remv():
    print(color.BLUE+":::::::::::::::::MÓDULO PARA MODIFICACIPNES::::::::::::::::"+color.END)
    print(" ")
    print("Esta es la base de datos, cual registro desería eliminar? Ingrese el número:")
    n=0
    for x in Lista_producto:
        n=n+1
        Nom=x["Nombre de producto"]
        FechIng=x["Fecha de ingreso"]
        PrecUni=x["Precio unitario"]
        FechVen=x["Fecha de vencimiento"]
        Ubica=x["Ubicación"]
        print(f"|  {Nom}  |  {FechIng}  |  {PrecUni}  |  {FechVen}  |  {Ubica}  |"+color.GREEN+f"→{n}"+color.END)
    print("-----------------------------------------------------------")
    respuesta=int(input(color.YELLOW+"Respuesta:"+color.END))
    del Lista_producto[respuesta-1]
    print(" ")
    print(color.GREEN+"Elemento eliminado (✓)"+color.END)
    print(" ")
    print("Desea remover otro porducto? si/no: ")
    print("-----------------------------------------------------------")
    respuesta=input(color.YELLOW+"Respuesta:"+color.END)
    if (respuesta.upper()=="SI"):
        M4_remv()
    if (respuesta.upper()=="NO"):
        M1_menu
    else:
        print(color.RED+"(!) Ingresó una opción no valida, devuelta al menu principal"+color.END)
        M1_menu()
M1_menu()