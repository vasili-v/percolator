import unittest

from percolator.runner import Runner
from percolator.parsers.null import Null
from percolator.parsers.collector import Collector

class TestRunner(unittest.TestCase):
    def test_creation_default(self):
        Runner()

    def test_creation_environment(self):
        Runner(Null, Null, {'PATH': '/home'})

    def test_run(self):
        collector = Collector()
        runner = Runner(collector, collector)
        self.assertEqual(runner.run(['printf', 'xxx\\nyyy\\nzzz']), 0)
        self.assertEqual(collector.items, ['xxx', 'yyy', 'zzz'])

test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRunner)

if __name__ == '__main__':
    unittest.main()

