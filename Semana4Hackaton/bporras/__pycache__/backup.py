#funcion para buscar un objeto ya registrado segun atributo de clase y lista donde se almacena
def search(item,identify,lst):
    if len(lst) > 0:
        for i in lst:
            if getattr(i,identify) == item:
                return True
            else:
                return False
    else:
        return False
def addItem(classItem):
    while True:
        try:
            tempclassitem = classItem()
            dicAtributes = tempclassitem.__dict__
            for k,v in dicAtributes.items():
                setattr(tempclassitem,k,input(f'Ingrese "{k}" del {tempclassitem.name()}: '))
            return tempclassitem
            break
        except:
            break

def validateinput(value,min,max,typev):
    if isinstance(int(value),typev):
        if value >= min and value <= max:
            return [True,value]
        else:
            print(f'El valor ingresado debe ser de tipo {typev}, ser >= {min} y <= {max}')
            return [False,value]
    else:
        print(f'El valor ingresado debe ser de tipo {typev}')
        return [False,value]

def validatestr(value):
    if isinstance(value,typev):
        print("El valor ingresado es OK")
        return [True,value]
    else:
        print(f'El valor ingresado debe ser de tipo "str"')
        return [False,value]
