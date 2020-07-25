from orator.seeds import Seeder


class EstadoUserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('estadouser').insert({
            'descripcion': 'Activo'
        })
        self.db.table('estadouser').insert({
            'descripcion': 'Inactivo'
        })
        self.db.table('estadouser').insert({
            'descripcion': 'Pendiente Aprobacion'
        })

