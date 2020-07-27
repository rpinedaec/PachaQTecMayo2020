from orator.seeds import Seeder


class TipoDocumentoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Tipo_Documento').insert({
            'Descripcion': 'DNI'
        })
        self.db.table('Tipo_Documento').insert({
            'Descripcion': 'Libreta Electoral'
        })
        self.db.table('Tipo_Documento').insert({
            'Descripcion': 'Carne Biblioteca'
        })
