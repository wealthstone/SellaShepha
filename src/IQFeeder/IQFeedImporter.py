# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:20:22 2017

@author: pashute
"""
'''
 see  either this: https://pypi.python.org/pypi/iqfeed/0.4.3
 or BETTER:  https://github.com/luketighe/IQFeed
'''
from iqFeed import historicData

class IQFeedImporter():
    def import_feed_symbol(self, dateStart, dateEnd, symbol):
        iq = historicData(dateStart, dateEnd, 60)
        symbolOneData = iq.download_symbol(symbolOne)
        # todo: store in .mat file and in database

    def importFeedAll(self, dateStart, dateEnd):
        #todo: read from symbols table
        symbols = ['CBOT', 'CFE', "SPY", "AAPL", "GOOG", "AMZN"]
        for sym in symbols:
            data = self.import_feed_symbol(dateStart, dateEnd, sym)
            data = "".join(data.split("\r"))
            data = data.replace(",\n","\n")[:-1]
        # Write the data stream to disk
        f = open("%s.csv" % sym, "w")
        f.write(data)
        f.close()
        # Remark 
