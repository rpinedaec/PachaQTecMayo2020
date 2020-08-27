from orator import DatabaseManager, Schema
DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'hackatons11',
        'user': 'postgres',
        'password': 'pachaqtec',
        'prefix': ''
    }
}
db = DatabaseManager(DATABASES)
schema = Schema(db)