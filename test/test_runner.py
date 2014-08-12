import unittest

from percolator.runner import Runner

class TestRunner(unittest.TestCase):
    def test_creation_default(self):
        Runner()

    def test_creation_environment(self):
        Runner(None, None, {'PATH': '/home'})

    def test_run(self):
        runner = Runner()
        self.assertEqual(runner.run(['echo']), 0)

if __name__ == '__main__':
    unittest.main()

