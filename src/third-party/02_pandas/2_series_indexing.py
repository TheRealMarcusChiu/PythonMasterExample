import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s[101])
print(s[0:3])
print(s[:3])

s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s[0])
print(s['a'])
print(s[['a', 'c', 'd']])  # retrieve multiple elements
