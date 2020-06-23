class Productos:
    def __init__(self, codigo, marca, peso, modelo, almacen):
        self.codigo = codigo
        self.marca = marca
        self.peso = peso
        self.modelo = modelo
        self.almacen = almacen


cemento = Productos("A001", "Sol", 20, "Premier", 10)
print(cemento.peso)
cemento.peso = 30
print(cemento.peso)


pos = Productos("1", "SITPEY", 0.200, "Smart", "Urbano")

print(pos.marca)
pos.marca = "AAAAAA"
print(pos.marca)
