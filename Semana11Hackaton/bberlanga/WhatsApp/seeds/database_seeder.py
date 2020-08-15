from orator.seeds import Seeder
from .cliente_table_seeder import ClienteTableSeeder
from .detalle_factura_table_seeder import DetalleFacturaTableSeeder
from .factura_table_seeder import FacturaTableSeeder
from .producto_table_seeder import ProductoTableSeeder
from .pedido_table_seeder import PedidoTableSeeder



class DatabaseSeeder(Seeder):
    def run(self):
        self.call(ClienteTableSeeder)
        self.call(ProductoTableSeeder)
        self.call(FacturaTableSeeder)
        self.call(DetalleFacturaTableSeeder)
        self.call(PedidoTableSeeder)


