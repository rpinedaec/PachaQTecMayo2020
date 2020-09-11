from orator.seeds import Seeder


class TipoAutomovilTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('tipo').insert({
            'descripcion' : 'Monovolumen', 
            'activo' : 1
        })
        self.db.table('tipo').insert({
            'descripcion' : 'Berlina', 
            'activo' : 1
        })
        self.db.table('tipo').insert({
            'descripcion' : 'sedan', 
            'activo' : 1
        })

        self.db.table('tipo').insert({
            'descripcion' : 'Cupe', 
            'activo' : 1
        })

        self.db.table('tipo').insert({
            'descripcion' : 'Hatchback', 
            'activo' : 1
        })

        self.db.table('tipo').insert({
            'descripcion' : 'Descapotable', 
            'activo' : 1
        })

        self.db.table('tipo').insert({
            'descripcion' : 'Roadster', 
            'activo' : 1
        })

        self.db.table('tipo').insert({
            'descripcion' : 'Familiar', 
            'activo' : 1
        })


        self.db.table('tipo').insert({
            'descripcion' : 'Todoterreno', 
            'activo' : 1
        })


        self.db.table('tipo').insert({
            'descripcion' : 'Crossover', 
            'activo' : 1
        })


        self.db.table('tipo').insert({
            'descripcion' : 'SUV Vehículo Deportivo Utilitario', 
            'activo' : 1
        })


        self.db.table('tipo').insert({
            'descripcion' : 'Deportivos', 
            'activo' : 1
        })


        self.db.table('tipo').insert({
            'descripcion' : 'Pick-up', 
            'activo' : 1
        })

