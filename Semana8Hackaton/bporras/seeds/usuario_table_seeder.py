from orator.seeds import Seeder


class UsuarioTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('usuarios').insert({
            'nombre': 'Juan Soto',
            'correo':'juansoto@gmail.com',
            'documento': 'documento 1',
        })
        self.db.table('usuarios').insert({
            'nombre': 'Raul Solir',
            'correo':'raulsolis@gmail.com',
            'documento': 'documento 2',
        })
