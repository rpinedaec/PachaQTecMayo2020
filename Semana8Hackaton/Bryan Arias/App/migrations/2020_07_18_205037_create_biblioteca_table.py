from orator.migrations import Migration


class CreateBibliotecaTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Biblioteca') as table:
            table.increments('idBiblioteca')
            table.string('Nombre_Biblioteca', 50)
            table.string('Direccion', 70)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Biblioteca')
