from orator.seeds import Seeder


class AutorTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('autors').insert({
            'nombre': 'Javier Santaolalla',
            'correo':'contratacion@javiersantaolalla.es',
            'tipo':'Autor'
        })
        self.db.table('autors').insert({
            'nombre': 'Santillana',
            'correo':'santillanaperu@santillana.com',
            'tipo':'Editorial'
        })
