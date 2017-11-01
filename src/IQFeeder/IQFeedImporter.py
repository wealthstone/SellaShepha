# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
"""
'''
 see  either this: https://pypi.python.org/pypi/iqfeed/0.4.3
 or BETTER:  https://github.com/luketighe/IQFeed
'''

# fix: cannot import name historicData 
# see: https://stackoverflow.com/questions/47015061/python-error-cannot-import-name-historicdata-from-iqfeed

# todo: future - test should not write o actual data folder.
# todo: Moshe to find advanced visual Python testing environment 

# fix: insert logging in project: 
#       e.g. logger.error("error message...")

from iqfeed import historicData
# import numpy as np
import pandas as pd 
import logging as lg                           # todo: logging

class IQFeedImporter():
    is_testing = False
    tickers = pd.DataFrame()
    symbols = [] #'CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]
    
    def __init__():
        pass
        
    
    def import_feed(self, dateStart, dateEnd, symbol):
        iq = historicData(dateStart, dateEnd, 60)
        symbolOneData = iq.download_symbol(symbol)
        self.tickers.concatenate(symbolOneData)
        
        # todo: store in .mat file and in database


    def import_feeds_all(self, dateStart, dateEnd):
        #todo: read from symbols table
        if self.symbols.count < 1:
            # fix: log.error(" ") 
            return
        
        for sym in self.symbols:
            data = self.import_feed_symbol(dateStart, dateEnd, sym)
            data = "".join(data.split("\r"))
            data = data.replace(",\n","\n")[:-1]
        # Write the data stream to disk
        f = open("%s.csv" % sym, "w")
        f.write(data)
        f.close()

    def load_symbols(self):
        df = load_assetNames() # todo: do i need to put assetNames here
        # fix: self.symbols = df. get column 5 
        # only if row not empty and if not 'N/A'
        # fix: if self.symbols is null or .count < 1 
        #    log.error("symbols no loaded")

    def load_assetNames(self):
        pathname = ""
        
        # pathname = "C:\\dev\\Data\\AssetNamesNew.v01.xlsx" # todo: config  
        pathname = "..\\dev\\data\\testing"
        sheetname = "Technical"                            # todo: config  
        assetColsToParse = [1, 2, 3]                       # todo: config
        
        '''
        read_excel(io, sheetname=0, header=0, 
                   skiprows=None, skip_footer=0, 
                   index_col=None, names=None, 
                   parse_cols=None, parse_dates=False, 
                   date_parser=None, na_values=None, 
                   thousands=None, convert_float=True,
                   has_index_names=None, converters=None,
                   dtype=None, true_values=None, 
                   false_values=None, engine=None,
                   squeeze=False, **kwds
        '''
        result = pd.read_excel(io=pathname, sheetname=sheetname, header=1, 
                      parse_cols = assetColsToParse)
        
        if result.empty:
             lg.error("Could not Open %s", pathname) 
             
        return result
                      