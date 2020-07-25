from orator.migrations import Migration


class CreateUsuarioTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('usuarios') as table:
            table.increments('id')
            table.string('nombre')
            table.string('correo')
            table.string('documento')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('usuarios')
