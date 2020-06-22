def validateinput(value,min,max,typev):
    if value >= min and value <= max:
        if isinstance(value,typev):
            print("El valor ingresado es OK")
            return True
        else:
            print(f'El valor ingresado debe ser de tipo "{typev}"')
            return False
    else:
        print(f'El valor ingresado debe ser de tipo {typev}, ser >= {min} y <= {max}')
        return False

value = validateinput(10.1,0,10,float)

