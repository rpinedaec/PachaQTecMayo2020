import consultaDNI
strdni=input("Ingrese su número de DNI: ")
Strnumever=input("Ingrese su número verificador: ")
NumeroDNI=consultaDNI.verificaDNI(strdni)
if NumeroDNI == int(Strnumever):
    print("Su número verificador es correcto")
else :
    print("Su número verificador es incorrecto")
