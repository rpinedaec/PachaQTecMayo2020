<<<<<<< HEAD
#Diccionario
dicnuevo ={
    "clave1":1,
    "clave2":"string",
    "clave3":1.44,
    "clave4": True
}

print (dicnuevo)
=======
#string
"hola mundo"
#int
12
#float
13.66
#bool
True
False

#list

lstEnteros = [1,2,3,4,5,6]
["uno","dos","tres","cuatro"]
[12.4,14.5,16.7]
[True,True,False]
[1,"uno",12.6,True]
#Agregar nuevo elemento
print(lstEnteros)
lstEnteros.append(9)
print(lstEnteros)
lstEnteros.append("diez")
print(lstEnteros)
lstEnteros.remove(4)
print(lstEnteros)
lstEnteros.remove("diez")
print(lstEnteros)
#lstEnteros.remove(7) #no se puede por que no existe
#print(lstEnteros)
print(lstEnteros.index(5))
lstEnteros.pop()
print(lstEnteros)
lstEnteros.pop(2)
print(lstEnteros)
print(len(lstEnteros))
lstEnteros.extend([10,15])
print(lstEnteros)
#tuple
tplNumeros = (0,1,2,3,4,5,6,7,8,9)
print(tplNumeros)
tplMixto = ("Uno", 1, 1.01, True, "Uno",1,1,1)
print(tplMixto)
print(tplMixto.count(1))
tplNuevo = tuple(range(20,50))
print(tplNuevo)
#dict
dicNuevo ={
    "clave1":1,
    "clave2":"string",
    "clave3":1.44,
    "clave4":True,
    1:1
}
print (dicNuevo)
print(dicNuevo["clave3"])

>>>>>>> upstream/develop
