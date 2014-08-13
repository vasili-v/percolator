import os
import fcntl
import errno
import subprocess

from percolator.parsers.null import Null

class Stream(object):
    def __init__(self, parser=None):
        self.__parser = parser if parser else Null()

        self.__clean()

    def __clean(self):
        self.__parse = self.__parser.start
        self.__out_descriptor = None
        self.__out = None
        self.__in_descriptor = None

    def clean(self):
        try:
            self.__out.close()
        except:
            try:
                os.close(self.__out_descriptor)
            except:
                pass

        try:
            os.close(self.__in_descriptor)
        except:
            pass

        self.__clean()

    def __same_parser(self, other):
        try:
            parser = other.__parser
        except AttributeError:
            return False

        return self.__parser is parser

    @staticmethod
    def __prepare_descriptor(descriptor):
        flags = fcntl.fcntl(descriptor, fcntl.F_GETFL)
        fcntl.fcntl(descriptor, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        return os.fdopen(descriptor)

    def begin(self, other=None):
        if self.__same_parser(other):
            return subprocess.STDOUT

        if self.__in_descriptor is None:
            self.clean()
            try:
                self.__parser.reset()
                self.__out_descriptor, self.__in_descriptor = os.openpty()
                self.__out = self.__prepare_descriptor(self.__out_descriptor)
            except:
                self.clean()
                raise

        return self.__in_descriptor

    def register(self, streams, other=None):
        if self.__same_parser(other):
            return

        streams[self.__out_descriptor] = self

    def process(self):
        data = None
        try:
            data = self.__out.read()
        except IOError as error:
            if error.errno != errno.EAGAIN:
                raise

        if data:
            self.__parse = self.__parse(data)

    def finalize(self):
        self.__parse = self.__parse()
