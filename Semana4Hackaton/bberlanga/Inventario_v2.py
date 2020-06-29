import os
import utils
import json


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
#----------------------------------------------------------------------------------


class person:
    def __init__(self, name, last_name, age, id_num):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.id_num = id_num


class client(person):
    def __init__(self, name, last_name, age, id_num, client_cod, client_type):
        super().__init__(name, last_name, age, id_num)
        self.client_cod = client_cod
        self.client_type = client_type

    def toDic(self):
        d = {
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "id_num": self.id_num,
            "client_cod": self.client_cod,
            "client_type": self.client_type
        }
        return d


class emplpoyee(person):
    def __init__(self, name, las_name, age, id_num, employee_cod, area):
        super().__init__(name, las_name, age, id_num)
        self.employee_cod = employee_cod
        self.area = area


class product:
    def __init__(self, name, price, enter_date, quantity):
        self.name = name
        self.price = price
        self.enter_date = enter_date
        self.quantity = quantity


class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("")
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.name.upper()+"::::::::::::::::::::"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(key+color.GREEN+" → "+color.END+value)
            print("")
            ans = input(
                color.YELLOW+"Por favor, ingrese su opción: "+color.END)
            print("")
            if(ans.upper() == "0"):
                print("Hasta, pronto")
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
        return ans

    def limpiarPantalla(self):
        def clear():
                #return os.system('cls')
            return os.system('clear')
        clear()
#----------------------------------------------------------------------------------
#Menus
Home_op = {"Clientes":"1","Empleados":"2","Exit":"0"}
Main_menu = Menu("home",Home_op)

Client_op = {"Agregar cliente":"1","Lista de clientes":"2","Remover cliente":"3","Back":"<","Exit":"0"}
Menu_client = Menu("cliente",Client_op,"Main_menu")

Employee_op = {"Horas de trabajo":"1","Inventario":"2","Back":"<","Exit":"0"}
Menu_Employee = Menu("trabajador",Employee_op,"Main_menu")

Inventory_op = {"Agregar producto":"1","Consulta":"2","Remover producto":"3","Back":"<","Exit":"0"}
Menu_Inventory = Menu("inventario",Inventory_op,"Menu_Employee")

Inventory_consult_op = {"Buscar producto":"1","Contar items":"2","Calcular valor del inventario":"3","Back":"<","Exit":"0"}
Consult_inv = Menu("consulta de inventario",Inventory_consult_op,"Menu_Inventory")

Working_hrs_op = {"Check-in":"1","Check-out":"2","Back":"<","Exit":"0"}
Working_hrs = Menu("horas trabajadas",Working_hrs_op,"Menu_Employee")

#----------------------------------------------------------------------------------
client_list = []
product_list = []
client_listDic = []
fileCliente = utils.fileManager("cliente.txt")

def cargainicial():
    res = fileCliente.leerArchivo()
    print(res)
    listTempCliente = json.loads(res)
    for dic in listTempCliente:
        newCliente = client(dic["name"],dic["last_name"],dic["age"],dic["id_num"], dic["client_cod"],dic["client_type"])
        client_list.append(newCliente)
#----------------------------------------------------------------------------------
cargainicial()
f = True
while f:
    ans = Main_menu.show()
