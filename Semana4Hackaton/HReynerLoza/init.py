import json
import os 
import PySimpleGUI as sg
class Person:
    # Inicializamos la clase


    #identityNumber = DNI
    def __init__(self,namePerson,lastNamePerson,agePerson, identityNumberPerson):
        self.namePerson = namePerson
        self.lastNamePerson = lastNamePerson
        self.agePerson = agePerson
        self.identityNumberPerson = identityNumberPerson
        self.personObject = Person.transformToObject(namePerson = namePerson,lastname=lastNamePerson,agePerson=agePerson,identityNumberPerson=identityNumberPerson)
        

    #Constructores Alternativos
    # Ingreso de la forma Reyner-Loza-14-72673935
    @classmethod
    def createPersonbyStr(cls, oneString): #Reyner-Loza-14-72673935
        namePerson ,lastNamePerson, agePerson , identityNumberPerson = oneString.split('-')
        return cls(namePerson,lastNamePerson,int(agePerson),int(identityNumberPerson))

    # Ingreso de la forma en Lista [Reyner,LozA,13,72673935]
    @classmethod
    def createPersonByList (cls, lista): # [Reyner,loza,13,72673935]
        [namePerson,lastNamePerson, agePerson, identityNumberPerson] = lista
        return cls(namePerson,lastNamePerson,agePerson,identityNumberPerson)

    def transformToObject(**kwargs):
        return kwargs

    def updatePerson(self,namePerson,lastNamePerson,agePerson,identityNumberPerson,*args):
        self.namePerson = namePerson
        self.lastNamePerson = lastNamePerson
        self.agePerson = agePerson
        self.identityNumberPerson = identityNumberPerson
        self.personObject["namePerson"] = namePerson
        self.personObject["lastNamePerson"] = lastNamePerson
        self.personObject["agePerson"] = agePerson
        self.personObject["identityNumberPerson"] = identityNumberPerson






class Client(Person):


    

    def __init__(self,nameClient,lastNameClient,ageClient,identityNumberClient, codeClient) :
        super().__init__(nameClient,lastNameClient,ageClient,identityNumberClient)
        #Person.__init__(self,name,lastName,age,identityNumber)
        self.codeClient = codeClient

        data = {} # Leemos la data del archivo y agrega1mos un nuevo objeto cliente
        with open('Client.txt') as json_file:
            data = json.load(json_file)
        data[codeClient] = self.personObject
        with open('Client.txt', 'w') as outfile:
            json.dump(data,outfile)


    def writeClient(self):
        data = {}

        data['Client'] = self.personObject

        with open('Client.txt', 'w') as outfile:
            json.dump(data,outfile)


def showClients():
    data = {}
    with open('Client.txt') as json_file:
        data = json.load(json_file)
        #print(json.dumps(data,indent=4))
        print(json.dumps(data,indent=4))

def showProducts():
    data = {}
    with open('Product.txt') as json_file:
        data = json.load(json_file)
        #print(json.dumps(data,indent=4))
        print(json.dumps(data,indent=4))

def showEmployee():
    data = {}
    with open('Employee.txt') as json_file:
        data = json.load(json_file)
        print(json.dumps(data,indent=4))



def validateClient(codeClient):
    with open('Client.txt') as json_file:
        data = json.load(json_file)
        for p in data:
            if  p == codeClient:
                print("Elemento ya ingresado")
                return True

def validateProduct(codeProduct):
    with open('Product.txt') as json_file:
        data = json.load(json_file)
        for p in data:
            if  p == codeProduct:
                print("Elemento ya ingresado")
                return True


def validateEmployee(codeEmployee):
    with open('Employee.txt') as json_file:
        data = json.load(json_file)
        for p in data:
            if  p == codeEmployee:
                print("Elemento ya ingresado")
                return True


