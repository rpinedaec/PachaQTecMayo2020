from orator import DatabaseManager
from orator import Model

def connec():
    config = {
        'mysql': {
            'driver': 'mysql',
            'host': 'localhost',
            'database': 'biblioteca',
            'user': 'root',
            'password': '3179billace',
            'prefix': '',
            'log_queries':True
        }
    }

    db = DatabaseManager(config)
    conn=Model.set_connection_resolver(db)
    return conn
