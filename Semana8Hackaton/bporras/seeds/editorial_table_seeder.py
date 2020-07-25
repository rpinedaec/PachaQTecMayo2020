from orator.seeds import Seeder


class EditorialTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('editoriales').insert({
            'nombre': 'Norma',
            'correo':'editorialnorma@correo.com',
            'dirección':'Lima-Peru',
        })
        self.db.table('editoriales').insert({
            'nombre': 'INKA',
            'correo':'editorialinka@correo.com',
            'dirección': 'cuzco-peru',
        })

