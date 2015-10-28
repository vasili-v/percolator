from percolator.parsers.base import Base

class _StdoutType(Base):
    def __init__(self):
        super(_StdoutType, self).__init__(self.__parse)

    def __parse(self, data=None):
        raise RuntimeError('Predefined parser "Stdout" can\'t be used for '
                           'parsing. It only redirects stderr to stdout')

Stdout = _StdoutType()

