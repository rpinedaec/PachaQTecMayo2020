from orator.seeds import Seeder


class LibroAutorTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Detalle_Libro_Autor').insert({
            'idAutor': '1',
            'idLibro': '2'
        })
        self.db.table('Detalle_Libro_Autor').insert({
            'idAutor': '2',
            'idLibro': '3'
        })
        self.db.table('Detalle_Libro_Autor').insert({
            'idAutor': '3',
            'idLibro': '1'
        })

