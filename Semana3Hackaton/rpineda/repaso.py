# var1 = "hola "
# var2 = 'otro string'
# print(var1 + var2)
# intvar1 = 22
# intvar2 = 33

# print(intvar1 + intvar2 - intvar1 * intvar2 / intvar1 ** intvar2)
# print(intvar1 + intvar2 - intvar1 * intvar2 // intvar1 ** intvar2)

# flvar1 = 44.5
# flvar2 = 0.9999999

# print(flvar1 + flvar2 - flvar1 * flvar2 / flvar1 ** flvar2)

# True
# False

# print(intvar1 == intvar2)
# print(intvar1 != intvar2)
# print(intvar1 > intvar2)
# print(intvar1 < intvar2)

tpl1 = (0,1,2,3,4,5,6,7)
tpl2 = (9,8,7,6,5,4,3,2,1,0)
# print(tpl1)
# print(tpl1[6])
# print(tpl2[3])

lst1 = ["uno","dos","tres"]

# print(lst1)
# lst1.append("cuatro")
# print(lst1)
# lst1.remove("dos")
# print(lst1)

dic1 = {
  "array": [
    1,
    2,
    3
  ],
  "boolean": True,
  "color": "gold",
  "null": None,
  "number": 123,
  "object": {
    "a": "b",
    "c": "d"
  },
  "string": "Hello World"
}
# print(dic1)
# dic1.update({"key3":"value3"})
# print(dic1)
# dic1.pop("key2")
# print(dic1)

# for iteracion in range(0,20,3):
#     print(iteracion)

# for tpl in tpl2:
#     print(tpl)

# for iteracion in lst1:
#     print(iteracion)

# for (key, value) in dic1.items():
#     print(key , " :: ", value )

# blvar = True
# itercionWh = 0
# while blvar:
#     itercionWh += 3
#     print(itercionWh)
#     if(itercionWh == 21):
#         #blvar = False
#         break
#     if(itercionWh == 20):
#         blvar = False


# strEdad = input("Ingrese su edad: ")
# intEdad = int(strEdad)
# res=intEdad / 2
# print(f"La mitad de tu edad es: {res}")

try:
    strEdad = input("Ingrese su edad: ")
    intEdad = int(strEdad)
    res=intEdad / 2
    res2 = 2 / intEdad
    print(f"La mitad de tu edad es: {res}")
    print(f"Otra operacion con tu edad es: {res2}")
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("no se puede convertir letras en numeros")
except ZeroDivisionError:
    print("ingresa unnumero mayor a 0")
except:
    print("Unexpected error:")
    raise
