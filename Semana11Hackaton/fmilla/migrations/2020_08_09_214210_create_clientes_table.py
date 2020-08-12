from orator.migrations import Migration


class CreateClientesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('clientes') as table:
            table.increments('id')
            table.string('nombre').unique()
            table.string('email').unique()
            table.string('telefono').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('clientes')
