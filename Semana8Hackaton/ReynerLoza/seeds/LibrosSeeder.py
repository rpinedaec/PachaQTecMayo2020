from orator.seeds import Seeder


class LibrosSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Libros').insert({
            'libro_nombre': 'Python Book',
            'libro_author': 'Carlos Vasquez',
            'estado': 0,
            'prestamo_id':1
        })

