class Productos:
    def __init__(self, dicProd):
        self.dicProductos = dicProd
        
    
    def verificarProducto(self,cod):
        existe = self.dicProductos.get(cod, -1)
        return(existe)
        