strDNI="71206364"
tplDNI=tuple(strDNI)
tplSerie=(3,2,7,6,5,4,3,2)
intproducto=[]
intsuma=0
tplreniec=(6,7,8,9,0,1,1,2,3,4,5)
for i in range(0,len(tplDNI)):
    intproducto = (int(tplDNI[i])*int(tplSerie[i]))
    intsuma += intproducto
intresiduo = intsuma %11
intindex = (11-intresiduo)
digitoverificador=tplreniec[intindex]
print(digitoverificador)