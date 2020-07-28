from orator.seeds import Seeder


class LectoresSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Lectores').insert({
            'lector_nombre': 'Reyner',
        })
