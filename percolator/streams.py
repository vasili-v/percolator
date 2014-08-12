import select

from percolator.stream import Stream

class Streams(object):
    def __init__(self, timeout=.1):
        self.__timeout = timeout

        self.__stdout = Stream()
        self.__stderr = Stream()

        self.__streams = {}
        self.__descriptors = []

    def clean(self):
        self.__streams = {}
        self.__descriptors = []

        self.__stdout.clean()
        self.__stderr.clean()

    def get_descriptors(self):
        stdout = self.__stdout.get_descriptor()
        self.__stdout.register(self.__streams)

        stderr = self.__stderr.get_descriptor()
        self.__stderr.register(self.__streams)

        self.__descriptors = list(self.__streams)

        return stdout, stderr

    def __wait_for_descriptors(self):
        return select.select(self.__descriptors, [], [], self.__timeout)[0]

    def process(self):
        for descriptor in self.__wait_for_descriptors():
            self.__streams[descriptor].process()

