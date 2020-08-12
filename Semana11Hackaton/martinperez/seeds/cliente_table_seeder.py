from orator.seeds import Seeder


class ClienteTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('clientes').insert({
            'nombre': 'Martin Perez',
            'email': 'perez@hotmail.com',
            'telefono': '+51927248582'
        })

