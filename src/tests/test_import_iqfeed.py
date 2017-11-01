# -*- coding: utf-8 -*-
'''
Created on Tue Oct 24 10:19:10 2017

@author: pashute

  see youtube: python unitests https://www.youtube.com/watch?v=6tNS--WetLI
  testcase documentation: https://docs.python.org/2/library/unittest.html#unittest.TestCase
  python -m unittest test_...
'''
import unittest
import datetime
import sys
sys.path.insert(0, 'C:\\dev\\SellaShepha\\src\\IQFeeder\\')
import IQFeedImporter


class TestIqFeedImport(unittest.TestCase):
   
    def test_import_singleAsset(self):
        symbol = "SPX.XO"

        # how do I call the iqfeed class
        #  we are in src/tests/test_import_iqfeed.py
        #  FeedImporter is in src/IQFeeder/FeedImporter
        # nope

        iqf = IQFeedImporter()
        self.assertIsNotNone(iqf, "Cannot create IQFeed class")


        dateStart = datetime.datetime(2014,10,1)
        dateEnd = datetime.datetime(2015,10,1)
        df = iqf.import_singleAsset(dateStart, dateEnd, symbol)
        self.assertIsNotNone(df, "No data retreived")

        result = False  # failing by design
        self.assertTrue(result)

    def test_import_allAssets(self):
        iqf = IQFeedImporter()
        self.assertIsNotNone(iqf, "Cannot create IQFeed class")

        dateStart = datetime.datetime(2014,10,1)
        dateEnd = datetime.datetime(2015,10,1)
        df = iqf.import_allAssets(dateStart, dateEnd)
        self.assertIsNotNone(df, "No data retreived")

        result = False  # failing by design


        self.assertTrue(result)

    # todo: other tests (1) nose2 ? , (2) Robot ?,

if __name__ == '__main__':
    unittest.main()
