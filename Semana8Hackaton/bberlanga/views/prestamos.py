from models.prestamo import Prestamo
import orator
import utils.contenedor
from datetime import date
import models.user
from models.biblioteca import Biblioteca
import models.libro
import models.biblioteca
from utils.menu import color
import os

clear = lambda: os.system('cls')


class Modulo_prestamos:
    def __init__(self,conexion):
        self.conexion=conexion  

    def execute_modulo(self,ans):
        clear()
        if(ans=='1'):
            pass
            # print("Ingrese la información solicitada")
            # id_doc=input("Documento del usuario: ")
            # records=models.user.User.where('documento','=',id_doc).get()
            # for record in records:
            #     print(record.id)    
        elif(ans=='2'):
            print('Ingrese la informacion solicitada')
            id_doc_urs=input(color.BOLD+"Id documento del usuario: "+color.END)
            userconx=models.user.Users()
            run=True
            while run:
                try:
                    "user = db.table('users').where('name', 'John').pluck('name')"
                    record_urs=userconx.where('documento',id_doc_urs ).pluck('documento')
                    print(record_urs)
                    id_user=record_urs.id
                    break
                except Exception as error:
                    print(error)
                    print(color.BOLD+'Opcion incorrecta'+color.END)
                    
            clear()
            libroconx=models.libro.Libro
            records_libro=libroconx.all()
            record_list=[]
            for record in records_libro:
                record_dict={'Id libro':record.id,'Titulo':record.nombre,'ISBN':record.isbn}
                record_list.append(record_dict)
            utils.contenedor.contenedor(record_list)
            while run:
                try:
                    print("")
                    id_libro=input('Id libro: ')
                    libroconx.where('id',int(id_libro)).first()
                    break
                except:
                    print('Opcion incorrecta')
            clear()
            bibconx=models.biblioteca.Biblioteca
            records_bib=bibconx.all()
            bib_list=[]
            for record in records_bib:
                record_dict={'Id biblioteca':record.id,'Nombre de la biblioteca':record.nombre,'Dirección':record.direccion}
                bib_list.append(record_dict)
            utils.contenedor.contenedor(bib_list)
            run=True
            while run:
                try:
                    id_biblioteca=input(color.BOLD+"Id biblioteca: "+color.END)
                    bibconx.where('id',int(id_biblioteca)).first()
                    break
                except:
                    print('Opcion incorrecta')
            clear()
            print("Seguro que deseas agregar la siguiente información: ")
            ans=("Respuesta(Y/N): ")
            if(ans=='Y'):
                print("")                                
                prtconx=Prestamo()
                prtconx.user_id=id_user
                prtconx.libros_id=id_libro
                prtconx.prestado_on=date.today()
                prtconx.bibliotecas_id=id_biblioteca
                prtconx.save()
                print("Se registro el prestamo")           
        elif(ans=='3'):
            pass
        elif(ans=='4'):
            pass


