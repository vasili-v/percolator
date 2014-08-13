import sys
import types

from percolator.parsers.splitter import Splitter

class Printer(Splitter):
    def __init__(self, prefix=None, stream=sys.stdout):
        if prefix:
            if callable(prefix):
                self.__prefix = prefix
                parse = self.__callable_parse
            else:
                if isinstance(prefix, types.StringTypes):
                    self.__prefix = prefix
                else:
                    self.__prefix = str(prefix)
                parse = self.__prefix_parse
        else:
            parse = self.__parse

        super(Printer, self).__init__(parse)

        self.__stream = stream

    def __parse(self, line):
        print >> self.__stream, line.rstrip()

    def __prefix_parse(self, line):
        print >> self.__stream, '%s%s' % (self.__prefix, line.rstrip())

    def __callable_parse(self, line):
        prefix = self.__prefix(line)
        if not isinstance(prefix, types.StringTypes):
            prefix = str(prefix)

        print >> self.__stream, prefix

