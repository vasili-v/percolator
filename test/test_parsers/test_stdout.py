import unittest

from percolator.parsers.stdout import Stdout

class TestParsersStdout(unittest.TestCase):
    def test_parse(self):
        parse = Stdout.start
        self.assertRaises(RuntimeError, parse, 'test data')

test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestParsersStdout)

if __name__ == '__main__':
    unittest.main()

