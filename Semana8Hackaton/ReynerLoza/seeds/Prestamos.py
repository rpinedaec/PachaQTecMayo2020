from orator.seeds import Seeder


class Prestamos(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Prestamos').insert({
            'prestamo_id': 1,
            'lector_id':  1

        })

