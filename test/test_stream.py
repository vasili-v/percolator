import unittest
import threading

from percolator.stream import Stream

class TestStream(unittest.TestCase):
    def setUp(self):
        self.event = threading.Event()
        self.event.clear()

    def tearDown(self):
        if hasattr(self, 'event'):
            self.event.set()

        if hasattr(self, 'stream'):
            self.stream.stop()
            del self.stream

        if hasattr(self, 'event'):
            del self.event

    def test_creation(self):
        Stream(None)

    def test_get_descriptor(self):
        self.stream = Stream(self.event)
        self.assertTrue(isinstance(self.stream.get_descriptor(), (int, long)))

    def test_get_descriptor_exception(self):
        self.stream = Stream(self.event)

        def exception_start():
            raise Exception()

        self.stream._Stream__start = exception_start
        self.assertRaises(Exception, self.stream.get_descriptor)

    def test_get_descriptor_twice(self):
        self.stream = Stream(self.event)
        descriptor = self.stream.get_descriptor()
        self.assertEqual(self.stream.get_descriptor(), descriptor)

    def test_stop(self):
        self.stream = Stream(self.event)
        self.stream.get_descriptor()
        self.event.set()
        self.stream.stop()

if __name__ == '__main__':
    unittest.main()

