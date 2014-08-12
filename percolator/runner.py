import subprocess

from percolator.stream import Stream

class Runner(object):
    def __init__(self, environment=None):
        self.__environment = dict(environment) if environment else {}

        self.__stdout = Stream()
        self.__stderr = Stream()

    def run(self, command):
        try:
            stdout = self.__stdout.get_descriptor()
            stderr = self.__stderr.get_descriptor()

            process = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                       env=self.__environment)
            return process.wait()

        finally:
            self.__stdout.stop()
            self.__stderr.stop()

