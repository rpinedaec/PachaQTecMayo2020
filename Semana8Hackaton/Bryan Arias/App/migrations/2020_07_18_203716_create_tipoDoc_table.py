from orator.migrations import Migration


class CreateTipoDocTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Tipo_Documento') as table:
            table.increments('idTipo_Documento')
            table.string('Descripcion', 25)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Tipo_Documento')
