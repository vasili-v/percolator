import subprocess
import select

from percolator.parsers.null import Null
from percolator.parsers.stdout import Stdout
from percolator.stream import Stream

class Streams(object):
    def __init__(self, stdout=Null, stderr=Stdout, timeout=.1):
        self.__timeout = timeout

        if stdout is Stdout:
            raise RuntimeError('Predefined parser "Stdout" can be only passed '
                               'to stderr argument')

        self.__stdout = Stream(stdout)
        if stderr is Stdout or stderr is stdout:
            self.__stderr = self.__stdout
        else:
            self.__stderr = Stream(stderr)

        self.__streams = {}
        self.__descriptors = []

    def clean(self):
        self.__streams = {}
        self.__descriptors = []

        self.__stdout.clean()
        self.__stderr.clean()

    def begin(self):
        stdout_read, stdout_write = self.__stdout.begin()
        self.__streams[stdout_read] = self.__stdout

        if self.__stderr is self.__stdout:
            stderr_write = subprocess.STDOUT
        else:
            stderr_read, stderr_write = self.__stderr.begin()
            self.__streams[stderr_read] = self.__stderr

        self.__descriptors = list(self.__streams)

        return stdout_write, stderr_write

    def __wait_for_descriptors(self):
        return select.select(self.__descriptors, [], [], self.__timeout)[0]

    def process(self):
        for descriptor in self.__wait_for_descriptors():
            self.__streams[descriptor].process()

    def finalize(self):
        for stream in self.__streams.itervalues():
            stream.parse()

