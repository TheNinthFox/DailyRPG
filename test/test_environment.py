import os
import sys
import unittest

basedir = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.append(basedir)

from src.dependency import setup_dependency_container


class TestEnvironment(unittest.TestCase):

    def setUp(self):
        setup_dependency_container('test')

    def test_environment(self):
        from src.dependency import env
        self.assertEqual(env['name'], 'Test')


if __name__ == '__main__':
    unittest.main()
