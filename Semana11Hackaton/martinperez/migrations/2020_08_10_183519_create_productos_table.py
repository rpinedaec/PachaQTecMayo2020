from orator.migrations import Migration


class CreateProductosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('productos') as table:
            table.increments('id')
            table.string('nombre')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('productos')

