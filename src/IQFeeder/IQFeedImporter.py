# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
"""
from iqfeed import historicData
import pandas as pd
# import numpy as np
import datetime
import scipy.io
import DataSys as dsys


import logging
logging.basicConfig(filename="log.iqfeed.txt", level=logging.WARN)
logger = logging.getLogger(__name__)


class IQFeedImporter(object):
    __is_testing = False
    tickers = pd.DataFrame()
    symbols = []  # 'CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]

    def __getTickerFilename(self, symbol):
        yyyymmdd_HHMMss = datetime.date.today().strftime('%Y%m%d_%H%M%s')
        filename = "{symbol}{yyyymmdd_HHMMss}".format(symbol, yyyymmdd_HHMMss)
        return filename

    def import_single_asset(self, dateStart, dateEnd, symbol):
        '''
        imports single asset
        '''
        iq = historicData(dateStart, dateEnd, 60)
        df = iq.download_symbol(symbol)
        if not(df.empty):
            df.dropna(how='all')

        if df.empty:  # Note: Second check, not an else. 
            logger.error("import_singleAsset failed: no data aquired.")
            return

        self.tickers.concatenate(df)
        logger.info("import_singleAsset succeeded") 
        #       , symbol, dateStart, dateEnd
      
    def import_all_assets(self, date_start, date_end):
        self.load_symbols()

        # todo: read from symbols table
        if self.symbols.count < 1:
            logger.error("Symbols count is less than 1")
            return

        for sym in self.symbols:
            data = self.import_single_asset(date_start, date_end, sym)
            data = "".join(data.split("\r"))
            data = data.replace(",\n", "\n")[:-1]

        # Write the data stream to disk
        f = open("{sym}.csv".format('sym'), "w")
        f.write(data)
        f.close()

    def load_symbols(self):
        '''
        loads symbols-list from excel
        '''
        dfld = dsys.DataFolders()
        settingsfldr = dfld.settings 
        assetslistfile = "assets.xlsx"  # "AssetNamesNew.v01.xlsx"  

        file_location = dsys.datafile(settingsfldr, assetslistfile)
        symbols_column = "C"  # todo: config
        dframe = pd.read_excel(file_location, index_col=None, 
                               na_values='NA', parse_cols=symbols_column)
        if dframe.empty:
            logger.error("Load symbols failed. No dataframe from {0}"
                         .format(file_location))
            return
        dframe = dframe.dropna(how='all')
        if dframe.empty:
            logger.error("Load symbols failed. All records were NA")
            return
        self.symbols = dframe.values.tolist()

    def loadBloomberg(self, dateStart, dateEn):
        dfld = dsys.DataFolders()
        comparefldr = dfld.compared
        bloomfile = "bloomFile.xls"
        file_location = dsys.datafile(comparefldr, bloomfile)
        bloomcols = "C,D,E,F"
        
        dframe = pd.read_excel(file_location, index_col=None, 
                               na_values='NA', parse_cols=bloomcols)
        return dframe

    def analyze(self, df1, df2, symbol):
        '''
        a if condition else b
        find dates not in first df
        find dates not in second df
        for each line: na1, na2, na, 
        for each line: zero2, (v1/v2)-1
          is number1, isnumber2 number2>0: (n1/n2)-1
        for each line:  
        '''

        # compare only dates
        df1['date'] = df1[(df1['i1'] == df1['i1']) & (df1['i1'] != 'z')]
        df2['i1'] = df2[(df2['i1'] == df1['i1']) & (df2['i1'] != 'z')]
        Ratio1 = (df2['i1']).astype(float)/(df1['i1']).astype(float)
        Indication1 = Ratio1 - 1


# ------------------------ Internals ---
    @staticmethod
    def __saveDataframe(dataframe, path, filename, ismatlab):
        if ismatlab:
            datadict = dataframe.to_dict()
            scipy.io.savemat(filename, datadict)
            logger.debug("saved to matlab file: {filename}".format(filename))

