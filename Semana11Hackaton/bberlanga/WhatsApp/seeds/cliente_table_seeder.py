from orator.seeds import Seeder

class ClienteTableSeeder(Seeder):
    def run(self):
        self.db.table('cliente').insert({
            'nombre': 'john',
            'correo': 'joshn@doe.com',
            'número_telefonico':'+5194051001'
        })

