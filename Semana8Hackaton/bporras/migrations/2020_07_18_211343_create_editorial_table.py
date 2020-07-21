from orator.migrations import Migration


class CreateEditorialTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('editoriales') as table:
            table.increments('id')
            table.string('nombre')
            table.string('correo')
            table.string('dirección')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
