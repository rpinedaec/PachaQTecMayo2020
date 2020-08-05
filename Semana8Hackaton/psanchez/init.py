from orator import DatabaseManager, Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'database',
        'user': 'root',
        'password': 'pachaqtec',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)