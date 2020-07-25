#Para crear este modelo; se debe ejecutar en la línea de comando: orator make:model TipoDocumento
# Orator, reconoce todo como letras minusculas, por lo que se crea el archivo "tipo_documento.py"
from orator import Model


class TipoDocumento(Model):
    #Nombraremos la tabla como tipodocumento
    __table__='tipodocumento'
