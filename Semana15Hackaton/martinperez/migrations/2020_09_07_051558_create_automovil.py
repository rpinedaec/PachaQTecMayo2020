from orator.migrations import Migration


class CreateAutomovil(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("automovil") as table:
            table.increments('id')
            table.string('descripcion')
            table.integer('marca_automovil_id').unsigned()
            table.foreign('marca_automovil_id').references('id').on('marca')
            table.integer('tipo_automovil_id').unsigned()
            table.foreign('tipo_automovil_id').references('id').on('tipo')
            table.integer('activo')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('automovil')
