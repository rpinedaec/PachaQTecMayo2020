from orator.seeds import Seeder
from .estado_user_table_seeder import *
from .autor_table_seeder import *
from .estado_libro_table_seeder import *
from .tipo_documento_table_seeder import *

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(EstadoUserTableSeeder)
        self.call(AutorTableSeeder)
        self.call(EstadoLibroTableSeeder)
        self.call(TipoDocumentoTableSeeder)


