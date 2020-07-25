from orator.seeds import Seeder


class BibliotecaTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Biblioteca').insert({
            'Nombre_Biblioteca': 'Biblioteca Nacional del Peru',
            'Direccion': 'Av. De la Poesía 160, San Borja'
        })
        self.db.table('Biblioteca').insert({
            'Nombre_Biblioteca': 'Gran Biblioteca Pública de Lima',
            'Direccion': 'Av. Abancay 4ta. Cdra. s/n Lima 01'
        })
