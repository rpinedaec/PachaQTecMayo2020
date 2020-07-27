from orator.seeds import Seeder


class BibliotecasTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('bibliotecas').insert({
            'nombre': 'Biblioteca Nacional',
            'direccion':'San Borja'
        })
        self.db.table('bibliotecas').insert({
            'nombre': 'Biblioteca Nacional',
            'direccion':'Centro de Lima'
        })

