#listas
'''
enteros = [1,2,3,4,5,6,7]
flotantes = [1.2,5.9,88.8,10.5]
cadenas = ["hola", "soy", "una","cadena"]
booleanos = [True,False]
Chanfainita = [1,"string", 5.5, True]

print(Chanfainita)
# agregar valor a una lista
Chanfainita.append("agregado")
print(Chanfainita)
#elimar un valor d euna lista
Chanfainita.remove("agregado")
print(Chanfainita)
#devuelve la posición del valor buscado
print(Chanfainita.index(5.5))
# eliminar un elemento segun su posición
Chanfainita.pop(0)
print(Chanfainita)
#saber longitud de una lista
print(len(Chanfainita))
#extender una lista ingresando otra lista
Chanfainita.extend(["otro valor",10])
print(Chanfainita)

'''
'''
#tuplas
enteros =(1,2,3,4,5,6,7,8,10,10)
# buscar cuantas veces se repite un elemento dentro de la tupla
print(enteros.count(10))
#crear tupla en unr ago definido
newtupla=tuple(range(1,51))
print(newtupla)
'''
#diccionarios

