# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
"""

# todo move all this documentation out

'''
for reading IQFeed see:
 see  either this: https://pypi.python.org/pypi/iqfeed/0.4.3
 or BETTER:  https://github.com/luketighe/IQFeed

You must have IQFeed installed

For efficient comparison of rows see:
    https://stackoverflow.com/questions/38222751/how-to-efficiently-compare-rows-in-a-pandas-dataframe
    
    Currently using: 
        isin and has as follows
        DatesIn1 = Df1[~Df1['Time(hhmmssqqq)'].isin(Df2['Time(hhmmssqqq)'].tolist())]
        DatesIn2 = Df2[~Df2['Time(hhmmssqqq)'].isin(Df1['Time(hhmmssqqq)'].tolist())]
        DatesInBoth = Df1[Df1['Time(hhmmssqqq)'].isin(Df2['Time(hhmmssqqq)'].tolist())]
        Df1['i1'] = Df1.i1.str.replace(' ','-').replace('z','').replace('','-')
        
For testing we can print out a few lines of the dataframe:
    print(dataframe.head())
    
    for fromatting time: import datetime...  mydatetime.strftime('%d-%m-%Y') 
    
    save df to .map: 1. to dict, 2. scipy.savemat
      1. http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html
      2. https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.io.savemat.html
'''

# fix: cannot import name historicData
# see: https://stackoverflow.com/questions/47015061/python-error-cannot-import-name-historicdata-from-iqfeed

# todo: future - test should not write to actual data folder.
# todo: Moshe to find advanced visual Python testing environment

# fix: insert logging in project:
#       e.g. logger.error("error message...")

# instead of pythonpath
# import sys
# sys.path.insert(0,'c:\\dev\\SellaShepha\\src\\packages\\IQFeed-master' )


from iqfeed import historicData
import pandas as pd
import numpy as np
import datetime
import scipy.io

import logging
logging.basicConfig(filename="log.wprophet.iqfeedlog.txt", level=logging.WARN)
logger = logging.getLogger(__name__)


class IQFeedImporter():
    is_testing = False
    tickers = pd.DataFrame()
    symbols = [] #'CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]

    def __init__():
        pass


    def getTickerFilename(self, symbol):
        yyyymmdd_HHMMss = datetime.date.today().strftime('%Y%m%d_%H%M%s')
        filename = "".format('{symbol}{yyyymmdd_HHMMss}', symbol, yyyymmdd_HHMMss)
        return filename

    
    def import_singleAsset(self, dateStart, dateEnd, symbol):
        
        iq = historicData(dateStart, dateEnd, 60)
        symbolOneData = iq.download_symbol(symbol)
        self.tickers.concatenate(symbolOneData)
        saveDataframe() # fix
        # fix todo: store in .mat file and in database
        

    def import_allAssets(self, dateStart, dateEnd):
        self.load_symbols()
        
        #todo: read from symbols table
        if self.symbols.count < 1:
            logger.error("Symbols count is less than 1")
            return

        for sym in self.symbols:
            data = self.import_feed_symbol(dateStart, dateEnd, sym)
            data = "".join(data.split("\r"))
            data = data.replace(",\n","\n")[:-1]
        # Write the data stream to disk
        f = open("{sym}.csv".format('sym'), "w")
        f.write(data)
        f.close()

    def load_symbols(self):
        datapath = __getDataPath(isTest=False) # todo: isTest as param?  as config? 
        assetFilename = "symbols.xlsx" # "AssetNamesNew.v01.xlsx"  # todo: config
        fileLocation = "{0}\\{1}".format(datapath, assetFilename)  # todo: config
        symbolsColumn = "C"  # todo: config
        df = pd.read_excel(fileLocation, index_col=None, na_values='NA', parse_cols=symbolsColumn)        
        if df.empty:
            logger.error("Load symbols failed. No dataframe from {0}", fileLocation )
            return
        df = df.dropna(how='all')
        if df.empty:
            logger.error("Load symbols failed. All records were NA")
            return
        self.symbols = df.values.tolist()
        

#
#        # df = load_assetNames() # todo: do i need to put assetNames here
#        # fix: self.symbols = df. get column 5
#        # only if row not empty and if not 'N/A'
#        # fix: if self.symbols is null or .count < 1
#        #    log.error("symbols no loaded")
#
#    def load_assetNames(self):
#        datapath = __getDataPath(isTest=False) # todo: isTest as param?  as config? 
#        assetFilename = "AssetNamesNew.v01.xlsx"  # todo: config
#        pathname = "{0}\\{1}".format(datapath, assetFilename)  # todo: config
#        assetColsToParse = [1, 2, 3]                       # todo: config
#
#        result = pd.read_excel(io=pathname, sheetname=sheetname, header=1,
#                      parse_cols = assetColsToParse)
#
#        if result.empty:
#             logger.error("Could not Open %s", pathname)
#
#        return result

    def loadBloomberg(self):
        bloompath = 
        df = pd.read_excel()

    def analyze(self, dfIQ, dfBloom):
        
        
        
# ------------------------ Internals ---
        # todo: move these to the project utils class
        # todo: make these relative
        
    def __addPaths(a,b)
        return "{0}\\{1}".format(a,b)
    
    def __getProjectPath():
        return "C:\dev\SellaShepha"
    
    def __getAquiredPath():
        projpath = __getProjectPath()
        return __addPaths(projpath, "Aquired")

    def __getDataPath(isTest):  # todo: config
        projpath = __getProjectPath()
        if isTest:
            return __addPaths(projpath, "data\results")
        else:
            return __addPaths(projpath, data\testing"

    def __saveDataframe(dataframe, path, filename, ismatlab):
        if ismatlab:
            datadict = dataframe.to_dict()
            scipy.io.savemat(filename, datadict)
            logger.debug("".format('saved to matlab file: {filename}', filename)


#  ----------------- Internals 
        #todo move internals out to static utils class 
    
    
    


