import unittest

from percolator.runner import Runner

class TestRunner(unittest.TestCase):
    def test_creation(self):
        Runner()

if __name__ == '__main__':
    unittest.main()

