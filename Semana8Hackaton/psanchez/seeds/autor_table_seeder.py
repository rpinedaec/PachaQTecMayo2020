from orator.seeds import Seeder


class AutorTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('autor').insert({
            'nombre': 'Javier Santaolalla',
            'correo':'contratacion@javiersantaolalla.es',
            'tipo':'Autor'
        })
        self.db.table('autor').insert({
            'nombre': 'Santillana',
            'correo':'santillanaperu@santillana.com',
            'tipo':'Editorial'
        })

