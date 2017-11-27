import pandas as pd
import datetime as dt

_columns = ['datetime', 'info1', 'info2', 'symbol']
_indexcols = ['symbol', 'datetime']

# dates we'll use later
_dt_both = dt.datetime(2017, 11, 21).strftime("%Y%m%d")
_dt_left = dt.datetime(2017, 11, 22).strftime("%Y%m%d")
_dt_right = dt.datetime(2017, 11, 23).strftime("%Y%m%d")

# create df_left and put some data in, row by row
# multi-index is: symbol/datetime columns

_data = [] # Array of arrays. called lists in Python
_data.append([_dt_left, 'Lr1c1', 'Lr1c2', 'aaa'])
_data.append([_dt_both, 'Lr2c1', 'Br2c2', 'aaa'])
_data.append([_dt_both, 'Lr3c1', 'Lr3c2', 'bbb'])
print(_data)

# construct dataframe with data
_df_left = pd.DataFrame(
    _data,
    columns=_columns)

print("before setindex")
print(_df_left)

_df_left = _df_left.set_index(keys=_indexcols)
print('after set index')
print(_df_left)

# empty dataset and appending [[],[],[]] list of lists 
_df_right = pd.DataFrame(columns=_columns)
#_df_right.loc[['aaa', _dt_right]] = ['Rr1c1', 'Rr1c2']
print(len(_df_right.index))  
_df_right.loc[len(_df_right.index)+1] = [_dt_right, 'Rr1c1', 'Rr1c2', 'aaa']
_df_right.loc[len(_df_right.index)+1] = [_dt_both, 'Rr2c1', 'Br2c2', 'aaa']
_df_right.loc[len(_df_right.index)+1] = [_dt_both, 'Rr3c1', 'Rr3c2', 'bbb']

# _data.append([_dt_right, 'Rr1c1', 'Rr1c2', 'aaa'])
# _data.append([_dt_both, 'Rr2c1', 'Br2c2', 'aaa'])
# _data.append([_dt_both, 'Rr3c3', 'Rr3c2', 'bbb']) 
# [[_dt_right, 'Rr1c1', 'Rr1c2', 'aaa'],
#          [_dt_both, 'Rr2c1', 'Br2c2', 'aaa'],
#          [_dt_both, 'Rr3c3', 'Rr3c2', 'bbb']]

# _df_right.append(_data, ignore_index=True)
print('before right index')
print(_df_right.head(3)) 

# _df_right.set_index(keys=_indexcols)  # returns a copy so nothing stored
_df_right = _df_right.set_index(keys=_indexcols)  # returns a copy so nothing stored
print('after right index')
print(_df_right.head(3)) 

_df_right.loc['zzz', _dt_right] = ['dz1', 'dz2']
print('after right add records by multi-index')
print(_df_right.head(3))
# Note: If ignore_index=False it fails with explanation

# -----  appending with explicit column-names ---
# _leftrow1 = {
#     'datetime': _dt_both, 
#     'info1':'left r1c1',
#     'info2':'left r1c2',
#     'symbol':'aaa' 
#     }
# _leftrow2 = {
#     'datetime': _dt_left, 
#     'info1':'left r2c1', 'info2':'left r2c2',
#     'symbol':'aaa' 
#     }
# _leftrow3 = {
#     'datetime': _dt_both, 
#     'info1':'left r2c3', 'info2':'left r2c3',
#     'symbol':'bbb' 
#     }


# _df_left.append(
#   _row, 
#   _ignore_index=True) # false gives explanation
