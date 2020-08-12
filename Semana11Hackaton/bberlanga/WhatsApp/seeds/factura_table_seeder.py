from orator.seeds import Seeder


class FacturaTableSeeder(Seeder):

    def run(self):
        self.db.table('factura').insert({
            'fecha':'8/08/2020',
            'cliente_id':1,
            'sub_total':319.8,
            'IGV':70.2,
            'monto_total':390
        })


