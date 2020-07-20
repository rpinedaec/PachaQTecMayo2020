#Programa para verificar el DNI
def clase(dni):
   strDNI="dni"
   tplDNI=tuple(strDNI)
   tplSerie=(3,2,7,6,5,4,3,2)
   intProducto=0
   intSumaProducto=0
   for i in range(0,len(tplDNI)):
        intProducto=int(tplDNI[i])*tplSerie[i]
        intSumaProducto+=intProducto
    intrestpProducto=intSumaProducto%11
    intMenos11=11-intrestpProducto
    tplListaReniec=(6,7,8,9,0,1,1,2,3,4,5)
    intDigitoVerificador=tplListaReniec[intMenos11]
    return intDigitoVerificador

