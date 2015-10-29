import unittest
import errno
import subprocess

from percolator.stream import ParserStream, RunnerStream, make_stream
from percolator.parsers.base import Base
from percolator.parsers.null import Null
from percolator.runner import Runner

class TestParserStream(unittest.TestCase):
    def test_creation(self):
        ParserStream()

    def test_begin(self):
        stream = ParserStream()
        write_descriptor, read_descriptor = stream.begin()
        self.assertTrue(isinstance(write_descriptor, (int, long)))
        self.assertTrue(isinstance(read_descriptor, (int, long)))

    def test_begin_exception(self):
        stream = ParserStream()

        def exception_func():
            raise Exception()

        stream._ParserStream__prepare_descriptor = exception_func
        self.assertRaises(Exception, stream.begin)

    def test_begin_twice(self):
        stream = ParserStream()
        descriptor = stream.begin()
        self.assertEqual(stream.begin(), descriptor)

    def test_clean(self):
        stream = ParserStream()
        stream.begin()
        stream.clean()

    def test_parse(self):
        class TestParser(Base):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

            def __parse(self, data):
                return self.__parse

        stream = ParserStream(TestParser())
        stream.parse()

    def test_process(self):
        stream = ParserStream()
        descriptor = stream.begin()
        stream.process()

    def test_process_exception(self):
        stream = ParserStream()

        class ExceptionFile(object):
            def read(self):
                raise IOError(errno.EIO, 'Test error')

        stream._ParserStream__out = ExceptionFile()
        self.assertRaises(Exception, stream.process)

    def test_process_data(self):
        stream = ParserStream()

        class TestFile(object):
            def read(self):
                return 'test data'

        stream._ParserStream__out = TestFile()
        stream.process()

class TestRunnerStream(unittest.TestCase):
    def test_creation(self):
        RunnerStream(Runner())

    def test_begin(self):
        stream = RunnerStream(Runner())
        self.assertEqual(stream.begin(), (None, subprocess.PIPE))

    def test_clean(self):
        stream = RunnerStream(Runner())
        stream.clean()

class TestStreamFactory(unittest.TestCase):
    def test_parser_stream(self):
        self.assertIsInstance(make_stream(Null), ParserStream)

    def test_runner_stream(self):
        self.assertIsInstance(make_stream(Runner()), RunnerStream)

    def test_invalid_receiver(self):
        self.assertRaises(RuntimeError, make_stream, None)

test_suite = unittest.TestSuite((unittest.defaultTestLoader.loadTestsFromTestCase(TestParserStream),
                                 unittest.defaultTestLoader.loadTestsFromTestCase(TestRunnerStream),
                                 unittest.defaultTestLoader.loadTestsFromTestCase(TestStreamFactory)))

if __name__ == '__main__':
    unittest.main()

