
def validarEntero(mensaje):
    booleanCampo = True
    entrada=0
    while booleanCampo:
        entrada = input(mensaje)
        try:
            entrada = int(entrada)
            booleanCampo=False
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")
    return entrada



def validarFloat(mensaje):
    booleanCampo = True
    entrada=0.0
    while booleanCampo:
        entrada = input(mensaje)
        try:
            entrada = float(entrada)
            booleanCampo=False
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero o con decimal")
    return entrada





def listarUnidadMedida(listUnidadMedida):
    strTexto = "Unidad de Medida: "
    Contador = 0
    for p in listUnidadMedida:
        Contador+=1
        strTexto += str(Contador)+")"+ p +"\t"
    print(strTexto)





def seleccionUnidadMedida(listUnidadMedida):
    strRetornar = "" 
    while strRetornar=="":
        strSeleccionUM=validarEntero("Para agregar UM=99 /Ingrese numero de UM: ")
        if(strSeleccionUM==99):
            pasarTrue = True 
            while pasarTrue:
                strNuevo = input("0=Salir / Nueva UM: ")
                if(strNuevo=="0"):
                    pasarTrue=False
                    break
                intConta = 0
                for p in listUnidadMedida:
                    if(strNuevo==p):
                        intConta+=1
                if(intConta>0):
                    pasarTrue=True
                    print("Valor existente.")
                else:
                    pasarTrue=False
                    strRetornar=strNuevo
                    break
        else:
            intContar2 = 0
            for p in listUnidadMedida:
                intContar2+=1
                if(intContar2==int(strSeleccionUM)):
                    strRetornar = p
                    break
    return strRetornar


def validarNombreEnLista(lstProductos, mensaje):
    strRetornar = "" 
    boolValor = True
    while boolValor:
        strNombreIngresado=input(mensaje)
        if(strNombreIngresado=="0"):
            boolValor = False
            break
        else:
            ValorTemporal = 0
            for p in lstProductos:
                print("Valor existente.")
                if(p["Nombre"]==strNombreIngresado):
                    ValorTemporal+=1
            if(ValorTemporal==0):
                strRetornar=strNombreIngresado
                boolValor=False
    return strRetornar



def addProducto(lstProductos, listUnidadMedida):
    print("Agregando Productos")
    blMenuProducto = True 
    while blMenuProducto:
        menuProducto = input("Agregar=A / Salir=S : ")
        if(menuProducto == "A"):
            strNombreProducto = validarNombreEnLista(lstProductos,"Salir=0 / Ingresa el nombre: ")
            if(strNombreProducto==""):
                blMenuProducto = False
                break
            flStockProducto = validarFloat(f"Stock de {strNombreProducto}: ")           
            listarUnidadMedida(listUnidadMedida)
            strUnidadMed = seleccionUnidadMedida(listUnidadMedida)
            print("Registrado: "+str(flStockProducto)+" "+strUnidadMed)
            flValorProducto = validarFloat(f"Valor por {strUnidadMed}: ")
            strTipoMoneda=""
            intTipoMonedaInput = 0
            while intTipoMonedaInput<1 or intTipoMonedaInput>2:
                intTipoMonedaInput = validarEntero("Moneda 1=Dolares / 2=Soles: ")
            if (intTipoMonedaInput==1):
                strTipoMoneda = "Dolares"
            elif (intTipoMonedaInput==2):
                strTipoMoneda = "Soles"
            else:
                strTipoMoneda = "Soles"
            dicProducto={}
            dicProducto.update({"Nombre":strNombreProducto})
            dicProducto.update({"Stock":round(flStockProducto,3)})
            dicProducto.update({"Valor":round(flValorProducto,3)})
            dicProducto.update({"UMedida":strUnidadMed})
            flTotal = flValorProducto*flStockProducto
            dicProducto.update({"Total":round(flTotal,3)}) 
            dicProducto.update({"Moneda":strTipoMoneda})
            lstProductos.append(dicProducto)
            print(f"Producto \"{strNombreProducto}\" agregado correctamente.")
        else:  
            blMenuProducto = False
    return lstProductos

def myFunc(e):
  return e['Nombre']

def listProducto(lstProductos):
    lstProductos = sorted(lstProductos, key=myFunc)
    print("\n\nLista de producto en inventario: (Monedas: Soles/Dolares, Redondeo a 3 decimales)")
    print("------------------------------------------------------------------------")
    for p in lstProductos:
        strTitulo = ""
        strTituloGuion = ""
        for(key, value) in p.items():
            strTitulo += str(key).ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t"
        print(strTitulo)
        print(strTituloGuion)
        break
    flTotalProductoSoles = 0.00
    flTotalProductoDolares = 0.00
    for p in lstProductos:
        strTexto = ""
        ValorTemporal = 0
        for (key, value) in p.items():
            strTexto += str(value).ljust(10)+"\t\t"
            if(key =="Total"): 
                ValorTemporal=round(value,3)
            if(key=="Moneda" and value=="Soles"):
                flTotalProductoSoles+=ValorTemporal
            elif(key=="Moneda" and value=="Dolares"):
                flTotalProductoDolares+=ValorTemporal
        print(strTexto)
    print("================================") 
    print("TOTAL VALORIZADO (SOLES):\t"+str(round(flTotalProductoSoles,2)))
    print("TOTAL VALORIZADO (DOLARES):\t"+str(round(flTotalProductoDolares,2)))
    print("------------------------------------------------------------------------ \n\n")
    input("Enter para seguir.")
    return lstProductos
     



def listSimpleProducto(lstProductos):
    lstProductos = sorted(lstProductos, key=myFunc)
    for p in lstProductos:
        strTitulo = "  "
        strTituloGuion = "  "
        for(key, value) in p.items():
            strTitulo += str(key).ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t"
        print(strTitulo)
        print(strTituloGuion)
        break
    intContador = 0
    for p in lstProductos:
        intContador+=1
        strTexto = str(intContador)+") " 
        for (key, value) in p.items():
            strTexto += str(value).ljust(10)+"\t\t" 
        print(strTexto)
     




def delProducto(lstProductos):
    print("Eliminando productos")
    blMenuProductoEliminar = True
    while blMenuProductoEliminar:
        menuProducto = input("Salir=S / Eliminar=D: ")
        if(menuProducto == "D" or menuProducto == "d"):
            print("Lista de productos:")
            listSimpleProducto(lstProductos)
            strNombreEliminar = input("Nombre del producto a eliminar: ")
            for p in lstProductos:
                for (key, value) in p.items():
                    key
                    if(value == strNombreEliminar):
                        strAfirmacion = input(f"borrar {value}???  S/N")
                        if(strAfirmacion == "s" or strAfirmacion == "S" ):
                            lstProductos.remove(p)
                        else:
                            break
        elif(menuProducto == "S" or menuProducto == "s"):
            blMenuProductoEliminar = False
        else:
            blMenuProductoEliminar = True
    return lstProductos
