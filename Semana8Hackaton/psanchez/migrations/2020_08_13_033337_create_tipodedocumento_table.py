from orator.migrations import Migration


class CreateTipodedocumentoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tipodedocumento') as table:
            table.increments('id')
            table.string('descripcion')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tipodedocumento')