#Clients
    if (ans.upper() =="1"):
        ans = Menu_client.show()
        #Add client
        if(ans.upper() =="1"):
            a = True
            while a:
                print("")
                print("Ingrese la información del cliente:")
                Name = input("Nombre del cliente     : ")
                Last_name = input("Apellido del cliente: ")
                Age = input("Edad del cliente:")
                Id_num = input("Id del cliente:")
                Client_cod = input("Código del cliente     :")
                Client_type = input("Nivel de fidelidad       :")
                print("")
                o = True
                while o:
                    print(f"Esta seguro que desea agregar al cliente {Name} a lista de clientes? (Y/N)")
                    ans = input(color.YELLOW+"Answer: "+color.END)
                    if(ans.upper() =="Y"):
                        client_n = client(Name,Last_name,Age,Id_num,Client_cod,Client_type)
                        client_list.append(client_n)
                        print("")
                        print(color.GREEN+f"{Name} fue agregado ☑"+color.END)
                        client_listDic.append(client_n.toDic())
                        jsonString = json.dumps(client_listDic)
                        fileCliente.borrarArchivo()

                        fileCliente.escribirArchivo(jsonString)
                        break
                    elif(ans.upper() =="N"):                  
                        print("")
                        break
                    else:
                        print("")
                        print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                        print("")
                r = True
                while r:
                    print("Desea agregar otro cliente? (Y/N)")
                    ans = input(color.YELLOW+"Answer: "+color.END)
                    if (ans.upper() =="Y"):
                        break
                    elif(ans.upper() =="N"):
                        p = True
                        while p:
                            print("")
                            print("Desea ir al menu o salir del programa? (M/0)")
                            ans = input(color.YELLOW+"Answer: "+color.END)
                            if(ans.upper() =="M"):
                                r = False
                                a = False
                                break
                            elif (ans.upper() =="0"):
                                r = False
                                a = False
                                f = False                                
                                break
                            else:
                                print("")
                                print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                                print("")
                    else:
                        print("")
                        print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                        print("")

        #View client list
        elif(ans.upper() =="2"):
            print(color.GREEN+"Esta es la lista de clientes ☑:"+color.END)
            for client in client_list:
                print(f"|{client.name}|{client.last_name}|{client.age}|{client.id_num}|{client.client_cod}|{client.client_type}|")
            g = True
            while g:
                print("")
                print("Desea ir al menu o salir del programa? (M/0)")
                ans = input(color.YELLOW+"Answer: "+color.END)
                if(ans.upper() =="M"):
                    g = False
                    break
                elif(ans.upper() =="0"):
                    g = False
                    f = False
                    break
                else:
                    print("")
                    print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                    print("")

        #Remove client
        elif(ans.upper() =="3"):
            s = True
            while s:
                print("Escoja in el numero del cliente que desea remover de la lista:")
                n = 0
                for client in client_list:
                    n = n+1
                    print(f"|{client.name}|{client.last_name}|{client.age}|{client.id_num}|{client.client_cod}|{client.client_type}|"+color.GREEN+"→"+color.END+str(n))
                u = True
                while u:
                    try:
                        ans_remove = input(color.YELLOW+"Answer: "+color.END)
                        if(int(ans_remove) <=n)and(int(ans_remove)>0):
                            break
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
                    except:
                        print("")
                        print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                        print("")
                b = True
                while b:
                    print("Esta seguro que desea remover el cliente seleccionado? (Y/N)")
                    ans = input(color.YELLOW+"Answer: "+color.END)
                    if (ans.upper() =="Y"):
                        print("")
                        del client_list[int(ans_remove)-1]
                        client_listDic.remove(int(ans_remove)-1)
                        jsonString = json.dumps(client_listDic)
                        
                        fileCliente.borrarArchivo()
                        fileCliente.escribirArchivo(jsonString)
                        print(color.GREEN+"El cliente fue removido ☑"+color.END)
                        break
                    elif (ans.upper() =="N"):
                        break
                    else:
                        print("")
                        print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                        print("")
                v = True
                while v:
                    print("")
                    print("Desearía remover otro cliente? (Y/N)")
                    ans = input(color.YELLOW+"Answer: "+color.END)
                    if(ans.upper() =="Y"):
                        break
                    elif(ans.upper() =="N"):
                        r = True
                        while r:
                            print("")
                            print("Desea ir al menu o salir del programa? (M/0)")
                            ans = input(color.YELLOW+"Answer: "+color.END)
                            if(ans.upper() =="M"):
                                s = False
                                v = False
                                break
                            elif (ans.upper() =="0"):
                                f = False
                                s = False
                                v = False
                                break
                            else:
                                print("")
                                print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                                print("")
                    else:
                        print("")
                        print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                        print("")

