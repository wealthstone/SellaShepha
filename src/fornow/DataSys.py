'''
Data folders paths and filenames
'''
# from enum import Enum
import logging
import scipy.io
# check: not sure if i have to set logger here too'
logging.basicConfig(filename="log.iqfeed.txt", level=logging.WARN)
logger = logging.getLogger(__name__)


class Prefixes(object):  # Enum):
    ''' prefixes enum '''
    # todo: config
    assets = "assets"  # symbols file
    bloomberg_compare = "bloom" # bloomberg input file
    bloomberg_only = "bloom_only"
    iqfeed_only = "iq_only"
    compiled = "ok"
    rejected = "rejects"


class Extensions(object):  # Enum):
    ''' supported extensions (excel, matlab, csv) enumeration '''
    excel = "xlsx"
    matlab = "mat"
    csv = "csv"
    # todo: config


class DataFolders(object):  # Enum):
    ''' data folders enumeration '''

    settings = "settings"  # asset names
    compare_from = "compare"  # bloomberg
    rejected = "rejected"  # rejected, or only in one of the frames
    compiled = "compiled"  # compilation results
    ''' data folders enumeration '''
    # todo: config


class DataSys(object):
    '''
    Methods for retrieving data folder names and full paths with filenames
    '''
    is_testing = False  # change this to true for testing

    project_path = "c:\\dev\\SellaShepha"  # WealthProphet
    data_mainpath = "{0}\\{1}".format(project_path, "data")
    data_testingpath = "{0}\\{1}".format(data_mainpath, "testing")

    @staticmethod
    def path_byfolder(datafolder):
        '''
        gets path to data folder for chosen data type
        data types are defined in the DataFolders class
        '''
        rootpath = DataSys.data_mainpath
        if (DataSys.is_testing and
                (datafolder == DataFolders.rejected or
                 datafolder == DataFolders.compiled)):
            rootpath = DataSys.data_testingpath
        return "{0}\\{1}".format(rootpath, datafolder)

    @staticmethod
    def details_byfolder(datafolder, filename):
        '''
        Gives correct full path for chosen filename in this data-folder
        data types are defined in the DataFolders class
        '''
        return "{0}\\{1}".format(DataSys.path_byfolder(datafolder), filename)

    @staticmethod
    def datafile_details(
            prefix, datafolder, symbol,
            date_start, date_end, extension=".xlsx"):
        ''' gives datafile path and filename details from parameters '''
        dstart = date_start.strftime('%Y%m%d')
        dend = date_end.strftime('%Y%m%d')
        filename = "{0}_{1}_{2}_{3}.{4}".format(
            prefix, symbol, dstart, dend, extension)

        datapath = DataSys.path_byfolder(datafolder)
        filedetails = "{0}\\{1}".format(datapath, filename)
        return filedetails

    @staticmethod
    def save_dataframe(dframe, file_details, savetype_extension):
        ''' saves dataframe to file (excel, matlab or csv) '''
        extension = savetype_extension
        success = False
        if extension == Extensions.matlab:
            datadict = dframe.to_dict()
            scipy.io.savemat(file_details, datadict)
            # logger.debug()
            success = True
        elif extension == Extensions.excel:
            dframe.to_excel(file_details)
            success = True
        elif extension == Extensions.csv:
            dframe.to_csv(file_details)
            success = True
        else:
            # success was set to false at beginning
            logger.error("Dataframe not saved. Wrong extension supplied")

        return success
