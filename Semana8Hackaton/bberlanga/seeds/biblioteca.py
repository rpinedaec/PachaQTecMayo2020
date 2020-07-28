from orator.seeds import Seeder


class BibliotecaSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('bibliotecas').insert({
            'nombre': 'Abraham Valdelor',
            'direccion':'La Molina',
        })
        self.db.table('bibliotecas').insert({
            'nombre': 'Jorge Basadre',
            'direccion':'Miraflores',
        })        
        self.db.table('bibliotecas').insert({
            'nombre': 'Ricardo Palma',
            'direccion':'Surco',
        })    
        self.db.table('bibliotecas').insert({
            'nombre': 'Mario Vargas Llosa',
            'direccion':'La Victoria',
        })    
