from orator.migrations import Migration


class CreatePedidosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Pedidos') as table:
            table.increments('id')
            table.long_text('ubicacion')
            table.integer('cliente', unsigned=True)
            table.integer('producto', unsigned=True)
            table.foreign('cliente').references('id').on('Clientes')
            table.foreign('producto').references('id').on('Productos')
            table.integer('cantidad')
            table.timestamps('fecha_pedido')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Pedidos')
