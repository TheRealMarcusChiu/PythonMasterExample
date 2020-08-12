import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])

s = pd.Series(data)
print('\nARRAY')
print(s)

s = pd.Series(data, index=[100, 101, 102, 103])
print('\nARRAY WITH INDEX')
print(s)

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print('\nDICT')
print(s)

s = pd.Series(data, index=['b', 'c', 'd', 'a'])
print('\nDICT WITH INDEX')
print(s)

s = pd.Series(5, index=[0, 1, 2, 3])
print('\nSCALAR')
print(s)
