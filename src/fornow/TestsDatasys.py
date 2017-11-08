''' tests datasys module '''

import unittest
# import unittest.mock as mck
import datetime as dt
import DataSys as dsys


class TestsDatasys(unittest.TestCase):
    ''' tests for datasys module and class '''

    def test_datafile_details_bloomberg_compare(self):
        ''' tests filedetails for bloomberg comparison '''
        expected = "bla"
        symbol = "bla"
        date_start = dt.datetime(2015, 1, 1)
        date_end = dt.datetime(2016, 1, 1)
        actual = dsys.DataSys.datafile_details(
            dsys.Prefixes.bloomberg_compare,
            dsys.DataFolders.compared,
            symbol, date_start, date_end,
            dsys.Extensions.excel)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
