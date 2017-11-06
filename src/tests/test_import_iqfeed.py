'''
Created on Tue Oct 24 10:19:10 2017

@author: pashute

  see youtube: python unitests https://www.youtube.com/watch?v=6tNS--WetLI
  testcase documentation:
    https://docs.python.org/2/library/unittest.html#unittest.TestCase
  python -m unittest test_...

# -*- coding: utf-8 -*-
'''

import unittest
import datetime as dt
import tests_setup
import sys
tests_setup.setpaths()
print(sys.path)
import IQFeedImporter


class TestIqFeedImport(unittest.TestCase):
    '''
    test IQFeedImport class and methods
    '''

    def test_setup(self):
        result = tests_setup.curpaths()
        iqfeeder = "c:\\dev\\SellaShepha\\src\\IQFeeder"
        isok = self.assertIn(iqfeeder, result, "paths not set up")
        if not isok:
            tests_setup.setpaths()
            self.assertIn(iqfeeder, result, "paths still not set up")
       
    def test_import_single_asset(self):
        '''
        Tests singal asset importing
        '''
        symbol = "SPX.XO"

        iqf = IQFeedImporter.IQFeedImporter()
        self.assertIsNotNone(iqf, "Cannot create IQFeed class")

        date_start = dt.datetime(2015, 10, 1)
        date_end = dt.datetime(2016, 10, 1)
        result = iqf.import_single_asset(symbol, date_start, date_end)
        self.assertIsNotNone(result,
                             "No data for symbol {0}".format(symbol))
        self.assertTrue(not result.empty, "")

    def test_import_all_assets(self):
        iqf = IQFeedImporter.IQFeedImporter()
        self.assertIsNotNone(iqf, "Cannot create IQFeed class")

        date_start = dt.datetime(2014, 10, 1)
        date_end = dt.datetime(2015, 10, 1)
        df = iqf.import_all_assets(date_start, date_end)
        self.assertIsNotNone(df, "No data retreived")

        result = iqf.tickers
        self.assertTrue(not result.empty)

    # todo: other tests (1) nose2 ? , (2) Robot ?,


if __name__ == '__main__':
    unittest.main()
