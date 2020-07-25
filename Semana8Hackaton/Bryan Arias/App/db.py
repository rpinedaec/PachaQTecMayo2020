#from orator import DatabaseManager

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'Biblioteca',
        'user': 'root',
        'password': 'admin',
        'prefix': ''
    }
}

#db = DatabaseManager(DATABASES)