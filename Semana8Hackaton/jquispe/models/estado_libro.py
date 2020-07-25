#Para crear este modelo; se debe ejecutar en la línea de comando: orator make:model EstadoLibro
# Orator, reconoce todo como letras minusculas, por lo que se crea el archivo "estado_libro.py"
from orator import Model


class EstadoLibro(Model):
    #Designamos el nombre de la tabla como 'estadolibro'
    __table__='estadolibro'
