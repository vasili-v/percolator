percolator
==========

Run script and parse its output

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
