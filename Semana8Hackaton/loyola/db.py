from orator import DatabaseManager, Schema

databases = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'biblioteca',
        'user': 'root',
        'password': 'pachaqtec',
        'prefix': ''
    }
}

db = DatabaseManager(databases)
schema = Schema(db)