#Para crear este modelo; se debe ejecutar en la línea de comando: orator make:model EstadoUser
# Orator, reconoce todo como letras minusculas, por lo que se crea el archivo "estado_user.py"
from orator import Model


class EstadoUser(Model):
    #nombraremos la tabla como 'estadouser'
    __table__='estadouser'