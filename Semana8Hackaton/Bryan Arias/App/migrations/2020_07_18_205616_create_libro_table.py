from orator.migrations import Migration


class CreateLibroTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Libro') as table:
            table.increments('idLibro')
            table.integer('idEditorial').unsigned()
            table.string('Nombre_Libro', 40)
            table.string('ISBN', 20)
            table.foreign('idEditorial').references('idEditorial').on('Editorial')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Libro')
