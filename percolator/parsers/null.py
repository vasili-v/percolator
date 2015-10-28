from percolator.parsers.base import Base

class _NullType(Base):
    def __init__(self):
        super(_NullType, self).__init__(self.__parse)

    def __parse(self, data=None):
        pass

Null = _NullType()

