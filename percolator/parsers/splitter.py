from percolator.parsers.base import Base

class Splitter(Base):
    def __init__(self, start):
        super(Splitter, self).__init__(self.__parse)

        self.__start = start

    def reset(self):
        super(Splitter, self).reset()

        self.__inner = self.__start
        self.__remainder = ''

    def __inner_parse(self, line):
        inner = self.__inner(line)
        if inner:
            self.__inner = inner

    def __parse(self, data=None):
        if data:
            lines = data.split('\n')
            lines[0] = self.__remainder + lines[0]

            for line in lines[:-1]:
                if line[-1] == '\r':
                    line = line[:-1]

                self.__inner_parse(line)

            self.__remainder = lines[-1]
        else:
            self.__inner_parse(self.__remainder)
            self.__remainder = ''

