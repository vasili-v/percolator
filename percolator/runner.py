import subprocess

from percolator.streams import Streams

class Runner(object):
    def __init__(self, stdout=None, stderr=None, environment=None):
        self.__environment = dict(environment) if environment else {}

        self.__streams = Streams(stdout, stderr)

    def run(self, command):
        try:
            stdout, stderr = self.__streams.begin()
            process = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                       env=self.__environment)
            while True:
                self.__streams.process()
                if process.poll() is not None:
                    return process.returncode

        finally:
            self.__streams.clean()

