import json
import os
list_clientes={"46934688":"Jorge Quispe","45782459":"Antonio Rojas"}
list_empleados={"jq001":"Jorge Quispe","ja001":"Junior Aquise"}
list_productos={"Leche Gloria 400 ml":[500,3.5],"Yogurt Gloria":[200,5.5]}
class producto():

    def __init__(self,nombre,cantidad,costo):
        self.nombre=nombre
        self.cantidad=cantidad
        self.costo=costo
    
    def validar_producto(self):
        if self.nombre in list_productos:
            print("El producto se encuentra registrado")
        else:
            print("El producto no se encuentra registrado")

    def agregar_producto(self):
        list_productos[nombre]=[cantidad,costo]
        print(list_productos)

    def quitar_producto(self):
        del list_productos[nombre]
        print(list_productos)

    def listar_producto(self):
        print(list_productos)

    def contar_producto(self):
        print("Se cuenta con: ",list_productos[nombre][0]," und")

    def valorizar_producto(self):
        print(int(list_productos[nombre][1]))
    
class persona():
    def __init__(self, nombre, ap_paterno):
        self.nombre=nombre
        self.ap_paterno=ap_paterno

#Se define la clase "empleado", la cual hereda los atributos de la clase persona.
class cliente(persona):
    
    def __init__(self,dni, nombre,ap_paterno):
        super().__init__(nombre,ap_paterno)
        self.dni=dni

    def validar_cliente(self):
        if self.dni in list_clientes:
            print("El cliente se encuentra registrado")
        else:
            print("El cliente no se encuentra registrado")
    
    def agregar_cliente(self):
        list_clientes[dni]=(nombre+" "+ap_paterno)
        print(list_clientes)
    
    def eliminar_cliente(self):
        del list_clientes[dni]
        print(list_clientes)

#Se define la clase "empleado", la cual hereda los atributos de la clase persona.
class empleado(persona):

    def __init__(self,codigo, nombre, ap_paterno):
        super().__init__(nombre, ap_paterno)
        self.codigo=codigo

    def validar_empleado(self):
        if self.codigo in list_empleados:
            print("El empleado se encuentra registrado")
        else:
            print("El empleado no se encuentra registrado")
    
    def agregar_empleado(self):
        list_empleados[codigo]=(nombre+" "+ap_paterno)
        print(list_empleados)

    def eliminar_empleado(self):
        del list_empleados[codigo]
        print(list_empleados)

#Se define la clase "archivo", la cual se editara, mostrara, entre otros.
class archivo():
    def __init__(self, nombre_archivo):
        self.nombre_archivo=nombre_archivo
    def mostrar_archivo(self):
        try:
            file=open(self.nombre_archivo,'r')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'error: {str(e)}')
        else:
            file.close()

persona=cliente(45782431,"Juan","Arteaga")
archivo=archivo("clientes.txt")
archivo.mostrar_archivo()

print("===========================")
print("PROGRAMA CARRITO DE TIENDAS")
print("===========================\n")
print("MENU DE OPCIONES\nEscoja una opción\n")
print("1. Clientes")
print("2. Empleados")
print("3. Productos\n")
opcion=int(input("Escriba su opción: "))

if opcion == 1:
    print("Escogio la opcion de Clientes\n")
    nombre=input("Nombre: ")
    ap_paterno=input("Apellido: ")
    dni=input("dni: ")
    cliente1=cliente(dni,nombre,ap_paterno)
    print("================")
    print("MENU DE CLIENTES\nEscoja una opción")
    print("================\n")
    print("1. Validar clientes")
    print("2. Agregar clientes")
    print("3. Eliminar clientes\n")
    opcion1=int(input("Ingrese su opción:"))

    if opcion1==1:
        print("Escogio la opcion de Validar clientes\n")
        cliente1.validar_cliente()
    elif opcion1==2:
        print("Escogio la opcion de Agregar clientes\n")
        cliente1.agregar_cliente()
    elif opcion1==3:
        print("Escogio la opcion de Eliminar clientes\n")
        cliente1.eliminar_cliente()

elif opcion == 2:
    print("Escogio la opcion de Empleados\n")

    nombre=input("Nombre: ")
    ap_paterno=input("Apellido: ")
    codigo=input("Codigo de empleado: ")
    empleado1=empleado(codigo,nombre,ap_paterno)
    
    print("=================")
    print("MENU DE EMPLEADOS\nEscoja una opción")
    print("=================\n")
    print("1. Validar empleados")
    print("2. Agregar empleados")
    print("3. Eliminar empleados\n")
    
    opcion1=int(input("Ingrese su opción:"))

    if opcion1==1:
        print("Escogio la opcion de Validar empleados\n")
        empleado1.validar_empleado()

    elif opcion1==2:
        print("Escogio la opcion de Agregar empleados\n")
        empleado1.agregar_empleado()

    elif opcion1==3:
        print("Escogio la opcion de Eliminar empleados\n")
        empleado1.eliminar_empleado()

elif opcion == 3:
    print("Escogio la opcion de Productos\n")
    
    nombre=input("Nombre del producto: ")
    cantidad=int(input("Cantidad: "))
    costo=float(input("Costo: "))
    producto1=producto(nombre,cantidad,costo)

    print("=================")
    print("MENU DE PRODUCTOS\nEscoja una opción")
    print("=================\n")
    print("1. Validar existencia de productos")
    print("2. Agregar productos")
    print("3. Quitar productos")
    print("4. Listar productos")
    print("5. Contar productos")
    print("6. Valorizar productos\n")
    
    opcion1=int(input("Ingrese su opción: "))
    
    if opcion1==1:
        print("Escogio la opcion de Validar existencia de productos\n")
        producto1.validar_producto()

    elif opcion1==2:
        print("Escogio la opcion de Agregar productos\n")
        producto1.agregar_producto()

    elif opcion1==3:
        print("Escogio la opcion de Quitar productos\n")
        producto1.quitar_producto()

    elif opcion1==4:
        print("Escogio la opcion de Listar productos\n")
        producto1.listar_producto()

    elif opcion1==5:
        print("Escogio la opcion de contar productos\n")
        producto1.contar_producto()
    
    elif opcion==6:
        print("Escogio la opcion de valorizar productos")
        producto1.valorizar_producto()
    
    else:
        print("fin")

print("\nFIN DEL PROGRAMA")