''' 
   main function to run the import
'''

import datetime as dt
# import pandas as pd
import IQFeedImporter as iqfi

iqf = iqfi.IQFeedImporter()

# symbol = "SPX.XO"
date_start = dt.datetime(1995, 1, 1)
date_end = dt.datetime(2017, 10, 1)
result  = iqf.import_all_assets(date_start, date_end)
# result = iqf.import_single_asset(symbol, date_start, date_end)
isok = result.startswith("ok")