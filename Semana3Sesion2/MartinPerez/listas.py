## string
#"Hola mundo"
##int
#12
##float
#13.66982
##bool
#True
#False


#listas     ---> modificables.
lstEnteros = [1,2,3,4,5,6,7]
["uno","dos","tres","cuatro","cinco"]
[12.5,25.9,35.5,45.01]
[True,True,False,False,True,True,False,True]
[1,"uno",12.9,True]
#Agregar nuevo elemento
print(lstEnteros)
lstEnteros.append(8)
print(lstEnteros)
lstEnteros.append("nueve")
print(lstEnteros)
lstEnteros.remove(1)
print(lstEnteros)
lstEnteros.remove("nueve")
print(lstEnteros)
print(lstEnteros[3])    #valor
print(lstEnteros.index(5)) # posicion
lstEnteros.pop(2) # recibe el indice y elimina el valor
print(lstEnteros)
print(len(lstEnteros)) # cantidad de valores
lstEnteros.extend([11,15])
print(lstEnteros)




#tuple  ---> se declara y no se puede cambiar.
tplNumeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(tplNumeros)
tplMixto = ("Uno", 1, 1.01, "Uno", True)
print(tplMixto)
print(tplMixto.count(1))
tplNuevo = tuple(range(20,29))
print(tplNuevo)

#dict  -->  diccionario
dicNuevo = {
    "clave1":1,
    "clave2":"texto",
    "clave3":15.5,
    "clave4":True
}
print(dicNuevo)
print(dicNuevo["clave2"])

