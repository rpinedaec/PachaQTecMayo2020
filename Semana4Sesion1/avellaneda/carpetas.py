import os
import shutil

directorioActual = os.getcwd()
print(directorioActual)
    #CREA UNA CARPETA EN EL DIRECTORIO EN EL QUE SE ENCUENTRE EL SISTEMA
os.makedirs("carpetaspython")
    #MUESTRA UNA LISTA DE LOS ELEMENTOS QUE ESTÁN EN EL DIRECTORIO
directorio = os.listdir(".")
print(directorio)

archivoACopiar = 'app.log'
directorioDestino = "/home/ricardo/Escritorio/Pacha-Q-Tec/PachaQTecMayo2020"
shutil.copy(archivoACopiar, directorioDestino)

try:
    file = open("archivoNuevo.txt", 'w')
    print(file.read())
except Exception as e:
    print(e)
