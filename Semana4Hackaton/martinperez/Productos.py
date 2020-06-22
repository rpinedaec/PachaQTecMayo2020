class Producto:
    def __init__(self, codigo, marca, peso, modelo, almacen):
        self.codigo = codigo
        self.marca = marca
        self.peso = peso
        self.modelo = modelo
        self.almacen = almacen



Cemento = Producto("A001","Sol",20,"Premier",10)

print(Cemento.peso)
Cemento.peso = 300
print(Cemento.peso)

pos = Producto("1","SITPEY", 0.2002,'Standar',11)



print(pos.marca)
pos.marca = "PERUANO"
print(pos.marca)


