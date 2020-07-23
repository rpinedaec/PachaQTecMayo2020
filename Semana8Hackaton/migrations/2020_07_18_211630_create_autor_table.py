from orator.migrations import Migration


class CreateAutorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('autors') as table:
            table.increments('id')
            table.string('nombre')
            table.string('correo')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('autors')
