import datetime as dt
import pandas as pd
import IQFeedImporter as iqfi

iqf = iqfi.IQFeedImporter()

symbol = "SPX.XO"
date_start = dt.datetime(2016, 1, 1)
date_end = dt.datetime(2017, 1, 1)
result  = iqf.import_all_assets(date_start, date_end)
# result = iqf.import_single_asset(symbol, date_start, date_end)
isok = result.startswith("ok")
bla = 1  # extra line so i can check. 

# ok. run with timeframe 60. no str, no quote, shutdown, close()
# no data 86440 - perhaps problem was shutdown
# ok. 1440
# no data 86439.
#   