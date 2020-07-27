from orator.seeds import Seeder
from .Autor_table_seeder import *
from .Biblioteca_table_seeder import *
from .Editorial_table_seeder import *
from .Libro_Autor_table_seeder import *
from .Libro_table_seeder import *
from .Tipo_Documento_table_seeder import *
from .Libro_Biblioteca_table_seeder import *



class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AutorTableSeeder)
        self.call(BibliotecaTableSeeder)
        self.call(EditorialTableSeeder)
        self.call(LibroTableSeeder)
        self.call(TipoDocumentoTableSeeder)
        self.call(LibroAutorTableSeeder)
        self.call(LibroBibliotecaTableSeeder)

