from orator.migrations import Migration


class Lectores(Migration):

    def up(self):
        """
        Run the migrations.

        """
        transactional = False 

        with self.db.transaction():
            with self.schema.create('lectores') as table:
                table.increments('lector_id')
                table.string('lector_nombre')
                table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('lectores')


