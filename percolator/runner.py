class Runner(object):
    def __init__(self, environment=None):
        self.__environment = dict(environment) if environment else {}

