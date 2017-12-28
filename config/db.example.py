from orator import DatabaseManager, Schema

databases = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'data/dailyrpg.db',
    }
}

db = DatabaseManager(databases)
schema = Schema(db)
