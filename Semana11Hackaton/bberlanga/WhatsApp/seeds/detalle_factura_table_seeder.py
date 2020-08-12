from orator.seeds import Seeder


class DetalleFacturaTableSeeder(Seeder):

    def run(self):
        self.db.table('detalle_factura').insert({
            'factura_id':1,            
            'cantidad':1,
            'sub_total':319.80,
            'IGV':70.20,
            'monto_total':390
        })



