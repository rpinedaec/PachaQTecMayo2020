from orator.seeds import Seeder


class AutorTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('autores').insert({
            'nombre': 'Javier Santaolalla',
            'correo':'contratacion@javiersantaolalla.es',
        })
        self.db.table('autores').insert({
            'nombre': 'Santillana',
            'correo':'santillanaperu@santillana.com',
        })



