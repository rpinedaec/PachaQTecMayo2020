from orator.seeds import Seeder


class TipodedocumentoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('tipodedocumento').insert({
            'descripcion': 'DNI'
        })
        self.db.table('tipodedocumento').insert({
            'descripcion': 'CE'
        })
        self.db.table('tipodedocumento').insert({
            'descripcion': 'Carnet Biblioteca'
        })

