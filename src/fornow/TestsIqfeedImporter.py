'''
Created on Tue Oct 24 10:19:10 2017

@author: pashute


# -*- coding: utf-8 -*-
'''

import unittest
import unittest.mock as mck
import datetime as dt
import pandas as pd
# import numpy as np
# import sys
import DataSys as dsys

# import tests_setup
# tests_setup.setpaths()
# print(sys.path)
import IQFeedImporter as iqfi

dsys.DataSys.is_testing = True


class TestsIqfeedImporter(unittest.TestCase):
    '''
    tests for IQFeedImport class and module
    '''

    '''-- def test_setup(self):
        result = tests_setup.curpaths()
        iqfeeder = "c:\\dev\\SellaShepha\\src\\IQFeeder"
        isok = self.assertIn(iqfeeder, result, "paths not set up")
        if not isok:
            tests_setup.setpaths()
            self.assertIn(iqfeeder, result, "paths still not set up")
    --'''

    def test_import_single_asset_returns_dataframe(self):
        ''' tests that import returns a dataframe using mock '''

        sys.modules['iqfeed'] = mck.Mock()
        iqf = iqfi.IQFeedImporter()

        symbol = "SPX.XO"
        date_start = dt.datetime(2015, 10, 1)
        date_end = dt.datetime(2016, 10, 1)

        actual = iqf.imp1_call_iqfeed(symbol, date_start, date_end)
        # expected = True
        self.assertTrue(actual)

    def test_import_single_asset__result_validated(self):
        ''' tests that result is validated'''
        symbol = "asymbol"  # todo: test settings?
        dframe = __fake_df_imported(symbol)

        iqf = iqfi.IQFeedImporter()
        actual = iqf.imp1_check_iqfeed_result(dframe)
        self.assertTrue(actual)

    def test_import_single_asset__result_manipulated(self):
        ''' tests that columns and index inserted in asset dataframe'''
        actual = False  # todo: call method with dataframe and symbol
        self.assertTrue(actual)

    def test_load_symbols(self):
        iqf = iqfi.IQFeedImporter()
        symbols = iqf.load_symbols()
        # expected = not isnull(symbols) & symbols.count > 0
        self.assertIsNotNone(symbols)
        self.assertGreater(len(symbols), 0)

    def test_import_single_asset(self):
        ''' Tests all single asset importing '''
        symbol = "SPX.XO"

        sys.modules['iqfeed'] = mck.Mock()
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


def __fake_df_imported(symbol):
    drange = pd.date_range('1/1/2015', periods=5, freq='D')
    dframe = pd.Series(drange, symbol, 2, 7, 1, 6, 0, 0)
    return dframe


if __name__ == '__main__':
    unittest.main()
