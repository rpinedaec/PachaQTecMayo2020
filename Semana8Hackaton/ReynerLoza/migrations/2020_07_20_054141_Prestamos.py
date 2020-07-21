from orator.migrations import Migration


class Prestamos(Migration):

    def up(self):
        """
        Run the migrations.
        """
        transactional = False

        with self.db.transaction():
            with self.schema.create('prestamos') as table:
                table.increments('prestamo_id')
                table.foreign('lector_id').references('lector_id').on('Lectores')
                table.timestamps()



    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('prestamos')
