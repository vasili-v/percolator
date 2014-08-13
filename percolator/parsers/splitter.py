from percolator.parsers.base import Base

class Splitter(Base):
    def __init__(self, start, separator='\n'):
        super(Splitter, self).__init__(self.__parse)

        self.__start = start
        self.__separator = separator

    def reset(self):
        super(Splitter, self).reset()

        self.__inner = self.__start
        self.__remainder = ''

    def __parse(self, data=None):
        if data:
            lines = data.split(self.__separator)
            lines[0] = self.__remainder + lines[0]

            for line in lines[:-1]:
                self.__inner = self.__inner(line)

            self.__remainder = lines[-1]
        else:
            self.__inner = self.__inner(self.__remainder)
            self.__remainder = ''

        return self.__parse
