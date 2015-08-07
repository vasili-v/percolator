import unittest

import test_base
import test_collector
import test_null
import test_printer
import test_splitter

test_suite = unittest.TestSuite((test_base.test_suite,
                                 test_collector.test_suite,
                                 test_null.test_suite,
                                 test_printer.test_suite,
                                 test_splitter.test_suite))

if __name__ == '__main__':
    unittest.main()
