from orator.seeds import Seeder


class EstadoLibroTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('estadolibro').insert({
            'descripcion': 'Disponible'
        })
        self.db.table('estadolibro').insert({
            'descripcion': 'Reservado'
        })
        self.db.table('estadolibro').insert({
            'descripcion': 'Prestado'
        })

