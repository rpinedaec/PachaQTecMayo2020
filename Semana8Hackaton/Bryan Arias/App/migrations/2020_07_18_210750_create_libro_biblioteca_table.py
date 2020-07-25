from orator.migrations import Migration


class CreateLibroBibliotecaTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Detalle_Libro_Biblioteca') as table:
            table.increments('idDetalle_Libro_Biblioteca')
            table.integer('idLibro').unsigned()
            table.foreign('idLibro').references('idLibro').on('Libro')
            table.integer('idBiblioteca').unsigned()
            table.foreign('idBiblioteca').references('idBiblioteca').on('Biblioteca')
            table.string('Estado',2).default('1')
            table.integer('Cantidad')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Detalle_Libro_Biblioteca')
