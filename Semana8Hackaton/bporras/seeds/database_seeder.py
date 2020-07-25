from orator.seeds import Seeder
from .autor_table_seeder import *
from .estado_libro_table_seeder import *

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AutorTableSeeder)
        self.call(EstadoLibroTableSeeder)