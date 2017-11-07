''' wrappers for IQFeed '''


class IQFeedClient(object):
    ''' wraps IQFeed object '''
    thefeeder = None

    def __init__(self, feeder):
        self.thefeeder = feeder

    def historic_data(self, date_start, date_end, period):
        result = self.thefeeder.historicData(date_start, date_end, period)
        return HistoricDataRequest(result)


class HistoricDataRequest(object):
    ''' wraps feeder request object '''
    therequest = None

    def __init__(self, historicdata_request):
        self.therequest = historicdata_request

    def download_symbol(self, symbol):
        ''' wraps download_signal call '''
        result = self.therequest.download_symbol(symbol)
        return result  # dataframe
