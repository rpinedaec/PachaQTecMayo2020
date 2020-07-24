from orator.migrations import Migration

class CreateUsersTable(Migration):
    
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('nombre')
            table.string('correo')
            table.integer('tipo_documento_id').unsigned()
            table.foreign('tipo_documento_id').references('id').on('tipodocumento')
            table.string('documento')
            table.integer('estado_user_id').unsigned()
            table.foreign('estado_user_id').references('id').on('estadouser')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')