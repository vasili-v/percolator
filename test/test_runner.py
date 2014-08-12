import unittest

from percolator.runner import Runner

class TestRunner(unittest.TestCase):
    def test_creation_default(self):
        Runner()

    def test_creation_environment(self):
        Runner({'PATH': '/home'})

if __name__ == '__main__':
    unittest.main()

