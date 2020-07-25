from orator.seeds import Seeder


class EditorialTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Editorial').insert({
            'Nombre_Editorial': 'MCGRAW-HILL'
        })
        self.db.table('Editorial').insert({
            'Nombre_Editorial': 'PEARSON'
        })
        self.db.table('Editorial').insert({
            'Nombre_Editorial': 'EPISTEME'
        })



