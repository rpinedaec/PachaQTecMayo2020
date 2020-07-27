import Cliente
import Producto
import Metodo_pago
import Create_factura
import Select_factura

class Menu:
    def __init__(self,menu_name,option_name,option_number):
        self.menu_name=menu_name
        self.option_name=option_name
        self.option_number=option_number
    
    def show(self):
        a=26-len(f'Menu {self.menu_name}')
        print(':'*round(a/2)+f'MENU {self.menu_name}'+':'*round(a/2))
        y=len(self.option_name)
        print("")
        for x in range(1,y+1):
            a=len(self.option_name[x-1])+len(self.option_number[x-1])            
            print(self.option_name[x-1]+' '*(25-a)+'→ '+self.option_number[x-1])
        print("")
        r=True
        while r:
            ans=input("Respuesta: ")
            n=0
            for x in self.option_number:
                if(x==ans):
                    n=n+1
            if(ans=='9'):
                exit()
            elif(n>0):
                break
            else:
                print('Opción invalida, ingrese una opción valida')
        return ans
               
opt_nam_lst=['Factura','Mantenimiento','salir']
opt_num_lst=['1','2','9']
Menu_home=Menu('HOME',opt_nam_lst,opt_num_lst)

opt_namemant_lst=['Cliente','Producto','Metodo de pago','salir']
opt_nummant_lst=['1','2','3','9']
Menu_mant=Menu('MANTENIMIENTO',opt_namemant_lst,opt_nummant_lst)

opt_fac_name_lst=['Buscar','Agregar','salir']
opt_fac_num_lst=['1','2','9']
Menu_fac=Menu('FACTURA',opt_fac_name_lst,opt_fac_num_lst)

opt_clnt_name_lst=['Buscar','Agregar','Update','Eliminar','salir']
opt_clnt_num_lst=['1','2','3','4','9']
Menu_clnt=Menu('CLIENTE',opt_clnt_name_lst,opt_clnt_num_lst)

opt_prdct_name_lst=['Buscar','Agregar','Update','Eliminar','salir']
opt_prdct_num_lst=['1','2','3','4','9']
Menu_prdct=Menu('PRODUCTO',opt_prdct_name_lst,opt_prdct_num_lst)

opt_mtd_pg_name_lst=['Buscar','Agregar','Update','Eliminar','salir']
opt_mtd_pg_num_lst=['1','2','3','4','9']
Menu_mtd_pg=Menu('METODO DE PAGO',opt_mtd_pg_name_lst,opt_mtd_pg_num_lst)


do=True
while do:
    ans1=Menu_home.show()
    if(ans1=='1'): #Factura
        ans=Menu_fac.show()
        if(ans=='2'):
            #Create
            Create_factura.create_factura_detalle()
        elif(ans=='1'):
            #Select
            print("Ingrese el id de la factura:")
            id_factura=int(input("Respuesta: "))
            Select_factura.select_factura(id_factura)
    elif(ans1=='2'): #Mantenimiento
        ans=Menu_mant.show()
        if(ans=='1'): #Cliente
            ans=Menu_clnt.show()
            if(ans=='2'):
                # Create
                print("Ingrese lo siguientes datos:")
                DNI_cliente=input('DNI: ')
                Nombre_cliente=input('Nombre: ')
                Correo_cliente=input('Correo: ')
                Cliente.insert_cliente(DNI_cliente,Nombre_cliente,Correo_cliente)
            elif(ans=='1'):
                # Read
                print("Ingrese el DNI del cliente:")
                DNI_cliente=input("Respuesta: ")
                Cliente.select_cliente(DNI_cliente)
            elif(ans=='3'):
                #Update
                print("Ingrese el DNI del cliente que desea actulizar")
                DNI_cliente=input("Respuesta: ")
                print("Cual campo desea modifica? DNI(1), nombre(2), correo(3)")
                field=input("Respuesta: ")
                print("Ingrese el nuevo valor")
                new_value=input("Respuesta: ")
                if(field=='1'):
                    field='DNI_cliente' 
                elif(field=='2'):
                    field='nombre_cliente'
                elif(field=='3'):
                    field='correo_cliente'
                Cliente.update_cliente(field,new_value,DNI_cliente)
            elif(ans=='4'):
                # Delete
                print("Ingrese el DNI del cliente que desea eliminar:")
                DNI_cliente=input("Respuesta: ")
                Cliente.delete_cliente(DNI_cliente)
        if(ans=='2'): # Producto
            ans=Menu_prdct.show()
            if(ans=='2'):
                # Create
                print("Ingrese lo siguientes datos:")
                Nombre_producto=input('Nombre: ')
                Precio_producto=input('Precio: ')
                Producto.insert_producto(Nombre_producto,Precio_producto)
            elif(ans=='1'):
                # Read
                print("Ingrese el id del producto:")
                id_producto=input("Respuesta: ")
                Producto.select_producto(id_producto)
            elif(ans=='3'):
                #Update
                print("Ingrese el id del producto que desea actulizar")
                id_producto=input("Respuesta: ")
                print("Cual campo desea modifica? nombre(1), precio(2)")
                field=input("Respuesta: ")
                print("Ingrese el nuevo valor")
                new_value=input("Respuesta: ")
                if(field=='1'):
                    field='nombre_producto' 
                elif(field=='2'):
                    field='precio_producto'
                Producto.update_producto(field,new_value,id_producto)
            elif(ans=='4'):
                # Delete
                print("Ingrese el id del producto que desea eliminar:")
                id_producto=input("Respuesta: ")
                Producto.delete_producto(id_producto)
        if(ans=='3'): # Metodo_pago
            ans=Menu_mtd_pg.show()
            if(ans=='2'):
                # Create
                print("Ingrese lo siguientes datos:")
                Descripcion_metodo_pago=input('Descripción del metodo de pago: ')
                Metodo_pago.insert_metodo_pago(Descripcion_metodo_pago)
            elif(ans=='1'):
                # Read
                print("Ingrese el id del metodo de pago:")
                id_metodo_pago=input("Respuesta: ")
                Metodo_pago.select_metodo_pago(id_metodo_pago)
            elif(ans=='3'):
                #Update
                print("Ingrese el id del metodo de pago que desea actulizar")
                id_metodo_pago=input("Respuesta: ")
                print("Ingrese el nueva descripcion del metodo de pago:")
                new_value=input("Respuesta: ")
                Metodo_pago.update_metodo_pago(new_value,id_metodo_pago)
            elif(ans=='4'):
                # Delete
                print("Ingrese el id del metodo de pago que desea eliminar:")
                id_metodo_pago=input("Respuesta: ")
                Metodo_pago.delete_metodo_pago(id_metodo_pago)
    print("Desea volver al menu(m) o slair (9) del programa:")
    ans:input("Respuesta: ")
    if(ans=='m'):
        pass
    elif (ans=='9'):
        print("Hasta luego")
        do=False


