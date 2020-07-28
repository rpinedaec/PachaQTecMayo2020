from orator.seeds import Seeder


class UserSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('users').insert({
            'nombre': 'Braulio Berlanga',
            'correo': 'braber@gmail.com',
            'tipo_documento_id': '1',
            'documento': '00739839',
            'estado_user_id': '2'
        })
        self.db.table('users').insert({
            'nombre': 'Manuel Sanchez',
            'correo': 'manu_san@gmail.com',
            'tipo_documento_id': '3',
            'documento': '2323454',
            'estado_user_id': '1'
        })
        self.db.table('users').insert({
            'nombre': 'Carla Rmirez',
            'correo': 'kram@gmail.com',
            'tipo_documento_id': '3',
            'documento': '32435454',
            'estado_user_id': '3'
        })
        self.db.table('users').insert({
            'nombre': 'Gloria Salas',
            'correo': 'gloriasalas@gmail.com',
            'tipo_documento_id': '4',
            'documento': '93493484',
            'estado_user_id': '1'
        })
