import unittest

from percolator.stream import Stream

class TestStream(unittest.TestCase):
    def test_creation(self):
        Stream()

if __name__ == '__main__':
    unittest.main()

