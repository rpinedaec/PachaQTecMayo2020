class Person:
    # Inicializamos la clase

    numberPerson = 0 

    #identityNumber = DNI
    def __init__(self,namePerson,lastNamePerson,agePerson, identityNumberPerson):
        self.namePerson = namePerson
        self.lastNamePerson = lastNamePerson
        self.agePerson = agePerson
        self.identityNumberPerson = identityNumberPerson
        Person.numberPerson += 1 

    #Constructores Alternativos
    # Ingreso de la forma Reyner-Loza-14-72673935
    @classmethod
    def createPersonbyStr(cls, oneString): #Reyner-Loza-14-72673935
        namePerson ,lastNamePerson, agePerson , identityNumberPerson = oneString.split('-')
        return cls(namePerson,lastNamePerson,int(agPerson),int(identityNumberPerson))

    # Ingreso de la forma en Lista [Reyner,LozA,13,72673935]
    @classmethod
    def createPersonByList (cls, lista): # [Reyner,loza,13,72673935]
        [namePerson,lastNamePerson, agePerson, identityNumberPerson] = lista
        return cls(namePerson,lastNamePerson,agePerson,identityNumberPerson)


class Client(Person):
    numberClients = 0 

    def __init__(self,nameClient,lastNameClient,ageClient,identityNumberClient, codeClient, productsClient=None) :
        super().__init__(nameClient,lastNameClient,ageClient,identityNumberClient)
        #Person.__init__(self,name,lastName,age,identityNumber)
        self.codeClient = codeClient
        if productsClient == None :
            self.productsClient = [] 
        else:
            self.productsClient = productsClient

    
    def dictClient(self):
        return {
            'nameClient' = self.nameClient,
            'lastNameClient' = self.lastNameClient,
            'ageClient' = self.ageClient,
            'identityNumberClient' =self.identityNumberClient,
            'productsClient' = self.productsClient

        }

class Product :

    currencyValueDolarToPEN = 3.43 # Tipo de cambio de la moneda dolares a soles 
    numberProducts = 0 

    #def __init__(self,nameProduct,typeProduct,entryDateProduct,priceProduct,quantityProduct,valueProduct,)
    def __init__(self,ObjectProduct):
        self.nameProduct = ObjectProduct["nameProduct"]
        self.typeProduct = ObjectProduct["typeProduct"]
        self.entryDateProduct = ObjectProduct["entryDateProduct"]
        self.priceProduct = ObjectProduct["priceProduct"]
        self.quantityProduct = ObjectProduct["quantityProduct"]
        self.valueProduct = ObjectProduct["valueProduct"]



    @property
    def convertedValueToPEN(self):
        return valueProduct * Product.currencyValueDolarToPEN


    def dictProduct (self):
        return {

            'nameProduct' = self.nameProduct,
            'typeProduct' = self.typeProduct,
            'entryDateProduct' = self.entryDateProduct, 
            'priceProduct' = self.priceProduct,
            'quantityProduct' = self.quantityProduct,
            'valueProduct' = self.valueProduct
        }

    @classmethod
    def createNoDict(cls,nameProduct,typeProduct,entryDateProduct,priceProduct,quantityProduct,valueProduct):
        return cls(nameProduct,typeProduct,entryDateProduct,priceProduct,quantityProduct,valueProduct)

    

class Employee(Person):

    def __init__(self,nameEmployee,lastNameEmployee,ageEmployee,identityNumberEmployee, codeEmployee) :
        super().__init__(nameEmployee,lastNameEmployee,ageEmployee,identityNumberEmployee)
        self.codeEmployee

    def dictEmployee (Self)


    
