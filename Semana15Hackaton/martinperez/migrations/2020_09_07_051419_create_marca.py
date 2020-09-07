from orator.migrations import Migration


class CreateMarca(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("marca") as table:
            table.increments('id')
            table.string('descripcion')
            table.integer('activo')
        
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('marca')
