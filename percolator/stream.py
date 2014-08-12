import os

class Stream(object):
    def __init__(self, event):
        self.__event = event

        self.__out_descriptor = None
        self.__in_descriptor = None

    def __clean(self):
        if self.__out_descriptor is not None:
            try:
                os.close(self.__out_descriptor)
            finally:
                self.__out_descriptor = None

        if self.__in_descriptor is not None:
            try:
                os.close(self.__in_descriptor)
            finally:
                self.__in_descriptor = None

    def get_descriptor(self):
        if self.__out_descriptor is None:
            self.__clean()
            self.__out_descriptor, self.__in_descriptor = os.openpty()

        return self.__out_descriptor

    def stop(self):
        self.__clean()
