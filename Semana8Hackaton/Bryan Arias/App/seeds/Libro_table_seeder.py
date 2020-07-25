from orator.seeds import Seeder


class LibroTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Libro').insert({
            'idEditorial': '1',
            'Nombre_Libro': 'INGENIERIA DEL SOFTWARE',
            'ISBN': '978-607-15-0314-5'
        })
        self.db.table('Libro').insert({
             'idEditorial': '2',
            'Nombre_Libro': 'INGENIERIA DEL SOFTWARE',
            'ISBN': '978-607-32-0603-7'
        })
        self.db.table('Libro').insert({
             'idEditorial': '3',
            'Nombre_Libro': 'EL PROYECTO DE INVESTIGACION',
            'ISBN': '980-07-8529-9'
        })

