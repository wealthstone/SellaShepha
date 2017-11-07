# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
useful dataframe code: https://gist.github.com/bsweger/e5817488d161f37dcbd2
"""
from iqfeed import historicData as iqfc
import pandas as pd
# import numpy as np
# import datetime
import scipy.io
import DataSys as dsys
import enum
# import IQFeedClient as iqfc

import logging
logging.basicConfig(filename="log.iqfeed.txt", level=logging.WARN)
logger = logging.getLogger(__name__)


class IQFeedImporter(object):
    __is_testing = False
    tickers = pd.DataFrame(
        columns=['symbol', 'date',
                 'open', 'high', 'low', 'close', 'volume'],
        index=['symbol', 'date'])

    symbols = []  # 'CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]
    
    def imp1_call_iqfeed(self, symbol, date_start, date_end):
        # x iqfeed = iqfc.IQFeedClient(feeder)
        iqreq = iqfc.historicData(date_start, date_end, 60)
        dframe = iqreq.download_symbol(symbol)
        return dframe
    
    def imp1_check_iqfeed_result(self, dframe):
        if not(dframe.empty):
            dframe.dropna(how='all')

        if dframe.empty:  # Note: Second check, not an else.
            logger.error("import_singleAsset failed: no data aquired.")
            return False
        
        return True

    def imp1_manip_result(self, symbol, dframe):
        # set column names
        dframe.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 
                          'other']

        # add column with symbol
        dframe['symbol'] = pd.Series([symbol for x in range(len(dframe.index))], 
                                     index=dframe.index)

        # set symbol and date column as multi index
        dframe.reindex(columns=['symbol', 'date'])

        return True

    def import_single_asset(self, symbol, date_start, date_end):
        '''
        imports single asset
        '''
        status = "failed. Import {0}".format(symbol) # todo: add date_start and end in status. 

        dframe = self.imp1_call_iqfeed(symbol, date_start, date_end)
        isok = self.imp1_check_iqfeed_result(self, dframe)
        if not isok:
            status = "import {0} failed: Empty or no results".format(symbol)
            logger.error(status)
            return status
 
        isok = self.imp1_manip_result(self, symbol, dframe)
        if not isok:
            status = "fail. Import {0}: Problem setting data".format(symbol)
            logger.error(status)
            return status
         
        self.tickers.append(dframe)

        status = "ok. Imported {0}".format(symbol)
        return status  # for testing that we got here
        
    def import_all_assets(self, date_start, date_end):
        self.load_symbols()  # get symbols list

        if self.symbols.count < 1:
            logger.error("Import all: Symbols not loaded correctly. Aborting")
            return

        for sym in self.symbols:
            data = self.import_single_asset(sym, date_start, date_end)
            data = "".join(data.split("\r"))
            data = data.replace(",\n", "\n")[:-1]

        # todo: write to database. 
        # currently: adding to tickers dataframe
        self.tickers.append(data)

        # Write the data stream to disk
        f = open("{0}.csv".format('sym'), "w")
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
            logger.error("Load symbols failed. No dataframe from %s",
                         file_location)
            return
        dframe = dframe.dropna(how='all')
        if dframe.empty:
            logger.error("Load symbols failed. All records were NA")
            return
        self.symbols = dframe.values.tolist()

    def loadBloomberg(self, date_start, date_end, symbol):
        dfld = dsys.DataFolders()
        comparefldr = dfld.compared
        datestring = "{0}_{1}".format(date_start, date_end)
        bloomfile = "bloomfile_{0}.xls".format(datestring)
        file_location = dsys.datafile(comparefldr, bloomfile)
        bloomcols = "1,2,3,4,5" 
        # "Date,PX_OPEN,PX_HIGH,PX_LOW,PX_LAST"

        dframe = pd.read_excel(file_location, index_col='date',
                               na_values='NA', parse_cols=bloomcols)
        return dframe

    def analyze_symbol(self, symbol, date_start, date_end):
        '''
        analyzes iqfeed vs. bloomberg
        outputs: in_iq, in_bloom, rejects, compared
        '''
        
        ''' ---
        pseudo: 
        a if condition else b
        startdate: max first1:first2
        enddate: min last1:last2

        find dates not in df1
        find dates not in df2
        for each line: na1, na2, na,
        for each line: zero2, (v1/v2)-1
          is number1, isnumber2 number2>0: (n1/n2)-1
        for each line:
        --- '''
        iq_only = pd.DataFrame(
            columns=['symbol', 'date', 
                     'open', 'high', 'low', 'close', 'volume'], 
            index=['symbol', 'date'])
        
        bloom_only = pd.DataFrame(
            columns=['symbol', 'date', 
                     'open', 'high', 'low', 'close', 'volume'], 
            index=['symbol', 'date'])

        compiled = pd.DataFrame(
            columns=['symbol', 'date', 
                     'open', 'high', 'low', 'close', 'volume',
                     'ook', 'hok', 'lok', 'cok', 'vok', 'rowok'],
            index=['symbol', 'date'])

        df1 = self.tickers.xs(symbol, level=('symbol'))
        if df1.empty:
            logger.error("Anaylyze %s failed: No feed data", symbol)
            return

        df2 = self.loadBloomberg(symbol, date_start, date_end)
        if df1.empty:
            logger.error("Anaylyze %s failed: No comparison data", symbol)
            return

        # 1. compare only dates inside both
        feedDate1 = df1['date'].head(1)
        bloomDate1 = df2['date'].head(1)  # .iloc[0]
        # df1['date'] = pd.to_datetime(df1['date'])
        date1 = max(feedDate1, bloomDate1)

        feedDate2 = df1['date'].tail(1)
        bloomDate2 = df2['date'].tail(1)
        date2 = min(feedDate2, bloomDate2)

        df1 = df1.xs(
            symbol, slice(date1, date2),
            level=('symbol', 'date'))

        # remove na-rows from both and then compare missing dates
        # Note: if both missing a date it will be removed without report
        # check na in columns except symbol and date
        cols1 = len(df1.columns) - 2
        cols2 = len(df2.columns) - 2
        df1 = df1.dropna(subset=df1.columns[cols1:], how='all')
        df2 = df2.dropna(subset=df2.columns[cols2:], how='all')

        # create the bloom only and iqfeed only
        dfcommon = df1.merge(df2, on=['symbol','date'])
        iq_only = df1[(~df1.index.isin(dfcommon.index))]
        bloom_only = df2[(~df1.index.isin(dfcommon.index))]
        
        # mark na's 
        # get the ratio and indication
        
        
        tolerance = 1.5  # config
        # see https://stackoverflow.com/questions/12376863/adding-calculated-columns-to-a-dataframe-in-pandas
        compiled = compiled.concat(common['symbol', 'date'])
        compiled['open']="na" if dp.isnull(df1['open']) else (df1['open']/df2['open'])-1
        df1['date'] = df1[(df1['i1'] == df1['i1']) & (df1['i1'] != 'z')]
        df2['i1'] = df2[(df2['i1'] == df1['i1']) & (df2['i1'] != 'z')]
        # Ratio1 = (df2['i1']).astype(float)/(df1['i1']).astype(float)
        # Indication1 = Ratio1 - 1
        # set indication in dataframe
        # mark over threshold
        

# ------------------------ Internals ---
    @staticmethod
    def __getTickerFilename(symbol, date_start, date_end, extention):
        '''
        filename for saving (or retrieving) iq data
        '''
        # x yyyymmdd_HHMMss = datetime.date.today().strftime('%Y%m%d_%H%M%s')
        dstart = date_start.strftime('%Y%m%d_%H%M%s')
        dend = date_end.strftime('%Y%m%d_%H%M%s')
        filename = "{0}_{1}_{2}.{3}".format(symbol, dstart, dend, extention)
        return filename

    @staticmethod
    def __getBloomFilename(symbol, date_start, date_end, extention):
        '''
        gets bloomberg filename
        '''
        # x yyyymmdd_HHMMss = datetime.date.today().strftime('%Y%m%d_%H%M%s')
        dstart = date_start.strftime('%Y%m%d_%H%M%s')
        dend = date_end.strftime('%Y%m%d_%H%M%s')
        filename = "{0}_{1}_{2}.{3}".format(symbol, dstart, dend, extention)
        return filename

    @staticmethod
    def __saveDataframe(dframe, file_details, filetype):
        if filetype == FilesaveType.matlab:
            datadict = dframe.to_dict()
            scipy.io.savemat(file_details, datadict)
            logger.debug("saved to matlab file: {0}".format(file_details))
        elif filetype == FilesaveType.excel:
            dframe.to_excel(file_details)
        elif filetype == FilesaveType.csv:
            dframe.to_csv(file_details)
        else:
            logger.error("Dataframe not saved. Wrong filetype supplied")


class FilesaveType(enum.Enum):
    matlab = ".mat"
    csv = ".csv"
    excel = ".xlsx"
