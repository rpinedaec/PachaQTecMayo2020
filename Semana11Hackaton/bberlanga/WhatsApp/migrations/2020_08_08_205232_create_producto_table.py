from orator.migrations import Migration


class CreateProductoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('producto') as table:
            table.increments('id')
            table.string('nombre')
            table.decimal('precio',5,2)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('producto')
