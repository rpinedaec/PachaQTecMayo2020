from orator.migrations import Migration


class CreateDetalleFacturaTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('detalle_factura') as table:
            table.increments('id')
            table.integer('factura_id', unsigned=True)
            table.integer('cantidad')
            table.decimal('sub_total',5,2)
            table.decimal('IGV',5,2)
            table.decimal('monto_total',5,2)
            table.timestamps()
            
            table.foreign('factura_id').references('id').on('factura')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('detalle_factura')
