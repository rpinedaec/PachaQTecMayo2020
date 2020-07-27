from orator.migrations import Migration


class Libros(Migration):

    def up(self):
        """
        Run the migrations.
        """
        transactional = False

        with self.db.transaction():
            with self.schema.create('libros') as table:
                table.increments('libro_id')
                table.string('libro_nombre',40)
                table.string('libro_autor',40)
                table.intenger('estado').unsigned()
                table.foreign('prestamo_id').references('prestamo_id').on('Prestamos')
                table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('libros')
