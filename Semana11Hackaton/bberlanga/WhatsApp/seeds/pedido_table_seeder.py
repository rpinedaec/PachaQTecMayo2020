from orator.seeds import Seeder


class PedidoTableSeeder(Seeder):

    def run(self):
        self.db.table('pedido').insert({
            'cliente_id':1,
            'factura_id':1,
            'fecha_despacho':'8/08/2020',
            'fecha_entrega':'12/08/2020',
            'estado':'0'
        })
 

