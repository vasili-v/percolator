import sys
import os
from coverage import coverage as Coverage

from distutils.core import setup
from distutils.cmd import Command
from unittest import main

test_modules = {'all': 'test.test',
                'runner': 'test.test_runner',
                'stream': 'test.test_stream',
                'streams': 'test.test_streams',
                'parsers': 'test.test_parsers',
                'base': 'test.test_parsers_base',
                'null': 'test.test_parsers_null',
                'splitter': 'test.test_parsers_splitter',
                'collector': 'test.test_parsers_collector',
                'printer': 'test.test_parsers_printer'}

class _Coverage(object):
    def __init__(self, *args, **kwargs):
        pass

    def start(self, *args, **kwargs):
        pass

    def stop(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

class test(Command):
    description = 'run tests for the package'

    user_options = [('module=', 'm', 'set of modules to test: all, runner, ' \
                                     'stream, streams, parsers, base, null, ' \
                                     'splitter, collector and printer ' \
                                     '(several modules can be listed using ' \
                                     'comma)'),
                    ('coverage-base', None, 'base installation directory'),
                    ('coverage', 'c', 'calculate test coverage')]

    boolean_options = ['coverage']

    def initialize_options(self):
        self.module = None
        self.coverage_base = None
        self.coverage = None

    def finalize_options(self):
        self.set_undefined_options('install',
                                   ('install_purelib', 'coverage_base'))

    def run(self):
        if self.module:
            modules = set([item.strip().lower() \
                               for item in self.module.split(',')])
        else:
            modules = ['all']

        if 'all' in modules and len(modules) > 1:
            raise Exception('"all" can\'t be used with other modules')

        for module in modules:
            if module not in test_modules:
                raise Exception('"%s" is not a valid module name' % module)

        coverage = Coverage if self.coverage else _Coverage
        source=[os.path.join(self.coverage_base, 'percolator')]
        coverage = coverage(source=source)

        for module in modules:
            coverage.start()
            try:
                sys.path.insert(0, self.coverage_base)
                main(test_modules[module], argv=sys.argv[:1], exit=False,
                     verbosity=self.verbose)
            finally:
                if sys.path[0] == self.coverage_base:
                    del sys.path[0]

            coverage.stop()

        if self.coverage:
            print '\nCoverage report:'
        coverage.report(show_missing=True)

setup(name='Percolator',
      version='0.0.1',
      description='Run script and parse its output',
      long_description='The library designed to run script and parse its ' \
                       'output. It uses line buffered pipe (os.openpty) ' \
                       'to retrieve the output allowing to get "realtime" ' \
                       'child output in python script (see README.md file)',
      author='Vasili Vasilyeu',
      author_email='vasili.v@tut.by',
      url='https://github.com/vasili-v/percolator',
      packages=['percolator', 'percolator.parsers'],
      license='MIT',
      platforms=('Linux', 'Darwin'),
      cmdclass={'test': test})

