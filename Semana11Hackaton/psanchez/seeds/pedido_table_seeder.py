from orator.seeds import Seeder


class PedidoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('pedidos').insert({
            'ubicacion': 'geo:-12.067174,-77.035878|IDAT',
            'cliente_id':1,
            'producto_id':1            
        })