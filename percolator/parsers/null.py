from percolator.parsers.base import Base

class Null(Base):
    def __init__(self):
        super(Null, self).__init__(self.__parse)

    def __parse(self, data):
        return self.__parse
