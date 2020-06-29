
def verificaDNI(dni):
    #strDNI = '45049685'
    strDNI = dni
    tplDNI = tuple(strDNI)
    #print(tplDNI)
    tplSerie=(3, 2, 7, 6, 5, 4, 3, 2)
    #print(tplSerie)
    #print(len(tplDNI))
    intProducto = 0
    intSumaProducto = 0
    for i in range(0,len(tplDNI)):
        #print(type(tplDNI[i]))
        #print(i, strDNI[i])
        #print(i, tplSerie[i])
        intProducto = int(tplDNI[i]) * tplSerie[i]
        #print(intProducto)
        intSumaProducto = intSumaProducto + intProducto
    #print(intSumaProducto)
    intRestoProducto = intSumaProducto%11
    #print(intRestoProducto)
    intMenos11 = 11-intRestoProducto
    #print(intMenos11)
    tplListaReniec = (6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5)
    #print(intValorMasUno)
    #print(tplListaReniec[intMenos11])
    intDigitoVerificador = tplListaReniec[intMenos11]
    #print(intDigitoVerificador)
    return intDigitoVerificador

