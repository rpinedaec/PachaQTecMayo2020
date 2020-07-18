from orator.migrations import Migration


class CreateBibliotecasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('bibliotecas') as table:
            table.increments('id')
            table.string('nombre')
            table.string('direccion')
            table.integer('tipo_documento_id').unsigned()
            table.foreign('tipo_documento_id').references('id').on('tipodocumento')
            table.string('documento')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('bibliotecas')
