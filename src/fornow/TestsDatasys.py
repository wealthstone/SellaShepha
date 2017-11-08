''' tests datasys module '''

import unittest
# import unittest.mock as mck
import datetime as dt
import DataSys as dsys


class TestsDatasys(unittest.TestCase):
    ''' tests for datasys module and class '''

    # projectfolder = sys.os.currentfolder or something like that
    PROJ_FOLDER = "c:\\dev\\SellaShepha"


    def test_datafile_details_bloomberg_compare(self):
        ''' tests filedetails for bloomberg comparison '''

        # projectfolder = sys.os.currentfolder or something like that
        symbol = "bla"
        expected = self.expected(
            symbol,
            "data\\compare\\bloom_", 
            "_20150101_20160101.xlsx")

        date_start = dt.datetime(2015, 1, 1)
        date_end = dt.datetime(2016, 1, 1)
        actual = dsys.DataSys.datafile_details(
            dsys.Prefixes.bloomberg_compare, dsys.DataFolders.compare_from,
            symbol, date_start, date_end,
            dsys.Extensions.excel)
        self.assertEqual(expected, actual)

    def test_datafile_details_compiled_testing(self):
        ''' 
        tests filedetails for compiled output in reality
        '''
        symbol = "bla"
        expected = self.expected(
            symbol,
            "data\\testing\\compiled\\ok_", 
            "_20150101_20160101.xlsx")

        saved_testingstate = dsys.DataSys.is_testing
        dsys.DataSys.is_testing = True
        symbol = "bla"

        date_start = dt.datetime(2015, 1, 1)
        date_end = dt.datetime(2016, 1, 1)
        actual = dsys.DataSys.datafile_details(
            dsys.Prefixes.compiled, dsys.DataFolders.compiled,
            symbol, date_start, date_end,
            dsys.Extensions.excel)
        self.assertEqual(expected, actual)
        
        ' clean up'
        dsys.DataSys.is_testing = saved_testingstate

    def test_datafile_details_compiled_real(self):
        ''' tests compiled file details from real run (not testing) '''

        saved_testingstate = dsys.DataSys.is_testing
        dsys.DataSys.is_testing = False

        symbol = "bla"
        expected = self.expected(
            symbol,
            "data\\compiled\\ok_", 
            "_20150101_20160101.xlsx")

        date_start = dt.datetime(2015, 1, 1)
        date_end = dt.datetime(2016, 1, 1)
        actual = dsys.DataSys.datafile_details(
            dsys.Prefixes.compiled,
            dsys.DataFolders.compiled,
            symbol, date_start, date_end,
            dsys.Extensions.excel)
        self.assertEqual(expected, actual)
        
        ' clean up'
        dsys.DataSys.is_testing = saved_testingstate

    @staticmethod
    def expected(symbol, part1, part2):
        return "{0}\\{1}{2}{3}".format(
                TestsDatasys.PROJ_FOLDER, 
                part1, symbol, part2)


if __name__ == '__main__':
    unittest.main()
