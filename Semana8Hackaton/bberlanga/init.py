import utils.menu
from utils.menu import color
import conex
import views.prestamos

prestamos=views.prestamos.Modulo_prestamos(conex.connec())

#Programm starts

ans=utils.menu.menu_home.show_menu()

run=True
while run:
    if(ans=='1'):
        ans=utils.menu.menu_prestamo.show_menu()
        prestamos.execute_modulo(ans)

    elif(ans=='2'):
        ans=utils.menu.menu_libro.show_menu()
        pass
    elif(ans=='3'):
        ans=utils.menu.menu_usuario.show_menu()
    elif(ans=='9'):
        run = False
    print(" ")
    print("Desea volver al menu (m) o salir(9) del programa ")
    t=True
    while t:
        ans=input("Respuesta: ")
        if(ans=='9'):
            r=False
            break
        elif(ans=='m'):            
            break
        else:
            print(" ")
            print(color.WARNING+"Opcion invalida deben ser numeros segun el menu"+color.END)
            print(" ")  

