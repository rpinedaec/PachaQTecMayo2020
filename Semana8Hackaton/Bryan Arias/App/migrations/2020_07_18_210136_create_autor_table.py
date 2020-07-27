from orator.migrations import Migration


class CreateAutorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Autor') as table:
            table.increments('idAutor')
            table.string('Nombre_Autor', 40)
            table.string('Correo', 30)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Autor')
