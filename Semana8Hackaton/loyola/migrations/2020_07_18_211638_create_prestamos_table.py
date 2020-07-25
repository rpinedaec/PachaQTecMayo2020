from orator.migrations import Migration


class CreatePrestamosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('prestamos') as table:
            table.increments('id')
            table.integer('users_id').unsigned()
            table.foreign('users_id').references('id').on('users')
            table.integer('libros_id').unsigned()
            table.foreign('libros_id').references('id').on('libros')
            table.date('prestado_on')
            table.integer('bibliotecas_id').unsigned()
            table.foreign('bibliotecas_id').references('id').on('bibliotecas')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('prestamos')
