from orator.seeds import Seeder
from .cliente_table_seeder import ClienteTableSeeder
from .pedido_table_seeder import PedidoTableSeeder
from .producto_table_seeder import ProductoTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(ClienteTableSeeder)
        self.call(ProductoTableSeeder)
        self.call(PedidoTableSeeder)
