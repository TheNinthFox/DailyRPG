import os
import sys
import unittest
from sqlalchemy.orm import sessionmaker
from src.database.models import Skill

basedir = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.append(basedir)

from src.dependency import setup_dependency_container


class TestDatabaseCreation(unittest.TestCase):

    def setUp(self):
        setup_dependency_container('test')

    def test_database_creation(self):
        from src.dependency import Base, engine, env
        Base.metadata.create_all(engine)

        self.assertTrue(os.path.isfile(env['database']))

        os.remove(env['database'])


class TestDatabaseTransactions(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDatabaseTransactions, self).__init__(*args, **kwargs)
        self.session = None

    def setUp(self):
        setup_dependency_container('test')
        from src.dependency import Base, engine
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def test_database_insertion(self):
        self._insert_data()
        self.assertEqual(self.session.query(Skill).count(), 2)

    def test_database_query(self):
        self._insert_data()

        guitar = self.session.query(Skill).filter_by(id=1).first()
        self.assertEqual(guitar.id, 1)
        self.assertEqual(guitar.name, 'Guitar')

        shred = self.session.query(Skill).filter_by(id=2).first()
        self.assertEqual(shred.id, 2)
        self.assertEqual(shred.name, "Shredding")

    def _insert_data(self):
        skill_guitar = Skill(name="Guitar", description="The proficiency of your guitar playing.")
        self.session.add(skill_guitar)
        self.session.commit()

        skill_guitar_shred = Skill(name="Shredding", description="Your ability to shred", parent=skill_guitar)
        self.session.add(skill_guitar_shred)
        self.session.commit()

    def tearDown(self):
        from src.dependency import env
        os.remove(env['database'])


if __name__ == '__main__':
    unittest.main()
