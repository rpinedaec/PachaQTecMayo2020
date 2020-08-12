from orator.migrations import Migration


class CreateFacturaTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('factura') as table:
            table.increments('id')
            table.date('fecha')
            table.integer('cliente_id', unsigned=True)
            table.decimal('sub_total',5,2)
            table.decimal('IGV',5,2)
            table.decimal('monto_total',5,2)            
            table.timestamps()

            table.foreign('cliente_id').references('id').on('cliente')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('factura')
