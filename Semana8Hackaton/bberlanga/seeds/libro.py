from orator.seeds import Seeder
from orator.orm import Factory


class LibroSeeder(Seeder):
    def run (self):
        """
        Run the database seeds.
        """
        self.db.table('libros').insert({
            'nombre': 'Harry Potter y el Caliz de Fuego',
            'isbn': '10381KJHBJ',
            'autor_id': '1',
            'estado_libro_id':'1'
        })

        self.db.table('libros').insert({
            'nombre': 'Robison Crusoe',
            'isbn': '32241KJHBJ',
            'autor_id': '2',
            'estado_libro_id':'1'
        })

        self.db.table('libros').insert({
            'nombre': 'El Viaje del Celta',
            'isbn': '563erHBJ',
            'autor_id': '2',
            'estado_libro_id':'1'
        })    