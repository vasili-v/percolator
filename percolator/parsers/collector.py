from percolator.parsers.splitter import Splitter

class Collector(Splitter):
    def __init__(self):
        super(Collector, self).__init__(self.__parse)

    def reset(self):
        super(Collector, self).reset()

        self.__items = []

    def __get_items(self):
        return self.__items

    items = property(__get_items)

    def __parse(self, data):
        self.__items.append(data)

