from orator import DatabaseManager
from orator import Model

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'Wassp',
        'user': 'postgres',
        'password': '3179billace',
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)
