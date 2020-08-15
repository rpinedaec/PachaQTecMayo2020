from orator.seeds import Seeder


class ClienteTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('clientes').insert({
            'nombre': 'Jorge Quispe',
            'email': 'jquispeg@gmail.com',
            'telefono': '+51997572739'
        })

