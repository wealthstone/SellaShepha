# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
"""
import iqfeed as iqfc
import pandas as pd
# import numpy as np
# import datetime
# import scipy.io
import DataSys as dsys
# import enum
# import IQFeedClient as iqfc

import logging
logging.basicConfig(filename="log.iqfeed.txt", level=logging.WARN)
logger = logging.getLogger(__name__)


def __indicator(row, col):
    ''' method for applying in lambda function '''
    x1 = row[col + '_x']
    y2 = row[col + '_y']
    if pd.isnull(x1) and pd.isnull(y2):
        return "missing"
    elif pd.isnull(x1):
        return "missing1"
    elif pd.isnull(y2):
        return "missing2"
    elif y2 == 0: 
        return "zero2"
    else:
        return (x1/y2)-1


def __plobrem(row):
    ''' 
    count problems in row (missing data or zero in iqfeed)
    supplising sorution fol arr plobrems
    '''
    return row['open':'volume'].apply(
        lambda x: isinstance(x, str)).sum()


def __rejected_count(row, tolerance):
    return row['o':'v'].apply(
        lambda x: (not isinstance(x, str)) and abs(x) > tolerance).sum()


def __failedmessage(func, symbol, reason):
    return "Failed {0} {1}: {2}".format(func, symbol, reason)


class IQFeedImporter(object):
    tickers = pd.DataFrame()
    #     columns=['datetime', 'open', 'high', 'low', 'close', 
    #              'volume', 'oi', 'symbol'])
    # tickers.set_index(['symbol', 'datetime'])
    df_assets = pd.DataFrame()
    symbols = []  # 'CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]

    def imp1_call_iqfeed(self, symbol, date_start, date_end):
        # x iqfeed = iqfc.IQFeedClient(feeder)
        timeframe = 86400  # 60*60*24  86400  1440
        iqreq = iqfc.historicData(date_start, date_end, timeframe)
        dframe = iqreq.download_symbol(symbol)
        return dframe

    def imp1_check_iqfeed_result(self, dframe):
        if not(dframe.empty):
            dframe.dropna(
                subset=['open', 'high', 'low', 'close', 'volume'],
                how='all')

        if dframe.empty:  # Note: Second check, not an else.
            logger.error("import_singleAsset failed: no data aquired.")
            return False
        
        return True

    def imp1_manip_result(self, symbol, dframe):
        # set column names
        # dframe.rename_axis("datetime")
        # dframe.columns = ['open', 'high', 'low', 'close', 'volume', 'oi']

        # add column with symbol
        dframe['symbol'] = pd.Series(
            [symbol for x in range(len(dframe.index))], 
            index=dframe.index)

        # set symbol and date column as multi index
        dframe.reindex(columns=['symbol', 'datetime'])

        return True

    def import_single_asset(self, symbol, date_start, date_end):
        '''
        imports single asset
        '''
        status = "failed. Import {0}".format(symbol)
        # todo: add date_start and end in status. 

        dframe = self.imp1_call_iqfeed(symbol, date_start, date_end)
        isok = self.imp1_check_iqfeed_result(dframe)
        if not isok:
            status = "import {0} failed: Empty or no results".format(symbol)
            logger.error(status)
            return status

        isok = self.imp1_manip_result(symbol, dframe)
        if not isok:
            status = "fail. Import {0}: Problem setting data".format(symbol)
            logger.error(status)
            return status

        file_details = dsys.DataSys.datafile_details(
            dsys.Prefixes.imported, dsys.DataFolders.imported, symbol)
        dsys.DataSys.save_dataframe(dframe, file_details)

        # self.tickers.reset_index()
        # dframe.reset_index()
        # self.tickers = self.tickers.append(dframe)
        # self.tickers.set_index(keys=['symbol', 'datetime'])
        status = "ok. Imported {0}".format(symbol)
        return status  # for testing that we got here

    def import_all_assets(self, date_start, date_end):
        self.load_symbols()  # get symbols list

        if len(self.symbols) < 1:
            logger.error("Import all: Symbols not loaded correctly. Aborting")
            return

        for item in self.symbols:
            data = self.import_single_asset(item, date_start, date_end)
            #data = "".join(data.split("\r"))
            #data = data.replace(",\n", "\n")[:-1]

        # todo: write to database. 
        # currently: adding to tickers dataframe
        # self.tickers.append(data)

        # Write the data stream to disk
        # f = open("{0}.csv".format('sym'), "w")
        # f.write(data)
        # f.close()

    def load_symbols(self):
        '''
        loads symbols-list from excel
        '''
        
        settingsfldr = dsys.DataFolders.settings
        assetslistfile = "{0}.{1}".format(
            dsys.Prefixes.assets, dsys.Extensions.excel)  # "AssetNamesNew.v01.xlsx"

        file_details = dsys.DataSys.details_byfolder(
                        settingsfldr, assetslistfile)
        symbols_column = 4  # todo: config
        sheetname = dsys.DataSys.assets_sheetname
                
        # dframe = pd.read_excel(file_details, sheetname=sheetname, index_col=0,
        #                       na_values='NA', usecols=symbols_column)
        assets_iq = ["SPX.XO", "COMPX.X","INDU.X","RUT.X",	"CAC.X"	,"DAX.X",	"UKX.X",	"HKHI.X",	"NIK.X",
        	"BVSP.X",	"QCL#",	"XAUUSD.FXCM"	,"@W#"	,"EURUSD.FXCM",	"@TY#",	"MMSWRLD.X"	,"MXEA.X"	,"RUI.X",
            "C.T0000.X"	,"QHG#"	,"QSI#","@C#","JPYUSD.COMP","GBPUSD.FXCM","AUDUSD.FXCM","CADUSD.COMP","CHFUSD.COMP",
            "KOREA.X","@CC#","ICF#","@HE#","@S#","@LE#","@RR#"]
        assets_bloom = [
            "SPX_Index",
            "CCMP_Index",
            "INDU_Index",
            "RTY_Index",
            "CAC_Index",
            "DAX_Index",
            "UKX_Index",
            "HSI_Index",
            "NKY_Index",
            "IBOV_Index",
            "CL1_Comdty",
            "XAU_Curncy",
            "W_1_Comdty",
            "EURUSD_Curncy",
            "TY1_Comdty",
            "MXWO_Index",
            "MXEA_Index",
            "RIY_Index",
            "SPTSX_Index",
            "HG1_Comdty",
            "SI1_Comdty",
            "C_1_Comdty",
            "JPYUSD_Curncy",
            "GBPUSD_Curncy",
            "AUDUSD_Curncy",
            "CADUSD_Curncy",
            "CHFUSD_Curncy",
            "KOSPI_Index",
            "CC1_Comdty",
            "AX1_Comdty",
            "LH1_Comdty",
            "S_1_Comdty",
            "LC1_Comdty",
            "RR1_Comdty"           
        ]

        # self.df_assets.loc[:,0] = assets_iq
        # self.df_assets.columns = assets_bloom
        


        # fix. Read from excel
        # if self.df_assets.empty:
        #    stage = "Load symbols failed. No dataframe from {0}".format(file_details)
        #    logger.error()
        #    return
        # self.df_assets = self.df_assets.dropna(how='all')

        self.symbols = assets_iq  # self.df_assets.values.tolist()
        # if self.symbols.count() < 1:
        #    stage = "Load symbols failed. Could not load symbols list"
        #    logger.error(stage)
        #    return  stage  # in case we do anything else later

        stage = "ok"
        return stage

    def load_bloomberg(self, symbol, date_start, date_end):
        file_details = dsys.DataSys.datafile_details(
            dsys.Prefixes.bloomberg_compare,
            dsys.DataFolders.compare_from,
            symbol, date_start, date_end,
            dsys.Extensions.excel)

        bloomcols = "1,2,3,4,5,6" 
        # "Date,PX_OPEN,PX_HIGH,PX_LOW,PX_LAST,PX_VOLUME"

        dframe = pd.read_excel(file_details,  # sheetname=bloomsheet, 
                              index_col=0,
                               na_values='NA', parse_cols=bloomcols)
        if dframe is None or dframe.empty:
            status = __failedmessage('loadbloom', symbol, 'No compare data')
            logger.error(status)
            return
        
        dframe.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'oi', 'symbol']
        dframe['symbol'] = symbol
        # X dframe['volume'] = 0
        dframe['oi'] = 0
        dframe.set_index(['symbol', 'datetime'])  

        return dframe

    def analyze_symbol(self, symbol, date_start, date_end):
        '''
        analyzes iqfeed vs. bloomberg
        outputs: in_iq, in_bloom, rejects, compared
        '''

        # pseudo: 
        # startdate: max first1:first2
        # enddate: min last1:last2

        # find dates not in df1
        # find dates not in df2
        # for each line: na1, na2, na, zero2
        # for each line: (v1/v2)-1

        stage = "failed"

        df1 = self.tickers.loc[(self.tickers['symbol'] == symbol)]
        if df1.empty:
            stage = __failedmessage('analyze', symbol, 'No feed data')
            logger.error(stage)
            return stage

        df2 = self.load_bloomberg(symbol, date_start, date_end)
        if df2 is None or df2.empty:
            stage = __failedmessage('analyze', symbol, 'No comparison data')
            logger.error(stage)
            return stage

        # 1. compare only dates inside both
        feedDate1 = df1['date'].head(1)
        bloomDate1 = df2['date'].head(1)  # .iloc[0]
        date1 = max(feedDate1, bloomDate1)
        # x df1['date'] = pd.to_datetime(df1['date'])

        feedDate2 = df1['date'].tail(1)
        bloomDate2 = df2['date'].tail(1)
        date2 = min(feedDate2, bloomDate2)
        # fix: check for errors in dates

        df1 = df1.xs(
            symbol, slice(date1, date2),
            level=('symbol', 'date'))

        df2 = df2.xs(
            symbol, slice(date1, date2),
            level=('symbol', 'date'))
        
        if df1.empty or df2.empty:
            stage = __failedmessage(
                'analyze', symbol, 'No date within compared dates')
            logger.error(stage)
            return stage
        
        # remove na-rows from both and then compare missing dates
        # Note: if both missing a date it will be removed without report
        # check na in columns except symbol and date
        cols1 = len(df1.columns) - 2
        cols2 = len(df2.columns) - 2
        df1 = df1.dropna(subset=df1.columns[cols1:], how='all')
        df2 = df2.dropna(subset=df2.columns[cols2:], how='all')

        if df1.empty or df2.empty:
            stage = __failedmessage('analyze', symbol, 'Missing input data')
            logger.error(stage)
            return stage

        # create the merge, the bloom only and iqfeed only
        dfcommon = df1.merge(
            df2, on=['symbol', 'date'], left_index=True, right_index=True)
        stage = "Failed. Analyze {0}"
        iq_only = df1[(~df1.index.isin(dfcommon.index))]
        bloom_only = df2[(~df1.index.isin(dfcommon.index))]
        stage = "Created summaries of unique in iqfeed and Bloomberg"        

        # mark indicators: col1/col2-1 or: missing/missing1/missing2/zero2
        tolerance = 1.5  # config
        for col in ['open', 'high', 'low', 'close', 'volume']:
            dfcommon[col] = dfcommon.apply(
                lambda row: __indicator(row, col), axis=1)
        # https://stackoverflow.com/questions/44140489/get-non-numerical-rows-in-a-column-pandas-python/44140542#44140542
        # https://stackoverflow.com/questions/10665889/how-to-take-column-slices-of-dataframe-in-pandas
        dfcommon['missing'] = dfcommon.apply(lambda row: __plobrem(row))
        dfcommon['rejected'] = dfcommon.apply(
            lambda row: __rejected_count(row, tolerance))
        stage = "done preparing common data"
        
        extension = dsys.Extensions.excel  # change this if we want matlab
        file_details = dsys.DataSys.datafile_details(
            dsys.Prefixes.bloomberg_only, dsys.DataFolders.rejected,
            symbol, date1, date2, extension)
        dsys.DataSys.save_dataframe(bloom_only, file_details, extension)
        stage = "symbol {0} saved dates unique to bloom".format(symbol)

        # save iq only
        extension = dsys.Extensions.excel  # change this if we want matlab
        file_details = dsys.DataSys.datafile_details(
            dsys.Prefixes.iqfeed_only, dsys.DataFolders.rejected,
            symbol, date1, date2, extension)
        dsys.DataSys.save_dataframe(iq_only, file_details, extension)
        stage = "symbol {0} saved dates unique to iqfeed".format(symbol)

        # save rejected
        rejectedrow_tolerance = 3
        dfrejected = dfcommon.loc[(
            (dfcommon['rejected'] > rejectedrow_tolerance) and
            (dfcommon['missing'] > rejectedrow_tolerance))]

        extension = dsys.Extensions.excel
        file_details = dsys.DataSys.datafile_details(
            dsys.Prefixes.rejected, dsys.DataFolders.rejected,
            symbol, date1, date2, extension)
        dsys.DataSys.save_dataframe(dfrejected, file_details, extension)
        stage = "symbol {0} saved rejected (over tolerance)".format(symbol)

        # save compiled
        dfcompiled = dfcommon.loc[(
            (dfcommon['rejected'] <= rejectedrow_tolerance) and
            (dfcommon['missing'] <= rejectedrow_tolerance))]

        extension = dsys.Extensions.excel
        file_details = dsys.DataSys.datafile_details(
            dsys.Prefixes.compiled, dsys.DataFolders.compiled,
            symbol, date1, date2, extension)
        dsys.DataSys.save_dataframe(dfcompiled, file_details, extension)
        # stage = "symbol {0} saved rejected (over tolerance)".format(symbol)

        stage = "Done"
        return stage

        
# ------------------------ Internals ---

