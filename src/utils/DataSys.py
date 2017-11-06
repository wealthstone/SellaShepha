'''
Data folders paths and filenames
'''
from enum import Enum
# see https://stackoverflow.com/questions/35988/c-like-structures-in-python


class DataFolders(Enum):
    ''' data folders enumeration '''

    # todo: config
    settings = "settings"  # asset names
    compared = "compared"  # bloomberg
    compiled = "compiled"  # compilation results
    testing = "testing"   # compilation results during QA testing


class DataSys(object):
    '''
    Methods for retrieving data folder names and full paths with filenames
    '''
    __project_path = "c:\\dev\\SellaShepha"  # WealthProphet
    __data_folder = "{0}\\{1}".format(__project_path, "data")

    def datapath(self, datatype):
        '''
        gets path to data folder for chosen data type
        data types are defined in the DataFolders class
        '''
        return "{0}\\{1}".format(self.__data_folder, datatype)

    def datafile(self, datatype, filename):
        '''
        gets full path for filename in this data-type
        data types are defined in the DataFolders class
        '''
        return "{0}\\{1}".format(self.datapath(datatype), filename)
