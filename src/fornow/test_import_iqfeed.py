'''
Created on Tue Oct 24 10:19:10 2017

@author: pashute

  see youtube: python unitests https://www.youtube.com/watch?v=6tNS--WetLI
  testcase documentation:
    https://docs.python.org/2/library/unittest.html#unittest.TestCase
  python -m unittest test_...
  mock a module: 
    https://stackoverflow.com/questions/8658043/how-to-mock-an-import

# -*- coding: utf-8 -*-
'''

import unittest
import unittest.mock
import datetime as dt
import pandas as pd
# import numpy as np
import sys

# import tests_setup
# tests_setup.setpaths()
# print(sys.path)
import IQFeedImporter as iqfi


class TestIqFeedImport(unittest.TestCase):
    '''
    test IQFeedImport class and methods
    '''

    '''-- def test_setup(self):
        result = tests_setup.curpaths()
        iqfeeder = "c:\\dev\\SellaShepha\\src\\IQFeeder"
        isok = self.assertIn(iqfeeder, result, "paths not set up")
        if not isok:
            tests_setup.setpaths()
            self.assertIn(iqfeeder, result, "paths still not set up")
    --'''

    def test_import_single_asset__returns_dataframe(self):
        expected = "tbd: mock"
        actual = "test not implemented"
        self.assertEqual(expected, actual)

    def test_import_single_asset__result_validated(self):
        symbol = "asymbol"  # todo: test settings?
        dframe = __fakeimported(symbol)                    

        iqimporter = iqfi.IQFeedImporter()
        actual = iqimporter.imp1_check_iqfeed_result(dframe)
        self.assertTrue(actual)

    def test_import_single_asset__result_manipulated(self):
        actual = False  # todo: call method with dataframe and symbol
        self.assertTrue(actual)

    def test_import_single_asset(self):
        '''
        Tests all single asset importing
        '''
        symbol = "SPX.XO"
        
        sys.modules['iqfeed'] = Mock()
        iqf = iqfi.IQFeedImporter()
        # self.assertIsNotNone(iqf, "Cannot create IQFeed class")

        date_start = dt.datetime(2015, 10, 1)
        date_end = dt.datetime(2016, 10, 1)
        actual = iqf.import_single_asset(symbol, date_start, date_end)
        expected = "ok."
        self.assertTrue(actual.startswith(expected))

    def test_import_all_assets(self):
        '''
        tests importing all assets according to symbols list
        '''
        iqf = iqfi.IQFeedImporter()
        self.assertIsNotNone(iqf, "Cannot create IQFeed class")

        date_start = dt.datetime(2014, 10, 1)
        date_end = dt.datetime(2015, 10, 1)
        dframe = iqf.import_all_assets(date_start, date_end)
        self.assertIsNotNone(dframe, "No data retreived")

        result = iqf.tickers
        self.assertTrue(not result.empty)

    # todo: other tests (1) nose2 ? , (2) Robot ?,


def __fakeimported(symbol):
    drange = pd.date_range('1/1/2015', periods=5, freq='D')
    dframe = pd.Series(drange, 'asymbol', 2, 7, 1, 6, 0, 0)
    return dframe


if __name__ == '__main__':
    unittest.main()
