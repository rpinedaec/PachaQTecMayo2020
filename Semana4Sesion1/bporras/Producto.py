class Producto:
    def __init__(self,codigo,marca,peso,modelo,almacen):
        self.codigo = codigo
        self.marca = marca
        self.peso = peso
        self.modelo = modelo
        self.almacen = almacen

producto_1 = Producto("A001","Andino",20,"anti salitre",10)
producto_2 = Producto("A002","Sol",20,"Premium",10)
print(producto_1.marca)
print(producto_2.marca)