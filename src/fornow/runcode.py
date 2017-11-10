''' this is just for fast testing  not part of production '''
import DataSys as dsys

symbol = "bla"
preimp = dsys.Prefixes.imported
foldimp = dsys.DataFolders.imported
file_details = dsys.DataSys.datafile_details(
    preimp, foldimp, symbol)
isok = file_details.startswith("C")

file_details = dsys.DataSys.datafile_details(
    dsys.Prefixes.imported, dsys.DataFolders.imported, symbol)
isok2 = file_details.startswith("C")
isok3 = true 