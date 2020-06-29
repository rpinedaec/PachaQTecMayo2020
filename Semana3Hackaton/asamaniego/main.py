
import sys
import time

# aldo samaniego pimentel


productos = {}

def menu():
    opcion = 0
    while (opcion != 6):
        print("-----------------------------")
        print("     PRODUCTOS (abarrotes)        ")
        print("-----------------------------")
        print("    ")
        print("1 - Agregar Productos")
        print("2 - Quitar Productos")
        print("3 - Listar Productos")
        print("- Inventariar Productos -")
        print("4 - Contar Productos")
        print("5 - Valorizar Productos")
        print("6 - Salir")
        try:
            opcion = int(input("Elige una opción [1 - 6 ]: "))
        except ValueError:
            print("Ingresa un número entre 1 y 6")
            time.sleep(3)   

        
        if opcion == 1: 
            agregar_productos()
        elif opcion == 2: 
            quitar_productos() 
        elif opcion == 3:
            listar_productos()
        elif opcion == 4: 
            contar_productos() 
        elif opcion == 5:
            valorizar_productos()
        elif opcion == 6:
            opcion =6
       
            

def agregar_productos():
    #existe = -1
    try:
        codpro = int(input("ingresa el código: "))
      
        codigo_producto = productos.get(codpro,-1) 
        if codigo_producto == -1:
            nompro = input("ingresa el nombre: ")
            try:
                cantpro = int(input("ingresa la cantidad: "))
            except ValueError:
                print("la cantidad es numerica")

            try:
                preciopro = float(input("ingresa el precio: "))
            except ValueError:
                print("El precio es numerico")

            productos.update({ codpro : [nompro, cantpro, preciopro]})
        else:
            print("este código de producto ya existe")
            time.sleep(3)  
    except ValueError:
            print("El código  es numerico")     
        
    
        
            

    
    

    
      
    

def listar_productos():
    print("-------Lista de productos --------")
    print(" ")
    print("-- Código ---- Descripción ----cantidad---- Precio ----")
    for key in productos:
        print(f"          { key} ->{ productos[key][0]} ->{ productos[key][1]} ---> { productos[key][2]} " )

    time.sleep(3)    
    

def quitar_productos():
    try:
        codpro = int(input("ingresa el código [100-999]: "))
        productos.pop(codpro)
    except ValueError:
        print("Ingresa un código entre [100-999]:")
        time.sleep(3)   
    except Exception:
        print("El código de producto ingresado no existe") 
        time.sleep(3)   
       
    
    


def contar_productos():
    totprod = 0
    print("------- Lista de productos --------")
    print(" ")
    print("-- Código ---- Descripción ---- Precio ----")
    for key in productos:
        print(f"{ key} ->{ productos[key][0]} -> {productos[key][1]}" )
        totprod = totprod + productos[key][1]

    print(f"Tenemos {totprod} productos")    
    time.sleep(3) 


def valorizar_productos():
    total = 0
    item_precio_cantidad = 0

    for key in productos:
        item_precio_cantidad = productos[key][1] * productos[key][2]
        total = (total + (item_precio_cantidad))
        print(f"{ key} ->{ productos[key][0]} -> { item_precio_cantidad }" )

    print(f"El monto total del inventario es: {total}" )
    time.sleep(3) 


menu()


