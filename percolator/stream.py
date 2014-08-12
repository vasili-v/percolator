import os
import fcntl
import errno

class Stream(object):
    def __init__(self):
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
        self.__out_descriptor = None
        self.__out = None

        try:
            os.close(self.__in_descriptor)
        except:
            pass
        self.__in_descriptor = None

    @staticmethod
    def __prepare_descriptor(descriptor):
        flags = fcntl.fcntl(descriptor, fcntl.F_GETFL)
        fcntl.fcntl(descriptor, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        return os.fdopen(descriptor)

    def get_descriptor(self):
        if self.__in_descriptor is None:
            self.clean()
            try:
                self.__out_descriptor, self.__in_descriptor = os.openpty()
                self.__out = self.__prepare_descriptor(self.__out_descriptor)
            except:
                self.clean()
                raise

        return self.__in_descriptor

    def register(self, streams):
        streams[self.__out_descriptor] = self

    def process(self):
        try:
            self.__out.read()
        except IOError as error:
            if error.errno != errno.EAGAIN:
                raise

