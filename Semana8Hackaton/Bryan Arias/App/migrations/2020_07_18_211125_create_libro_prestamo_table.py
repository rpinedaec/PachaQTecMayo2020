from orator.migrations import Migration


class CreateLibroPrestamoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Prestamo') as table:
            table.increments('idPrestamo')
            table.integer('idLector').unsigned()
            table.foreign('idLector').references('idLector').on('Lector')   
            table.integer('idDetalle_Libro_Biblioteca').unsigned()
            table.foreign('idDetalle_Libro_Biblioteca').references('idDetalle_Libro_Biblioteca').on('Detalle_Libro_Biblioteca')
            table.string('Estado', 5).default('1')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Prestamo')
