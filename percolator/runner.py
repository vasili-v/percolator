import subprocess

class Runner(object):
    def __init__(self, environment=None):
        self.__environment = dict(environment) if environment else {}

    def run(self, command):
        process = subprocess.Popen(command, env=self.__environment)
        return process.wait()

