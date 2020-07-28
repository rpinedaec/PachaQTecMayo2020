from orator.seeds import Seeder
from .estado_user_table_seeder import *
from .autor_table_seeder import *
from .estado_libro_table_seeder import *
from .tipo_documento_table_seeder import *
from .biblioteca import *
from .libro import *
from .user import *

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(EstadoUserTableSeeder)
        self.call(AutorTableSeeder)
        self.call(EstadoLibroTableSeeder)
        self.call(TipoDocumentoTableSeeder)
        self.call(BibliotecaSeeder)
        self.call(LibroSeeder)
        self.call(UserSeeder)