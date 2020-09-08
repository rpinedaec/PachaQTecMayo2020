from orator.migrations import Migration


class CreateTipo(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("tipo") as table:
            table.increments('id')
            table.string('descripcion')
            table.integer('activo')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tipo')
