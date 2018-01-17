import os
import sys
import unittest

basedir = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.append(basedir)

from src.dependency import setup_dependency_container


class TestDatabaseCreation(unittest.TestCase):

    def setUp(self):
        setup_dependency_container('test')

    def test_database_creation(self):
        from src.dependency import Base, engine
        Base.metadata.create_all(engine)

        database_path = 'data/test.db'

        self.assertTrue(os.path.isfile(database_path))

        os.remove(database_path)


if __name__ == '__main__':
    unittest.main()
