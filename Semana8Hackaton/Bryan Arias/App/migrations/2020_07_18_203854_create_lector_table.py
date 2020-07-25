from orator.migrations import Migration


class CreateLectorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Lector') as table:
            table.increments('idLector')
            table.integer('idTipo_Documento').unsigned()
            table.string('Nombres', 20)
            table.string('Apellidos', 30)
            table.string('Numero_Documento', 10)
            table.foreign('idTipo_Documento').references('idTipo_Documento').on('Tipo_Documento')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Lector')
