import unittest

from percolator.parsers.null import Null

class TestParsersNull(unittest.TestCase):
    def test_creation(self):
        null = Null()
        self.assertTrue(callable(null.start))

    def test_parse(self):
        null = Null()
        parse = null.start
        self.assertEqual(parse('test data'), parse)
        self.assertEqual(parse(), parse)

if __name__ == '__main__':
    unittest.main()

