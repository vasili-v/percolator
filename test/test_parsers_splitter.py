import unittest

from percolator.parsers.splitter import Splitter

class TestParsersSplitter(unittest.TestCase):
    def test_creation(self):
        class TestParser(Splitter):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

            def __parse(self, line):
                return self.__parse

        test_parser = TestParser()
        self.assertTrue(callable(test_parser.start))

    def test_parse(self):
        class TestParser(Splitter):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

                self.lines = []

            def __parse(self, line):
                self.lines.append(line)
                return self.__parse

        test_parser = TestParser()
        parse = test_parser.start
        test_parser.reset()
        self.assertEqual(parse('xxx\nyy'), parse)
        self.assertEqual(parse('y\nzzz'), parse)
        self.assertEqual(parse(), parse)
        self.assertEqual(test_parser.lines, ['xxx', 'yyy', 'zzz'])

    def test_reset(self):
        class TestParser(Splitter):
            def __init__(self):
                super(TestParser, self).__init__(self.__parse)

                self.lines = []

            def __parse(self, line):
                self.lines.append(line)
                return self.__parse

        test_parser = TestParser()
        parse = test_parser.start
        test_parser.reset()
        self.assertEqual(parse('xxx\nyyy'), parse)
        test_parser.reset()
        self.assertEqual(parse('zzz\nyyy'), parse)
        self.assertEqual(test_parser.lines, ['xxx', 'zzz'])

if __name__ == '__main__':
    unittest.main()

