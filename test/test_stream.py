import unittest
import errno

from percolator.stream import Stream, Streams

class TestStream(unittest.TestCase):
    def test_creation(self):
        Stream()

    def test_get_descriptor(self):
        stream = Stream()
        self.assertTrue(isinstance(stream.get_descriptor(), (int, long)))

    def test_get_descriptor_exception(self):
        stream = Stream()

        def exception_func():
            raise Exception()

        stream._Stream__prepare_descriptor = exception_func
        self.assertRaises(Exception, stream.get_descriptor)

    def test_get_descriptor_twice(self):
        stream = Stream()
        descriptor = stream.get_descriptor()
        self.assertEqual(stream.get_descriptor(), descriptor)

    def test_clean(self):
        stream = Stream()
        stream.get_descriptor()
        stream.clean()

    def test_register(self):
        stream = Stream()
        descriptor = stream.get_descriptor()
        streams = {}
        stream.register(streams)
        self.assertEqual(list(streams.itervalues()), [stream])

    def test_process(self):
        stream = Stream()
        descriptor = stream.get_descriptor()
        stream.process()

    def test_process_exception(self):
        stream = Stream()

        class ExceptionFile(object):
            def read(self):
                raise IOError(errno.EIO, 'Test error')

        stream._Stream__out = ExceptionFile()
        self.assertRaises(Exception, stream.process)

class TestStreams(unittest.TestCase):
    def test_creation(self):
        Streams()

    def test_get_descriptors(self):
        streams = Streams()
        stdout, stderr = streams.get_descriptors()
        self.assertTrue(isinstance(stdout, (int, long)))
        self.assertTrue(isinstance(stderr, (int, long)))

    def test_clean(self):
        streams = Streams()
        streams.get_descriptors()
        streams.clean()

    def test_process(self):
        streams = Streams()
        streams.get_descriptors()
        streams.process()

    def test_process_all_descriptors(self):
        streams = Streams()
        streams.get_descriptors()

        def descriptors():
            return streams._Streams__descriptors
        streams._Streams__wait_for_descriptors = descriptors

        streams.process()

if __name__ == '__main__':
    unittest.main()

