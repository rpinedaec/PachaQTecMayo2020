db=[{'id':1343,'name':'Braulio','last name':'Berlanga'},{'id':233,'name':'Carlos','last name':'Miranda'},{'id':345,'name':'Esteban','last name':'Suarez'},{'id':233,'name':'Diego','last name':'Flores'}]

class color:
    Yellow = '\033[33m'
    Blue = '\033[94m'
    Grenn = '\033[92m'
    ENDC = '\033[0m'
    
def contenedor(db):
    rcd_list=len(db)
    rcd_dict=len(db[0])
    char_list=[]
    for x in range(rcd_dict):
        key=list(db[0].keys())[x]
        max_len=[]
        for i in range(rcd_list):
            char=len(str(db[i-1][key]))
            max_len.append(char)
        max_len.append(len(key))
        char_list.append(max(max_len))
    
    top=""
    body=""
    for y in range(rcd_dict):
        key=list(db[x].keys())[y]
        factor=char_list[y]-len(str(key))          
        top=top+"{}{}".format('-'*char_list[y],'+')
        body=body+"{}{}{}".format(color.Yellow+key.upper()+color.ENDC," "*factor,'|')
    print('+'+top)
    print('|'+body)
 
    for x in range(rcd_list):
        top=""
        body=""
        for y in range(rcd_dict):
            value=list(db[x].values())[y]
            factor=char_list[y]-len(str(value))          
            top=top+"{}{}".format('-'*char_list[y],'+')
            body=body+"{}{}{}".format(value," "*factor,'|')
        print('+'+top)
        print('|'+body)
    print('+'+top)

contenedor(db)
