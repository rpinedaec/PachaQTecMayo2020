#EJEMPLO DE HERENCIA SIMPLE SIN super()
class Padre(object):                                #Creamos la clase "Padre"
    def __init__(self, ojos, cejas):                #Define los atributos de la clase, __init__ es un constructor y se usa cuando hay muchos atributos en la clase para no repetirlos
        self.ojos = ojos                            #Define a "ojos"
        self.cejas = cejas                          #Define a "cejas"

class Hijo(Padre):                                  #Se crea la clase "Hijo" que hereda de "Padre"
    def __init__(self, ojos, cejas, cara):          #Se crea el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas)           #Se especifica la clase y se llama a su constructor y SUS atributos (Linea 3)
        self.cara = cara                            #Se especifica el nuevo atributo del "Hijo" que es "cara"

Tomas = Hijo('negros', 'bacanes', 'redonda')        #Se le atribuye "Tomas" a "Hijo" y se le pone adjetivos a los atributos en el mismo orden
print(Tomas.ojos, Tomas.cejas, Tomas.cara)          #Se pide mostrar los: "Ojos.de.Tomas", "Cejas.de.Tomas", "Cara.de.Tomas"

#********************************************************************************
#EJEMPLO DE HERENCIA CON super()

class Agregarelemento(list):
    def append(self, alumno):
        print(("Añadido el alumno"), (alumno))
        super().append(alumno)
Lista1 = Agregarelemento()
Lista1.append('Papo')
print(Lista1)
