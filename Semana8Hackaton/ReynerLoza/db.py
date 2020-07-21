from orator import DatabaseManager
from orator import Model


config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'pachatec',
        'user': 'root',
        'password': 'admin',
        'prefix': ''
    }
}

db= DatabaseManager(config)
