from orator.seeds import Seeder


class ProductoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('productos').insert({
            'nombre': 'SSD 256GB'            
        })

