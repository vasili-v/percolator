[![Build Status](https://scrutinizer-ci.com/g/vasili-v/percolator/badges/build.png?b=master)](https://scrutinizer-ci.com/g/vasili-v/percolator/build-status/master) [![Code Coverage](https://scrutinizer-ci.com/g/vasili-v/percolator/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/vasili-v/percolator/?branch=master)
#percolator
The library designed to run script and parse its output. It uses line buffered
pipe (os.openpty) to retrieve the output allowing to get "realtime" child
output in python script.
