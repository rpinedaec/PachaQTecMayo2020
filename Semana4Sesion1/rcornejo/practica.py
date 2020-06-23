class Persona:
    programa = "Pachaqtec" #Variable global
    #__programa = "Pachaqtec" #Variable privada
    
#     dni = "46247351"
#     nombres = "Ricardo"
#     apellidos = "Cornejo Villacorta"
#     sexo = "M"
    
# persona = Persona()

# print(persona.dni, persona.nombres)

    def __init__(self, dni, nombres, apellidos, sexo):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.sexo = sexo
           
persona_1 = Persona("46247351", "Ricardo", "Cornejo Villacorta", "M")
print(persona_1.programa)