import unittest
import StringIO

from percolator.parsers.printer import Printer

class TestParsersPrinter(unittest.TestCase):
    def test_creation(self):
        printer = Printer()
        self.assertTrue(callable(printer.start))

    def test_creation_prefix(self):
        printer = Printer('>>> ')
        self.assertTrue(callable(printer.start))

    def test_creation_integer_prefix(self):
        printer = Printer(1)
        self.assertTrue(callable(printer.start))

    def test_creation_function_prefix(self):
        printer = Printer(lambda x: '>>> %s' % x)
        self.assertTrue(callable(printer.start))

    def test_parse(self):
        stream = StringIO.StringIO()
        printer = Printer(stream=stream)
        printer.reset()
        printer.start('xxx    \nyyy   ')
        self.assertEqual(stream.getvalue(), 'xxx\n')

    def test_parse_prefix(self):
        stream = StringIO.StringIO()
        printer = Printer('>>> ', stream)
        printer.reset()
        printer.start('xxx    \nyyy   ')
        self.assertEqual(stream.getvalue(), '>>> xxx\n')

    def test_parse_function_prefix(self):
        stream = StringIO.StringIO()
        printer = Printer(lambda x: '>>> %s' % x.rstrip(), stream)
        printer.reset()
        printer.start('xxx    \nyyy   ')
        self.assertEqual(stream.getvalue(), '>>> xxx\n')

    def test_parse_function_integer_prefix(self):
        stream = StringIO.StringIO()
        printer = Printer(lambda x: len(x), stream)
        printer.reset()
        printer.start('xxx    \nyyy   ')
        self.assertEqual(stream.getvalue(), '7\n')

test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestParsersPrinter)

if __name__ == '__main__':
    unittest.main()

