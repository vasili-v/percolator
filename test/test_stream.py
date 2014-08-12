import unittest

from percolator.stream import Stream

class TestStream(unittest.TestCase):
    def test_creation(self):
        Stream()

    def test_get_descriptor(self):
        stream = Stream()
        self.assertTrue(isinstance(stream.get_descriptor(), (int, long)))

    def test_get_descriptor_twice(self):
        stream = Stream()
        descriptor = stream.get_descriptor()
        self.assertEqual(stream.get_descriptor(), descriptor)

    def test_stop(self):
        stream = Stream()
        stream.get_descriptor()
        stream.stop()

if __name__ == '__main__':
    unittest.main()

