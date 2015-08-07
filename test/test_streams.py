import unittest
import errno

from percolator.streams import Streams

class TestStreams(unittest.TestCase):
    def test_creation(self):
        Streams()

    def test_begin(self):
        streams = Streams()
        stdout, stderr = streams.begin()
        self.assertTrue(isinstance(stdout, (int, long)))
        self.assertTrue(isinstance(stderr, (int, long)))

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

