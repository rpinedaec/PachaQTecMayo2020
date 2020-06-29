import clase
#Programa para verificar DNI - Capa de Presentacion
print("Ingresa tu numero de DNI")
strDNIIngresado=input()
print("Ahora dame tu digito verificador")
strDigitoIngresado=input()
print(f"Tu DNI es {strDNIIngresado} y tu nro verificador es {strDigitoIngresado}")

intResultadoVerificacion=verificaDNI.clase(strDNIIngresado)
intDigitoIngresado=int(strDigitoIngresado)
if(intResultadoVerificacion==strDigitoIngresado):
   print("Perfecto tu DNI es correcto y real")
else:
    print("Te equivocaste")