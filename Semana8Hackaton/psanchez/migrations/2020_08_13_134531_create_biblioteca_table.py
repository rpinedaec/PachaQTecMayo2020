from orator.migrations import Migration


class CreateBibliotecaTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('biblioteca') as table:
            table.increments('id')
            table.string('nombre')
            table.string('direccion')
            table.integer('tipodedocumento_id').unsigned()
            table.foreign('tipodedocumento_id').references('id').on('tipodedocumento')
            table.string('documento')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('biblioteca')
