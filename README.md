percolator
==========

The library designed to run script and parse its output. It uses line buffered
pipe (os.openpty) to retrieve the output allowing to get "realtime" child
output in python script.

Build
-----

python setup.py build

Install
-------

python setup.py install

Test
----

python test/test.py

Coverage
--------

coverage run --source="${SITEPACKAGES}"/percolator test/test.py

coverage report -m
