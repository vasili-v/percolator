import os
import fcntl
import errno
import subprocess

from percolator.parsers.base import Base
from percolator.parsers.null import Null

class ParserStream(object):
    def __init__(self, parser=Null):
        self.__parser = parser
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

    @staticmethod
    def __prepare_descriptor(descriptor):
        flags = fcntl.fcntl(descriptor, fcntl.F_GETFL)
        fcntl.fcntl(descriptor, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        return os.fdopen(descriptor)

    def begin(self):
        if self.__in_descriptor is None:
            self.clean()
            try:
                self.__parser.reset()
                self.__out_descriptor, self.__in_descriptor = os.openpty()
                self.__out = self.__prepare_descriptor(self.__out_descriptor)
            except:
                self.clean()
                raise

        return self.__out_descriptor, self.__in_descriptor

    def parse(self, data=None):
        parse = self.__parse(data)
        if parse:
            self.__parse = parse

    def process(self):
        data = None
        try:
            data = self.__out.read()
        except IOError as error:
            if error.errno != errno.EAGAIN:
                raise

        if data:
            self.parse(data)

class RunnerStream(object):
    def __init__(self, runner):
        self.__runner = runner

    def clean(self):
        pass

    def begin(self):
        return None, subprocess.PIPE

def make_stream(receiver):
    if isinstance(receiver, Base):
        return ParserStream(receiver)

    from percolator.runner import Runner
    if isinstance(receiver, Runner):
        return RunnerStream(receiver)

    raise RuntimeError('Can\'t redirect to %s. '
                       'Receiver should be a parser or a runner' % repr(receiver))
