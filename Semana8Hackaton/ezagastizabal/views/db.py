from orator.migrations import Migration
from orator import Model,DatabaseManager, Schema




DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'Lana2409',
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)