#Employee
    elif (ans.upper() =="2"):
        ans = Menu_Employee.show()
        if (ans.upper() =="1"):
            Working_hrs.show()
        elif (ans.upper() =="2"):
            ans = Menu_Inventory.show()
            #Add product
            if (ans.upper() =="1"):
                k = True
                while k:
                    print("")
                    print("Ingrese la información del producto:")
                    Name = input("Nombre del producto: ")
                    Price = input("Precio del producto: ")
                    Enter_date = input("Fecha de ingreso: ")
                    Quantity = input("Cantidad: ")
                    print("")
                    i = True
                    while i:
                        print(f"Esta seguro que desea agregar el producto {Name} a la lista? (Y/N)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if(ans.upper() =="Y"):
                            product_n = product(Name,Price,Enter_date,Quantity)
                            product_list.append(product_n)
                            print("")
                            print(color.GREEN+f"Producto {Name} fue agregado ☑"+color.END)
                            print("")
                            product_dict={"name":product_n.name,"las_name":product_n.price,"age":product_n.enter_date,"id_num":Quantity}
                            dict_me_json=json.dumps(product_dict)
                            path=os.getcwd()+"\\Semana4Hackaton\\bberlanga\\product.txt"
                            try:
                                open(path,'a').write("'"+dict_me_json+"'"+"\n")
                            except:
                                open(path,'w').write("'"+dict_me_json+"'")                                     
                            break
                        elif(ans.upper() =="N"):
                            break
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
                    t = True
                    while t:
                        print("Desearía agregar otro porducto? (Y/N)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if(ans.upper() =="Y"):
                            break
                        if(ans.upper() =="N"):
                            r = True
                            while r:
                                print("Desea ir al menu o salir del programa? (M/0)")
                                ans = input(color.YELLOW+"Answer: "+color.END)
                                if(ans.upper() =="M"):
                                    t = False
                                    k = False
                                    break
                                elif(ans.upper() =="0"):
                                    f = False
                                    t = False
                                    k = False
                                    break
                                else:
                                    print("")
                                    print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                                    print("")
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
            #Consult product
            elif (ans.upper() =="2"):
                ans = Consult_inv.show()
                #View product list
                if (ans.upper() =="1"):
                    print("Esta es la lista de productos:")
                    for product in product_list:
                        print(f"|{product.name}|{product.price}|{product.enter_date}|{product.quantity}|")
                    o = True
                    while o:
                        print("Desea ir al menu o salir del programa? (M/0)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if(ans.upper() =="M"):
                            break
                        elif(ans.upper() =="0"):
                            f = False
                            break
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
                #Calculate number of items
                elif (ans.upper() =="2"):
                    print(color.GREEN+"El número de items es de:"+color.END)
                    n = 0
                    for product in product_list:
                        n = n+float(product.quantity)
                    print(color.GREEN+str(n)+color.END)
                    o = True
                    while o:
                        print("Desea ir al menu o salir del programa? (M/0)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if(ans.upper() =="M"):
                            break
                        elif(ans.upper() =="0"):
                            f = False
                            break
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
                #Calculate inventory value
                elif (ans.upper() =="3"):
                    print("")
                    print(color.GREEN+"El valor de inventario es de:"+color.END)
                    n = 0
                    for product in product_list:
                        n = n+float(product.price)
                    print(color.GREEN+str(n)+color.END)
                    print("")
                    o = True
                    while o:
                        print("Desea ir al menu o salir del programa? (M/0)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if(ans.upper() =="M"):
                            break
                        elif(ans.upper() =="0"):
                            f = False
                            break
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
            #Remove product
            elif (ans.upper() =="3"):
                s = True
                while s:
                    print("Escoja el número del producto que desea remover:")
                    n = 0
                    for product in product_list:
                        n = n+1
                        print(f"|{product.name}|{product.price}|{product.enter_date}|{product.quantity}|"+color.GREEN+"→"+color.END+str(n))
                    u = True
                    while u:
                        try:
                            ans_remove = input(color.YELLOW+"Answer: "+color.END)
                            if(int(ans_remove) <=n)and(int(ans_remove)>0):
                                break
                            else:
                                print("")
                                print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                                print("")
                        except:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
                    b = True
                    while b:
                        print("Esta seguro que desea remover el producto seleccionado? (Y/N)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if (ans.upper() =="Y"):
                            print("")
                            del product_list[int(ans_remove)-1]
                            print(color.GREEN+"El producto due removido ☑"+color.END)
                            break
                        elif (ans.upper() =="N"):
                            break
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
                    v = True
                    while v:
                        print("")
                        print("Desearía remover otro producto? (Y/N)")
                        ans = input(color.YELLOW+"Answer: "+color.END)
                        if(ans.upper() =="Y"):
                            break
                        elif(ans.upper() =="N"):
                            r = True
                            while r:
                                print("")
                                print("Desea ir al menu o salir del programa? (M/0)")
                                ans = input(color.YELLOW+"Answer: "+color.END)
                                if(ans.upper() =="M"):
                                    s = False
                                    v = False
                                    break
                                elif (ans.upper() =="0"):
                                    f = False
                                    s = False
                                    v = False
                                    break
                                else:
                                    print("")
                                    print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                                    print("")
                        else:
                            print("")
                            print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                            print("")
#----------------------------------------------------------------------------------
