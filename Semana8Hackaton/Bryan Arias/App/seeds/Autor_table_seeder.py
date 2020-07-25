from orator.seeds import Seeder


class AutorTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Autor').insert({
            'Nombre_Autor': 'Ian Sommerville',
            'Correo': 'sommerville@gmail.com'
        })
        self.db.table('Autor').insert({
            'Nombre_Autor': 'Fidias Arias',
            'Correo': 'fidias20@hotmail.com'
        })
        self.db.table('Autor').insert({
            'Nombre_Autor': 'Roger Pressman',
            'Correo': 'pressman@hotmail.com'
        })

