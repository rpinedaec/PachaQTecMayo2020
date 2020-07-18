from orator.seeds import Seeder


class UsersTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """

        # Here you could just use random string generators
        # rather than hardcoded values
        self.db.table('users').insert({
            'name': 'john',
            'email': 'john@doe.com'
        })