from orator.seeds import Seeder


class EstadolibroTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('estadolibro').insert({
            'descripcion': 'D'
        })
        self.db.table('estadolibro').insert({
            'descripcion': 'R'
        })
        self.db.table('estadolibro').insert({
            'descripcion': 'P'
        })