class Product :

    currencyValueDolarToPEN = 3.43 # Tipo de cambio de la moneda dolares a soles 
    

    def __init__(self,codeProduct,nameProduct,typeProduct,entryDateProduct,priceProduct,quantityProduct):
        self.codeProduct = codeProduct
        self.nameProduct = nameProduct
        self.typeProduct = typeProduct
        self.entryDateProduct = entryDateProduct
        self.priceProduct = priceProduct
        self.quantityProduct = quantityProduct
        self.productObject = Product.transformToObject(codeProduct = codeProduct, nameProduct = nameProduct, typeProduct = typeProduct, entryDateProduct = entryDateProduct, priceProduct=priceProduct,quantityProduct=quantityProduct ) # El Pylint lo manda como error pero si funciona
        data = {} # Leemos la data del archivo y agrega1mos un nuevo objeto cliente
        with open('Product.txt') as json_file:
            data = json.load(json_file)
        data[codeProduct] = self.productObject
        with open('Product.txt', 'w') as outfile:
            json.dump(data,outfile)


    @property
    def convertedValueToPEN(self):
        return self.valueProduct * Product.currencyValueDolarToPEN



    def transformToObject(**kwargs): ## Agrega un diccionario a nustro atributo de nuestra clae producto
        return kwargs

    @classmethod
    def createNoDict(cls,codeProduct,nameProduct,typeProduct,entryDateProduct,priceProduct,quantityProduct,valueProduct):
        return cls(codeProduct,nameProduct,typeProduct,entryDateProduct,priceProduct,quantityProduct,valueProduct)

    

class Employee(Person):
    def __init__(self,nameEmployee,lastNameEmployee,ageEmployee,identityNumberEmployee, codeEmployee):
        super().__init__(nameEmployee,lastNameEmployee,ageEmployee,identityNumberEmployee)
        self.codeEmployee = codeEmployee
        
        data = {} # Leemos la data del archivo y agrega1mos un nuevo objeto cliente
        with open('Employee.txt') as json_file:
            data = json.load(json_file)
        data[codeEmployee] = self.personObject # Agregamos el diccionario cada vez que se inicializa un instancia de Employee
        with open('Employee.txt', 'w') as outfile:
            json.dump(data,outfile)
        
  
    


######### Unca clase a futuro en el cual se maneja todas las compras, tendra como atributo un objeto Cliente, un Objeto Employeee y una Lista de atributos Products



# class Compra : 

#     def __init__(self,idShop,Client,Employee):

#         listProducts = []

#         self.shop = { 
#             "idShop": idShop,
#             "Client": ListClient,
#             "Employee": Employee,
#             "Products": listProducts
#         }

#     def addProduct(self,product):
#         self.shop["Products"].append(product)

#     def removeProductByCodeProduct(self,product,codeProduct):

#         if len(self.shop["Products"]) != 0 :
#             for value in range(self.shop["Products"]) :
#                 if self.shop["Products"][value].codeProduct == codeProduct : 
#                     self.shop["Products"].pop(value)
            
#         else:
#             return None
            


def createCliente():

    print("Valor 1 Ingresado")
    print("Se tiene la siguiente lista de valores ingresados. No repetir el mismo codigo")
    showClients()

                
    cliente = [
    [sg.Text('INGRESO DATOS CLIENTE ')],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('Apellido', size=(15, 1)), sg.InputText()],
    [sg.Text('Edad', size=(15, 1)), sg.InputText()],
    [sg.Text('DNI', size=(15, 1)), sg.InputText()],
    [sg.Text('CodigoCliente', size=(15, 1)), sg.InputText()],
    [sg.Submit('Submit'), sg.Cancel('Cancel')]
    ]
    windowCliente = sg.Window('HENNIO REYNER LOZA ', cliente)

    while True:
        eventCliente, valuesCliente = windowCliente.read()
        if eventCliente == sg.WIN_CLOSED or eventCliente == 'Cancel': # if user closes window or clicks cancel
            break
        elif eventCliente == 'Submit':
            if validateClient(valuesCliente[4]):
                print("Producto Ingresado¡¡ Intente de nuevo")
                
            else:
                print("Elemento Agregado")
                showClients()
                cliente = Client(valuesCliente[0],valuesCliente[1],int(valuesCliente[2]),int(valuesCliente[3]),int(valuesCliente[4])) # Internamente ya se agregó al TXT
                print(json.dumps(cliente.personObject,indent=4))
        windowCliente.close()

