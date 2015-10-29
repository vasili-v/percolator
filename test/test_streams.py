import unittest
import errno
import subprocess

from percolator.parsers.base import Base
from percolator.parsers.stdout import Stdout
from percolator.streams import Streams
from percolator.runner import Runner

class TestStreams(unittest.TestCase):
    def test_creation(self):
        Streams()

    def test_creation_invalid_stdout_parser(self):
        self.assertRaises(RuntimeError, Streams, Stdout)

    def test_creation_not_implemented(self):
        runner = Runner()
        self.assertRaises(NotImplementedError, Streams, stdout=runner)
        self.assertRaises(NotImplementedError, Streams, stderr=runner)

    def test_begin(self):
        streams = Streams()
        stdout, stderr = streams.begin()
        self.assertTrue(isinstance(stdout, (int, long)))
        self.assertEqual(stderr, subprocess.STDOUT)

    def test_begin_with_stdout_parser(self):
        class TestParser(Base):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

            def __parse(self, data=None):
                pass

        streams = Streams(TestParser(), Stdout)
        stdout, stderr = streams.begin()
        self.assertTrue(isinstance(stdout, (int, long)))
        self.assertEqual(stderr, subprocess.STDOUT)

    def test_begin_different_parsers(self):
        class TestParser(Base):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

            def __parse(self, data=None):
                pass

        streams = Streams(TestParser(), TestParser())
        stdout, stderr = streams.begin()
        self.assertTrue(isinstance(stdout, (int, long)))
        self.assertTrue(isinstance(stderr, (int, long)))
        self.assertNotEqual(stdout, stderr)

    def test_clean(self):
        streams = Streams()
        streams.begin()
        streams.clean()

    def test_process(self):
        streams = Streams()
        streams.begin()
        streams.process()

    def test_process_all_descriptors(self):
        streams = Streams()
        streams.begin()

        def descriptors():
            return streams._Streams__descriptors
        streams._Streams__wait_for_descriptors = descriptors

        streams.process()

test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStreams)

if __name__ == '__main__':
    unittest.main()

