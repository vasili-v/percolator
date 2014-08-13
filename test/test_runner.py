import unittest

from percolator.runner import Runner
from percolator.parsers.collector import Collector

class TestRunner(unittest.TestCase):
    def test_creation_default(self):
        Runner()

    def test_creation_environment(self):
        Runner(None, None, {'PATH': '/home'})

    def test_run(self):
        collector = Collector()
        runner = Runner(collector, collector)
        self.assertEqual(runner.run(['printf', 'xxx\\nyyy\\nzzz']), 0)
        self.assertEqual(collector.items, ['xxx', 'yyy', 'zzz'])

if __name__ == '__main__':
    unittest.main()

