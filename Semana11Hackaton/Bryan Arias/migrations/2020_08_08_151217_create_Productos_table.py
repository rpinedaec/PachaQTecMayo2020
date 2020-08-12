from orator.migrations import Migration


class CreateProductosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Productos') as table:
            table.increments('id')
            table.string('descripcion', 20)
            table.integer('cantidad')
            table.double('precio', 5, 2)            
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Productos')
