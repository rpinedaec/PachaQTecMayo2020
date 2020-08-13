from orator.seeds import Seeder


class PedidoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('pedidos').insert({
            'ubicacion': 'geo:37.787890,-122.391664|375 Beale St',
            'cliente_id':1,
            'producto_id':1            
        })
