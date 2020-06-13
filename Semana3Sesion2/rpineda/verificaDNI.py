import consultaDNI
#Programa para verfificar el DNI
print("Hola dame tu numero de DNI")
strDNIIngresado = input()
print("Ahora dame tu digito verificador")
strDigitoIngresado = input()

print(f"Tu dni es {strDNIIngresado} y tu nro verificador es {strDigitoIngresado}")

intResultadoVerificacion = consultaDNI.verificaDNI(strDNIIngresado)
intDigitoIngresado = int(strDigitoIngresado)
if(intResultadoVerificacion == intDigitoIngresado):
    print("Perfecto tu DNI es correcto y real")
else:
    print("Te equivocaste")
