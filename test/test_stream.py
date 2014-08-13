import unittest
import errno
import subprocess

from percolator.stream import Stream
from percolator.parsers.base import Base
from percolator.parsers.null import Null

class TestStream(unittest.TestCase):
    def test_creation(self):
        Stream()

    def test_begin(self):
        stream = Stream()
        self.assertTrue(isinstance(stream.begin(), (int, long)))

    def test_begin_exception(self):
        stream = Stream()

        def exception_func():
            raise Exception()

        stream._Stream__prepare_descriptor = exception_func
        self.assertRaises(Exception, stream.begin)

    def test_begin_twice(self):
        stream = Stream()
        descriptor = stream.begin()
        self.assertEqual(stream.begin(), descriptor)

    def test_begin_same_parser(self):
        null = Null()

        first_stream = Stream(null)
        second_stream = Stream(null)

        self.assertEqual(second_stream.begin(first_stream), subprocess.STDOUT)

    def test_clean(self):
        stream = Stream()
        stream.begin()
        stream.clean()

    def test_register(self):
        stream = Stream()
        descriptor = stream.begin()
        streams = {}
        stream.register(streams)
        self.assertEqual(list(streams.itervalues()), [stream])

    def test_register_same_parser(self):
        null = Null()

        first_stream = Stream(null)
        second_stream = Stream(null)

        streams = {}
        second_stream.register(streams, first_stream)

        self.assertEqual(streams, {})

    def test_parse(self):
        class TestParser(Base):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

            def __parse(self, data):
                return self.__parse

        stream = Stream(TestParser())
        stream.parse()

    def test_process(self):
        stream = Stream()
        descriptor = stream.begin()
        stream.process()

    def test_process_exception(self):
        stream = Stream()

        class ExceptionFile(object):
            def read(self):
                raise IOError(errno.EIO, 'Test error')

        stream._Stream__out = ExceptionFile()
        self.assertRaises(Exception, stream.process)

    def test_process_data(self):
        stream = Stream()

        class TestFile(object):
            def read(self):
                return 'test data'

        stream._Stream__out = TestFile()
        stream.process()

if __name__ == '__main__':
    unittest.main()

