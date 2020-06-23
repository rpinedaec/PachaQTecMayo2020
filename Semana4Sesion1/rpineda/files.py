import os
import shutil

# directorioActual = os.getcwd()

# print(directorioActual)

# #os.makedirs("pchqtc")

# directorio = os.listdir("E:\\Users\\rpineda\\Documents\\LEADS")
# print(directorio)

# archivoACopiar = 'app.log'
# directorioDestino = "E:\\Users\\rpineda\\Documents\\LEADS"
# shutil.copy(archivoACopiar,directorioDestino)

try:
    file = open("archivoNuevo.txt", 'r')
    print(file.read())
except Exception as e:
    print(e)

try:
    file = open("archivoNuevo.txt", 'r')
    for lineas in file.readlines():
        print(f"Linea {lineas}")
except Exception as e:
    print(e)

# try:
#     file = open("archivoNuevo.txt", 'w')
#     file.write("Nueva linea")
# except Exception as e:
#     print(e)

try:
    file = open("archivoNuevo.txt", 'a')
    for i in range(1, 10, 1):
        file.write(f"Nueva linea desde for {i} con append de nuevo \n")

except Exception as e:
    print(e)
