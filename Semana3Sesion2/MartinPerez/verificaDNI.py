import consultaDNI
#Programa para verificar el DNI
print("Hola dame tu numero de DNI")
strDNIIngresado = input()
print("Ahora dame tu digito verificador")
strDigitoIngresado = input()
#print(f"Tu dni es {strDNIIngresado} y tu número verificador"
#    +f" es {strDigitoIngresado}")

strDigitoVerificado=consultaDNI.verificaDNI(strDNIIngresado)
print("----------------------------------------")
print(strDigitoIngresado)
print(strDigitoVerificado)
#print(consultaDNI.verificaDNI('45049685'))

if strDigitoVerificado==strDigitoIngresado:
    print("Perfecto tu DNI es correcto y real")
else:
    print("Te equivocaste.")


