import os
import threading

class Stream(object):
    def __init__(self, event):
        self.__event = event

        self.__thread = None
        self.__out_descriptor = None
        self.__in_descriptor = None

    def __clean(self):
        self.__thread = None
        try:
            os.close(self.__out_descriptor)
        except:
            pass
        self.__out_descriptor = None

        try:
            os.close(self.__in_descriptor)
        except:
            pass
        self.__in_descriptor = None

    def __source(self):
        while not self.__event.is_set():
            self.__event.wait(.1)

    def __start(self):
        self.__thread = threading.Thread(None, self.__source)
        self.__thread.start()

    def get_descriptor(self):
        if self.__out_descriptor is None:
            self.__clean()
            try:
                self.__out_descriptor, self.__in_descriptor = os.openpty()
                self.__start()
            except:
                self.__clean()
                raise

        return self.__out_descriptor

    def stop(self):
        try:
            self.__thread.join()
        except:
            pass
        self.__clean()
