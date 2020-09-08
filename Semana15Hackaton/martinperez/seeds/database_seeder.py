from orator.seeds import Seeder
from .marca_automovil_table_seeder import *
from .tipo_automovil_table_seeder import *


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(MarcaAutomovilTableSeeder)
        self.call(TipoAutomovilTableSeeder)

