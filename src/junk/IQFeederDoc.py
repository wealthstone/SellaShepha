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

# see: https://stackoverflow.com/questions/47015061/python-error-cannot-import-name-historicdata-from-iqfeed

# instead of pythonpath
# import sys
# sys.path.insert(0,'c:\\dev\\SellaShepha\\src\\packages\\IQFeed-master' )
'''

# code removed...
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

# todo: future - test should not write to actual data folder.
# todo: Moshe to find advanced visual Python testing environment

# fix: insert logging in project:
#       e.g. logger.error("error message...")
