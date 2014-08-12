import subprocess
import threading

from percolator.stream import Stream

class Runner(object):
    def __init__(self, environment=None):
        self.__environment = dict(environment) if environment else {}

        self.__event = threading.Event()

        self.__stdout = Stream(self.__event)
        self.__stderr = Stream(self.__event)

    def run(self, command):
        self.__event.clear()
        try:
            stdout = self.__stdout.get_descriptor()
            stderr = self.__stderr.get_descriptor()

            process = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                       env=self.__environment)
            return process.wait()

        finally:
            self.__event.set()

            self.__stdout.stop()
            self.__stderr.stop()