def createProducto():

    print("Valor 1 Ingresado")
    print("Se tiene la siguiente lista de valores ingresados. No repetir el mismo codigo")
    showProducts()

                
    producto = [
    [sg.Text('INGRESO DATOS PRODUCTO: ')],
    [sg.Text('CodigoProducto', size=(15, 1)), sg.InputText()],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('TipoProducto', size=(15, 1)), sg.InputText()],
    [sg.Text('FechaProducto', size=(15, 1)), sg.InputText()],
    [sg.Text('Precio de Producto', size=(15, 1)), sg.InputText()],
    [sg.Text('Cantidad del Producto', size=(15, 1)), sg.InputText()],
    [sg.Submit("Submit"), sg.Cancel("Cancel")]
    ]
    windowProducto = sg.Window('HENNIO REYNER LOZA ', producto)

    while True:
        eventProducto, valuesProducto = windowProducto.read()
        if eventProducto == sg.WIN_CLOSED or eventProducto == 'Cancel': # if user closes window or clicks cancel
            break
        elif eventProducto == 'Submit':
            if validateClient(valuesProducto[1]):
                print("Producto Ingresado¡¡ Intente de nuevo")
                
            else:
                print("Elemento Agregado")
                showProducts()
                producto = Product(valuesProducto[0],valuesProducto[1],valuesProducto[2],valuesProducto[3],float(valuesProducto[4]),int(valuesProducto[5])) # Internamente ya se agregó al TXT
                print(json.dumps(producto.productObject,indent=4))
        windowProducto.close()


def createEmployee():

    print("Valor 1 Ingresado")
    print("Se tiene la siguiente lista de valores ingresados. No repetir el mismo codigo")
    showEmployee()
    employee = [
    [sg.Text('INGRESO DATOS CLIENTE ')],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('Apellido', size=(15, 1)), sg.InputText()],
    [sg.Text('Edad', size=(15, 1)), sg.InputText()],
    [sg.Text('DNI', size=(15, 1)), sg.InputText()],
    [sg.Text('CodigoEmpleado', size=(15, 1)), sg.InputText()],
    [sg.Submit('Submit'), sg.Cancel('Cancel')]
    ]
    windowEmployee = sg.Window('HENNIO REYNER LOZA ', employee)

    while True:
        eventEmployee, valuesEmployee = windowEmployee.read()
        if eventEmployee == sg.WIN_CLOSED or eventEmployee == 'Cancel': # if user closes window or clicks cancel
            break
        elif eventEmployee == 'Submit':
            if validateEmployee(valuesEmployee[4]):
                print("Producto Ingresado¡¡ Intente de nuevo")
                
            else:
                print("Elemento Agregado")
                showEmployee()
                cliente = Client(valuesEmployee[0],valuesEmployee[1],int(valuesEmployee[2]),int(valuesEmployee[3]),int(valuesEmployee[4])) # Internamente ya se agregó al TXT
                print(json.dumps(cliente.personObject,indent=4))
        windowEmployee.close()




def main ():
        while True:
            print("Choose the next option:")
            print("1: Create Client")
            print("2: Create Product")
            print("3: Create Employee")
            print("4: Mostrar Productos")
            print("5: Salir")
            valueEntered = input("Ingrese el valor a escoger : \n")
            print("Valor Ingresado es : " + valueEntered)
            # sincronizamos nuestro remoto con nuestro diccionario local
            if valueEntered == "1":
                createCliente()

            elif valueEntered == "2":
                createProducto()
                input("Presione cualquier tecla para continuar")
            elif valueEntered == "3":
                createEmployee()
                input("Presione cualquier tecla para continuar")
            elif valueEntered == "4":
                showProducts()
                input("Presione cualquier tecla para continuar")

            elif valueEntered == "5":
                break



