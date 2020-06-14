
def addproducto():
    while True:
 #       if(menuproducto=="A"):
 #          menuproducto = input("Que deseas hacer Agregarc: A/Salir : ")
        try:
            print("Escogio Agregar Producto")       
            nombreproducto = input("Digita el nombre del Producto: ")
            cantproducto= int(input(f"Digita la cantidad de {nombreproducto}: "))
            valorproducto = float(input(f"Digita valor de {nombreproducto}: "))
            dicproducto={}
            dicproducto.update({"NombreProducto":nombreproducto})
            dicproducto.update({"CantidadProducto":cantproducto})
            dicproducto.update({"ValorUnitario":valorproducto})
            dicproducto.update({"ValorProducTotal":valorproducto * cantproducto})
            print(dicproducto)
            lstproductos.append(dicproducto)
            print(lstproductos)  
            print("Felicidades Producto Agregado Correctamente")
            menuproducto=""
            menuproducto=input("Presione (a) si desea agregar más Productos sino Presione (s) : s/a ")
        except ValueError:
            print("No se puede convertir letras en números")  
        if(menuproducto == "s"):
            break
        

def delproducto():
    print("Ingresó a ELiminar Productos")
    while True:
        print("Busca en la lista el producto que deseas quitar")
        for p in lstproductos:
            for (key, value) in p.items():
                print(key , " :: ",value)

        print("Escribe el nombre del Producto que quieres ELiminar")
        nombreeliminar=input()
        for p in lstproductos:
            for (key, value) in p.items():
        
                if(value == nombreeliminar):
                    print(f"Borrar {value}???")
                    lstproductos.remove(p)
        print(lstproductos)



def showproducto():
    print("           *********INVENTARIO DE PRODUCTOS******")
    print("-----------------------------------------------------------------")
    flindex=0
    fltotal=0.0
    print("ID\t|PRODUCTO\t|CANTIDAD\t|VALOR UNIT.\t|SUBTOTAL")
    print("-----------------------------------------------------------------")
    for p in lstproductos:
        flindex += 1
        print(f"{flindex}\t|{p['NombreProducto']}\t\t|{p['CantidadProducto']}\t\t|{p['ValorUnitario']}\t\t|{p['ValorProducTotal']}")
        valortotal= p['CantidadProducto'] * p['ValorUnitario']
        fltotal += valortotal
    print("-----------------------------------------------------------------")
    print(f"El Precio Total de todos los Productos es: S/.{fltotal}")
    #print(fltotal)

 


lstproductos=[]
dicproducto={}


menu = ""
opcionsalir=""
while menu != "0":
  
    print("---------------------------")
    print("Bienvenido Escoge la opcion:")
    print("1 : Agregar Producto")
    print("2 : Quitar Producto")
    print("3 : Inventario")
    print("0 : Salir")
    menu= input()
    if(menu == "1"):
         addproducto()        
    elif(menu=="2"):
         delproducto()
    elif(menu=="3"):
        showproducto()
    elif(menu=="0"):
        break
    else:
        opcionsalir = input("No escogió las opciones indicadas;desea salir s/n")
    if(opcionsalir == "s"):
        break
