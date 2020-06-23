import os
# directorioActual = os.getcwd()
# print(directorioActual)

# CREACION DE CARPETA
# os.makedirs("pachaqtecMPerez")

# Lista todos los archivos en el directorio actual
# directorio = os.listdir(".")
# print(directorio)


import shutil
# Copiar un archivo de una carpeta a otra
# archivoACopiar = "archivocopiado.txt"
# directorioDestino = "E:\\BACKEND-PAQ\\git-repositorio2\\PachaQTecMayo2020\\Semana4Sesion1\\martinperez\\pachaqtecMPerez"
# shutil.copy(archivoACopiar,directorioDestino)



#try:
#    #file = open("archivonuevo.txt",'r')
#    file = open("archivocopiado.txt",'r')    
#    print(file.read())
#except Exception as e:
#    print("error: ",str(e))
#else:
#    file.close()



# try: 
#     file = open("archivocopiado.txt",'r')    
#     for lineas in file.readlines():
#         print(f"linea {lineas}")
#     print(file.read())
# except Exception as e:
#     print("error: ",str(e))
# else:
#     file.close()





# try: 
#     file = open("archivocopiado.txt",'w')
#     file.write("Nueva linea")
#     file = open("archivocopiado.txt",'r')
#     for lineas in file.readlines():
#          print(f"linea {lineas}")
# except Exception as e:
#     print("error: ",str(e))
# else:
#     file.close()


#  try: 
#      file = open("archivocopiado.txt",'w') 
#      for i in range(1,10,1):
#          file.write(f"Nueva Linea de for2222 -  {i} \n")
#  except Exception as e:
#      print("error: ",str(e))
#  else:
#      file.close()


try: 
    file = open("archivocopiado.txt",'a') 
    for i in range(1,10,1):
        file.write(f"Nueva Linea de for2222 -  {i} \n")
except Exception as e:
    print("error: ",str(e))
else:
    file.close()

