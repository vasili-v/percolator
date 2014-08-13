import unittest

from percolator.parsers.collector import Collector

class TestParsersCollector(unittest.TestCase):
    def test_creation(self):
        collector = Collector()
        self.assertTrue(callable(collector.start))

    def test_parse(self):
        collector = Collector()
        parse = collector.start
        collector.reset()
        parse('xxx\nyy')
        parse('y\nzzz')
        parse()
        self.assertEqual(collector.items, ['xxx', 'yyy', 'zzz'])

    def test_reset(self):
        collector = Collector()
        parse = collector.start
        collector.reset()
        parse('xxx\nyyy')
        self.assertEqual(collector.items, ['xxx'])
        collector.reset()
        self.assertEqual(collector.items, [])

if __name__ == '__main__':
    unittest.main()

