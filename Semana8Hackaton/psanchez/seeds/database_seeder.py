from orator.seeds import Seeder
from .estadousuario_table_seeder import *
from .autor_table_seeder import *
from .estadolibro_table_seeder import *
from .tipodedocumento_table_seeder import *

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(EstadousuarioTableSeeder)
        self.call(AutorTableSeeder)
        self.call(EstadolibroTableSeeder)
        self.call(TipodedocumentoTableSeeder)

