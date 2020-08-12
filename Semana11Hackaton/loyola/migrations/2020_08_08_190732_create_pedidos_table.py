from orator.migrations import Migration


class CreatePedidosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('pedidos') as table:
            table.increments('id')
            table.long_text('ubicacion')
            table.integer('cliente_id').unsigned()
            table.foreign('cliente_id').references('id').on('clientes')
            table.integer('producto_id').unsigned()
            table.foreign('producto_id').references('id').on('productos')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pedidos')
