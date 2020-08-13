from orator.migrations import Migration


class CreatePedidoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('pedido') as table:
            table.increments('id')
            table.integer('cliente_id', unsigned=True)
            table.integer('factura_id', unsigned=True)
            table.date('fecha_despacho')
            table.date('fecha_entrega')
            table.integer('estado')
            table.timestamps()

            table.foreign('cliente_id').references('id').on('cliente')
            table.foreign('factura_id').references('id').on('factura')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pedido')
