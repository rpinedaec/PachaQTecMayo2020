import os
from time import sleep

class color:
    INDICT = '\33[33m'
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    

class Menu:
    def __init__(self,nombre,list_nom,list_num):
        self.nombre=nombre
        self.list_nom=list_nom
        self.list_num=list_num
    
    def show_menu(self):
        self.limpiarPantalla()
        show=True
        while show:            
            print(color.HEADER+":::::::::::::   BIBLIOTECA NACIONAL  ::::::::::::::"+color.END)
            n=len(self.nombre)+6
            x=round((51-n)/2)
            print(color.HEADER+":"*x+"   " +self.nombre + "   "+":"*x+color.END)
            print("")
            print(color.INDICT+"Ingrese la opcion que desea realizar"+color.END)
            print("")
            n=len(self.list_nom)
        #    log.logging.info(n)
            for x in range(n):
                s=20-len(self.list_nom[x])
                print(self.list_nom[x]+" "*s+color.OKGREEN+"➡ "+color.END+self.list_num[x])
            print("")
            print("-"*51)
            ans=input(color.BOLD+"Respuesta: "+color.END)
            v=0
            for x in self.list_num:
                if (ans==x):
                    v=v+1
            if(v>0):
                if(int(ans)<9):
                    break
                elif(ans=='9'):
                    exit()
            else:
                print(" ")
                print(color.WARNING+"Opcion invalida deben ser numeros segun el menu"+color.END)
                print(" ")
        return ans

    def limpiarPantalla(self):
        def clear():
            #return os.system('cls')
            return os.system('clear')
        clear()


# Menu_principal
lst_op_num_home=['1','2','3','9']
lst_op_nom_home=['Prestamos', 'Libros', 'Usuarios','Salir']
menu_home=Menu('Inicio',lst_op_nom_home,lst_op_num_home)

# Menu_libro
lst_op_num_libro=['1','2','3','4','9']
lst_op_nom_libro=['Buscar libro', 'Agregar libro', 'Actulizar información','Elimnar','Salir']
menu_libro=Menu('Repertorio de libros',lst_op_nom_libro,lst_op_num_libro)
# Menu_prestamos
lst_op_num_prts=['1','2','3','4','9']
lst_op_nom_prts=['Buscar prestamo', 'Agregar nuevo', 'Actulizar información','Elimnar','Salir']
menu_prestamo=Menu('Prestamos',lst_op_nom_prts,lst_op_num_prts)
# Menu_usuario
lst_op_num_usr=['1','2','3','4','9']
lst_op_nom_usr=['Buscar usuario', 'Agregar usuario', 'Actulizar información','Elimnar','Salir']
menu_usuario=Menu('Base de usuario',lst_op_nom_usr,lst_op_num_usr)
