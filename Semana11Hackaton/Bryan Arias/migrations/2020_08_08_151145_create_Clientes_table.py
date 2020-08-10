from orator.migrations import Migration


class CreateClientesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Clientes') as table:
            table.increments('id')
            table.string('nombres', 50)
            table.string('tipo_doc', 30)
            table.string('num_doc', 10)
            table.string('num_cel', 30)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Clientes')
