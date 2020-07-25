from orator.seeds import Seeder


class BibliotecaTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('bibliotecas').insert({
            'nombre': 'Sede principal',
            'direccion':'Av. Javier Prado',
            'documento':'Documento 1',
        })
        self.db.table('bibliotecas').insert({
            'nombre': 'Sede sur,
            'direccion':'Av.Alisos',
            'documento':'documento 2',
        })
