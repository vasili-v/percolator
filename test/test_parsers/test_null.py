import unittest

from percolator.parsers.null import Null

class TestParsersNull(unittest.TestCase):
    def test_parse(self):
        parse = Null.start
        parse('test data')
        parse()

test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestParsersNull)

if __name__ == '__main__':
    unittest.main()

