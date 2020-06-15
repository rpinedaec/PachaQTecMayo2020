ListaProducto=[]
ListaKardex=[]
VectorProducto=[]
Vector=[]
 
#usamos para ver si el vector se encuentra vacío o lleno
def Buscar(Codigo):
    Posicion=len(ListaProducto)
    return Posicion
 
#Buscamos el nombre del producto a consultar
def BuscarNombre(Codigo):
    Posicion=len(ListaProducto)
    if Posicion==0:
        Nombre=''
    else:
        for VectorProducto in ListaProducto:
            if VectorProducto[0]==Codigo:
                Nombre=VectorProducto[1]
            else:
                Nombre=''
    return Nombre
 
#Extraemos todos los datos del producto a buscar
def BuscarProducto(Codigo):
    VPRODUCTO=[]
    for VectorProducto in ListaProducto:
        if VectorProducto[0]==Codigo:
            VPRODUCTO.append(VectorProducto[0])
            VPRODUCTO.append(VectorProducto[1])
            VPRODUCTO.append(VectorProducto[2])
            VPRODUCTO.append(VectorProducto[3])
            VPRODUCTO.append(VectorProducto[4])
    return VPRODUCTO
 
#Mostramos los datos del producto buscado
def BuscarProducto2(Codigo):
    VPRODUCTO=[]
    for VPRODUCTO in ListaProducto:
        if VPRODUCTO[0]==Codigo:
            print("Codigo: ",VPRODUCTO[0])
            print("Nombre: ",VPRODUCTO[1])
            print("Saldo Disponible: ",VPRODUCTO[2])
            print("Costo Promedio: ",VPRODUCTO[3])
            print("Total: ",VPRODUCTO[4])
 
#Actualizamos el Saldo del Producto deacuerdo al movimiento (Ingreso/Egreso)
def ActualizarSaldo(Codigo,TipoMov,Cantidad,Total):
    VPRODUCTO=[]
    for VectorProducto in ListaProducto:
        if VectorProducto[0]==Codigo:
            ListaProducto.remove(VectorProducto)
            CantidadT=float(VectorProducto[2])
            TotalT=float(VectorProducto[4])
            if TipoMov=='I':
                CantidadT=CantidadT+float(Cantidad)
                TotalT=TotalT+float(Total)
                print('I',CantidadT)
                print('I',TotalT)
            else:
                CantidadT=CantidadT-float(Cantidad)
                TotalT=TotalT-float(Total)
                print('E',CantidadT)
                print('E',TotalT)
            if CantidadT==0:
                Costo=0
            else:
                Costo=TotalT/CantidadT
            VPRODUCTO.append(VectorProducto[0])
            VPRODUCTO.append(VectorProducto[1])
            VPRODUCTO.append(CantidadT)
            VPRODUCTO.append(Costo)
            VPRODUCTO.append(TotalT)
            ListaProducto.append(VPRODUCTO)
 
#Realizamos el Ingreso de Producto
def Ingreso():
    VKARDEX=[]
    print('')
    print('****** INGRESO DE PRODUCTO ******')
    Codigo=input("Ingrese el Código del Producto: ")
    Nombre=BuscarNombre(Codigo)
    if Nombre=='':
        Nombre=input("Ingrese la Descripción del Producto: ")
    else:
        Nombre=BuscarNombre(Codigo)
        print("Nombre del Producto: ",Nombre)
    Cantidad=input("Ingrese la Cantidad del Producto: ")
    Precio=input("Ingrese el Precio Unitario: ")
    Total=float(Cantidad)*float(Precio)
    Orden=input("Ingrese el N° de Orden de Compra: ")
    if Buscar(Codigo)==0:
        VectorProducto.append(Codigo)
        VectorProducto.append(Nombre)
        VectorProducto.append(Cantidad)
        VectorProducto.append(Precio)
        VectorProducto.append(Total)
        ListaProducto.append(VectorProducto)
    else:
        ActualizarSaldo(Codigo,'I',Cantidad,Total)
    VKARDEX.append("I")
    VKARDEX.append(Codigo)
    VKARDEX.append(Nombre)
    VKARDEX.append(Cantidad)
    VKARDEX.append(Precio)
    VKARDEX.append(Total)
    VKARDEX.append(Orden)
    ListaKardex.append(VKARDEX)
    print('')
 
#Realizamos el Egreso (Venta)
def Egreso():
    VKARDEX=[]
    print('')
    print('****** EGRESO DE PRODUCTO ******')
    Codigo=input("Ingrese el Código del Producto: ")
    Vector=BuscarProducto(Codigo)
    if len(Vector)>0:
        print("Nombre del Producto: ",Vector[1])
        print("Costo del Producto: ",Vector[3])
        Cantidad=float(input("Ingrese la Cantidad a Egresar: "))
        Total=float(Vector[3])*Cantidad
        Orden=input("Ingrese el N° de Factura: ")
        VKARDEX.append("E")
        VKARDEX.append(Codigo)
        VKARDEX.append(Vector[1])
        VKARDEX.append(Cantidad)
        VKARDEX.append(float(Vector[3]))
        VKARDEX.append(Total)
        VKARDEX.append(Orden)
        ActualizarSaldo(Codigo,'E',Cantidad,Total)
        ListaKardex.append(VKARDEX)
        print('')
    else:
        print("Producto No Existe!!")
 
#Mostramos el Kardex de un Producto
def Kardex():
    VKARDEX=[]
    VPRODUCTO=[]
    print('')
    print('****** KARDEX DE PRODUCTO ******')
    print('')
    Codigo=input("Ingrese el Código del Producto: ")
    print('')
    print('CODIGO','NOMBRE','TIPO MOV','CANTIDAD','COSTO','DOCUMENTO',sep="\t")
    if BuscarNombre(Codigo)=='':
        print("Código No Existente")
    else:
        for VKARDEX in ListaKardex:
            if VKARDEX[1]==Codigo:
                print(VKARDEX[1],VKARDEX[2],VKARDEX[0],VKARDEX[3],VKARDEX[4],VKARDEX[6],sep="\t")
    print('')
 
 
# Menú Principal
while True:
    print('SISTEMA DE INVENTARIO')
    print('')
    print('****** Menú Principal ******')
    print('0. SALIR')
    print('1. INGRESO DE PRODUCTO')
    print('2. EGRESO DE PRODUCTO')
    print('3. KARDEX')
    print('4. BUSQUEDA DE PRODUCTO')
    opcion=input('Digitar una Opción: ')
    if opcion=='0':
        break
    elif opcion=='1':
        Ingreso()
    elif opcion=='2':
        Egreso()
    elif opcion=='3':
        Kardex()
    elif opcion=='4':
        print('')
        print('****** BUSQUEDA DE PRODUCTO ******')
        Codigo=input("Ingrese el Código del Producto: ")
        BuscarProducto2(Codigo)
    else:
        print('Opción no válida')