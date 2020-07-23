from orator.migrations import Migration


class CreateEditorialTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Editorial') as table:
            table.increments('idEditorial')
            table.string('Nombre_Editorial', 40)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Editorial')
