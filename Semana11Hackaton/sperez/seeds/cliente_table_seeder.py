from orator.seeds import Seeder


class ClienteTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('clientes').insert({
            'nombre': 'Sergio Perez',
            'email': 'john@doe.com',
            'telefono': '+51959364540'
        })

