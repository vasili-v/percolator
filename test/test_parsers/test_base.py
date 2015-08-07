import unittest

from percolator.parsers.base import Base

class TestParsersBase(unittest.TestCase):
    def test_creation(self):
        base = Base('start')
        self.assertEqual(base.start, 'start')

    def test_reset(self):
        base = Base('start')
        base.reset()

test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestParsersBase)

if __name__ == '__main__':
    unittest.main()

