#Clase de productos
#Ferreteria --> Artivulos = Items = Productos
#Nombre, Codigo, UnidaMedida, Color, Modelo, Precio
#Venderlos, Comprar, AsignarDescuento, Desechar
#Vendido/Disponible, Disponible en tienda, Averiado, Activo/Inactivo, Nuevo/Usado, EnTransito

#Nombre:    Cemento     --> Cemento
# Cod:      A001        --> A002
# UM:       Kg          --> Bolsa
#Color:     Blanco      --> Gris
#Marca:     Sol         --> Pacasmayo
#Precio:    10          --> 15

#Comprar / Vender

#Clase de personas
#Atributos
    #Nombre
    #Apellido
    #Estatura
    #Peso
    #Sexo
    #DNI
    #FechaNacimiento
#Funciones
    #Comprar
    #Devolver
    #Consultar
    #Reclamar
    #Robar
    #Atender
#Estados ==> Tipos de usuario
    #Activo
    #Inactivo

class Personas():
    Nombre = "Roberto"
    Apellido = "Pineda"
    Estatura = 1.69
    Peso = 75
    Genero = "M"
    DNI = 71206364
    Edad = 36
    TipoUsuario = "Vendedor"
    def vender():
        pass
    def consultar():
        pass
    


persona_1 = Personas()
print(persona_1.Nombre)