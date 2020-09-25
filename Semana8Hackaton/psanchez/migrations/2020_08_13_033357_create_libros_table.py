from orator.migrations import Migration


class CreateLibrosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('libros') as table:
            table.increments('id')
            table.string('nombre')
            table.string('isbn')
            table.integer('autor_id').unsigned()
            table.foreign('autor_id').references('id').on('autor')
            table.integer('estadolibro_id').unsigned()
            table.foreign('estadolibro_id').references('id').on('estadolibro')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('libros')
