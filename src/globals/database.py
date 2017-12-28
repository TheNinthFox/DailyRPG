from orator import Model
from orator import DatabaseManager


class Database:
    instance = None  # type: DatabaseManager

    @staticmethod
    def connect(config):
        Database.instance = DatabaseManager(config)
        Model.set_connection_resolver(Database.instance)
