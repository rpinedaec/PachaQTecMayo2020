from orator.migrations import Migration


class CreatePrestamosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('prestamos') as table:
            table.increments('id')
            table.integer('usuario_id').unsigned()
            table.foreign('usuario_id').references('id').on('usuario')
            table.integer('libros_id').unsigned()
            table.foreign('libros_id').references('id').on('libros')
            table.date('prestado_on')
            table.integer('biblioteca_id').unsigned()
            table.foreign('biblioteca_id').references('id').on('biblioteca')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('prestamos')
