from orator.migrations import Migration


class CreateUsuarioTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('usuario') as table:
            table.increments('id')
            table.string('nombre')
            table.string('correo')
            table.integer('tipodedocumento_id').unsigned()
            table.foreign('tipodedocumento_id').references('id').on('tipodedocumento')
            table.string('documento')
            table.integer('estadousuario_id').unsigned()
            table.foreign('estadousuario_id').references('id').on('estadousuario')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('usuario')
