from setuptools import setup, find_packages

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
      packages = find_packages(exclude=['test']),
      license='MIT',
      platforms=('Linux', 'Darwin'),
      test_suite = "test")
