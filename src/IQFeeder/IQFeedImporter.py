# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
"""
'''
 see  either this: https://pypi.python.org/pypi/iqfeed/0.4.3
 or BETTER:  https://github.com/luketighe/IQFeed
'''

# todo: future - test should not write to actual data folder.
# todo: Moshe to find advanced visual Python testing environment 

from iqFeed import historicData
# import numpy as np
import pandas as pd 
import logging as lg                           # todo: logging

class IQFeedImporter():
    
    tickers = pd.DataFrame()
    symbols = [] #'CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]
    
    def __init__():
        pass
        
    
    def import_feed_symbol(self, dateStart, dateEnd, symbol):
        iq = historicData(dateStart, dateEnd, 60)
        symbolOneData = iq.download_symbol(symbol)
        self.tickers.concatenate(symbolOneData)
        
        # todo: store in .mat file and in database

    def importFeedAll(self, dateStart, dateEnd):
        #todo: read from symbols table
        
        for sym in self.symbols:
            data = self.import_feed_symbol(dateStart, dateEnd, sym)
            data = "".join(data.split("\r"))
            data = data.replace(",\n","\n")[:-1]
        # Write the data stream to disk
        f = open("%s.csv" % sym, "w")
        f.write(data)
        f.close()
        # Remark 

    def readAssetNames():
        pathname = "C:\\dev\\Data\\AssetNamesNew.v01.xlsx" # todo: config  
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
                      