############################ Intento agregar un GUI pero no se termino de completar () #####################################

def gui () :
    
    sg.theme('Light Blue 2')   # Add a touch of color
    # All the stuff inside your window.
    
    #Layout Cliente

    principal = [
    [sg.Text('1. Crear Cliente ')],
    [sg.Text('2. Crear Producto ')],
    [sg.Text('3. Crear Trabajador ')],
    [sg.Text('4. Crear Compra ')],
    [sg.Text('Escoga Opcion', size=(15, 1)), sg.InputText()],
    [sg.Submit('Submit'), sg.Cancel('Cancel')]
    ]


    cliente = [
    [sg.Text('INGRESO DATOS CLIENTE ')],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('Apellido', size=(15, 1)), sg.InputText()],
    [sg.Text('Edad', size=(15, 1)), sg.InputText()],
    [sg.Text('DNI', size=(15, 1)), sg.InputText()],
    [sg.Text('CodigoCliente', size=(15, 1)), sg.InputText()],
    [sg.Submit('Submit'), sg.Cancel('Cancel')]
    ]

    #layout Employee
    trabajador = [
    [sg.Text('INGRESO DATOS TRABAJADOR: ')],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('Apellido', size=(15, 1)), sg.InputText()],
    [sg.Text('Edad', size=(15, 1)), sg.InputText()],
    [sg.Text('DNI', size=(15, 1)), sg.InputText()],
    [sg.Text('Codigo Empleado', size=(15, 1)), sg.InputText()],
    [sg.Submit('Submit'), sg.Cancel('Cancel')]
    ]

    producto = [
    [sg.Text('INGRESO DATOS PRODUCTO: ')],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('Apellido', size=(15, 1)), sg.InputText()],
    [sg.Text('Edad', size=(15, 1)), sg.InputText()],
    [sg.Text('DNI', size=(15, 1)), sg.InputText()],
    [sg.Text('Codigo Producto', size=(15, 1)), sg.InputText()],
    [sg.Submit("Submit"), sg.Cancel("Cancel")]
    ]


    # Create the Window
    #windowPrincipal = sg.Window('HENNIO REYNER LOZA ', principal)
    windowCliente = sg.Window('HENNIO REYNER LOZA ', cliente)
    windowProducto = sg.Window('HENNIO REYNER LOZA ', producto)
    #sg.Print("", do_not_reroute_stdout=False)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        print("Menu Principal")
        windowPrincipal = sg.Window('HENNIO REYNER LOZA ', principal)
        eventPrincipal, valuesPrincipal = windowPrincipal.read()
        if eventPrincipal == sg.WIN_CLOSED or eventPrincipal == 'Cancel': # if user closes window or clicks cancel
            break
        elif eventPrincipal == "Submit":
            windowPrincipal.close()
            if valuesPrincipal[0] == "1":
                print("Valor 1 Ingresado")
                print("Se tiene la siguiente lista de valores ingresados")
                showClients()
                eventCliente, valuesCliente = windowCliente.read(close = False)
                if eventCliente == sg.WIN_CLOSED or eventCliente == 'Cancel': # if user closes window or clicks cancel
                    break
                else: 
                    # Mostramos los clientes ya ingresados
                    if validateClient(valuesCliente[4]):
                        pass
                    else:
                        print("Elemento Agregado")
                        
                        cliente = Client(valuesCliente[0],valuesCliente[1],int(valuesCliente[2]),int(valuesCliente[3]),int(valuesCliente[4])) # Internamente ya se agregó al TXT
                        print(json.dumps(cliente.personObject,indent=4))

                eventCliente, valuesCliente = windowCliente.read(close = False)

        
        
    


if __name__ == '__main__': 
    main()





     
     