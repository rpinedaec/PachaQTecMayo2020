from orator.migrations import Migration


class CreateLibroAutorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Detalle_Libro_Autor') as table:
            table.increments('idDetalle_Libro_Autor')
            table.integer('idAutor').unsigned()
            table.foreign('idAutor').references('idAutor').on('Autor')
            table.integer('idLibro').unsigned()
            table.foreign('idLibro').references('idLibro').on('Libro')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Detalle_Libro_Autor')
