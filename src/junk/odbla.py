import pandas as pd
import numpy as np

def mytest(a, b):
    return a % b

def habad(row):
    if row.iloc()

df = pd.DataFrame({'a': ['l1', 'm2', 'n3', 'o4', 'p5', 'q6'],
                   'b': np.random.randn(6),
                   'c': [1, 'bla'] * 3,
                   'd': np.random.randn(6)})

df['value'] = df.apply(lambda row: mytest(row['b'], row['d']), axis=1)
df['bad'] = df.['b','c','d'].apply(lambda row: hasbad(row), axis=1)

print(df.head)

# class A(object):
#     ''' does A '''

#     def __init__(self, name, x):
#         self.X = x
#         self.Name = name
    
#     Y = 5

#     def setX(self, x):
#         self.X = x

#     def setY(self, y):
#         self.Y = y
    
# a = A('a', 1)
# b = A('b', 2)
# print(a.Name, a.X, a.Y)
# print(b.Name, b.X, b.Y)


# a.setY(77)
# a.X = 3
# print(a.Name, a.X, a.Y)
# print(b.Name, b.X, b.Y)

# b.Y = 88
# a.setY = 99
# print(a.Name, a.X, a.Y)
# print(b.Name, b.X, b.Y)

# a.setX = 111
