import pandas as pd

def fake_df_imported(symbol):
    drange = pd.date_range('1/1/2015', periods=5, freq='D')
    _dframe = pd.DataFrame()
    _dframe['datetime'] = drange
    _dframe['a'] = [2, 3, 2, 2, 2]
    _dframe['b'] = [7, 7 ,7, 6, 7]
    _dframe['c'] = [1, 1, 1, 2, 1]
    _dframe['d'] = [6, 6, 6, 6, 6]
    _dframe['e'] = symbol
    _dframe.columns = ['datetime', 'open', 'high', 'low', 'close', 'symbol']
    # dframe.reset_index()
    _dframe.set_index(['symbol', 'datetime'])
    print(_dframe.head())
    # dframe['symbol'] = symbol
    # dframe.columns = ['datetime','open', 'high', 'low', 'close', 'symbol']
    # dframe.set_index(['symbol', 'datetime'])

    drange2 = pd.date_range('1/1/2015', periods=5, freq='D')
    dframe2 = pd.DataFrame()
    dframe2['datetime'] = drange2
    dframe2['a'] = [2, 3, 2, 1, 2]
    dframe2['b'] = [9, 7, 9, 6, 7]
    dframe2['c'] = [1, 0, 1, 2, 1]
    dframe2['d'] = [6, 6, 8, 6, 6]
    dframe2['e'] = "blu"
    dframe2.columns=['datetime', 'open', 'high', 'low', 'close', 'symbol']
    # dframe2.reset_index()
    dframe2.set_index('symbol', 'datetime')

    _dframe.reset_index()
    dframe2.reset_index()
    dframe2 = _dframe.merge(dframe2,how='inner',  )
    dframe2.set_index(['symbol', 'datetime'])
    return _dframe

_dframe = fake_df_imported("bla")
print(_dframe.head(3))
a = 5
