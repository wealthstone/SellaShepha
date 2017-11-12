''' this is just for fast testing  not part of production '''
import datetime as dt
import DataSys as dsys

symbol = "bla"
preimp = dsys.Prefixes.imported
foldimp = dsys.DataFolders.imported
date_start = dt.datetime(1997,1,1)
date_end = dt.datetime(2015,1,1)
file_details = dsys.DataSys.datafile_details(
    preimp, foldimp, symbol, date_start, date_end)
isok = file_details.startswith("C")

file_details = dsys.DataSys.datafile_details(
    dsys.Prefixes.imported, dsys.DataFolders.imported, symbol)
isok2 = file_details.startswith("C")
isok3 = true 