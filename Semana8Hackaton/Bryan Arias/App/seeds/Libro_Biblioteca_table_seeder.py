from orator.seeds import Seeder


class LibroBibliotecaTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Detalle_Libro_Biblioteca').insert({
            'idLibro': '2',
            'idBiblioteca': '1',
            'cantidad': '3'
        })
        self.db.table('Detalle_Libro_Biblioteca').insert({
            'idLibro': '3',
            'idBiblioteca': '1',
            'cantidad': '2'
        })
        self.db.table('Detalle_Libro_Biblioteca').insert({
            'idLibro': '1',
            'idBiblioteca': '1',
            'cantidad': '2'
        })
        self.db.table('Detalle_Libro_Biblioteca').insert({
            'idLibro': '3',
            'idBiblioteca': '2',
            'cantidad': '1'
        })
        self.db.table('Detalle_Libro_Biblioteca').insert({
            'idLibro': '1',
            'idBiblioteca': '2',
            'cantidad': '3'
        })


