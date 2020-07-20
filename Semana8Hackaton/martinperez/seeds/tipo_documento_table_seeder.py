from orator.seeds import Seeder


class TipoDocumentoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('tipodocumento').insert({
            'descripcion' : 'DNI'
        })
        self.db.table('tipodocumento').insert({
            'descripcion' : 'RUC'
        })
        self.db.table('tipodocumento').insert({
            'descripcion' : 'Carnet de Estranjeria'
        })
        self.db.table('tipodocumento').insert({
            'descripcion' : 'Carnet de Biblioteca'
        })

