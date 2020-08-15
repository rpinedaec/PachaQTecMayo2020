from orator.migrations import Migration


class CreateClienteTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cliente') as table:
            table.increments('id')
            table.string('nombre')
            table.string('correo').unique()
            table.string('número_telefonico').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cliente')
