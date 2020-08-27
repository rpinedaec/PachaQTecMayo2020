from orator.seeds import Seeder


class ClienteTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('clientes').insert({
            'nombre': 'jacqui barreto',
            'email': 'jacqui@doe.com',
            'telefono': '+51992787417'
        })

