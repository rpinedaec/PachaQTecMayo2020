from orator.seeds import Seeder


class ProductoTableSeeder(Seeder):
    def run(self):
        self.db.table('producto').insert({
            'nombre': 'Zapatillas-tennis',
            'precio': 390      
        })


